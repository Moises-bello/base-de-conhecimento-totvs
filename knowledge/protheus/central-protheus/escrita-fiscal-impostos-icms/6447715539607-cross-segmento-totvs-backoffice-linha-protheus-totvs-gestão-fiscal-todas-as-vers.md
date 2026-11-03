---
article_id: 6447715539607
category: Escrita Fiscal - Impostos - ICMS
content_hash: 05c9fc4931062ad302acfab465345dd57c8625622a5accbea51f85dd42bb27ff
fetched_at: '2026-06-28T22:39:24.089384+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  Todas as versões - Onde é gravado o valor do FRETE no Matr930 ?
type: support-article
updated_at: '2022-05-31T16:49:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6447715539607-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-Todas-as-vers%C3%B5es-Onde-%C3%A9-gravado-o-valor-do-FRETE-no-Matr930
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:00**min** **Dúvida** Onde é gravado o valor do FRETE no Matr930 ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Temos alguns casos que há a cobrança do FRETE no documento, porém o mesmo não entra na base de calculo do ICMS , neste caso o mesmo é tratado como Despesa, dentro da TES temos campo especifico para o tratamento de despesa do ICMS

|  |  |
| --- | --- |
| ICMS | Desp. Ac. ICMS (F4\_DESPICM) |

quando configurado = Não

O frete vai compor o valor de despesas do documento e será gravado nos campos F3\_DESPESA/ FT\_DESPESA 

Na SF3 os valores são somados e apresentados no campo F3\_DESPESA, por ser um campo que armazena todas as despesas acessórias e por não ter campos específicos para o detalhamento dessas despesas separadamente na tabela.  
  
Já na SFT existem os campos específicos, para separar o frete e o seguro, mas o campo FT\_DESPESA grava toda despesa acessória do documento, assim o valor é somado no campo da despesa também.  
  
Exemplo de gravação no livro Matr930

TES

Calcula icms = sim

L. fiscal icms = outros

Desp ac icms = não

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6444542784279/mceclip1.png)

TES

Calcula icms = sim

L. fiscal icms = tributado

Desp ac icms = não

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6444912149783/mceclip3.png)

Esse comportamento é o mesmo para notas fiscais de entradas e saídas
