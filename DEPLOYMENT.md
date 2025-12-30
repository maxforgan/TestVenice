# Deployment Guide - Venice AI Interface

## GitHub Pages Deployment

Since I can't directly push to the `gh-pages` branch due to branch protection, here's how to deploy manually:

### Option 1: Enable GitHub Pages via Web Interface (Easiest)

1. Go to your repository on GitHub: `https://github.com/maxforgan/TestVenice`

2. Click on **Settings** (top right)

3. Scroll down to **Pages** in the left sidebar

4. Under "Build and deployment":
   - **Source**: Select "Deploy from a branch"
   - **Branch**: Select `claude/venice-api-interface-5iKhx`
   - **Folder**: Select `/ (root)`

5. Click **Save**

6. Wait 1-2 minutes for GitHub to build and deploy

7. Your site will be available at:
   ```
   https://maxforgan.github.io/TestVenice/
   ```

8. Bookmark this URL on your mobile device!

### Option 2: Create a Main Branch and Deploy from There

If you prefer a cleaner setup, merge the changes to a main branch:

```bash
# Create and switch to main branch
git checkout -b main

# Push main branch
git push -u origin main

# Then configure GitHub Pages to use the 'main' branch
```

### Option 3: Use GitHub Actions (Automated)

I can create a GitHub Actions workflow that automatically deploys to GitHub Pages:

```yaml
# .github/workflows/deploy.yml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ claude/venice-api-interface-5iKhx ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: .
```

Would you like me to set this up?

## Alternative Deployment Options

### Netlify (Very Easy, Drag & Drop)

1. Go to [netlify.com](https://netlify.com)
2. Sign up/login with GitHub
3. Click "Add new site" → "Import an existing project"
4. Select your GitHub repository
5. Deploy settings:
   - **Branch**: `claude/venice-api-interface-5iKhx`
   - **Build command**: (leave empty)
   - **Publish directory**: `.`
6. Click "Deploy"
7. Your site will be live at a netlify.app URL
8. You can customize the subdomain or add a custom domain

### Vercel (Also Very Easy)

1. Go to [vercel.com](https://vercel.com)
2. Sign up/login with GitHub
3. Click "Add New" → "Project"
4. Import your GitHub repository
5. Configure:
   - **Framework Preset**: Other
   - **Root Directory**: `.`
   - **Build Command**: (leave empty)
   - **Output Directory**: `.`
6. Click "Deploy"
7. Your site will be live at a vercel.app URL

### Cloudflare Pages

1. Go to [pages.cloudflare.com](https://pages.cloudflare.com)
2. Sign up/login
3. Click "Create a project" → "Connect to Git"
4. Select your repository
5. Configure build settings:
   - **Build command**: (leave empty)
   - **Build output directory**: `.`
6. Click "Save and Deploy"

## After Deployment

Once deployed, you can:

1. **Access from any device**: The URL works on desktop, mobile, tablet
2. **Add to mobile home screen**:
   - iOS: Safari → Share → Add to Home Screen
   - Android: Chrome → Menu → Add to Home screen
3. **Share with others**: Anyone can use it (with their own API key)
4. **Custom domain** (optional): Most hosting services support custom domains

## Security Note

When deployed publicly:
- The interface is accessible to anyone
- Users must provide their own Venice API key
- API keys are stored only in the browser's localStorage
- No API keys are sent to the hosting server
- Always use HTTPS hosting (automatic with GitHub Pages, Netlify, Vercel)

## Need Help?

Let me know which deployment option you'd prefer, and I can provide more detailed guidance or set up automated deployment for you!
