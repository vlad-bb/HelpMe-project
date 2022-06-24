from collections import UserDict


class Field:

  def __init__(self, value):
    self.value = value

  def __str_(self):
    return self.value

  def __repr__(self):
    return self.value

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self, value):
    self.__value = value


class Title(Field):

  @property
  def value(self) -> str:
    return self.__value

  @value.setter
  def value(self, value: str):
    max_title_length = 20

    if len(value) > max_title_length:
      raise AttributeError(f"The note title is too long, be sure it is less then {max_title_length} symbols")
    elif value[0].lower() in Translator.CYRILLIC_SYMBOLS:
      print("All cyrillic letters will be translated to latin:")
      self.__value = Translator(value).translate_text()


class Note(Field):

  @property
  def value(self) -> str:
    return self.__value

  @value.setter
  def value(self, value: str):
    self.__value = Translator(value).translate_text()


class Translator:
  CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"

  def __init__(self, text):
    self.text = text

  def translate_text(self):
    TRANSLATION = (
      "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
      "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")
    TRANS = {}

    CYRILLIC = tuple([char for char in self.CYRILLIC_SYMBOLS])

    for cyrillic, latin in zip(CYRILLIC, TRANSLATION):
      TRANS[ord(cyrillic)] = latin
      TRANS[ord(cyrillic.upper())] = latin.upper()

    return self.text.translate(TRANS)



class Record:

  def __init__(self, title: str, note = None, tag = None ):
    self.title = title
    if note is None:
      self.note = []
    else:
      self.note = [note]
    self.tag = tag


  def add_note(self, note: str):
    print(type(Note(note).value))
    self.note.append(Note(note).value)
    print(self.note)


class NoteBook(UserDict):

  def add_record(self, record: list):
    self.data[record.title.value] = record

title = Title("Коробов sdsfsfdgf")
#title = Title("datata")
note = Note("bla")
rec = Record(title, note, "tag1")
rec.add_note("nananan")
nb = NoteBook()
nb.add_record(rec)
print(rec.note)
print(rec.tag)
print(nb['Korobov sdsfsfdgf'])


