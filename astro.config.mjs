import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

const SITE_URL = 'https://socialsecuritybronx.com';

export default defineConfig({
  site: SITE_URL,
  integrations: [
    sitemap({ changefreq: 'weekly', priority: 0.7, lastmod: new Date() }),
  ],
  build: { format: 'directory' },
  compressHTML: true,
});
