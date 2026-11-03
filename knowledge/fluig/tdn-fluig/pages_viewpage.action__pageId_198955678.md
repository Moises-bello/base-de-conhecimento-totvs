---
content_hash: b265df6dca87a6329fd9310320083e8ac4e6b48722acb0eda2d2e665ddedc3de
fetched_at: '2026-06-28T21:35:19.216491+00:00'
page_id: '198955678'
product: fluig
source: tdn-fluig
title: CON - Por que ocorre erro (Usuário sem Permissão) na consulta de WebService
  de Dataset?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198955678
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Tipo de API:** Web service

# Ocorrência

Por que ao utilizar o método getDataset do WebService ECMDatasetService, retorna a mensagem: "Usuário sem permissão para consultar esse dataset."

# Causa

Usuário não tem permissão para acessar o formulário relacionado a este dataset.

# Solução

Para que um dataset seja consultado via WebService é necessário que o usuário utilizado tenha permissão no formulário. Para isso, com um usuário administrador (ou que tenha permissão de acesso ao formulário), deve-se acessar a pasta onde o formulário está armazenado, editar as propriedades e [adicionar permissão de leitura](http://tdn.totvs.com/x/WQV8Dg) para o usuário utilizado no WebService.

A partir da atualização **Essential 1.7.0-200714**, a plataforma passa a ter oferecer o controle de permissões para datasets, webservices e APIs. Para mais detalhes, consulte a documentação de .
