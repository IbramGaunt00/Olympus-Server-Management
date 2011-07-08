#ifndef _ASHAJAX_PP_H_
#define _ASHAJAX_PP_H_
#include <string>
std::string getGET(std::string input) {
  int start;
  int length;
  for (unsigned int i = 0; i < input.size()-3; i++) {
    if (input[i] == 'G') {
      if (input[i+1] == 'E' && input[i+2] == 'T') {
        start = i+3;
        break;
      }
    }
  }
  for (unsigned int i = start; i < input.size(); i ++) {
    if (input[i] == '\r') { // newline characters consist of /r/n assumidly
    
      length=i-start;
      break;
    }
  }
  return input.substr(start,length);
}
#endif