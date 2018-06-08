from mockito import mock, verify
import unittest

from helloworld import helloworld

class HelloworldTest(unittest.TestCase):
  def test_should_issue_hello_word_message(self):
    out = mock()

    helloworld(out)

    verify(out).write("Hello world of Python\n")
