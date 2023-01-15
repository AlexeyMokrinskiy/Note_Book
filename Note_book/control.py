import base_creator as b_c
import data_collector as d_c
import veiw_line_base as vlb
import veiw_column_base as vcb
import export_in_file as eif
import menu

def choise():
    num = menu.user_choise()
    if num == 1:
        data = d_c.input_data()
        b_c.line_type_base(data)
        b_c.column_type_base(data)
    if num == 2:
        vlb.view_lb()
    if num == 3:
        vcb.view_cb()
    if num == 4:
        eif.export_txt()

