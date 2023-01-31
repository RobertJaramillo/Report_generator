from fpdf import FPDF
import matplotlib.pyplot as plt


class PDF(FPDF):

    logo_path = ""
    report_name = ""
    header_text = ""

    def set_logo_path(self, path=""):
        '''Sets the path to the logo file 

           -path - The path to the file being used for the logo
        '''

        self.logo_path = path
        return 0

    def set_report_name(self, name=""):
        '''Sets the default report name 
           name - the name of the report to be generated 
        '''
        self.report_name =  name

    def set_title(self, title=""):
        '''Sets the title that will be used in the headers and footers
           title -The title used in the footer
        '''
        self.header_text = title

    def create_cover_page(self, title=None):
        '''Creates a cover page of a report based on the given inputs
    
           Args: 
           text - The text to be displayed  
        '''        

        if title is None: 
            return -1


        self.add_page()
        self.cell(80, 200)
        self.cell(210,10, title.upper(), 0)
        self.ln()
        
        return 0

    def header(self):
        
        if self.header_text != "": 
            self.cell(0, 0, self.header_text)
        if self.logo_path != "":
            self.image(self.logo_path, 180 ,5, 30)
        
        self.ln()
        self.ln()
            
        return 0

    def create_section_heading(self, text=None):
        '''Creates a section heading in the pdf. 
    
           Args: 
           text - The text to be displayed  
        '''
        if text is None:
           print("No text")
           return -1
        
        
        self.cell(210, 10, text.upper(), 0)
        self.ln()
        
        return 0

    def create_paragraph(self, text=None):
        '''Creates a paragraph in the pdf. 
    
           Args: 
           text - The text to be displayed  
        '''
        if text is None:
            return 0 

        self.ln()
        self.write(5, text, '')
        self.ln()
        
        return 0

    def add_image(self, path=None):
        '''Adds a image to the pdf. 
    
           Args: 
           text - The text to be displayed  
        '''
        if path is None:  
            print("Please specify a valid path")
            return -1
        
        self.ln()
        self.image(name=path)
        return 0

    def add_vertical_bar_graph(self, title=None, label_vals=None, data_vals=None, 
                               x_label=None, y_label=None, width=2, height=2.2, MyDpi=120):
        '''Creates a vertical bar graph in the pdf. 
    
           Args: 
           title - The title of the chart
           label_vals - The values for the various labels of the graph
           data_vals - The data being charted 
           x_label - The charts x-label
           y_label - The charts y-label
           width - Width of the charts in inches 
           Heigth - Heigth  of the charts in inches 
           MyDpi - The DPI for the rendering of the chart  
        '''
        if label_vals is None:
            print("Labes must be specified and cannot be None")
            return -1
        if data_vals is None: 
            print("Values must be specified and cannot be None")
            return -1
        if width is None or height is None:
            print("Please specify the width and heigth of the graph")
            return -1
        if MyDpi is None:
            print("Please specify the dpi of the image")
            return -1
        if title is None:
            print("A title must be specified")
            return -1

        plt.figure(figsize=(width, height), dpi=MyDpi)
        plt.bar(label_vals, data_vals)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.tight_layout()
        file_name = title+'.png'
        plt.savefig(file_name)
        self.add_image(file_name)
        
        return 0

    def add_horizontal_bar_graph(self, title=None, label_vals=None, data_vals=None, 
                                 x_label=None, y_label=None, width=3, height=2, MyDpi=120):
        '''Creates a horizontal bar graph in the pdf. 
    
           Args: 
           title - The title of the chart
           label_vals - The values for the various labels of the graph
           data_vals - The data being charted 
           x_label - The charts x-label
           y_label - The charts y-label
           width - Width of the charts in inches 
           Heigth - Heigth  of the charts in inches 
           MyDpi - The DPI for the rendering of the chart  
        '''
        if label_vals is None:
            print("Labes must be specified and cannot be None")
            return -1
        if data_vals is None: 
            print("Values must be specified and cannot be None")
            return -1
        if width is None or height is None:
            print("Please specify the width and heigth of the graph")
        if MyDpi is None:
            return  -1
            print("Please specify the dpi of the image")
        if title is None:
            print("A title must be specified")
            return  -1

        plt.figure(figsize=(width, height), dpi=MyDpi)
        plt.barh(label_vals, data_vals)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.tight_layout()
        file_name = title+'.png'
        plt.savefig(file_name)
        self.add_image(file_name)
        
        return 0

    def add_pie_chart(self, title=None, chart_labels=None, values=None, width=3, height=2, MyDpi=120):
        '''Creates a pie chart in the pdf. 
    
           Args: 
           title - The title of the chart
           chart_labels - The values for the various labels of the graph
           values - The data being charted 
           width - Width of the charts in inches 
           Heigth - Heigth  of the charts in inches 
           MyDpi - The DPI for the rendering of the chart  
        '''

        if chart_labels is None:  
           print("Labels, cannot be none and must be specified.")
           return -1
        if values is None:
           print("Values, cannot be none and must be specified.")
           return -1
        if len(chart_labels) != len(values):
           print("The number of labels must match the number of values entered. ")
           return -1
        if title is None:
           print("A title needs to be provided")
           return -1 

        plt.figure(figsize=(width, height), dpi=MyDpi)
        plt.title(title)
        plt.pie(values, labels=chart_labels)
        file_name = title+'.png'
        plt.savefig(file_name)
        self.add_image(file_name)

        return 0
    
    def add_line_chart(self, title=None, x_label='', y_label='', label_vals=None, data_vals=None,
                       width=3, height=2, MyDpi=120):
        '''Creates a line graph in the pdf. 
    
           Args: 
           title - The title of the chart
           label_vals - The values for the various labels of the graph
           data_vals - The data being charted 
           x_label - The charts x-label
           y_label - The charts y-label
           width - Width of the charts in inches 
           Heigth - Heigth  of the charts in inches 
           MyDpi - The DPI for the rendering of the chart  
        '''

        if title is None:
           print("A title needs to be provided")
           return -1
        if label_vals is None:
           print("A title needs to be provided")
           return -1
        if data_vals is None:
           print("A title needs to be provided")
           return -1
        if len(label_vals) != len(data_vals):
           print("The number of labels must match the number of values entered. ")
           return -1

        plt.figure(figsize=(width, height), dpi=MyDpi)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.plot(label_vals, data_vals)
        file_name = title+'.png'
        plt.savefig(file_name)
        self.add_image(file_name)

        return 0


    def add_histogram(self, title=None, x_label='', y_label='', data=None,
                       width=3, height=2, MyDpi=120):
        '''Creates a line graph in the pdf. 
    
           Args: 
           title - The title of the chart
           label_vals - The values for the various labels of the graph
           data_vals - The data being charted 
           x_label - The charts x-label
           y_label - The charts y-label
           width - Width of the charts in inches 
           Heigth - Heigth  of the charts in inches 
           MyDpi - The DPI for the rendering of the chart  
        '''

        if title is None:
           print("A title needs to be provided")
           return -1
        if data is None:
           print("A title needs to be provided")
           return -1

        plt.figure(figsize=(width, height), dpi=MyDpi)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.hist(data)
        file_name = title+'.png'
        plt.savefig(file_name)
        self.add_image(file_name)

        return 0
