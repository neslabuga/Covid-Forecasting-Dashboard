import pickle
import plotly.graph_objects as go

def generate_covid_deaths_graph():
    try:
        fig_pickle_filename = 'graph_figure.pkl'

        with open(fig_pickle_filename, 'rb') as fig_file:
            loaded_fig = pickle.load(fig_file)

        fig = go.Figure()

        for ax in loaded_fig.get_axes():
            for line in ax.get_lines():
                fig.add_trace(go.Scatter(
                    x=line.get_xdata(),
                    y=line.get_ydata(),
                    mode='lines',
                    name=line.get_label()
                ))

        graph_json = fig.to_json()
        return graph_json

    except Exception as e:
        print(f"Error generating graph: {e}")
        raise

def generate_covid_cases_graph(model, horizon):
    try:
        fig_pickle_filename = f'{model}_{horizon}.pkl'
        
        with open(fig_pickle_filename, 'rb') as file:
            loaded_fig = pickle.load(file)

        fig = go.Figure()

        for ax in loaded_fig.get_axes():
            for line in ax.get_lines():
                fig.add_trace(go.Scatter(
                    x=line.get_xdata(),
                    y=line.get_ydata(),
                    mode='lines',
                    name=line.get_label()
                ))

        fig.update_layout(
            title="Covid 19 Weekly Forecast",
            xaxis_title="Days",
            yaxis_title='new_cases',
            legend_title="Legend"
        )

        pickle_file_path = 'PatchTST_horizon1_results.pkl'
        
        with open(pickle_file_path, 'rb') as f:
            best_results = pickle.load(f)
        
        data_summary = []

        for model_run, results in best_results.items():
            realMAE = results.get('average_realMAE', 'N/A')
            mae = results.get('average_MAE', 'N/A')
            smape = results.get('average_smape', 'N/A')

            if isinstance(realMAE, list) and realMAE != 'N/A':
                best_realMAE = min(realMAE)
            else:
                best_realMAE = realMAE

            if isinstance(mae, list) and mae != 'N/A':
                best_MAE = min(mae)
            else:
                best_MAE = mae

            if isinstance(smape, list) and smape != 'N/A':
                best_sMAPE = min(smape)
            else:
                best_sMAPE = smape

            data_summary.append({
                'model_run': model_run.split(' ')[0],
                'best_realMAE': best_realMAE,
                'best_MAE': best_MAE,
                'best_sMAPE': best_sMAPE,
                'realMAE_list': realMAE,
                'mae_list': mae,
                'smape_list': smape
            })

        graph_json = fig.to_json()
        return graph_json, data_summary

    except Exception as e:
        print(f"Error generating COVID cases graph: {e}")
        raise
