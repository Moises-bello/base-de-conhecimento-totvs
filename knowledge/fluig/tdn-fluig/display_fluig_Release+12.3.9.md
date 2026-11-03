---
content_hash: 91733ff36b4500315ca71a57e2b649a0df8b8e4f35c85bb8ca01e7029f4d07a8
fetched_at: '2026-06-28T21:35:26.311501+00:00'
page_id: '353289708'
product: fluig
source: tdn-fluig
title: Release 12.3.9
type: documentation
url: https://tdn.totvs.com/display/fluig/Release+12.3.9
version: 5
---

Este documento contém breves descritivos acerca das implementações e correções efetuadas no pacote **12.3.9**.

## Implementações

#### TOTVS | ESB Plugin e TOTVS | ESB Server

**Função: Horário do Monitor**

**Situação**:Apresentação incorreta do horário da mensagem processada mostrada nos detalhes da mensagem no Monitor do TOTVS | ESB Server.

**Solução**: Correção realizada na conversão da informação entre o banco de dados e o Monitor do ESB.

**Função: Correção na importação de projetos do TOTVS | ESB plugin**

**Situação**: Não era possível importar projetos pelo ESB plugin para o ESB Server.

**Solução**: Corrigida inconsistência no plugin de ESB que causava erro ao importar projetos para o servidor.
