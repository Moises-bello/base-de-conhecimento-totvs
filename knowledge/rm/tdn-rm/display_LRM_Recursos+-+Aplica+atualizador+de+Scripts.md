---
content_hash: f8ca890526ae1b148f36537e5a4da4334d41f858aa5de38a25688fdc25fad49d
fetched_at: '2026-06-29T00:12:07.147835+00:00'
page_id: '919063656'
product: rm
source: tdn-rm
title: Recursos - Aplica atualizador de Scripts
type: documentation
url: https://tdn.totvs.com/display/LRM/Recursos+-+Aplica+atualizador+de+Scripts
version: 1
---

**Recebe**: Essa atividade recebe os seguintes parâmetros configuráveis:

* **Alias**: Nome do Alias da base de dados. (Opcional)
* **DbUser**: Usuário para acesso ao banco de dados. Padrão: "rm".
* **DbUserPassword**: Senha de acesso ao banco de dados. Padrão: "rm".
* **Environment**: Código do ambiente. 0 para Produção e 1 para Homologação. Padrão: 1.
* **HostPort**: Porta do host onde o banco de dados está localizado. Padrão: 8051.
* **HostDns**: DNS ou IP do host onde o banco de dados está localizado. Padrão: "localhost".

**É Oferecido**: **Recurso de Alias:** Caso o parâmetro "Alias" não seja fornecido, a atividade pode utilizar um recurso de Alias previamente configurado pela atividade "Cria Alias RM".
