---
content_hash: 74c6934208b13ba0598f4055b1f92c98ab4e421a0cc34bd6f554056580201bac
fetched_at: '2026-06-28T21:35:19.867794+00:00'
page_id: '224113492'
product: fluig
source: tdn-fluig
title: DES - Por que a mensagem de erro "Parâmetros informados para conexão são inválidos"?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224113492
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto**: TOTVS Fluig Plataforma

# Ocorrência

Tenho a plataforma integrada ao TOTVS Identity e na criação do servidor Fluig no TOTVS Developer Studio ou Eclipse ocorre o erro "O servidor foi criado, mas ocorreu um erro ao tentar buscar informações. Após solucionado o problema, edite e grave novamente o servidor. Erro: Parâmetros informados para conexão são inválidos".   
  
Por que isso acontece e como corrigir?

# Solução

Quando a plataforma está integrada ao Identity, o login no TDS deve ser feito com o mesmo login utilizado no Identity. Isso acontece porque a autenticação é feita no Identity e somente depois na plataforma.   
  
No cadastro do seu servidor, altere o valor de usuário e senha e informe, respectivamente, o email e a senha utilizados no Identity e salve.   
  
Se algum dia você deixar de utilizar a plataforma integrada ao Identity, será preciso alterar o cadastro do servidor e então utilizar o login e a senha da plataforma para a conexão.
