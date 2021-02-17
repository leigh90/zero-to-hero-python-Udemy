from pack import my_func
from mypackage.mainscript import report_main
from mypackage.mysubpackage.subscript import sub_report

my_func()
report_main()
sub_report()

# OR
from mypackage import mainscript
from mypackage.mysubpackage import subscript

mainscript.report_main()
subscript.sub_report()


