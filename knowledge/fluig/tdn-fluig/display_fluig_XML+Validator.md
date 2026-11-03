---
content_hash: 5c9ed2fd12bf9a20821f7a1d5b95fc0ea7859e0195e167a88ce677ace8e9290f
fetched_at: '2026-06-28T21:35:28.067269+00:00'
page_id: '6066569'
product: fluig
source: tdn-fluig
title: XML Validator
type: documentation
url: https://tdn.totvs.com/display/fluig/XML+Validator
version: 8
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade desse componente é fazer a validação de um documento XML, para verificar se o XML está corretamente estruturado e possibilitar a validação contra um *schema*.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Type | Selecionar qual o tipo de validação que se deseja fazer no XML.  1. **XML Validation**: verifica se o arquivo XML está formatado corretamente, se todas as *tags* abertas estão fechadas corretamente; 2. **Schema Validation**: valida o XML com um arquivo XSD; 3. **Signature Validation**: valida se a assinatura do XML está correta. |
| Return Type | Selecionar qual o tipo de retorno se deseja obter da validação do XML.  1. **Original message**: retorna apenas a mensagem que foi recebida; 2. **Error message**: retorna uma mensagem contendo os erros que foram encontrados na validação do XML; 3. **Both**: retorna uma mensagem que agrupa a mensagem que foi recebida e os erros que foram encontrados. |
