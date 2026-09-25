# Module 1 — Git & GitHub

**Student:** Delos Santos, Junelle
**Date:** 9/25/2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is a tool that tracks our changes in our code, it is useful because you can go back to older versions if something goes wrong.
GitHub on the other hand is a website that allows us to collaborate with other developers because it stores the Git repositories online. 
---

## Key vocabulary (in your own words)

- repository: repository is where you store your files and this is also where Git history is stored.
- commit: commit is when you want to save the changes you made
- branch: think of it as a tree, and from the word itself, “branch,” you can imagine a branch growing separately from the main trunk. In Git, a branch is a separate line of development where you can work on new features or changes without affecting the main branch.
- push / pull: push sends your local changes to remote repository while pull gets the remote changes to your local computer. Push is like offline to online and pull is like online to offline.
- pull request: a request to have your changes reviewed and potentially merged into another branch.
- merge conflict: merge conflict is when you are trying to merge branches or changes, but Git cannot automatically merge them. That is when Git need a human input to identify which changes you want to keep.

---

## Walking through what I did

I created a Git repository for my practice project and created a branch called practice-branch. I made changes to my project and committed them to save the changes. Then, I tried to push my branch to GitHub. Git showed an error because my practice-branch did not have an upstream branch yet. I fixed this by setting the GitHub repository as the upstream branch and successfully pushing practice-branch to GitHub. After pushing the branch, I created a pull request on GitHub to propose merging my changes from practice-branch into the master branch. 

```
# paste your actual commands here
```
git init
git add .
git commit -m "practice"
git switch -c practice-branch
git branch
git push https://github.com/delossantosjunelle18-rgb/practice-repository
git push --set-upstream https://github.com/delossantosjunelle18-rgb/practice-repository
git push --set-upstream https://github.com/delossantosjunelle18-rgb/practice-repository.git
git push --set-upstream https://github.com/delossantosjunelle18-rgb/practice-repository.git practice-branch
---

## A mistake I made (or one I want to avoid)

## A mistake I made (or one I want to avoid)

One mistake I made was when I tried to push my practice-branch to GitHub without setting an upstream branch. Git showed an error saying that the current branch had no upstream branch. At first, I was confused about what this meant, but I learned that I needed to tell Git which remote repository and branch my local practice-branch should track. I fixed the problem by using the command git push --set-upstream followed by the GitHub repository URL and practice-branch. 

---

## How this connects to something else

This connects to programming because I can use Git and GitHub when working on my coding projects. It can help me organize my work, share my projects, and work with other people.
