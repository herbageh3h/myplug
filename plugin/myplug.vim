let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

if exists('g:myplug_loaded')
    finish
endif

let g:myplug_loaded = 1

python3<<EOF
import sys
from os.path import normpath, join
import vim

plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python3'))
sys.path.insert(0, python_root_dir)

import hello
EOF

function! PrintCountry()
    python3 hello.print_country()
endfunction
command! -nargs=0 PrintCountry call PrintCountry()

function! InsertMarker()
    python3 hello.insert_marker()
endfunction
command! -nargs=0 InsertMarker call InsertMarker()

nnoremap <Leader>sop :source %<CR>
