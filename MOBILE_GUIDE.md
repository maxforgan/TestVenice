# Venice AI Mobile Setup Guide

## Using the Web Interface on Mobile

The Venice AI web interface is fully mobile-responsive and works great on smartphones and tablets!

### Quick Setup Options

#### Option 1: Access from Same WiFi Network

1. On your computer, start the local server:
   ```bash
   cd /path/to/TestVenice
   python3 -m http.server 8000
   ```

2. Find your computer's local IP address:
   ```bash
   # Linux/Mac:
   hostname -I | awk '{print $1}'
   # Or on Mac:
   ipconfig getifaddr en0
   # Windows:
   ipconfig
   ```

3. On your mobile device, open a browser and navigate to:
   ```
   http://YOUR-IP-ADDRESS:8000
   ```
   Example: `http://192.168.1.100:8000`

4. Configure your API key in Settings and start using Venice AI!

#### Option 2: Deploy to GitHub Pages (Recommended)

Host the interface online for access from anywhere:

1. Push your code to GitHub (already done!)

2. Enable GitHub Pages:
   - Go to your repository settings
   - Navigate to "Pages" section
   - Select branch: `claude/venice-api-interface-5iKhx`
   - Select folder: `/ (root)`
   - Click "Save"

3. Access your interface at:
   ```
   https://YOUR-USERNAME.github.io/TestVenice/
   ```

4. Bookmark this URL on your mobile device for easy access!

#### Option 3: Use Other Free Hosting Services

Deploy `index.html` to any of these services:
- **Netlify**: Drag and drop deployment
- **Vercel**: Connect your GitHub repo
- **Cloudflare Pages**: Free hosting with custom domains
- **GitHub Gist**: Quick single-page hosting

### Mobile-Specific Tips

**Security Considerations:**
- Your API key is stored only in your browser's localStorage
- Never share your hosted URL with your API key already configured
- Use HTTPS hosting (like GitHub Pages) for better security

**Performance:**
- Image generation works well but may take longer on mobile data
- Chat is very responsive and works great on mobile
- Consider using WiFi for image generation to save data

**Browser Compatibility:**
- Works on Safari (iOS)
- Works on Chrome (Android/iOS)
- Works on Firefox Mobile
- Works on Samsung Internet

### Troubleshooting Mobile Access

**Can't connect to local server:**
- Ensure your mobile device and computer are on the same WiFi network
- Check if your computer's firewall is blocking port 8000
- Try using your computer's hostname instead of IP address

**API calls failing:**
- Make sure you've entered your API key in the Settings tab
- Check that you have internet connection
- Verify your API key is valid at venice.ai

**Page not loading after deployment:**
- Wait a few minutes for GitHub Pages to build (first time)
- Clear your mobile browser cache
- Try accessing in incognito/private mode first

### Creating a Home Screen Shortcut (iOS/Android)

Make it feel like a native app:

**On iOS:**
1. Open the page in Safari
2. Tap the Share button
3. Select "Add to Home Screen"
4. Name it "Venice AI"
5. Tap "Add"

**On Android:**
1. Open the page in Chrome
2. Tap the menu (three dots)
3. Select "Add to Home screen"
4. Name it "Venice AI"
5. Tap "Add"

Now you have a Venice AI app icon on your home screen!
