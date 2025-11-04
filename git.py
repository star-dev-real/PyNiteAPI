import os
import subprocess
import sys
from pathlib import Path

def run_command(command, cwd=None):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def setup_git():
    """Automatically set up Git repository and push to GitHub"""
    
    
    repo_url = "https://github.com/star-dev-real/PyNiteAPI.git"
    project_path = Path(__file__).parent  
    
    print("🚀 Starting Git automation...")
    print(f"📁 Project path: {project_path}")
    print(f"🔗 Repository: {repo_url}")
    print("-" * 50)
    
    
    print("1. Initializing Git repository...")
    returncode, stdout, stderr = run_command("git init", project_path)
    if returncode == 0:
        print("   ✅ Git repository initialized")
    else:
        print(f"   ❌ Failed to initialize: {stderr}")
        return
    
    
    gitignore_path = project_path / ".gitignore"
    if not gitignore_path.exists():
        print("2. Creating .gitignore file...")
        gitignore_content = """
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/


.vscode/
.idea/
*.swp
*.swo


.DS_Store
Thumbs.db


*.log


.env
*.env


.ipynb_checkpoints


*.tmp
*.temp
"""
        with open(gitignore_path, 'w') as f:
            f.write(gitignore_content)
        print("   ✅ .gitignore created")
    else:
        print("   ✅ .gitignore already exists")
    
    
    print("3. Adding files to Git...")
    returncode, stdout, stderr = run_command("git add .", project_path)
    if returncode == 0:
        print("   ✅ Files added to staging area")
    else:
        print(f"   ❌ Failed to add files: {stderr}")
        return
    
    
    returncode, stdout, stderr = run_command("git status --porcelain", project_path)
    if not stdout.strip():
        print("   ℹ️  No changes to commit")
        
    else:
        
        print("4. Committing changes...")
        returncode, stdout, stderr = run_command('git commit -m "Initial commit: PyNite Backend API"', project_path)
        if returncode == 0:
            print("   ✅ Changes committed")
        else:
            print(f"   ❌ Failed to commit: {stderr}")
            
            returncode, stdout, stderr = run_command('git commit -m "Auto commit"', project_path)
            if returncode == 0:
                print("   ✅ Changes committed with alternative message")
            else:
                print(f"   ❌ Still failed: {stderr}")
                return
    
    
    print("5. Setting up remote repository...")
    returncode, stdout, stderr = run_command(f'git remote add origin {repo_url}', project_path)
    if returncode == 0:
        print("   ✅ Remote origin added")
    else:
        
        if "already exists" in stderr:
            print("   ℹ️  Remote origin already exists")
        else:
            print(f"   ❌ Failed to add remote: {stderr}")
            return
    
    
    print("6. Setting up branch...")
    returncode, stdout, stderr = run_command("git branch --show-current", project_path)
    current_branch = stdout.strip()
    
    if current_branch != "main":
        returncode, stdout, stderr = run_command("git branch -M main", project_path)
        if returncode == 0:
            print("   ✅ Branch renamed to 'main'")
        else:
            print(f"   ❌ Failed to rename branch: {stderr}")
    
    
    print("7. Pushing to GitHub...")
    returncode, stdout, stderr = run_command("git push -u origin main", project_path)
    
    if returncode == 0:
        print("   ✅ Successfully pushed to GitHub!")
        print("🎉 Your repository is now live at: https://github.com/star-dev-real/PyNiteAPI")
    else:
        
        print(f"   ⚠️  First push failed: {stderr}")
        response = input("   Try force push? (y/n): ").lower().strip()
        if response == 'y':
            returncode, stdout, stderr = run_command("git push -u origin main --force", project_path)
            if returncode == 0:
                print("   ✅ Successfully force-pushed to GitHub!")
            else:
                print(f"   ❌ Force push also failed: {stderr}")
        else:
            print("   ℹ️  You may need to resolve conflicts manually")

def check_git_installed():
    """Check if Git is installed on the system"""
    returncode, stdout, stderr = run_command("git --version")
    return returncode == 0

if __name__ == "__main__":
    print("PyNite Git Automation Script")
    print("=" * 40)
    
    
    if not check_git_installed():
        print("❌ Git is not installed or not in PATH")
        print("Please install Git from: https://git-scm.com/")
        sys.exit(1)
    
    
    try:
        setup_git()
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
    
    print("\nScript completed!")