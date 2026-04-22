// ═══════════════════════════════════════════════════════════
//  SCHOOL ASSISTANT — FRONTEND JAVASCRIPT
//  With: Markdown Rendering, Content-Aware Formatting,
//        Adaptive Response, Prompt-Conditioned Output
// ═══════════════════════════════════════════════════════════

const API_BASE = window.location.origin;

// ─── DOM Refs ────────────────────────────────────────────
const messagesEl    = document.getElementById('messages');
const messagesWrap  = document.getElementById('messages-wrap');
const welcomeScreen = document.getElementById('welcome-screen');
const userInput     = document.getElementById('user-input');
const sendBtn       = document.getElementById('send-btn');
const clearBtn      = document.getElementById('clear-btn');
const geminiKey     = document.getElementById('gemini-key');
const apiIndicator  = document.getElementById('api-indicator');
const sidebarToggle = document.getElementById('sidebar-toggle');
const sidebar       = document.getElementById('sidebar');

// Model status els
const modelStatus = document.getElementById('model-status');
const modelFile   = document.getElementById('model-file');
const modelParams = document.getElementById('model-params');
const modelLoss   = document.getElementById('model-loss');

// ─── State ───────────────────────────────────────────────
let history  = [];
let isTyping = false;
let currentSessionId = localStorage.getItem('school_bot_session_id') || Date.now().toString();

const historyListEl = document.getElementById('history-list');
const newChatBtn    = document.getElementById('new-chat-btn');

function renderHistoryList() {
  const sessions = JSON.parse(localStorage.getItem('school_chat_sessions') || '[]');
  historyListEl.innerHTML = '';
  
  sessions.forEach(session => {
    const item = document.createElement('div');
    item.className = `history-item ${session.id === currentSessionId ? 'active' : ''}`;
    item.textContent = session.title;
    item.onclick = () => switchSession(session.id);
    historyListEl.appendChild(item);
  });
}

function switchSession(id) {
  if (isTyping) return;
  currentSessionId = id;
  localStorage.setItem('school_bot_session_id', id);
  history = [];
  messagesEl.innerHTML = '';
  loadHistory();
  renderHistoryList();
}

newChatBtn.addEventListener('click', () => {
  if (isTyping) return;
  currentSessionId = Date.now().toString();
  localStorage.setItem('school_bot_session_id', currentSessionId);
  history = [];
  messagesEl.innerHTML = '';
  showWelcome();
  renderHistoryList();
});

// Task 6 & 7: Persistence
function saveHistory() {
  localStorage.setItem(`school_chat_${currentSessionId}`, JSON.stringify(history));
  
  let sessions = JSON.parse(localStorage.getItem('school_chat_sessions') || '[]');
  const sessionIndex = sessions.findIndex(s => s.id === currentSessionId);
  
  if (sessionIndex === -1) {
    if (history.length > 0) {
      const title = history[0].content.substring(0, 25) + '...';
      sessions.unshift({ id: currentSessionId, title, date: new Date().toLocaleDateString() });
    }
  } else if (history.length > 0 && sessions[sessionIndex].title === 'New Chat') {
    sessions[sessionIndex].title = history[0].content.substring(0, 25) + '...';
  }
  
  localStorage.setItem('school_chat_sessions', JSON.stringify(sessions));
  localStorage.setItem('school_bot_session_id', currentSessionId);
  renderHistoryList();
}

function loadHistory() {
  const saved = localStorage.getItem(`school_chat_${currentSessionId}`);
  if (saved) {
    history = JSON.parse(saved);
    if (history.length > 0) {
      hideWelcome();
      messagesEl.innerHTML = '';
      history.forEach(msg => {
        if (msg.role === 'user') appendUserBubble(msg.content, false);
        else appendBotBubble(msg.content, '', false, false);
      });
      scrollToBottom();
    } else {
      showWelcome();
    }
  } else {
    showWelcome();
  }
  renderHistoryList();
}

