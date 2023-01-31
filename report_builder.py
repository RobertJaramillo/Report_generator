from fpdf import FPDF
import matplotlib.pyplot as plt


class PDF(FPDF):

    logo_path = ""
    report_name = ""
    header_text = ""

    def __init__(self, report_name= "", logo_path="", title_font_size=14, paragraph_font_size=12, font_family='Arial'):
        super().__init__()

        if report_name == "":
            print("You must specify a report name")
        
        else: 
            self.report_name = report_name

        self.title_font_size = title_font_size
        self.paragraph_font_size = paragraph_font_size
        self.font_family = font_family
        self.logo_path = logo_path

        plt.rc('font', size=8)# Set the axes title font size
        plt.rc('axes', titlesize=6)# Set the axes labels font size
        plt.rc('axes', labelsize=6)# Set the font size for x tick labels
        plt.rc('xtick', labelsize=6)# Set the font size for y tick labels
        plt.rc('ytick', labelsize=6)# Set the legend font size
        plt.rc('legend', fontsize=8)# Set the font size of the figure legend
        plt.rc('figure', titlesize=16)# Set the font size of the figure title


        self.set_font(family=self.font_family)

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
        self.set_top_margin(0)
        self.add_page()
        
        self.set_xy(80, 125)
        self.set_font(family=self.font_family, style='B')
        self.cell(210,10, title.upper(), 0)
        self.set_font(family=self.font_family, style='')
        self.add_page()
        
        return 0

    def header(self):
        ''' Creates the header for our report to include our company name and the logo
        '''
        self.set_font(family=self.font_family, style='B', size=self.title_font_size)
        

        if self.header_text != "": 
            self.cell(0, 20, self.header_text)
        if self.logo_path != "":
            self.image(self.logo_path, 161 ,0, 50, 15)
        self.line(10, 15, 210, 15) 
        self.set_y(20)
            
        return 0

    def create_section_heading(self, heading=None, line_height=5):
        '''Creates a section heading in the pdf. 
    
           Args: 
           text - The text to be displayed  
           heading - The heading we are giving our section 
           line_height - The hieght of the text line we are going to be writing
        '''
        if heading is None:
           print("No heading provided")
           return -1
        
        self.set_font(family=self.font_family, style='BU')       
        self.write(line_height, heading.upper())
        self.ln()
        self.set_font(family=self.font_family, style='')       

        return 0

    def create_paragraph(self, text=None):
        '''Creates a paragraph in the pdf. 
    
           Args: 
           text - The text to be displayed  
        '''
        if text is None:
            return 0 
        
        self.ln()
        self.set_font(family=self.font_family, style='')    
        self.write(5, text)
        
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

    def create_table(self, data=None, col_names=None, data_font_size=8, column_font_size=14):
        '''Creates a table with rows consisting of the data passed in and column names consisting 
           of information in col_names. The assumptiopn is data is given as an array of rows 
           with each row containing the data for each column.

           data - The data we want placed in our rows 
           col_names - The names of the columns in our table    
        '''

        if data is None or len(data) == 0: 
            print("Create table received no data")
            return -1 
        if col_names is None or len(col_names) == 0: 
            print("Create table received no data")
            return -1 

        self.ln()
        self.ln()

        # Get the width of the pdf so we can appropriately divide our tabels cells
        effective_page_width = self.w - 2*self.l_margin

        # Get the width for each individual column
        col_width =  effective_page_width/len(col_names)

        #Set the text height to the same size as the current font size
        text_height = self.font_size_pt

        self.set_text_color(r=255, g=255, b=255)
        self.set_fill_color(r=30,g=60,b=84)
        self.set_font(size=column_font_size, family=self.font_family, style='')
        for col in col_names:
            self.cell(col_width, text_height,  str(col), border=1, align='C', fill=True)
        
        self.set_text_color(r=0, g=0, b=0)
        self.set_fill_color(r=188,g=227,b=222)
        self.set_font(size=data_font_size, family=self.font_family, style='')
        index = 0
        for row in data:
            self.ln()
            
            for item in row:
               if (index%2) == 0: 
                   self.cell(col_width, text_height,  str(item), border=1, align='C', fill=True)
               else:
                   self.cell(col_width, text_height,  str(item), border=1, align='C', fill=False)
            index += 1
               

        return 0