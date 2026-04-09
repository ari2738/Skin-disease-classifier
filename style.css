<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DermAI — Skin Disease Classifier</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <nav class="nav">
    <div class="nav-brand">Derm<span>AI</span></div>
    <div class="nav-tabs">
      <button class="nav-tab active" onclick="showTab('analyse')">Analyse</button>
      <button class="nav-tab" onclick="showTab('history')">History</button>
    </div>
  </nav>

  <!-- ── Analyse Tab ─────────────────────────────────────────── -->
  <div id="tab-analyse" class="tab active">
    <div class="hero">
      <h1>Skin Disease<br><em>Classification</em></h1>
      <p>Upload a dermoscopic image for instant AI-powered analysis across 7 skin conditions.</p>
    </div>

    <div class="main-grid">

      <!-- Upload -->
      <div class="card upload-card" id="uploadCard">
        <div class="upload-zone" id="uploadZone">
          <input type="file" id="fileInput" accept="image/*" hidden>
          <div class="upload-icon">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
              <polyline points="17 8 12 3 7 8"/>
              <line x1="12" y1="3" x2="12" y2="15"/>
            </svg>
          </div>
          <p class="upload-label">Drop image here</p>
          <p class="upload-sub">or</p>
          <button class="btn-outline" onclick="document.getElementById('fileInput').click()">Browse File</button>
        </div>
        <img id="preview" src="" alt="Preview" hidden>
        <div class="upload-actions" id="uploadActions" hidden>
          <button class="btn-ghost" onclick="clearImage()">Clear</button>
          <button class="btn-primary" id="analyseBtn" onclick="predict()">
            <span>Analyse Image</span>
          </button>
        </div>
      </div>

      <!-- Result -->
      <div class="card result-card" id="resultCard">
        <div class="result-placeholder" id="resultPlaceholder">
          <p>Results will appear here after analysis</p>
        </div>

        <div id="resultContent" hidden>
          <div class="result-header">
            <div>
              <div class="result-label">Diagnosis</div>
              <div class="result-disease" id="diseaseName"></div>
              <div class="result-code" id="diseaseCode"></div>
            </div>
            <div class="severity-badge" id="severityBadge"></div>
          </div>

          <div class="result-desc" id="diseaseDesc"></div>
          <div class="result-action" id="diseaseAction"></div>

          <div class="conf-main">
            <span class="conf-label">Confidence</span>
            <span class="conf-value" id="mainConf"></span>
          </div>

          <div class="bars-title">All Classes</div>
          <div id="barsContainer"></div>
        </div>
      </div>

    </div>
  </div>

  <!-- ── History Tab ─────────────────────────────────────────── -->
  <div id="tab-history" class="tab">
    <div class="history-header">
      <h2>Prediction History</h2>
      <p>Last 20 analyses</p>
    </div>
    <div id="historyGrid" class="history-grid"></div>
    <div id="historyEmpty" class="history-empty" hidden>No predictions yet.</div>
  </div>

  <script src="script.js"></script>
</body>
</html>
