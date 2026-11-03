---
content_hash: 74df646aef1670eec6b5428ce3b603e726d9fa6881e0ad665ca6bce8fdbee2da
fetched_at: '2026-06-28T21:35:31.038377+00:00'
page_id: '870389961'
product: fluig
source: tdn-fluig
title: DES - Por que ocorre o erro 401 - Unauthorized ao utilizar alguns exemplos
  de desenvolvimento?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=870389961
version: 5
---

# Índice

Índice

# Plataforma

**Produto:**TOTVS Fluig

# Ocorrência

Ao utilizar alguns exemplos de desenvolvimento disponibilizados no , ocorre a inconsistência **401 - Unauthorized** e a execução é interrompida.

# Causa

Isso ocorre porque alguns exemplos utilizam bibliotecas que são disponibilizadas no repositório de artefatos do Fluig no Nexus, que agora é privado e passou a exigir autenticação.

# Solução

É necessário solicitar as credenciais de acesso ao Nexus, que permitirá que as dependências dos exemplos sejam baixadas corretamente.

Para isso, abra um [*ticket*](https://centraldeatendimento.fluig.com/hc/pt-br) para o time de Atendimento Fluig.

## Como utilizar as credenciais?

Com as credenciais em mãos, adicione o bloco de código abaixo no arquivo **settings.xml** do projeto, substituindo:

* "inserir\_o\_usuário\_fornecido" pelo **usuário enviado** pelo atendimento;

* "inserir\_a\_senha\_fornecida" pela **senha enviada** pelo atendimento.

nexus
inserir\_o\_usuário\_fornecido
inserir\_a\_senha\_fornecida
]]>
