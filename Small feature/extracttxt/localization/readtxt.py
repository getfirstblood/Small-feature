import os

check_path = '.'
out_path = '..'
debug_str = '#define new DEBUG_NEW'
report_log = 'report_debug_new_check.log'
out_file = "out.txt"
config_file = "config.txt"
check_ext = '.txt'
report_list = []
out_list = []
config_list = []

def check_file(fp):
    if check_ext not in fp:
        return
        
    #out_list2 = []
    lines = 0;
    f = open(fp, 'r')
    try:
        for line in f.readlines():
        	out_list.append(line)
        	lines += 1
        #out_list2.append("\n\n\n");
        #lines += 2
        #print len(out_list2)
        config_list.append(str(lines) + '#' + str(fp) + '\n');
    finally:
        f.close()
        #f = open(fp, 'r+w')
        #f.writelines(out_list2)
    

def walk_dir(dirname):
    try:
        sub_items = os.listdir(dirname)
    except:
        print 'Access denied:', dirname
    else:
        for item in sub_items:
            full_path = os.path.join(dirname, item)
            if os.path.isdir(full_path):
                walk_dir(full_path)
            else:
                check_file(full_path)

 
if __name__ == "__main__":
    if os.path.isdir(check_path):
        check_path += '/'
    walk_dir(check_path)
    log_file = open(os.path.join(out_path, report_log), 'w')
    out_file = open(os.path.join(out_path, out_file), 'w')
    config_file = open(os.path.join(out_path, config_file), 'w')
    try:
        log_file.writelines(report_list)
        out_file.writelines(out_list)
        config_file.writelines(config_list)
        
    finally:
        log_file.close()
