---
content_hash: d47f945a438616bef14d696e6866bb3fc05e963a248aea47f28203fd8ce4b0b4
fetched_at: '2026-06-28T21:35:25.997489+00:00'
page_id: '329032235'
product: fluig
source: tdn-fluig
title: Identity | Por que ocorre erro de conexão ao acessar o contexto da minha empresa,
  mas outros estão no ar?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=329032235
version: 6
---

**Ocorrência**

Por que recebo um erro de conexão ao acessar o contexto da minha empresa, mas outros estão no ar? Ao acessar a URL https://[minhaempresa].fluigidentity.com ocorre o erro abaixo, mas ao tentar acessar [https://totvs.fluigidentity.com](http://totvs.fluigidentity.com), por exemplo, o acesso é realizado normalmente.

**Causa**

O acesso ao contexto da empresa é realizado via , mas um problema na rede interna do cliente está afetando a conexão.

Repare na imagem acima que a URL na barra de endereços do navegador aponta para o arquivo remote\_auth.asp do Desktop SSO, que é hospedado no servidor IIS do cliente.

**Solução**

Verificar junto à equipe de infraestrutura da empresa se foi feita alguma alteração ou se há algum bloqueio na rede interna, no servidor IIS, na , etc.

Dica

A disponibilidade do Identity pode ser verificada a partir do endereço [status.fluigidentity.com](http://status.fluigidentity.com).
