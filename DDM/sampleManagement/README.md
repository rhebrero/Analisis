# how to transfer files from EOS cern to CIEMAT

1. use `copyNTuplesCIEMAT.py` script to rsync files from eos cern to pnfs, by default it copies the ['NTuples', 'rNTuples'] directories from 
    '/eos/cms/store/group/phys_exotica/displacedMuons/' to '/pnfs/ciemat.es/data/cms/store/user/escalant/displacedMuons/' and it does not 
    delete the files in the target directory (not present in the source directory).

    ```python
    # dry run
    python copyNTuplesCIEMAT.py -debug
    # actual run
    python copyNTuplesCIEMAT.py 
    ```

