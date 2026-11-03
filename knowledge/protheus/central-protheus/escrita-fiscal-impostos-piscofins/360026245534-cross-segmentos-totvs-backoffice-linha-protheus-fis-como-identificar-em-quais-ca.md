---
article_id: 360026245534
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: c88a594cb9a5cd3fd6bed6bfc61719054ea3ad7ad57d1fdf12340d15e1c23a2d
fetched_at: '2026-06-28T22:39:36.917554+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como identificar
  em quais campos foram gravados o PIS/COFINS apuração?
type: support-article
updated_at: '2021-10-11T16:52:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026245534-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-identificar-em-quais-campos-foram-gravados-o-PIS-COFINS-apura%C3%A7%C3%A3o
---

**Dúvida:**

Como identificar em quais campos foram gravados o PIS/COFINS Apuração?  
  
**Ambiente:**

Protheus – Faturamento – A partir da versão 12.1.17.  
  
**Solução:**

- Seguem abaixo as tabelas e campos que destacam o**PIS/COFINS Apuração** via documento fiscal:

1 - Tabela **SD2 (Itens de venda da nota fiscal)**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403231100951/mceclip1.png)

2 - Tabela **SF2 (cabeçalho das notas fiscais de saída)**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403225573783/mceclip2.png)

3 - Tabela **SFT (Itens do Livro Fiscal)**:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403231203095/mceclip3.png)

**Nota:** No livro fiscal o PIS e COFINS não são destinados nos campos FT\_BASIMP5 ou FT\_BASIMP6, pois a tabela SFT faz a correta separação para a correta integração na EFD das contribuições, sendo:

FT\_BASEPIS e FT\_BASECOF destinados para o PIS e COFINS apuração.

FT\_BRETPIS e FT\_BRETCOF destinados para o PIS e COFINS retenção.

Qualquer dúvida quanto a configuração do PIS e COFINS, o artigo complementar abaixo pode auxiliar:

[MP - FIS - Qual a Configuração Necessária Para Gerar Nota Fiscal Com Cálculo de PIS E COFINS Via Apuração?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038813773-MP-FIS-Qual-a-Configura%C3%A7%C3%A3o-Necess%C3%A1ria-Para-Gerar-Nota-Fiscal-Com-C%C3%A1lculo-de-PIS-E-COFINS-Via-Apura%C3%A7%C3%A3o-?source=search)
