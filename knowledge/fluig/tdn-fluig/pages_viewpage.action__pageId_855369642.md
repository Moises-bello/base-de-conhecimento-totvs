---
content_hash: 46b6e0b19e8bf36a878d9a6b28ac8f9247fa5e112c9db0a49b980417aed3ce3e
fetched_at: '2026-06-28T21:35:30.445011+00:00'
page_id: '855369642'
product: fluig
source: tdn-fluig
title: Identity | SmartSync - Segurança de Dados em Trânsito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=855369642
version: 5
---

Esta página tem por objetivo explicar os mecanismos de segurança implementados no tráfego de informações entre o SmartSync(*client*) e o Identity(*server*).

## Dados em trânsito

---

Toda comunicação entre o cliente e servidor é criptograda usando [TLS/SSL](https://www.cloudflare.com/pt-br/learning/ssl/how-does-ssl-work/). Além do uso da criptografia em trânsito, o campo de "senha" é encriptado usando [chaves assimétricas](https://www.cloudflare.com/pt-br/learning/ssl/how-does-public-key-encryption-work/), ou seja a chave pública permanece com o servidor, enquanto a chave privada é usada pelo cliente para decriptar a senha e em seguida verificar se a senha bate com a contida no Active Directory.   
  
As chaves criptográficas são criadas durante a configuração do AD no Identity e são únicas para cada configuração.

## Autenticação entre SmartSync e Identity

---

Como um meio mais eficiente e performático de receber as requisições de sincronização e login via AD, é utilizada uma [Api-Key](https://aws.amazon.com/pt/what-is/api-key/) para identificar o SmartSync que está solicitando ou enviando dados para o servidor, sendo ela exclusiva para cada SmartSync configurado.

Fique atento!

Esta documentação é válida a partir da **versão 5.0.0** ou superior do SmartSync. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê no seu ambiente.

]]>
