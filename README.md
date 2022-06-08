# EdgeRedirector
This short snippet of code is inspired by the work done by @da2x ([EdgeDeflector](https://github.com/da2x/EdgeDeflector)), the problem with his implementation is it apparently got blocked by Microsoft.  
Microsoft should theoretically never be able to block my implementation since I basically pretending to be Microsoft Edge by replacing the executable.  Now I am not familiar enough with all the different ways Windows uses "microsoft-edge:" protocol, but will look to cover all the possibilities (some of which will result in actually passing it to Microsoft Edge).

# Compiling
If you are skeptical of downloading executable and would rather compile it yourself, follow the instruction:
1. Download msedge.py
2. Open the terminal
3. Navigate to where you saved msedge.py
4. Execute "pyinstaller --noconsole --onefile .\msedge.py"
5. Resulting "msedge.exe" will be placed under "dist" directory

# Installation

1. Download the latest version of EdgeRedirector from [GitHub releases](https://github.com/hhsiao/EdgeRedirector/releases)
6. Navigate to where Microsoft Edge is installed (should be "C:\Program Files (x86)\Microsoft\Edge\Application")
7. Rename the original "msedge.exe" to "msedge-old.exe"
8. Move the "msedge.exe" you downloaded to the directory

