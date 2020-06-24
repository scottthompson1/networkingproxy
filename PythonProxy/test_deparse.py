#!/usr/bin/python3

import proxy
import unittest

class TestProxy(unittest.TestCase):
    def test_request_deparse_no_options(self):
        request = proxy.HTTPRequest("GET",
                proxy.URI("http://www.example.com"))
        expected = "GET http://www.example.com HTTP/1.1\r\n\r\n"
        actual = request.deparse()
        print("EXPECTED: %s" % repr(expected))
        print("ACTUAL: %s" % repr(actual))
        self.assertEqual(actual, expected)

    def test_request_deparse_with_headers(self):
        request = proxy.HTTPRequest("GET",
            proxy.URI("http://www.example.com"),"HTTP/1.1",{"User-Agent": "me","Age": 20})
        expected = "GET http://www.example.com HTTP/1.1\r\nAge: 20\r\nUser-Agent: me\r\n\r\n"
        actual = request.deparse()
        print("EXPECTED: %s" % repr(expected))
        print("ACTUAL: %s" % repr(actual))
        self.assertIn("Age: 20", actual)
        self.assertIn("User-Agent: me", actual)

    def test_response_no_options(self):
        response = proxy.HTTPResponse("400","Failed")
        expected = "HTTP/1.1 400 Failed\r\n\r\n"
        actual = response.deparse()
        print("EXPECTED: %s" % repr(expected))
        print("ACTUAL: %s" % repr(actual))
        self.assertEqual(actual,expected)

    def test_response_with_headers(self):
        response = proxy.HTTPResponse("400","Failed","HTTP/1.1",{"Age": 20})
        expected = "HTTP/1.1 400 Failed\r\nAge: 20\r\n\r\n"
        actual = response.deparse()
        print("EXPECTED: %s" % repr(expected))
        print("ACTUAL: %s" % repr(actual))
        self.assertEqual(actual,expected)

    def test_response_with_headers_and_body(self):
        response = proxy.HTTPResponse("400","Failed","HTTP/1.1",{"Age": 20},"This is the body")
        expected = "HTTP/1.1 400 Failed\r\nAge: 20\r\n\r\nThis is the body"
        actual = response.deparse()
        print("EXPECTED: %s" % repr(expected))
        print("ACTUAL: %s" % repr(actual))
        self.assertEqual(actual,expected)



if __name__ == '__main__':
    unittest.main()
