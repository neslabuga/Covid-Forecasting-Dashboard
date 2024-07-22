COVID-19 Forecast Evaluation Dashboard
This dashboard allows users to visualize and evaluate COVID-19 forecasts using various models. The current setup includes models like PatchTST, Dlinear, GRU, and NLinear.

Adding a New Model
To add a new model to the list, follow these steps:

1. Update the HTML File
Open the visualization.html file.
Locate the model selection dropdown menu (<select id="model-select">).
Add a new <option> element for the new model inside the dropdown.
html
Copy code
<select id="model-select">
  <option value="PatchTST">PatchTST</option>
  <option value="Dlinear">Dlinear</option>
  <option value="GRU">GRU</option>
  <option value="NLinear">NLinear</option>
  <!-- Add the new model here -->
  <option value="NewModel">NewModel</option>
</select>
2. Update the Data Generation Script
Open the load_graph.py file.
Ensure that the script can handle the new model by ensuring it has the correct file naming convention and processes the data correctly.
3. Prepare the Pickle Files
Create the necessary pickle files for the new model.
The file containing the graph data should be named using the pattern {model}_{horizon}.pkl (e.g., NewModel_horizon1.pkl).
The file containing the results data should be named using the pattern {model}_{horizon}_results.pkl (e.g., NewModel_horizon1_results.pkl).
4. Update the Flask Application
Open the app.py file.
Ensure the /load_covid_cases_analysis endpoint can handle the new model. The existing logic should be sufficient as long as the new model's pickle files follow the naming conventions.
5. Verify the Integration
Start the Flask application:
sh
Copy code
flask run
Open the dashboard in your web browser.
Select the new model from the dropdown menu and submit the form to verify that the graph and data summary are displayed correctly.