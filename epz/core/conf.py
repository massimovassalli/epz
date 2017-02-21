# EPZ 1.0
# Configuration file object
# for internal use
# it parses the .conf file provided as a list of : separated names and values

class Conf(object):
  def __init__(self, fname=None):
    self.fname = fname
    self.defname = '/opt/epz.conf'
    self.data = {}
    if self.fname is not None:
      self.parse()

  def parse(self): #simplicistic conf format NAME:VALUE
    if self.fname is None:
      f = open(self.defname, 'r')
    else:
      f = open(self.fname, 'r')
    for line in f:
      if line[0] != '#':
        pre, post = line.strip().split(':')
        self.data[pre] = post
    f.close()

  def __iter__(self):
    self.n = 0
    return self

  def __next__(self):
    if self.n <= len(self.data) - 1:
      result = self.data[list(self.data.keys())[self.n]]
      self.n += 1
      return result
    else:
      raise StopIteration

  def __getitem__(self, item):
    if item in self.data.keys():
      return self.data[item]
    else:
      try:
        w = int(item)
        return self.data[list(self.data.keys())[w]]
      except:
        raise (KeyError)