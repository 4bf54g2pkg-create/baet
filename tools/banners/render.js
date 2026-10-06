// Rendert banners: node render.js <html> <width> <height> <out.png> [scale]
const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const [f, w, h, out, sc] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: +(sc || 1) });
  await p.goto('file://' + f); await p.waitForTimeout(800);
  await p.screenshot({ path: out });
  await b.close();
})();
