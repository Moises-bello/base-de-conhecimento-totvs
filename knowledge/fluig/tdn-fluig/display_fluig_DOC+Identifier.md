---
content_hash: e077b1576a79da649888b24e6d39c9fb91eda0665eeab2b260511df5047a0544
fetched_at: '2026-06-28T21:35:28.090249+00:00'
page_id: '6066575'
product: fluig
source: tdn-fluig
title: DOC Identifier
type: documentation
url: https://tdn.totvs.com/display/fluig/DOC+Identifier
version: 9
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade desse componente é buscar informações dos documentos trafegados pelo Fluig | ESB, para serem utilizados posteriormente como consulta. Este componente é utilizado para que seja possível fazer um melhor acompanhamento das transações que são realizadas pelo Fluig | ESB.

Por exemplo, caso se esteja conectando à Sefaz (Secretaria da Fazenda) para geração de Nota Fiscal Eletrônica (NF-e), é possível no campo origem pegar o nome do sistema local, no campo destino o nome ao qual será conectado e no campo número do documento obter o número da nota fiscal que será gerada.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Origin Document | Inserir o nome (informando uma String ou diretamente a expressão XPath) que busca a informação da Origem do Documento. O valor retornado será armazenado no banco de dados (campo ToPartner) e será utilizado para futuras consultas no monitoramento de mensagens. |
| Target Document | Inserir o nome (informando uma String ou diretamente a expressão XPath) que busca a informação do Destino do Documento. O valor retornado será armazenado no banco de dados (campo FromPartner) e será utilizado para futuras consultas no monitoramento de mensagens. |
| Document Number | Inserir a expressão  XPath que busca a informação do Número do Documento. O valor retornado será armazenado no banco de dados (campo NrDoc) e será utilizado para futuras consultas no monitoramento de mensagens. |
| Document Type | Inserir a expressão  XPath que busca a informação do Tipo do Documento. O valor retornado será armazenado no banco de dados (campo Type) e será utilizado para futuras consultas no monitoramento de mensagens. |
| Document Group | Inserir a expressão XPath que busca a informação de agrupamento. O valor retornado será armazenado no banco de dados (campo GroupType) e será utilizado para futuras consultas no monitoramento de mensagens. |