// ─── Init ────────────────────────────────────────────────
fetchStatus();
updateApiIndicator();
loadHistory();

// ─── Sidebar Toggle ──────────────────────────────────────
const sidebarToggleBtn = document.getElementById('sidebar-toggle');

// Restore sidebar state from last session
if (localStorage.getItem('sidebar-collapsed') === 'true') {
  document.body.classList.add('sidebar-collapsed');
  sidebarToggleBtn.textContent = '☰';
}

sidebarToggleBtn.addEventListener('click', () => {
  const isCollapsed = document.body.classList.toggle('sidebar-collapsed');
  sidebarToggleBtn.textContent = isCollapsed ? '☰' : '✕';
  localStorage.setItem('sidebar-collapsed', isCollapsed);
});

// ─── API Key indicator ───────────────────────────────────
geminiKey.addEventListener('input', updateApiIndicator);
function updateApiIndicator() {
  const hasKey = geminiKey.value.trim().length > 0;
  apiIndicator.classList.toggle('inactive', !hasKey);
  apiIndicator.title = hasKey ? 'Cloud mode active (Gemini)' : 'Local PyTorch mode';
}

// ─── Model Status Fetch ──────────────────────────────────
async function fetchStatus() {
  try {
    const res = await fetch(`${API_BASE}/api/status`);
    const data = await res.json();
    modelStatus.innerHTML = `<span class="status-dot"></span>Online`;
    modelFile.textContent   = data.model  || '—';
    modelParams.textContent = data.params ? (data.params / 1_000_000).toFixed(2) + 'M' : '—';
    modelLoss.textContent   = data.loss   || '—';
  } catch {
    modelStatus.innerHTML = `<span style="color:var(--danger)">Offline</span>`;
  }
}

// ─── Sidebar Mobile Toggle ───────────────────────────────
sidebarToggle.addEventListener('click', () => sidebar.classList.toggle('open'));
document.addEventListener('click', (e) => {
  if (window.innerWidth <= 768 &&
      !sidebar.contains(e.target) &&
      !sidebarToggle.contains(e.target)) {
    sidebar.classList.remove('open');
  }
});

// ─── Clear Chat ──────────────────────────────────────────
clearBtn.addEventListener('click', () => {
  localStorage.removeItem(`school_chat_${currentSessionId}`);
  history = [];
  messagesEl.innerHTML = '';
  showWelcome();
  
  // Create new session id
  currentSessionId = Date.now().toString();
  localStorage.setItem('school_bot_session_id', currentSessionId);
});

// ─── Quick-start / Sidebar chips ─────────────────────────
document.querySelectorAll('.chip').forEach(chip => {
  chip.addEventListener('click', () => {
    const q = chip.dataset.q;
    if (!isTyping) submitQuestion(q);
  });
});
document.querySelectorAll('.welcome-chip').forEach(chip => {
  chip.addEventListener('click', () => {
    const q = chip.dataset.q;
    if (!isTyping) submitQuestion(q);
  });
});

// ─── Input events ────────────────────────────────────────
userInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    handleSend();
  }
});
sendBtn.addEventListener('click', handleSend);

// Auto-resize textarea
userInput.addEventListener('input', () => {
  userInput.style.height = 'auto';
  userInput.style.height = Math.min(userInput.scrollHeight, 140) + 'px';
});

function handleSend() {
  const q = userInput.value.trim();
  if (!q || isTyping) return;
  userInput.value = '';
  userInput.style.height = 'auto';
  submitQuestion(q);
}

