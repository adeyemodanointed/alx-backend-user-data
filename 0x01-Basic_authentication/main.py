#!/usr/bin/python3
""" Check response
"""

if __name__ == "__main__":
    from api.v1.auth.basic_auth import BasicAuth

    ba = BasicAuth()
    res = ba.extract_base64_authorization_header("Basic HBTN")
    if res is None:
        print("extract_base64_authorization_header must return the decoded value of 'authorization_header'")
        exit(1)
    
    if res != "HBTN":
        print("extract_base64_authorization_header must return the decoded value of 'authorization_header': {}".format(res))
        exit(1)
    
    print("OK", end="")
