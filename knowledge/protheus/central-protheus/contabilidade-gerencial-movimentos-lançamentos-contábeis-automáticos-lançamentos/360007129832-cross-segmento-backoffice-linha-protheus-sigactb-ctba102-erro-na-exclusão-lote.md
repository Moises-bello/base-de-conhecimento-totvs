---
article_id: 360007129832
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: c81594d59e27cae68f47664c2743941ba76aa1ca3bbbe7fdc919e08fa35c4ce6
fetched_at: '2026-06-28T22:40:32.584572+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus- SIGACTB - CTBA102 Erro na exclusão
  Lote '
type: support-article
updated_at: '2022-06-10T22:40:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007129832-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Erro-na-exclus%C3%A3o-Lote
---

**Dúvida**

Sistema apresenta erro na exclusão de  Lote CTBA102

Alias does not exist: XX5  
 on CT2CLEARLA(CTBXATU.PRW)

**Ambiente**  
Protheus – Contabilidade Gerencial – A partir da versão 12.1.17  
  
   
**Solução**O erro é gerado porque o sistema não encontra o registro de origem para efetuar a limpeza do flag de contabilização, provavelmente porque a origem desse lançamento é uma contabilização txt.  
  
Para resolver o problema o parâmetro MV\_CTBAPLA deve ser desabilitado e apos a exclusão habilitado novamente.

**Obs.**

Esse procedimento não e necessário para movimentos gerados na própria versão 12, uma vez que o erro não ocorre mais em ambientes atualizados.
