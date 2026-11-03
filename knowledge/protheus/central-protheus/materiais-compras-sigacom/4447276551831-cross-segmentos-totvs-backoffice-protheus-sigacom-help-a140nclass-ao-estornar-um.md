---
article_id: 4447276551831
category: Materiais - Compras (SIGACOM)
content_hash: 6f3f48ffdb956511f77aa8ac95f641ee345b145dfa8ff4c26aa4c8b883c55a46
fetched_at: '2026-06-28T22:41:18.886723+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - HELP A140NCLASS ao
  estornar uma Nota do tipo Complemento na rotina de Pre Nota de Entrada
type: support-article
updated_at: '2022-05-19T20:38:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4447276551831-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-A140NCLASS-ao-estornar-uma-Nota-do-tipo-Complemento-na-rotina-de-Pre-Nota-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:02 min** **Dúvida**Ao estonar a classificação da Nota do tipo Complemento na rotina de Pre Nota de Entrada é apresentado o Help A140NCLASS

![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4446848899095/imagem1.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**A função de Estornar apenas limpa o conteúdo os campos D1\_TES (Tipo Entrada) e F1\_STATUS (Status).

A partir do momento em que a Prenota é classificada, ela se torna um Documento de Entrada.

A rotina de Pre Nota de Entrada (MATA140) permite estornar apenas Notas do tipo Normal, Devolução e Beneficiamento e as Notas com status = A.

As Notas do tipo Complemento, devem excluídas pela rotina do Documento de Entrada (MATA103) e após a exclusão, inclui-las novamente.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
