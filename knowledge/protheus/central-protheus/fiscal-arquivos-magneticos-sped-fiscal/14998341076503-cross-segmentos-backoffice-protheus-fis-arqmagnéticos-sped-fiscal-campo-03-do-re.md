---
article_id: 14998341076503
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: eaa7401fd56442a40b5b754e7c5613c4a3d34da40a5d9ed9238df1f4abdf76a9
fetched_at: '2026-06-28T22:42:02.699934+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Campo 03 do registro C100 gera = 0 para nota de Terceiros (Formulário Próprio
  = Não)
type: support-article
updated_at: '2023-06-01T19:54:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14998341076503-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Campo-03-do-registro-C100-gera-0-para-nota-de-Terceiros-Formul%C3%A1rio-Pr%C3%B3prio-N%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Por que o campo **03** do registro **C100** está gerando = **0** para notas com **Formulário Próprio = Não**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Conforme determinação do Guia Prático, o campo possui duas possibilidades:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14997807649175)

Se for uma operação de **Formulário Próprio**, deverá ser apresentado = **0**Caso for **Formulário Próprio = Não**, deve apresentar = **1** no campo do registro.  
  
O incidente ocorre pois o campo **03** do registro **C100** depende do campo **FT\_FORMUL**, onde o mesmo existe apenas duas validações:

- **FT\_FORMUL** = **Vazio**, irá apresentar o campo **03** do registro **C100** = **1**- **FT\_FORMUL** = **S**, irá apresentar como = **0**

Caso possua qualquer outra informação no campo **FT\_FORMUL** diferente das duas validações (ex: **N**) o campo não irá identificar o processo correto e alimentará o campo no registro como **0** mesmo a nota sendo com **Formulário Próprio = Não.**

Corrija a questão e faça um novo teste.