// ─── Core: Submit Question ────────────────────────────────
async function submitQuestion(question) {
  isTyping = true;
  sendBtn.disabled = true;

  hideWelcome();
  appendUserBubble(question);
  history.push({ role: 'user', content: question });

  const typingEl = appendTypingIndicator();

  try {
    const res = await fetch(`${API_BASE}/api/chat`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        question,
        history: history.slice(0, -1),
        gemini_api_key: geminiKey.value.trim()
      })
    });

    typingEl.remove();

    if (!res.ok) throw new Error(`Server error ${res.status}`);
    const data = await res.json();
    const answer = data.answer || "Sorry, I couldn't get a response.";

    history.push({ role: 'assistant', content: answer });
    saveHistory(); // Save after each exchange
    await appendBotBubble(answer, question);

  } catch (err) {
    typingEl.remove();
    const errMsg = `Could not connect to the backend. Make sure the server is running.\n\nDetail: ${err.message}`;
    appendBotBubble(errMsg, '', true);
  }

  isTyping = false;
  sendBtn.disabled = false;
  userInput.focus();
}

// ═══════════════════════════════════════════════════════════
//  MARKDOWN RENDERER — Content-Aware Formatting
// ═══════════════════════════════════════════════════════════

/**
 * Detects the type of content for adaptive styling
 */
function detectContentType(text, question) {
  const q = (question || '').toLowerCase();
  const t = text.toLowerCase();
  const combined = q + ' ' + t;

  // Check most specific patterns first to avoid misclassification
  if (/subject|syllabus|curriculum|mathematics|science|english|hindi|social science|stream|cbse board|grading|grade|result|exam|co-curricular|ncc|club/.test(combined)) return 'academic';
  if (/fee|cost|price|amount|rupee|rs\.|₹|pay|installment|scholarship|deposit|concession/.test(combined)) return 'fees';
  if (/transport|bus|route|pickup|drop|van/.test(combined)) return 'transport';
  if (/admission|enroll|enrol|apply|document|certificate|rte|age criteria/.test(combined)) return 'admission';
  if (/time|timing|hour|schedule|holiday|ptm|saturday|reopen/.test(combined)) return 'schedule';
  if (/rule|policy|uniform|attendance|guideline|phone|mobile|leave|discipline|bullying/.test(combined)) return 'policy';
  if (/library|computer|lab|canteen|lunch|cctv|sports|ground|nurse|medical|facility|fire|water|lost and found/.test(combined)) return 'facility';
  if (/salary|payslip|casual leave|earned leave|maternity|prt|non-teaching|staff leave|hr/.test(combined)) return 'hr';
  if (/annual day|sports day|farewell|independence day|republic day|science exhibition|inter-school|competition|event|celebration/.test(combined)) return 'events';
  if (/portal|parent app|mobile app|attendance online|fee receipt|feedback|parent login|school app/.test(combined)) return 'portal';
  if (/counselor|counselling|mental health|debate club|student council|art club|music club|drama|photography|coding club|ncc|clubs/.test(combined)) return 'counseling';
  if (/fire|water|gate|pick.?up|drop.?off|guardian|lost|found|safety|ragging|bully|cctv|surveillance/.test(combined)) return 'safety';
  if (/\d+\.\s|\*\s|\n-\s/i.test(text)) return 'list';
  return 'general';
}

/**
 * Gets icon + accent color for each content type
 */
function getContentMeta(type) {
  const map = {
    fees:      { icon: '', label: 'Fee Information',       accent: '#10B981' },
    academic:  { icon: '', label: 'Academic Info',         accent: '#3B82F6' },
    admission: { icon: '', label: 'Admission Process',     accent: '#6C6FFF' },
    schedule:  { icon: '', label: 'Schedule & Timing',     accent: '#F59E0B' },
    policy:    { icon: '', label: 'School Policy',         accent: '#A78BFA' },
    transport: { icon: '', label: 'Transport Info',        accent: '#06B6D4' },
    facility:  { icon: '', label: 'School Facilities',     accent: '#EC4899' },
    hr:        { icon: '', label: 'Staff & HR',            accent: '#F97316' },
    events:    { icon: '', label: 'Events & Activities',   accent: '#EAB308' },
    portal:    { icon: '', label: 'Parent Portal',         accent: '#8B5CF6' },
    counseling:{ icon: '', label: 'Counseling & Clubs',    accent: '#14B8A6' },
    safety:    { icon: '', label: 'Safety & Security',     accent: '#EF4444' },
    list:      { icon: '', label: 'Details',               accent: '#9166f5' },
    general:   { icon: '', label: 'School Assistant',      accent: '#6C6FFF' },
  };
  return map[type] || map.general;
}

