import streamlit as st
import streamlit.components.v1 as com

  <title>TFF Audio Moderation</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <style>
    body {
      background-color: #b2d8d8;
      font-family: Arial, sans-serif;
    }
    
    .container {
      max-width: 500px;
      margin-top: 80px;
    }
    
    .logo {
      max-width: 150px;
      height: auto;
      margin-bottom: 20px;
    }
    
    .title {
      font-size: 32px;
      font-weight: bold;
      margin-top: 30px;
      margin-bottom: 30px;
      color: #333;
      text-shadow: 1px 1px 2px #888888;
    }
    
    .search-bar {
      background-color: #fff;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      align-items: center;
      margin-top: 30px;
    }
    
    .search-input {
      border: none;
      border-radius: 4px;
      padding: 10px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    
    .search-input:focus {
      outline: none;
      box-shadow: 0 0 0 2px #007bff;
    }
    
    .search-button {
      border-radius: 4px;
    }
    
    #output {
      display: none;
      background-color: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      margin-top: 30px;
    }
    
    .progress {
      height: 5px;
      margin-bottom: 0;
    }
    
    /* Custom Styles */
    .logo {
      filter: brightness(90%);
    }
    
    .search-bar {
      border: 1px solid #ddd;
    }
    
    .search-button {
      background-color: #007bff;
      border-color: #007bff;
      transition: all 0.3s ease-in-out;
    }
    
    .search-button:hover {
      background-color: #0056b3;
      border-color: #0056b3;
    }
    
    #output {
      border: 1px solid #ddd;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col-md-12 text-center">
        <img src="C:\Users\sudha\Downloads\logo.png" alt="Logo" class="logo">
        <h1 class="title">TFF Moderation</h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <div class="search-bar">
          <form>
            <div class="input-group">
              <input type="text" class="form-control search-input" placeholder="Enter URL of Youtube video" id="urlInput" oninput="checkInput()">
              <div class="input-group-append">
                <button class="btn btn-primary search-button" type="submit" id="searchButton" disabled>GO</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <div id="outputContainer">
          <div id="output"></div>
        </div>
      </div>
    </div>
  </div>

  <script>
    function checkInput() {
      var input = document.getElementById('urlInput').value;
      var searchButton = document.getElementById('searchButton');
      
      if (input.trim() !== '') {
        searchButton.disabled = false;
      } else {
        searchButton.disabled = true;
      }
    }
   
    document.getElementById('searchForm').addEventListener('submit', function(event) {
      event.preventDefault();
      generateOutput();
    });
    
    function generateOutput() {
      var outputContainer = document.getElementById('outputContainer');
      var output = document.getElementById('output');
      
      // Generate the output content here
      
      // Show the output container
      outputContainer.style.display = 'block';

      // Scroll to the output container
      outputContainer.scrollIntoView({ behavior: 'smooth' });
    }
  </script>
</body>
</html>

