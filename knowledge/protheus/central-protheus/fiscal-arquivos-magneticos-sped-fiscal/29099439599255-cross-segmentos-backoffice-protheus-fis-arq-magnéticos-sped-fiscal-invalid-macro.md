---
article_id: 29099439599255
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: ab8ef89d744f4e17e23aec83659b464b3ebfe062cb804a61ebc76d035b3e633a
fetched_at: '2026-06-28T22:42:02.346700+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - invalid macro source (SSYacc0105e: Error token failed, no valid token):(SCGN0000D7->"B1_DATREF")
  on SFRG0200(SPEDFISCAL.PRW)'
type: support-article
updated_at: '2025-05-20T21:39:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29099439599255-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-invalid-macro-source-SSYacc0105e-Error-token-failed-no-valid-token-SCGN0000D7-B1-DATREF-on-SFRG0200-SPEDFISCAL-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29099444977943) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como corrigir o error log: **invalid macro source (SSYacc0105e: Error token failed, no valid token):(SCGN0000D7->"B1\_DATREF") on SFRG0200(SPEDFISCAL.PRW)** ao gerar o **Sped Fiscal**?  
  
**Ambiente**

Cross Segmentos - TOTVS Backofiice (Linha Protheus ) - A partir da **2210**  
  
**Solução**

O incidente ocorre devido o conteúdo do parâmetro **MV\_DTINCB1** está com aspas duplas, por exemplo:

**MV\_DTINCB1** = "**B1\_DATREF"**

Para corrigir esta questão, altere o conteúdo do parâmetro **MV\_DTINCB1** = **B1\_DATREF** via **Configurador sem as aspas duplas;**

**Estrutura:**

|  |  |
| --- | --- |
| **Itens/Pastas** | **Descrição** |
| **Nome da Variável** | MV\_DTINCB1 |
| **Tipo** | Caracter |
| **Descrição** | <definido pelo cliente> |
| **Valor Padrão** | Determina a rotina qual o campo da tabela SB1 que contém a data de cadastro (inclusão) do produto no sistema. |
| ***Default*** | O conteúdo *default* deste parâmetro é o campo B1\_DATREF. |

Após isso, acesse a rotina do **Sped Fiscal** e gere um novo **Arquivo TXT**.
