---
article_id: 360033735033
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 3e9319e4f0b8b0b023ff7abb4dfec6f88d9029a854c8d3b4555e47e235eff064
fetched_at: '2026-06-28T22:40:47.633155+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - SIGACTB_ECF REGISTRO L210 É GERADO
  NO TXT POREM NÃO É EXPORTADO PARA O PGE
type: support-article
updated_at: '2022-07-12T18:07:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033735033-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-REGISTRO-L210-%C3%89-GERADO-NO-TXT-POREM-N%C3%83O-%C3%89-EXPORTADO-PARA-O-PGE
---

**Ocorrência**

No TXT o registro L210 está sendo gerado, porem ao validar o arquivo, não é exportado para o PGE. O que deve ser analisado?

![](https://totvssuporte.zendesk.com/attachments/token/0GbCphJHBrCYRtixH4IsHzpBZ/?name=inline1736757520.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042550934/mceclip0.png)

Ocasionando também o erro ["SALDO DOS SERVIÇOS VENDIDOS INFORMADO NO REGISTRO L210 (66) DIFERENTE DO CUSTO DOS SERVIÇOS VENDIDOS NO REGISTRO L300 .."](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025703393-MP-SIGACTB-ECF-ERRO-SALDO-DOS-SERVI%C3%87OS-VENDIDOS-INFORMADO-NO-REGISTRO-L210-66-DIFERENTE-DO-CUSTO-DOS-SERVI%C3%87OS-VENDIDOS-NO-REGISTRO-L300-?source=search)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042557954/mceclip0.png)  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus  – Contabilidade Gerencial – A partir da versão 11.80  
  
**Causa**

O PGE tem uma validação que não aceita para o L210 linhas diferente de E.

R = Rótulo; E = Editável; CA = Cálculo Alterável; CNA = Cálculo Não Alterável

**REGRA\_OBRIGATORIO\_TIPO\_DIFERENTE\_R:** Verifica se o campo está preenchido quando o tipo da linha é diferente de “R”.

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043395533/mceclip2.png)**

 Através da tabela dinâmica da receita <http://sped.rfb.gov.br/arquivo/show/2910>

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043395493/mceclip1.png)

**Solução:**

Para solucionar o contador deve avaliar a [tabela dinâmica da ECF](http://sped.rfb.gov.br/pasta/show/1644) (VIDE PLANILHA) e relacionar as contas analíticas da visão gerencial (CTBA161) somente a linhas com identificador "E- EDITÁVEL"

Sendo assim as entidades, 32, 37, 38 e 66 (por exemplo) não devem ser preenchidas na visão gerencial (ctba161)

* “[Tabelas\_Dinamicas\_ECF\_Leiaute\_5\_AC2018\_SIT\_ESP\_2019.xlsx](http://sped.rfb.gov.br/pasta/show/1644)”

Visão gerencial no Protheus (rotina ctba161)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043395973/mceclip3.png)
