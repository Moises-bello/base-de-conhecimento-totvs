---
content_hash: 7894d32a3ce0b292c765647ddd1cbc9c89e4745ec1f63ab6c0bbd30c0a61f91e
fetched_at: '2026-06-29T00:12:15.178818+00:00'
page_id: '971956251'
product: rm
source: tdn-rm
title: FISCAL01-25903 - Guias de Recolhimento - Você não está autorizado a utilizar
  essa funcionalidade do sistema
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=971956251
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | Guias de Recolhimento |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25903 |

## **02. SITUAÇÃO/REQUISITO**

Ao acessar a opção **Guias de Recolhimento** no módulo Gestão Fiscal é apresentada a inconsistência: 'Você não está autorizado a utilizar essa funcionalidade do sistema'  
No módulo Gestão Fiscal | Obrigações Principais | Mais... | Guias de Recolhimento |

## **03. SOLUÇÃO**

Ajustado a tag de segurança para a rotina. Estava sendo utilizado uma tag do Delphi, alteramos para utilizar a tag nova.
