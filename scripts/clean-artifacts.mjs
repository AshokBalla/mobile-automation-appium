import fs from 'node:fs';
for (const dir of ['reports', 'screenshots']) {
  fs.mkdirSync(dir, { recursive: true });
}
