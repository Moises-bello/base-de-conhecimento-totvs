---
content_hash: f6119abbd40cfe07789de8b38bb11aabda9eeee7ef71a261eead063d8394345b
fetched_at: '2026-06-28T21:35:19.295522+00:00'
page_id: '201732230'
product: fluig
source: tdn-fluig
title: IDE - Por que os campos da integração com o Identity estão em branco?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201732230
version: 11
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma integrado ao TOTVS Identity

**Versão:** 1.5.0 ou superior

# Ocorrência

Após ativar a integração com o Identity em uma empresa, informar os dados de conexão (URL e Token) e salvar, ao retornar a essa mesma página as informações estão em branco.

# Causa

A plataforma não consegue buscar as informações de integração com o Identity porque foi configurado em ambiente seguro (HTTPS), mas o campo URL do Portal não foi preenchido corretamente.

# Solução

Com o usuário wcmadmin, acessar **Painel de controle** → **WCM** → **Configurações do Sistema**, e ajustar o campo **URL do portal** para o endereço correto, certificando-se de que protocolo **HTTPS** foi informado.

Por exemplo: <https://fluig.empresa.com:8080/portal.>

Recomenda-se verificar se as configurações HTTPS da plataforma estão corretas, conforme o documento  . Caso o Apache seja utilizado, consultar a documentação .
