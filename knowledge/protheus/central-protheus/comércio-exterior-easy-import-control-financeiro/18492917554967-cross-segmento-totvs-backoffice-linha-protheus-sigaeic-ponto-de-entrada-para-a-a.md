---
article_id: 18492917554967
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 4a1cbb65794a72b5faf225d65266270255aa85cee8193c387b0bc9c9bd8cfe25
fetched_at: '2026-06-28T22:39:44.518520+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ponto de Entrada
  para a alteração do Pagamento Antecipado.
type: support-article
updated_at: '2023-10-23T15:12:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18492917554967-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-Entrada-para-a-altera%C3%A7%C3%A3o-do-Pagamento-Antecipado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18492933295127) Tempo aproximado para leitura: **02:00 min** **Dúvida**Existe algum Ponto de Entrada para alteração da Data do Pagamento Antecipado no momento da inclusão do mesmo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  –*Easy Import Control*– Todas versões.  
  
**Solução**É possível utilizar o Ponto de Entrada da Função "**EICFI400**", parâmetro **"ADIANT"**, modificando o array **cOriRdm**,  **cTipoRdm** ou **lAutRdm**.

|  |  |  |  |
| --- | --- | --- | --- |
| Nome | Tipo | Descrição | Referência |
| "ADIANT" | Array of Record | Array of RecordPermite a manipulação dos dados antes da geração de títulos no financeiro. | cOriRdm   cTipoRdm   lAutRdm |

|  |
| --- |
| User function eicfi400()  Do case  Case PARAMIXB == "ADIANT" ------intruções -------    EndCase return .t. |

**Saiba mais:****[Ponto de entrada EICFI400](https://tdn.totvs.com/display/public/mp/EICFI400)**
