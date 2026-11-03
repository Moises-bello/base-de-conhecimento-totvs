---
content_hash: 6c51ab3b13a22f0dc546b556f9bdfc793f3712d9693f3e0039057082ff68da7f
fetched_at: '2026-06-28T21:35:28.064394+00:00'
page_id: '6066568'
product: fluig
source: tdn-fluig
title: Transformer
type: documentation
url: https://tdn.totvs.com/display/fluig/Transformer
version: 10
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade desse componente é converter um arquivo de XML para XML, de XML para Texto e XML para HTML.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Type | Selecionar o tipo de tecnologia a ser utilizada para a transformação.  1. **XSL**: indica a utilização do padrão XSL para transformação de arquivos. Atualmente as opções disponíveis são de XML para Texto, XML para XML e XML para HTML. 2. **None**: Não utilizar nenhum XSL para transformação. Esta opção é muito utilizada quando se deseja retirar caracteres especiais da mensagem. |
| File Name | Inserir o nome do arquivo de transformação. |
| Processor | Selecionar o tipo de processor que será utilizado para a transformação.  1. **Xalan**: Suporta XSLT 1.0 para transformação. 2. **Saxon**: Suporta XSLT 2.0 para transformação. |
| Remove special Characters | Quando selecionado, o Fluig ESB irá retirar todos os caracteres especiais que encontrar na mensagem, por exemplo, vogais acentuadas e “ç”. |
| Remove Line Break | Quando selecionado, o Fluig ESB irá retirar todas as quebras de linha que existirem na mensagem. |
