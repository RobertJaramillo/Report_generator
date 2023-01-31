from report_builder import PDF

def main():
    myReport = PDF(report_name="Testing.pdf", logo_path="./Logo.png")
    myReport.set_title("COMAPNY NAME - REPORT DATE")
   
    myReport.create_cover_page("This is the cover page")
    myReport.create_section_heading("SECTION")
    myReport.create_paragraph("This is what a paragraph would look like.  ")
   
    myReport.add_vertical_bar_graph(title='test', label_vals=['Cat', 'Dog', 'Bird'],
                                    data_vals=[0,1,2], height=4, width=3, x_label="Animal",
                                    y_label="Quantity" )
    myReport.ln()
    myReport.add_horizontal_bar_graph(title='test2', label_vals=['Cat', 'Dog', 'Bird'],
                                     data_vals=[0,1,2], height=1, width=3, x_label="Animal",
                                     y_label="Quantity" )
    myReport.ln()
    myReport.add_pie_chart(title='test3', chart_labels=["CAT", "DOG", "BIRD", "PLANE"], values=[2,4,5,7])
    myReport.add_line_chart(title='test4', label_vals=["CAT", "DOG", "BIRD", "PLANE"], data_vals=[2,4,5,7])
    myReport.add_histogram(title='test5', data=[2,2,3,7,4,4,5,7])

    data = [['JOHN', 6, 'CAT'],
            ['DAVE', 3, 'DOG'], 
            ['SARAH', 6, 'BIRD']]
    
    cols = ['OWNER', 'AGE', 'ANIMAL']

    myReport.create_table(data=data, col_names=cols)

    myReport.output(myReport.report_name)
    return


if __name__ == "__main__":
    main()