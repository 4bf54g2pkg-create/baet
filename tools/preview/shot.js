const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const w = Number(process.argv[2]||390), name = process.argv[3]||'m';
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: w, height: 844 }, deviceScaleFactor: 1 });
  p.on('pageerror', e => console.log('PAGEERROR', e.message));
  await p.goto('file://' + __dirname + '/page.html'); await p.waitForTimeout(800);
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const sw = await p.evaluate(() => document.documentElement.scrollWidth);
  console.log('height', h, 'scrollWidth', sw);
  await p.screenshot({ path: name + '.png', fullPage: true });
  await b.close();
})();
