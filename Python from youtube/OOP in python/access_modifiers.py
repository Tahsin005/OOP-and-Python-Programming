'''Public'''
# class ABC:
#     def __init__(self):
#         self.public_attribute = None # this is a public attribute

#     def public_functio(): # this is a public function
#         pass 

'''Private'''
# class ABC:
#     # just add two underscore
#     def __init__(self):
#         self.__private_attribute = None # this is a private attribute

#     def __private_functio(): # this is a private function
#         pass 

'''Protected'''
class ABC:
    # just add one underscore
    # should be accessed only from inside the class or
    # child of the class (after inheritance)
    def __init__(self):
        self._protected_attribute = None # this is a protected attribute

    def _protected_functio(): # this is a protected function
        pass 
