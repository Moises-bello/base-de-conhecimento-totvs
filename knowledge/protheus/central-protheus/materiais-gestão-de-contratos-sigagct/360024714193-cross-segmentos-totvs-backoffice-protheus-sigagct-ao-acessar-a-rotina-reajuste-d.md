---
article_id: 360024714193
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 9f75658a51f3ec4975af38e0ae2bd2da60779efb8f0976d361188eb7743d544f
fetched_at: '2026-06-28T22:37:20.358144+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ao acessar a rotina
  Reajuste de Saldos (CNTA320), ocorre error log - array out of bounds ( 1 of 0 )
  on PERGUNTE(MSLIB.PRW)
type: support-article
updated_at: '2022-05-19T21:05:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024714193-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-acessar-a-rotina-Reajuste-de-Saldos-CNTA320-ocorre-error-log-array-out-of-bounds-1-of-0-on-PERGUNTE-MSLIB-PRW
---

|  |  |
| --- | --- |
| **Pergunte** | Contrato de? |
| **Grupo** | CNTA320 |
| **Ordem** | 01 |
| **Tipo** | Caracter |
| **Tamanho** | 15 |
| **Help** | Informe o contrato inicial para reajuste dos saldos. |
| **Consulta Padrão** | CN9 - Contratos |

|  |  |
| --- | --- |
| **Pergunte** | Contrato Ate? |
| **Grupo** | CNTA320 |
| **Ordem** | 01 |
| **Tipo** | Caracter |
| **Tamanho** | 15 |
| **Help** | Informe o contrato final para reajuste dos saldos. |
| **Consulta Padrão** | CN9 - Contratos |

2.  No **Configurador (SIGACFG),**acesse **Ambientes/Cadastro/Menu (CFGX013)**. Informe a nova opção de menu do ***Gestão de Contratos***, conforme instruções a seguir:

|  |  |
| --- | --- |
| **Menu** | Miscelânea |
| **Submenu** | Processamento |
| **Nome da Rotina** | Reajuste de Saldos |
| **Programa** | CNTA320 |
| **Módulo** | SIGAGCT |
| **Tipo** | Função Protheus |

3. Em ambos perguntes preencher na coluna X1\_GCS  = G
