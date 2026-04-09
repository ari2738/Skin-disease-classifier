const API = 'http://127.0.0.1:5000';

// ── Tab switching ─────────────────────────────────────────────
function showTab(name) {
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
  document.getElementById('tab-' + name).classList.add('active');
  event.target.classList.add('active');
  if (name === 'history') loadHistory();
}

// ── Drag & drop ───────────────────────────────────────────────
const uploadZone = document.getElementById('uploadZone');
uploadZone.addEventListener('dragover',  e => { e.preventDefault(); uploadZone.classList.add('drag-over'); });
uploadZone.addEventListener('dragleave', () => uploadZone.classList.remove('drag-over'));
uploadZone.addEventListener('drop', e => {
  e.preventDefault();
  uploadZone.classList.remove('drag-over');
  const file = e.dataTransfer.files[0];
  if (file && file.type.startsWith('image/')) loadPreview(file);
});
uploadZone.addEventListener('click', () => document.getElementById('fileInput').click());

document.getElementById('fileInput').addEventListener('change', e => {
  if (e.target.files[0]) loadPreview(e.target.files[0]);
});

function loadPreview(file) {
  const reader = new FileReader();
  reader.onload = ev => {
    const preview = document.getElementById('preview');
    preview.src = ev.target.result;
    preview.hidden = false;
    uploadZone.style.display = 'none';
    document.getElementById('uploadActions').hidden = false;
  };
  reader.readAsDataURL(file);
}

function clearImage() {
  document.getElementById('preview').hidden = true;
  document.getElementById('preview').src = '';
  uploadZone.style.display = 'flex';
  document.getElementById('uploadActions').hidden = true;
  document.getElementById('fileInput').value = '';
  document.getElementById('resultContent').hidden = true;
  document.getElementById('resultPlaceholder').hidden = false;
}

// ── Predict ───────────────────────────────────────────────────
async function predict() {
  const file = document.getElementById('fileInput').files[0];
  if (!file) return alert('Please select an image first.');

  const btn = document.getElementById('analyseBtn');
  btn.innerHTML = '<span class="spinner"></span> Analysing...';
  btn.disabled = true;

  try {
    const formData = new FormData();
    formData.append('image', file);

    const res  = await fetch(`${API}/predict`, { method: 'POST', body: formData });
    const data = await res.json();

    if (data.error) { alert(data.error); return; }

    // Populate result
    document.getElementById('diseaseName').textContent = data.disease_name;
    document.getElementById('diseaseCode').textContent = data.prediction.toUpperCase();
    document.getElementById('diseaseDesc').textContent = data.description;
    document.getElementById('diseaseAction').textContent = data.action;
    document.getElementById('mainConf').textContent = data.confidence + '%';

    const badge = document.getElementById('severityBadge');
    badge.textContent = data.severity;
    badge.className = 'severity-badge severity-' + data.severity;

    // Confidence bars
    const bars = document.getElementById('barsContainer');
    bars.innerHTML = '';
    Object.entries(data.all_confidences)
      .sort((a, b) => b[1] - a[1])
      .forEach(([cls, conf], i) => {
        const isTop = i === 0;
        bars.innerHTML += `
          <div class="bar-row">
            <span class="bar-label">${cls}</span>
            <div class="bar-track">
              <div class="bar-fill ${isTop ? 'top' : 'rest'}" style="width:0%" data-width="${conf}%"></div>
            </div>
            <span class="bar-val">${conf}%</span>
          </div>`;
      });

    document.getElementById('resultPlaceholder').hidden = true;
    document.getElementById('resultContent').hidden = false;
    document.getElementById('resultContent').classList.add('fade-in');

    // Animate bars after render
    setTimeout(() => {
      document.querySelectorAll('.bar-fill').forEach(el => {
        el.style.width = el.dataset.width;
      });
    }, 50);

  } catch (err) {
    alert('Could not connect to backend. Make sure Flask is running on port 5000.');
    console.error(err);
  } finally {
    btn.innerHTML = '<span>Analyse Image</span>';
    btn.disabled = false;
  }
}

// ── History ───────────────────────────────────────────────────
async function loadHistory() {
  try {
    const res  = await fetch(`${API}/history`);
    const data = await res.json();
    const grid = document.getElementById('historyGrid');
    const empty = document.getElementById('historyEmpty');

    if (!data.length) {
      grid.innerHTML = '';
      empty.hidden = false;
      return;
    }

    empty.hidden = true;
    grid.innerHTML = data.map(r => {
      const date = new Date(r.timestamp).toLocaleString('en-IN', {
        day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit'
      });
      const sevClass = r.severity ? 'severity-' + r.severity : '';
      return `
        <div class="history-card fade-in">
          <img src="data:image/jpeg;base64,${r.image_b64}" alt="${r.disease_name}">
          <div class="history-card-body">
            <div class="hc-name">${r.disease_name}</div>
            <div class="hc-code">${r.prediction.toUpperCase()}</div>
            <div class="hc-row">
              <span class="hc-conf">${r.confidence}% confidence</span>
              ${r.severity ? `<span class="hc-sev severity-badge ${sevClass}">${r.severity}</span>` : ''}
            </div>
            <div class="hc-time" style="margin-top:6px">${date}</div>
          </div>
        </div>`;
    }).join('');
  } catch (err) {
    console.error('History error:', err);
  }
}

loadHistory();
