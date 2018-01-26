# encoding: utf-8
# module caffe._caffe
# from /usr/local/caffe/python/caffe/_caffe.so
# by generator 1.145
# no doc

# imports
import Boost.Python as __Boost_Python


# Variables with simple values

__version__ = '1.0.0'

# functions

def get_solver(p_str, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    get_solver( (str)arg1) -> Solver :
    
        C++ signature :
            caffe::Solver<float>* get_solver(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
    """
    pass

def has_nccl(): # real signature unknown; restored from __doc__
    """
    has_nccl() -> bool :
    
        C++ signature :
            bool has_nccl()
    """
    return False

def init_log(): # real signature unknown; restored from __doc__
    """
    init_log() -> None :
    
        C++ signature :
            void init_log()
    
    init_log( (int)arg1) -> None :
    
        C++ signature :
            void init_log(int)
    
    init_log( (int)arg1, (bool)arg2) -> None :
    
        C++ signature :
            void init_log(int,bool)
    """
    pass

def layer_type_list(): # real signature unknown; restored from __doc__
    """
    layer_type_list() -> StringVec :
    
        C++ signature :
            std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > layer_type_list()
    """
    return StringVec

def log(p_str, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    log( (str)arg1) -> None :
    
        C++ signature :
            void log(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
    """
    pass

def set_device(p_int, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_device( (int)arg1) -> None :
    
        C++ signature :
            void set_device(int)
    """
    pass

def set_mode_cpu(): # real signature unknown; restored from __doc__
    """
    set_mode_cpu() -> None :
    
        C++ signature :
            void set_mode_cpu()
    """
    pass

def set_mode_gpu(): # real signature unknown; restored from __doc__
    """
    set_mode_gpu() -> None :
    
        C++ signature :
            void set_mode_gpu()
    """
    pass

def set_multiprocess(bool, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_multiprocess( (bool)arg1) -> None :
    
        C++ signature :
            void set_multiprocess(bool)
    """
    pass

def set_random_seed(p_int, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_random_seed( (int)arg1) -> None :
    
        C++ signature :
            void set_random_seed(unsigned int)
    """
    pass

def set_solver_count(p_int, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_solver_count( (int)arg1) -> None :
    
        C++ signature :
            void set_solver_count(int)
    """
    pass

def set_solver_rank(p_int, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_solver_rank( (int)arg1) -> None :
    
        C++ signature :
            void set_solver_rank(int)
    """
    pass

def solver_count(): # real signature unknown; restored from __doc__
    """
    solver_count() -> int :
    
        C++ signature :
            int solver_count()
    """
    return 0

def solver_rank(): # real signature unknown; restored from __doc__
    """
    solver_rank() -> int :
    
        C++ signature :
            int solver_rank()
    """
    return 0

# classes

class Solver(__Boost_Python.instance):
    # no doc
    def add_callback(self, Solver, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        add_callback( (Solver)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void add_callback(caffe::Solver<float>*,boost::python::api::object,boost::python::api::object)
        
        add_callback( (Solver)arg1) -> None :
        
            C++ signature :
                void add_callback(caffe::Solver<float>*)
        """
        pass

    def restore(self, Solver, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        restore( (Solver)arg1, (str)arg2) -> None :
        
            C++ signature :
                void restore(caffe::Solver<float> {lvalue},char const*)
        """
        pass

    def share_weights(self, Solver, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        share_weights( (Solver)arg1, (Net)arg2) -> None :
        
            C++ signature :
                void share_weights(caffe::Solver<float>*,caffe::Net<float>*)
        """
        pass

    def snapshot(self, Solver, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        snapshot( (Solver)arg1) -> None :
        
            C++ signature :
                void snapshot(caffe::Solver<float> {lvalue})
        """
        pass

    def solve(self, Solver, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        solve( (Solver)arg1 [, (str)arg2]) -> None :
        
            C++ signature :
                void solve(caffe::Solver<float> {lvalue} [,char const*])
        """
        pass

    def step(self, Solver, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        step( (Solver)arg1, (int)arg2) -> None :
        
            C++ signature :
                void step(caffe::Solver<float> {lvalue},int)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    iter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    net = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    param = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    test_nets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class AdaDeltaSolver(Solver):
    # no doc
    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1, (str)arg2) -> None :
        
            C++ signature :
                void __init__(_object*,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __instance_size__ = 32


class AdaGradSolver(Solver):
    # no doc
    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1, (str)arg2) -> None :
        
            C++ signature :
                void __init__(_object*,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __instance_size__ = 32


class AdamSolver(Solver):
    # no doc
    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1, (str)arg2) -> None :
        
            C++ signature :
                void __init__(_object*,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __instance_size__ = 32


class Blob(__Boost_Python.instance):
    # no doc
    def reshape(self, tuple_args, dict_kwds): # real signature unknown; restored from __doc__
        """
        object reshape(tuple args, dict kwds) :
        
            C++ signature :
                object reshape(tuple args, dict kwds)
        """
        return object()

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    channels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    diff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BlobVec(__Boost_Python.instance):
    # no doc
    def add_blob(self, tuple_args, dict_kwds): # real signature unknown; restored from __doc__
        """
        object add_blob(tuple args, dict kwds) :
        
            C++ signature :
                object add_blob(tuple args, dict kwds)
        """
        return object()

    def append(self, BlobVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        append( (BlobVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(std::vector<boost::shared_ptr<caffe::Blob<float> >, std::allocator<boost::shared_ptr<caffe::Blob<float> > > > {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, BlobVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        extend( (BlobVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void extend(std::vector<boost::shared_ptr<caffe::Blob<float> >, std::allocator<boost::shared_ptr<caffe::Blob<float> > > > {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, BlobVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __contains__( (BlobVec)arg1, (object)arg2) -> bool :
        
            C++ signature :
                bool __contains__(std::vector<boost::shared_ptr<caffe::Blob<float> >, std::allocator<boost::shared_ptr<caffe::Blob<float> > > > {lvalue},_object*)
        """
        pass

    def __delitem__(self, BlobVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __delitem__( (BlobVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(std::vector<boost::shared_ptr<caffe::Blob<float> >, std::allocator<boost::shared_ptr<caffe::Blob<float> > > > {lvalue},_object*)
        """
        pass

    def __getitem__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<std::vector<boost::shared_ptr<caffe::Blob<float> >, std::allocator<boost::shared_ptr<caffe::Blob<float> > > >&>,_object*)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        """
        pass

    def __iter__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_value_policy<boost::python::return_by_value, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<boost::shared_ptr<caffe::Blob<float> >*, std::vector<boost::shared_ptr<caffe::Blob<float> >, std::allocator<boost::shared_ptr<caffe::Blob<float> > > > > > __iter__(boost::python::back_reference<std::vector<boost::shared_ptr<caffe::Blob<float> >, std::allocator<boost::shared_ptr<caffe::Blob<float> > > >&>)
        """
        pass

    def __len__(self, BlobVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __len__( (BlobVec)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(std::vector<boost::shared_ptr<caffe::Blob<float> >, std::allocator<boost::shared_ptr<caffe::Blob<float> > > > {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, BlobVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __setitem__( (BlobVec)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(std::vector<boost::shared_ptr<caffe::Blob<float> >, std::allocator<boost::shared_ptr<caffe::Blob<float> > > > {lvalue},_object*,_object*)
        """
        pass

    __instance_size__ = 40


class BoolVec(__Boost_Python.instance):
    # no doc
    def append(self, BoolVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        append( (BoolVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(std::vector<bool, std::allocator<bool> > {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, BoolVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        extend( (BoolVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void extend(std::vector<bool, std::allocator<bool> > {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, BoolVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __contains__( (BoolVec)arg1, (object)arg2) -> bool :
        
            C++ signature :
                bool __contains__(std::vector<bool, std::allocator<bool> > {lvalue},_object*)
        """
        pass

    def __delitem__(self, BoolVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __delitem__( (BoolVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(std::vector<bool, std::allocator<bool> > {lvalue},_object*)
        """
        pass

    def __getitem__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<std::vector<bool, std::allocator<bool> >&>,_object*)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        """
        pass

    def __iter__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_value_policy<boost::python::return_by_value, boost::python::default_call_policies>, std::_Bit_iterator> __iter__(boost::python::back_reference<std::vector<bool, std::allocator<bool> >&>)
        """
        pass

    def __len__(self, BoolVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __len__( (BoolVec)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(std::vector<bool, std::allocator<bool> > {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, BoolVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __setitem__( (BoolVec)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(std::vector<bool, std::allocator<bool> > {lvalue},_object*,_object*)
        """
        pass

    __instance_size__ = 56


class DtypeVec(__Boost_Python.instance):
    # no doc
    def append(self, DtypeVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        append( (DtypeVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(std::vector<float, std::allocator<float> > {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, DtypeVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        extend( (DtypeVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void extend(std::vector<float, std::allocator<float> > {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, DtypeVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __contains__( (DtypeVec)arg1, (object)arg2) -> bool :
        
            C++ signature :
                bool __contains__(std::vector<float, std::allocator<float> > {lvalue},_object*)
        """
        pass

    def __delitem__(self, DtypeVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __delitem__( (DtypeVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(std::vector<float, std::allocator<float> > {lvalue},_object*)
        """
        pass

    def __getitem__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<std::vector<float, std::allocator<float> >&>,_object*)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        """
        pass

    def __iter__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_value_policy<boost::python::return_by_value, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<float*, std::vector<float, std::allocator<float> > > > __iter__(boost::python::back_reference<std::vector<float, std::allocator<float> >&>)
        """
        pass

    def __len__(self, DtypeVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __len__( (DtypeVec)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(std::vector<float, std::allocator<float> > {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, DtypeVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __setitem__( (DtypeVec)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(std::vector<float, std::allocator<float> > {lvalue},_object*,_object*)
        """
        pass

    __instance_size__ = 40


class IntVec(__Boost_Python.instance):
    # no doc
    def append(self, IntVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        append( (IntVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(std::vector<int, std::allocator<int> > {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, IntVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        extend( (IntVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void extend(std::vector<int, std::allocator<int> > {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, IntVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __contains__( (IntVec)arg1, (object)arg2) -> bool :
        
            C++ signature :
                bool __contains__(std::vector<int, std::allocator<int> > {lvalue},_object*)
        """
        pass

    def __delitem__(self, IntVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __delitem__( (IntVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(std::vector<int, std::allocator<int> > {lvalue},_object*)
        """
        pass

    def __getitem__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<std::vector<int, std::allocator<int> >&>,_object*)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        """
        pass

    def __iter__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_value_policy<boost::python::return_by_value, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<int*, std::vector<int, std::allocator<int> > > > __iter__(boost::python::back_reference<std::vector<int, std::allocator<int> >&>)
        """
        pass

    def __len__(self, IntVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __len__( (IntVec)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(std::vector<int, std::allocator<int> > {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, IntVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __setitem__( (IntVec)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(std::vector<int, std::allocator<int> > {lvalue},_object*,_object*)
        """
        pass

    __instance_size__ = 40


class Layer(__Boost_Python.instance):
    # no doc
    def reshape(self, Layer, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        reshape( (Layer)arg1, (RawBlobVec)arg2, (RawBlobVec)arg3) -> None :
        
            C++ signature :
                void reshape(caffe::Layer<float> {lvalue},std::vector<caffe::Blob<float>*, std::allocator<caffe::Blob<float>*> >,std::vector<caffe::Blob<float>*, std::allocator<caffe::Blob<float>*> >)
        """
        pass

    def setup(self, Layer, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        setup( (Layer)arg1, (RawBlobVec)arg2, (RawBlobVec)arg3) -> None :
        
            C++ signature :
                void setup(caffe::Layer<float> {lvalue},std::vector<caffe::Blob<float>*, std::allocator<caffe::Blob<float>*> >,std::vector<caffe::Blob<float>*, std::allocator<caffe::Blob<float>*> >)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1, (LayerParameter)arg2) -> None :
        
            C++ signature :
                void __init__(_object*,caffe::LayerParameter)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    blobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __instance_size__ = 32


class LayerParameter(__Boost_Python.instance):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass


class LayerVec(__Boost_Python.instance):
    # no doc
    def append(self, LayerVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        append( (LayerVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(std::vector<boost::shared_ptr<caffe::Layer<float> >, std::allocator<boost::shared_ptr<caffe::Layer<float> > > > {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, LayerVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        extend( (LayerVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void extend(std::vector<boost::shared_ptr<caffe::Layer<float> >, std::allocator<boost::shared_ptr<caffe::Layer<float> > > > {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, LayerVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __contains__( (LayerVec)arg1, (object)arg2) -> bool :
        
            C++ signature :
                bool __contains__(std::vector<boost::shared_ptr<caffe::Layer<float> >, std::allocator<boost::shared_ptr<caffe::Layer<float> > > > {lvalue},_object*)
        """
        pass

    def __delitem__(self, LayerVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __delitem__( (LayerVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(std::vector<boost::shared_ptr<caffe::Layer<float> >, std::allocator<boost::shared_ptr<caffe::Layer<float> > > > {lvalue},_object*)
        """
        pass

    def __getitem__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<std::vector<boost::shared_ptr<caffe::Layer<float> >, std::allocator<boost::shared_ptr<caffe::Layer<float> > > >&>,_object*)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        """
        pass

    def __iter__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_value_policy<boost::python::return_by_value, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<boost::shared_ptr<caffe::Layer<float> >*, std::vector<boost::shared_ptr<caffe::Layer<float> >, std::allocator<boost::shared_ptr<caffe::Layer<float> > > > > > __iter__(boost::python::back_reference<std::vector<boost::shared_ptr<caffe::Layer<float> >, std::allocator<boost::shared_ptr<caffe::Layer<float> > > >&>)
        """
        pass

    def __len__(self, LayerVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __len__( (LayerVec)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(std::vector<boost::shared_ptr<caffe::Layer<float> >, std::allocator<boost::shared_ptr<caffe::Layer<float> > > > {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, LayerVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __setitem__( (LayerVec)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(std::vector<boost::shared_ptr<caffe::Layer<float> >, std::allocator<boost::shared_ptr<caffe::Layer<float> > > > {lvalue},_object*,_object*)
        """
        pass

    __instance_size__ = 40


class NCCL(__Boost_Python.instance):
    # no doc
    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1, (Solver)arg2, (str)arg3) -> None :
        
            C++ signature :
                void __init__(_object*,boost::shared_ptr<caffe::Solver<float> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __instance_size__ = 32


class NesterovSolver(Solver):
    # no doc
    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1, (str)arg2) -> None :
        
            C++ signature :
                void __init__(_object*,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __instance_size__ = 32


class Net(__Boost_Python.instance):
    # no doc
    def after_backward(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        after_backward( (Net)arg1 [, (object)arg2]) -> None :
        
            C++ signature :
                void after_backward(caffe::Net<float>* [,boost::python::api::object])
        """
        pass

    def after_forward(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        after_forward( (Net)arg1, (object)arg2) -> None :
        
            C++ signature :
                void after_forward(caffe::Net<float>*,boost::python::api::object)
        """
        pass

    def backward(self, *args, **kwargs): # real signature unknown
        """
        Backward pass: prepare diffs and run the net backward.
        
            Parameters
            ----------
            diffs : list of diffs to return in addition to bottom diffs.
            kwargs : Keys are output blob names and values are diff ndarrays.
                    If None, top diffs are taken from forward loss.
            start : optional name of layer at which to begin the backward pass
            end : optional name of layer at which to finish the backward pass
                (inclusive)
        
            Returns
            -------
            outs: {blob name: diff ndarray} dict.
        """
        pass

    def before_backward(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        before_backward( (Net)arg1, (object)arg2) -> None :
        
            C++ signature :
                void before_backward(caffe::Net<float>*,boost::python::api::object)
        """
        pass

    def before_forward(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        before_forward( (Net)arg1, (object)arg2) -> None :
        
            C++ signature :
                void before_forward(caffe::Net<float>*,boost::python::api::object)
        """
        pass

    def clear_param_diffs(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        clear_param_diffs( (Net)arg1) -> None :
        
            C++ signature :
                void clear_param_diffs(caffe::Net<float> {lvalue})
        """
        pass

    def copy_from(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        copy_from( (Net)arg1, (str)arg2) -> None :
        
            C++ signature :
                void copy_from(caffe::Net<float> {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def forward(self, *args, **kwargs): # real signature unknown
        """
        Forward pass: prepare inputs and run the net forward.
        
            Parameters
            ----------
            blobs : list of blobs to return in addition to output blobs.
            kwargs : Keys are input blob names and values are blob ndarrays.
                     For formatting inputs for Caffe, see Net.preprocess().
                     If None, input is taken from data layers.
            start : optional name of layer at which to begin the forward pass
            end : optional name of layer at which to finish the forward pass
                  (inclusive)
        
            Returns
            -------
            outs : {blob name: blob ndarray} dict.
        """
        pass

    def forward_all(self, *args, **kwargs): # real signature unknown
        """
        Run net forward in batches.
        
            Parameters
            ----------
            blobs : list of blobs to extract as in forward()
            kwargs : Keys are input blob names and values are blob ndarrays.
                     Refer to forward().
        
            Returns
            -------
            all_outs : {blob name: list of blobs} dict.
        """
        pass

    def forward_backward_all(self, *args, **kwargs): # real signature unknown
        """
        Run net forward + backward in batches.
        
            Parameters
            ----------
            blobs: list of blobs to extract as in forward()
            diffs: list of diffs to extract as in backward()
            kwargs: Keys are input (for forward) and output (for backward) blob names
                    and values are ndarrays. Refer to forward() and backward().
                    Prefilled variants are called for lack of input or output blobs.
        
            Returns
            -------
            all_blobs: {blob name: blob ndarray} dict.
            all_diffs: {blob name: diff ndarray} dict.
        """
        pass

    def load_hdf5(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        load_hdf5( (Net)arg1, (str)arg2) -> None :
        
            C++ signature :
                void load_hdf5(caffe::Net<float>*,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def reshape(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        reshape( (Net)arg1) -> None :
        
            C++ signature :
                void reshape(caffe::Net<float> {lvalue})
        """
        pass

    def save(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        save( (Net)arg1, (str)arg2) -> None :
        
            C++ signature :
                void save(caffe::Net<float>,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def save_hdf5(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        save_hdf5( (Net)arg1, (str)arg2) -> None :
        
            C++ signature :
                void save_hdf5(caffe::Net<float>,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def set_input_arrays(self, *args, **kwargs): # real signature unknown
        """
        Set input arrays of the in-memory MemoryDataLayer.
            (Note: this is only for networks declared with the memory data layer.)
        """
        pass

    def share_with(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        share_with( (Net)arg1, (Net)arg2) -> None :
        
            C++ signature :
                void share_with(caffe::Net<float> {lvalue},caffe::Net<float> const*)
        """
        pass

    def _backward(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        _backward( (Net)arg1, (int)arg2, (int)arg3) -> None :
        
            C++ signature :
                void _backward(caffe::Net<float> {lvalue},int,int)
        """
        pass

    def _batch(self, *args, **kwargs): # real signature unknown
        """
        Batch blob lists according to net's batch size.
        
            Parameters
            ----------
            blobs: Keys blob names and values are lists of blobs (of any length).
                   Naturally, all the lists should have the same length.
        
            Yields
            ------
            batch: {blob name: list of blobs} dict for a single batch.
        """
        pass

    def _bottom_ids(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        _bottom_ids( (Net)arg1, (int)arg2) -> IntVec :
        
            C++ signature :
                std::vector<int, std::allocator<int> > _bottom_ids(caffe::Net<float> {lvalue},int)
        """
        pass

    def _forward(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        _forward( (Net)arg1, (int)arg2, (int)arg3) -> float :
        
            C++ signature :
                float _forward(caffe::Net<float> {lvalue},int,int)
        """
        pass

    def _set_input_arrays(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        _set_input_arrays( (Net)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void _set_input_arrays(caffe::Net<float>*,boost::python::api::object,boost::python::api::object)
        """
        pass

    def _top_ids(self, Net, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        _top_ids( (Net)arg1, (int)arg2) -> IntVec :
        
            C++ signature :
                std::vector<int, std::allocator<int> > _top_ids(caffe::Net<float> {lvalue},int)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1, (str)network_file, (int)phase [, (int)level=0 [, (object)stages=None [, (object)weights=None]]]) -> object :
        
            C++ signature :
                void* __init__(boost::python::api::object,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,int [,int=0 [,boost::python::api::object=None [,boost::python::api::object=None]]])
        
        __init__( (object)arg1, (str)arg2, (str)arg3, (int)arg4) -> object :
        
            C++ signature :
                void* __init__(boost::python::api::object,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,int)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    blobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    An OrderedDict (bottom to top, i.e., input to output) of network
    blobs indexed by name
    """

    blob_loss_weights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    An OrderedDict (bottom to top, i.e., input to output) of network
    blob loss weights indexed by name
    """

    bottom_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inputs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layer_dict = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    An OrderedDict (bottom to top, i.e., input to output) of network
    layers indexed by name
    """

    outputs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    params = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    An OrderedDict (bottom to top, i.e., input to output) of network
    parameters indexed by name; each is a list of multiple blobs (e.g.,
    weights and biases)
    """

    top_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _blobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _blob_loss_weights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _blob_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _inputs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _layer_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _outputs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class NetVec(__Boost_Python.instance):
    # no doc
    def append(self, NetVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        append( (NetVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(std::vector<boost::shared_ptr<caffe::Net<float> >, std::allocator<boost::shared_ptr<caffe::Net<float> > > > {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, NetVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        extend( (NetVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void extend(std::vector<boost::shared_ptr<caffe::Net<float> >, std::allocator<boost::shared_ptr<caffe::Net<float> > > > {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, NetVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __contains__( (NetVec)arg1, (object)arg2) -> bool :
        
            C++ signature :
                bool __contains__(std::vector<boost::shared_ptr<caffe::Net<float> >, std::allocator<boost::shared_ptr<caffe::Net<float> > > > {lvalue},_object*)
        """
        pass

    def __delitem__(self, NetVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __delitem__( (NetVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(std::vector<boost::shared_ptr<caffe::Net<float> >, std::allocator<boost::shared_ptr<caffe::Net<float> > > > {lvalue},_object*)
        """
        pass

    def __getitem__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<std::vector<boost::shared_ptr<caffe::Net<float> >, std::allocator<boost::shared_ptr<caffe::Net<float> > > >&>,_object*)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        """
        pass

    def __iter__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_value_policy<boost::python::return_by_value, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<boost::shared_ptr<caffe::Net<float> >*, std::vector<boost::shared_ptr<caffe::Net<float> >, std::allocator<boost::shared_ptr<caffe::Net<float> > > > > > __iter__(boost::python::back_reference<std::vector<boost::shared_ptr<caffe::Net<float> >, std::allocator<boost::shared_ptr<caffe::Net<float> > > >&>)
        """
        pass

    def __len__(self, NetVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __len__( (NetVec)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(std::vector<boost::shared_ptr<caffe::Net<float> >, std::allocator<boost::shared_ptr<caffe::Net<float> > > > {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, NetVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __setitem__( (NetVec)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(std::vector<boost::shared_ptr<caffe::Net<float> >, std::allocator<boost::shared_ptr<caffe::Net<float> > > > {lvalue},_object*,_object*)
        """
        pass

    __instance_size__ = 40


class RawBlobVec(__Boost_Python.instance):
    # no doc
    def append(self, RawBlobVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        append( (RawBlobVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(std::vector<caffe::Blob<float>*, std::allocator<caffe::Blob<float>*> > {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, RawBlobVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        extend( (RawBlobVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void extend(std::vector<caffe::Blob<float>*, std::allocator<caffe::Blob<float>*> > {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, RawBlobVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __contains__( (RawBlobVec)arg1, (object)arg2) -> bool :
        
            C++ signature :
                bool __contains__(std::vector<caffe::Blob<float>*, std::allocator<caffe::Blob<float>*> > {lvalue},_object*)
        """
        pass

    def __delitem__(self, RawBlobVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __delitem__( (RawBlobVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(std::vector<caffe::Blob<float>*, std::allocator<caffe::Blob<float>*> > {lvalue},_object*)
        """
        pass

    def __getitem__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<std::vector<caffe::Blob<float>*, std::allocator<caffe::Blob<float>*> >&>,_object*)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        """
        pass

    def __iter__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_value_policy<boost::python::return_by_value, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<caffe::Blob<float>**, std::vector<caffe::Blob<float>*, std::allocator<caffe::Blob<float>*> > > > __iter__(boost::python::back_reference<std::vector<caffe::Blob<float>*, std::allocator<caffe::Blob<float>*> >&>)
        """
        pass

    def __len__(self, RawBlobVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __len__( (RawBlobVec)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(std::vector<caffe::Blob<float>*, std::allocator<caffe::Blob<float>*> > {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, RawBlobVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __setitem__( (RawBlobVec)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(std::vector<caffe::Blob<float>*, std::allocator<caffe::Blob<float>*> > {lvalue},_object*,_object*)
        """
        pass

    __instance_size__ = 40


class RMSPropSolver(Solver):
    # no doc
    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1, (str)arg2) -> None :
        
            C++ signature :
                void __init__(_object*,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __instance_size__ = 32


class SGDSolver(Solver):
    # no doc
    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1, (str)arg2) -> None :
        
            C++ signature :
                void __init__(_object*,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __instance_size__ = 32


class SolverParameter(__Boost_Python.instance):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    display = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layer_wise_reduce = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_iter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class StringVec(__Boost_Python.instance):
    # no doc
    def append(self, StringVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        append( (StringVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, StringVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        extend( (StringVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void extend(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, StringVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __contains__( (StringVec)arg1, (object)arg2) -> bool :
        
            C++ signature :
                bool __contains__(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > {lvalue},_object*)
        """
        pass

    def __delitem__(self, StringVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __delitem__( (StringVec)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > {lvalue},_object*)
        """
        pass

    def __getitem__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&>,_object*)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        """
        pass

    def __iter__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_value_policy<boost::python::return_by_value, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > > __iter__(boost::python::back_reference<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&>)
        """
        pass

    def __len__(self, StringVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __len__( (StringVec)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, StringVec, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __setitem__( (StringVec)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > {lvalue},_object*,_object*)
        """
        pass

    __instance_size__ = 40


class Timer(__Boost_Python.instance):
    # no doc
    def start(self, Timer, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        start( (Timer)arg1) -> None :
        
            C++ signature :
                void start(caffe::Timer {lvalue})
        """
        pass

    def stop(self, Timer, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        stop( (Timer)arg1) -> None :
        
            C++ signature :
                void stop(caffe::Timer {lvalue})
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    ms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __instance_size__ = 32


