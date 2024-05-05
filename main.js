const { app, BrowserWindow, Menu } = require('electron');
const { spawn } = require('child_process');
const path = require('path');

let mainWindow;
let djangoServerProcess;

function createWindow() {
  // Specify the working directory where the manage.py script is located
  const projectPath = 'D:\\Excella'; // Replace with the actual path

  // Create the main window
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
  });

  // Start the Django server as a child process with '0.0.0.0:8000'
  djangoServerProcess = spawn('python', ['manage.py', 'runserver', '127.0.0.1:8000'], { cwd: projectPath });

  // Load your Django app's URL or local HTML file here
  mainWindow.loadURL('http://127.0.0.1:8000'); // Run the Django server at '0.0.0.0:8000'

  // Create a menu template
  const template = [
    {
      label: 'File',
      submenu: [
        {
          label: 'Open',
          click: () => {
            // Implement open functionality here
          },
        },
        {
          label: 'Exit',
          click: () => {
            // Terminate the Django server process when the app is closed
            if (djangoServerProcess) {
              djangoServerProcess.kill();
            }
            app.quit(); // Close the app
          },
        },
      ],
    },
    // Add more menu items as needed
  ];

  // Create the menu from the template
  const menu = Menu.buildFromTemplate(template);

  // Set the menu for the app
  Menu.setApplicationMenu(menu);

  // Handle window closed event
  mainWindow.on('closed', () => {
    // Terminate the Django server process when the app is closed
    if (djangoServerProcess) {
      djangoServerProcess.kill();
    }
    mainWindow = null;
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});
