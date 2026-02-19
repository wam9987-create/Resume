from pathlib import Path
from datetime import datetime

OUTPUT = Path("contents.html")

# 수집 대상: 레포 전체
SEARCH_ROOT = Path("Resume")

# 제외할 파일/경로 패턴
EXCLUDE_NAMES = {"contents.html"}
EXCLUDE_DIRS = {".git", ".github"}  # 원하면 추가 가능

def should_exclude(path: Path) -> bool:
    # 제외 파일명
    if path.name in EXCLUDE_NAMES:
        return True
    # 제외 디렉토리 내부면 제외
    for part in path.parts:
        if part in EXCLUDE_DIRS:
            return True
    return False

def main():
    html_files = []
    for p in SEARCH_ROOT.rglob("*.html"):
        if p.is_file() and not should_exclude(p):
            html_files.append(p)

    # 파일명(상대경로 문자열) 기준 정렬
    html_files = sorted(html_files, key=lambda x: x.as_posix().lower())

    generated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    lines = []
    lines.append("<!doctype html>")
    lines.append("<html lang='ko'>")
    lines.append("<head>")
    lines.append("  <meta charset='utf-8'/>")
    lines.append("  <meta name='viewport' content='width=device-width, initial-scale=1'/>")
    lines.append("  <title>Contents</title>")
    lines.append("  <style>")
    lines.append("    body{font-family:system-ui,-apple-system,Segoe UI,Roboto,'Noto Sans KR',sans-serif;max-width:900px;margin:40px auto;padding:0 16px;line-height:1.6;}")
    lines.append("    h1{margin:0 0 10px 0;font-size:24px;}")
    lines.append("    .muted{color:#6b7280;font-size:13px;margin-bottom:18px;}")
    lines.append("    ul{padding-left:18px;}")
    lines.append("    li{margin:6px 0;}")
    lines.append("    a{text-decoration:none;border-bottom:1px solid rgba(0,0,0,0.12);color:#111;}")
    lines.append("    a:hover{border-bottom-color:rgba(0,0,0,0.3);}")
    lines.append("    code{background:rgba(0,0,0,0.04);padding:2px 6px;border-radius:8px;}")
    lines.append("  </style>")
    lines.append("</head>")
    lines.append("<body>")
    lines.append("  <h1>Contents</h1>")
    lines.append(f"  <div class='muted'>Generated: <code>{generated}</code> · Files: <code>{len(html_files)}</code></div>")
    lines.append("  <ul>")

    if not html_files:
        lines.append("    <li>(No HTML files found.)</li>")
    else:
        for p in html_files:
            rel = p.as_posix()
            lines.append(f"    <li><a href='{rel}'>{rel}</a></li>")

    lines.append("  </ul>")
    lines.append("</body></html>")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ Wrote {OUTPUT} with {len(html_files)} link(s).")

if __name__ == "__main__":
    main()

