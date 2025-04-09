#!/bin/bash

# Initialize a new git repository
cd $(dirname "$0")
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit of Latent Drifting website"

# Add remote repository (will need to authenticate)
git remote add origin https://github.com/latentdrifting/latentdrifting.github.io.git

# Push to GitHub Pages
git push -u origin main

echo "Deployment script completed. If GitHub authentication is required, a prompt should have appeared."
echo "The website should be available at https://latentdrifting.github.io/ after a few minutes."