/**
 * Full markdown-to-HTML renderer with school-specific formatting
 */
function renderMarkdown(text) {
  let html = escapeHtml(text);

  // Bold: **text** or __text__
  html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/__(.+?)__/g, '<strong>$1</strong>');

  // Italic: *text* or _text_
  html = html.replace(/\*([^*]+?)\*/g, '<em>$1</em>');
  html = html.replace(/_([^_]+?)_/g, '<em>$1</em>');

  // Inline code: `code`
  html = html.replace(/`([^`]+?)`/g, '<code class="inline-code">$1</code>');

  // Process line by line
  const lines = html.split('\n');
  const result = [];
  let inOrderedList = false;
  let inUnorderedList = false;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();

    // Skip empty lines — close open lists
    if (!line) {
      if (inOrderedList)   { result.push('</ol>'); inOrderedList = false; }
      if (inUnorderedList) { result.push('</ul>'); inUnorderedList = false; }
      result.push('<div class="line-break"></div>');
      continue;
    }

    // Headings: ## or ###
    if (/^###\s/.test(line)) {
      if (inOrderedList)   { result.push('</ol>'); inOrderedList = false; }
      if (inUnorderedList) { result.push('</ul>'); inUnorderedList = false; }
      result.push(`<h4 class="md-h3">${line.replace(/^###\s/, '')}</h4>`);
      continue;
    }
    if (/^##\s/.test(line)) {
      if (inOrderedList)   { result.push('</ol>'); inOrderedList = false; }
      if (inUnorderedList) { result.push('</ul>'); inUnorderedList = false; }
      result.push(`<h3 class="md-h2">${line.replace(/^##\s/, '')}</h3>`);
      continue;
    }

    // Ordered list: 1. item
    const olMatch = line.match(/^(\d+)\.\s+(.*)/);
    if (olMatch) {
      if (inUnorderedList) { result.push('</ul>'); inUnorderedList = false; }
      if (!inOrderedList)  { result.push('<ol class="md-ol">'); inOrderedList = true; }
      result.push(`<li>${olMatch[2]}</li>`);
      continue;
    }

    // Unordered list: - item or * item
    const ulMatch = line.match(/^[-*]\s+(.*)/);
    if (ulMatch) {
      if (inOrderedList)   { result.push('</ol>'); inOrderedList = false; }
      if (!inUnorderedList){ result.push('<ul class="md-ul">'); inUnorderedList = true; }
      result.push(`<li>${ulMatch[1]}</li>`);
      continue;
    }

    // Regular paragraph
    if (inOrderedList)   { result.push('</ol>'); inOrderedList = false; }
    if (inUnorderedList) { result.push('</ul>'); inUnorderedList = false; }
    result.push(`<p class="md-p">${line}</p>`);
  }

  if (inOrderedList)   result.push('</ol>');
  if (inUnorderedList) result.push('</ul>');

  // Inline highlights: currency (Rs. X,XXX / ₹X) → green badge
  let final = result.join('');
  final = final.replace(/(Rs\.\s*[\d,]+|₹[\d,]+)/g, '<span class="badge-money">$1</span>');
  // Time highlights: 8:00 AM, 7:50 AM etc.
  final = final.replace(/\b(\d{1,2}:\d{2}\s*(?:AM|PM))\b/gi, '<span class="badge-time">$1</span>');
  // Percentage highlights
  final = final.replace(/\b(\d+%)\b/g, '<span class="badge-percent">$1</span>');

  return final;
}

// ═══════════════════════════════════════════════════════════
//  RENDER HELPERS
// ═══════════════════════════════════════════════════════════

