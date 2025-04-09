# Deployment Instructions for Latent Drifting Website

We've created a GitHub Pages website for the "Latent Drifting in Diffusion Models for Counterfactual Medical Image Synthesis" paper. The website is ready to be deployed to GitHub Pages, but requires GitHub authentication.

## Files Created

1. `index.html` - The main HTML file for the website
2. `style.css` - CSS styling for the website
3. `script.js` - JavaScript functionality for the website
4. `images/` - Directory for storing images (currently empty)
5. `README.md` - Information about the project
6. `deploy.sh` - Shell script for deployment

## Next Steps for Deployment

1. Create a GitHub repository named `latentdrifting.github.io` at https://github.com/organizations/latentdrifting/repositories/new
   - Make sure the repository is public
   - Initialize it without any files (no README, no .gitignore)

2. Authenticate with GitHub
   - Run `git config --global user.name "Your Name"`
   - Run `git config --global user.email "your.email@example.com"`
   - Set up a GitHub Personal Access Token or use SSH authentication

3. Push the repository to GitHub
   - The repository is already initialized locally
   - Files have been added and committed
   - The remote repository has been added
   - Run `git push -u origin master` after authentication is set up

4. Verify Deployment
   - After pushing, wait a few minutes for GitHub Actions to deploy the site
   - Visit https://latentdrifting.github.io/ to see the deployed website

## Additional Considerations

1. Add actual images from the paper to the `images/` directory
2. Update links in the website once the paper and code are published
3. Consider adding Google Analytics or other tracking to measure visitor engagement

## Manual Deployment Alternative

If direct Git push doesn't work, you can also:

1. Create the GitHub repository through the GitHub web interface
2. Upload the files manually through the GitHub web interface
3. Enable GitHub Pages in the repository settings (Settings → Pages)
   - Set the source branch to `master` or `main`
   - Save the settings to trigger the deployment