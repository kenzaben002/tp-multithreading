#include <cpr/cpr.h>
#include <iostream>

int main() {

  std::string url = "http://localhost:8000";

  cpr::Response response = cpr::Get(cpr::Url{url});

  if (response.error) {
    std::cerr << "Erreur lors de la requête HTTP : " << response.error.message
              << std::endl;
    return 1;
  }

  std::cout << "Code réponse HTTP : " << response.status_code << std::endl;

  std::cout << "Corps de la réponse : " << response.text << std::endl;

  return 0;
}