function hideWelcome() {
  if (welcomeScreen.style.display !== 'none') {
    welcomeScreen.style.opacity = '0';
    welcomeScreen.style.transition = 'opacity 0.3s ease';
    setTimeout(() => { welcomeScreen.style.display = 'none'; }, 300);
  }
}

function showWelcome() {
  welcomeScreen.style.display = 'flex';
  welcomeScreen.style.opacity = '1';
}

function appendUserBubble(text, shouldScroll = true) {
  const group = document.createElement('div');
  group.className = 'msg-group user-group';
  group.innerHTML = `
    <div class="msg-label user-label">You</div>
    <div class="bubble user-bubble">${escapeHtml(text)}</div>
  `;
  messagesEl.appendChild(group);
  if (shouldScroll) scrollToBottom();
}

async function appendBotBubble(text, question = '', isError = false, isAnimated = true) {
  const type = isError ? 'general' : detectContentType(text, question);
  const meta = getContentMeta(type);

  const group = document.createElement('div');
  group.className = 'msg-group bot-group';

  // Label with content-type icon
  const label = document.createElement('div');
  label.className = 'msg-label bot-label';
  label.textContent = meta.label;

  // Bubble
  const bubble = document.createElement('div');
  bubble.className = 'bubble bot-bubble' + (isError ? ' error-bubble' : '');
  bubble.style.setProperty('--content-accent', meta.accent);

  // Color bar on left
  const colorBar = document.createElement('div');
  colorBar.className = 'bubble-accent-bar';

  bubble.appendChild(colorBar);
  group.appendChild(label);
  group.appendChild(bubble);
  messagesEl.appendChild(group);
  scrollToBottom();

  if (isError) {
    bubble.innerHTML += `<p class="md-p error-text">${escapeHtml(text)}</p>`;
    if (isAnimated) scrollToBottom();
    return;
  }

  if (isAnimated) {
    // Stream words into bubble
    await streamMarkdown(bubble, text);
  } else {
    // Instant render for history loading
    const content = document.createElement('div');
    content.className = 'bubble-content';
    content.innerHTML = renderMarkdown(text);
    bubble.appendChild(content);
  }
}

/**
 * Word-level streaming that works with HTML markdown
 * Renders full markdown at each step so tags are never broken
 */
async function streamMarkdown(el, text) {
  const words = text.split(' ');
  let accumulated = '';
  el.classList.add('streaming-cursor');

  // Content container inside bubble (after color bar)
  const content = document.createElement('div');
  content.className = 'bubble-content';
  el.appendChild(content);

  for (let i = 0; i < words.length; i++) {
    accumulated += (i === 0 ? '' : ' ') + words[i];
    content.innerHTML = renderMarkdown(accumulated);
    scrollToBottom();

    // Adaptive delay: pause at sentence ends, fast through spaces
    const word = words[i];
    let delay = 18;
    if (/[.!?]$/.test(word)) delay = 60;
    else if (/[,;:]$/.test(word)) delay = 30;
    await sleep(delay);
  }

  el.classList.remove('streaming-cursor');
}

function appendTypingIndicator() {
  const group = document.createElement('div');
  group.className = 'msg-group bot-group';
  const label = document.createElement('div');
  label.className = 'msg-label bot-label';
  label.textContent = 'School Assistant';
  const bubble = document.createElement('div');
  bubble.className = 'typing-bubble';
  bubble.innerHTML = `
    <div class="typing-dot"></div>
    <div class="typing-dot"></div>
    <div class="typing-dot"></div>
  `;
  group.appendChild(label);
  group.appendChild(bubble);
  messagesEl.appendChild(group);
  scrollToBottom();
  return group;
}

// ─── Utility ──────────────────────────────────────────────
function scrollToBottom() {
  // Use a slight timeout to ensure DOM layout has calculated new heights
  messagesWrap.scrollTop = messagesWrap.scrollHeight;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function escapeHtml(str) {
  const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
  return str.replace(/[&<>"']/g, m => map[m]);
}
