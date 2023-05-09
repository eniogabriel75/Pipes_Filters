def turma(search, filter):
  new_search = []
  for x in search:
      if x["turma"] == filter:
          new_search.append(x)
  return new_search