from report_builder import ReportGenerator

def main():
    myReport = ReportGenerator(name="Yes.pdf")
    myReport.create_cover_page()
    myReport.create_section_heading("Title")
    myReport.add_vertical_bar_graph(title='test', label_vals=['Cat', 'Dog', 'Bird'],
                                    data_vals=[0,1,2], height=3, width=2, x_label="Animal",
                                    y_label="Quantity" )
    myReport.add_horizontal_bar_graph(title='test2', label_vals=['Cat', 'Dog', 'Bird'],
                                    data_vals=[0,1,2], height=1, width=3, x_label="Animal",
                                    y_label="Quantity" )
    
    myReport.add_pie_chart(title='test3', chart_labels=["CAT", "DOG", "BIRD", "PLANE"], values=[2,4,5,7])
    myReport.add_line_chart(title='test4', label_vals=["CAT", "DOG", "BIRD", "PLANE"], data_vals=[2,4,5,7])
    myReport.add_histogram(title='test5', data=[2,2,3,7,4,4,5,7])
    #myReport.add_image(path="./test.png")
    myReport.generate_pdf()
    return


if __name__ == "__main__":
    main()