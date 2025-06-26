# Automated script to clean up Git repository and rename folders with proper zero-padding
Write-Host "Starting Git repository cleanup and folder renaming..." -ForegroundColor Green

# Step 1: Remove all old folder references from Git (the ones that were deleted)
Write-Host "Removing old folder references from Git..." -ForegroundColor Yellow
git rm -r --cached Day1 2>$null
git rm -r --cached Day2 2>$null
git rm -r --cached Day3 2>$null
git rm -r --cached Day4 2>$null
git rm -r --cached Day5 2>$null
git rm -r --cached Day6 2>$null
git rm -r --cached Day7 2>$null
git rm -r --cached Day8 2>$null
git rm -r --cached Day9 2>$null
git rm -r --cached Day10 2>$null
git rm -r --cached Day11 2>$null
git rm -r --cached Day12 2>$null

# Step 2: Rename single-digit day folders to use zero-padding
Write-Host "Renaming folders with zero-padding..." -ForegroundColor Yellow

$foldersToRename = @(
    @{Old="Day_1"; New="Day_01"},
    @{Old="Day_2"; New="Day_02"},
    @{Old="Day_3"; New="Day_03"},
    @{Old="Day_4"; New="Day_04"},
    @{Old="Day_5"; New="Day_05"},
    @{Old="Day_6"; New="Day_06"},
    @{Old="Day_7"; New="Day_07"},
    @{Old="Day_8"; New="Day_08"},
    @{Old="Day_9"; New="Day_09"}
)

foreach ($folder in $foldersToRename) {
    if (Test-Path $folder.Old) {
        Write-Host "Renaming $($folder.Old) to $($folder.New)..." -ForegroundColor Cyan
        Rename-Item $folder.Old $folder.New
    } else {
        Write-Host "Folder $($folder.Old) not found, skipping..." -ForegroundColor Red
    }
}

# Step 3: Add all current folders to Git
Write-Host "Adding all folders to Git..." -ForegroundColor Yellow
git add .

# Step 4: Commit the changes
Write-Host "Committing changes..." -ForegroundColor Yellow
git commit -m "Fix folder naming: rename Day_X to Day_0X for proper sorting and remove old folder references"

# Step 5: Show the current status
Write-Host "Current Git status:" -ForegroundColor Green
git status

Write-Host "`nFolder renaming and Git cleanup completed!" -ForegroundColor Green
Write-Host "Your folders are now properly ordered. Ready to push to GitHub!" -ForegroundColor Green 