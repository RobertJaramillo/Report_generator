from fpdf import FPDF
import matplotlib.pyplot as plt


class ReportGenerator: 
    
    def __init__(self, name, default_font_type='Arial',  default_font_size=22): 
        ''' Initialize the settings for the report  
        
            Args: 
            name - The name of the report
            default_font_type - The type of font to be used i.e. Arial, Times New Roman, etc
            default_font_size -  The size of the font to use for the report 

            return 
        '''
        self.name = name
        self.pdf =  FPDF(orientation='P', unit='in',  format='A4')

        self.pdf.set_font(default_font_type, '', default_font_size)
        # Set the default text font size
        plt.rc('font', size=8)# Set the axes title font size
        plt.rc('axes', titlesize=6)# Set the axes labels font size
        plt.rc('axes', labelsize=6)# Set the font size for x tick labels
        plt.rc('xtick', labelsize=6)# Set the font size for y tick labels
        plt.rc('ytick', labelsize=6)# Set the legend font size
        plt.rc('legend', fontsize=8)# Set the font size of the figure title
        plt.rc('figure', titlesize=16)

    def create_cover_page(self, text=None):
        '''Creates a cover page of a report based on the given inputs
    
           Args: 
           text - The text to be displayed  
        '''
        if text is None: 
            return -1

        self.pdf.add_page()
        self.pdf.cell(210,10, 'Cover Page', 0)
        self.pdf.ln()
        self.pdf.ln()
        return 0

    def generate_pdf(self, name='output.pdf'):
        '''Generates the PDF and saves it as the given name.
           Note it will be saved in the same directory as 
           being run. 
    
           Args: 
           text - The text to be displayed  
        '''
        self.pdf.output(name, 'F')

        return 0

    def create_section_heading(self, text=None):
        '''Creates a section heading in the pdf. 
    
           Args: 
           text - The text to be displayed  
        '''
        if text is None:
           print("No text")
           return -1
        
        self.pdf.add_page()
        self.pdf.cell(210, 10, text, 0)
        self.pdf.ln()
        self.pdf.ln()

        return 0

    def create_paragraph(self, text=None):
        '''Creates a paragraph in the pdf. 
    
           Args: 
           text - The text to be displayed  
        '''
        if text is None:
            return 0 

        self.pdf.ln()
        self.pdf.write(5, text, '')
        self.pdf.ln()
        self.pdf.ln()

        return 0

    def add_image(self, path=None):
        '''Adds a image to the pdf. 
    
           Args: 
           text - The text to be displayed  
        '''
        if path is None:  
            print("Please specify a valid path")
            return -1
        
        self.pdf.ln()
        self.pdf.image(name=path)
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
