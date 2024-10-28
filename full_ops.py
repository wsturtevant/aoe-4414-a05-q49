#full_ops
#
# Usage: python3 full_ops.py c_in n_wv
#
# Arguments:
#   c_in: input channel count
#   n_wv: number of weight vectors
#
# Written by Wheat Sturtevant
# Other contributors: None

# import Python modules
import math # math module
import sys  # argv

# "constants"
w = 7.292115*10**-5

# initialize script arguments
c_in = float('nan')  
n_wv = float('nan')

# parse script arguments (always 1 more than the number of arguments)
if len(sys.argv) == 3:
    c_in = float(sys.argv[1])
    n_wv = float(sys.argv[2])
else:
    print(\
        'python3 conv_ops.py c_in n_wv'\
        )
    exit()

# write script below this line
c_out = n_wv
h_out = 1
w_out = 1
adds = n_wv*c_in
mults = n_wv*c_in
divs = 0

print(int(c_out))   # channel count
print(int(h_out))   # height count
print(int(w_out))   # width count
print(int(adds))    # additions performed
print(int(mults))   # multiplications performed
print(int(divs))    # divisions performed

# Test usage:
# python3 full_ops.py c_in n_wv