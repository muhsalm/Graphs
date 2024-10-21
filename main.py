from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
import matplotlib.pyplot as plt
import numpy as np

class GraphPlotterApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.x_input = TextInput(hint_text="Enter X Values (comma-separated)", text="A, B, C, D")
        self.y_input = TextInput(hint_text="Enter Y Values (comma-separated)", text="2, 3, 5, 7")
        self.graph_title_input = TextInput(hint_text="Enter Title of the Graph", text="My Graph Title")
        self.x_axis_title_input = TextInput(hint_text="Enter Title for X-Axis", text="X Axis Title")
        self.y_axis_title_input = TextInput(hint_text="Enter Title for Y-Axis", text="Y Axis Title")

        self.graph_type_spinner = Spinner(
            text='Select Graph Type',
            values=["Line", "Bar", "Scatter", "Area", "Histogram", "Pie", "Box"]
        )

        self.plot_button = Button(text="Plot Graph")
        self.plot_button.bind(on_press=self.plot_graph)

        self.layout.add_widget(self.x_input)
        self.layout.add_widget(self.y_input)
        self.layout.add_widget(self.graph_title_input)
        self.layout.add_widget(self.x_axis_title_input)
        self.layout.add_widget(self.y_axis_title_input)
        self.layout.add_widget(self.graph_type_spinner)
        self.layout.add_widget(self.plot_button)

        return self.layout

    def plot_graph(self, instance):
        x_values = self.x_input.text.split(",")
        y_values = np.array(list(map(float, self.y_input.text.split(","))))
        
        if len(x_values) != len(y_values):
            print("Error: The number of X values must match the number of Y values.")
            return
        
        norm = plt.Normalize(y_values.min(), y_values.max())
        colors = plt.cm.Blues(norm(y_values))

        plt.figure(facecolor='black')
        plt.gca().set_facecolor('black')

        graph_type = self.graph_type_spinner.text

        if graph_type == "Line":
            plt.plot(x_values, y_values, color='blue', linewidth=2)
        elif graph_type == "Bar":
            plt.bar(x_values, y_values, color=colors)
        elif graph_type == "Scatter":
            plt.scatter(x_values, y_values, color=colors)
        elif graph_type == "Area":
            plt.fill_between(x_values, y_values, color='blue', alpha=0.5)
        elif graph_type == "Histogram":
            plt.hist(y_values, bins=len(y_values), color='blue', alpha=0.7)
        elif graph_type == "Pie":
            plt.pie(y_values, labels=x_values, colors=colors, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
        elif graph_type == "Box":
            plt.boxplot(y_values)
            plt.xticks([1], [self.x_axis_title_input.text])

        plt.xlabel(self.x_axis_title_input.text, color='white')
        plt.ylabel(self.y_axis_title_input.text, color='white')
        plt.title(self.graph_title_input.text, color='white')
        plt.xticks(color='white')
        plt.yticks(color='white')
        plt.ylim(y_values.min() - 1, y_values.max() + 1)

        plt.show()

if __name__ == '__main__':
    GraphPlotterApp().run()
