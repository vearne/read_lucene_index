# -rw-r--r--  1 zhuwei  wheel  88347547  5 29 09:59 _2.fdt
# -rw-r--r--  1 zhuwei  wheel       124  5 29 09:59 _2.fdx
# -rw-r--r--  1 zhuwei  wheel        66  5 29 09:59 _2.fnm
# -rw-r--r--  1 zhuwei  wheel   1070778  5 29 09:59 _2.frq
# -rw-r--r--  1 zhuwei  wheel        36  5 29 09:59 _2.nrm
# -rw-r--r--  1 zhuwei  wheel   5545871  5 29 09:59 _2.prx
# -rw-r--r--  1 zhuwei  wheel    244672  5 29 09:59 _2.tii
# -rw-r--r--  1 zhuwei  wheel  18984879  5 29 09:59 _2.tis
# -rw-r--r--  1 zhuwei  wheel        83  5 29 09:59 _2.tvd
# -rw-r--r--  1 zhuwei  wheel  18188809  5 29 09:59 _2.tvf
# -rw-r--r--  1 zhuwei  wheel       244  5 29 09:59 _2.tvx
# -rw-r--r--  1 zhuwei  wheel        66  5 29 09:59 _3.fnm
# -rw-r--r--  1 zhuwei  wheel    106599  5 29 09:59 _3.frq
# -rw-r--r--  1 zhuwei  wheel        32  5 29 09:59 _3.nrm
# -rw-r--r--  1 zhuwei  wheel   1482925  5 29 09:59 _3.prx
# -rw-r--r--  1 zhuwei  wheel     22663  5 29 09:59 _3.tii
# -rw-r--r--  1 zhuwei  wheel   1849217  5 29 09:59 _3.tis
# -rw-r--r--  1 zhuwei  wheel        20  5 29 09:59 segments.gen
# -rw-r--r--  1 zhuwei  wheel       442  5 29 09:59 segments_3
# read segments.gen

filepath = "/var/tmp/index_dir/segments.gen"
import struct
from struct_utils import unpack_int, unpack_long
fp = open(filepath, 'r')
ss = fp.read()
fp.close()
print 'SegmentInfos.FORMAT_LOCKLESS', unpack_int(ss[0:4])
print 'generation', unpack_long(ss[4:12])

