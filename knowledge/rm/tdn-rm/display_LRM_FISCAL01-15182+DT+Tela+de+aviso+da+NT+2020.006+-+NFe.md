---
content_hash: bd5da6e4d6d9e0ede262f5b9a755ad2f5b4a11597acc03bad8a2fb5b124822c1
fetched_at: '2026-06-29T00:10:58.813013+00:00'
page_id: '607038351'
product: rm
source: tdn-rm
title: FISCAL01-15182 DT Tela de aviso da NT 2020.006 - NFe
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-15182+DT+Tela+de+aviso+da+NT+2020.006+-+NFe
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: |  |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal e Nucleus |
| Função: | Enviar NF-e |
| País: | Brasil |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15182 |

## **02. SITUAÇÃO/REQUISITO**

Tela de aviso da NT 2020.006

A Tela deverá ser exibida somente no dia 05/04 e a geração do XML da NF-e deverá considerar a opção do usuário para a montagem do xml.

A nossa documentação deve ser atualizada, se possível com um print, indicando que a tela de avisa será exibida durante todo o dia que não pode ser desabilitada, mas que no dia seguinte a mesma sumirá sozinha.

[https://tdn.totvs.com/pages/viewpage.action?pageId=599050993](https://tdn.totvs.com/pages/viewpage.action?pageId=599050993 "Follow link")

## **03. SOLUÇÃO**

Foi criado na tela de Movimento, a tela com aviso sobre a mudança da NT2020.006 para ser exibida no dia 05/04/2021 de 00:00 até 13:00. Caso no período de intermitência o usuário queira utilizar a nova NT,ele deve clicar em SIM e o XML irá gerar com a tag do Intermediador,caso clique em Não a tag não deve ser gerada
