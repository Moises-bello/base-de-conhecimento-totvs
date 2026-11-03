---
content_hash: 1bb055cd6a50e1247e773cb07e4c67aa9c722a99a9815ece1ce9add5a3799d39
fetched_at: '2026-06-28T21:35:17.351593+00:00'
page_id: '1048504602'
product: fluig
source: tdn-fluig
title: Identity | Validação do MFA desvinculado do Login
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1048504602
version: 2
---

Para criar uma API que valide a autenticação multifator (MFA) utilizando o TOTP  (API via Swagger para validação do response), você pode seguir os seguintes passos:

1. **Receber as Credenciais:** A API deve receber o nome de usuário e a senha para autenticação, além do TOTP gerado pelo aplicativo autenticador.
2. **Validar o Usuário:** Utilize o endpoint de autenticação do TOTVS Identity para validar as credenciais do usuário. Se a autenticação for bem-sucedida, você pode prosseguir para a validação do TOTP.
3. **Validar o TOTP:** Após a autenticação, você deve verificar se o TOTP fornecido pelo usuário é válido. Isso geralmente envolve a utilização de uma biblioteca que suporte a geração e validação da autenticação.
4. **Implementar *Rate Limiting*:** Para garantir que a API tenha um limite de requisições (rate limit) baixo, você pode implementar um mecanismo que permita apenas 5 requisições por minuto por usuário. Isso pode ser feito utilizando middleware em frameworks como Express (Node.js) ou Flask (Python).
5. **Retornar Resposta:** A API deve retornar um JSON informando se o token é válido ou não, além de mensagens de erro apropriadas em caso de falhas.
