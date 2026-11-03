---
article_id: 21859974844567
category: SIGAEST - LEGAIS
content_hash: 8825ff47c26503dd67e7430ffe935eac99a0c583c328ac9330d72c6f3c600bbb
fetched_at: '2026-06-28T22:38:51.762801+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR947 - Relatório
  da Policia Civil não apresenta saldo do trimestre anterior corretamente
type: support-article
updated_at: '2024-03-06T17:28:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21859974844567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR947-Relat%C3%B3rio-da-Policia-Civil-n%C3%A3o-apresenta-saldo-do-trimestre-anterior-corretamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21859974817559) Tempo aproximado para leitura: **00:01:13min** **Dúvida**  
Estou gerando o relatório MATR947, e mesmo existindo movimentações de entrada e saída (SD1 e SD2) no trimestre anterior o relatório não lista o campo "Saldo Trimestre Anterior":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21859974820247)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Normalmente esse problema está relacionado com a falta de fechamento do estoque nos períodos envolvidos, ou um fechamento incorreto (data de fechamento por exemplo).

Desta maneira, antes da geração do Mapa, deve ser efetuado o “Fechamento do Estoque” no ambiente SIGAEST, pois o relatório precisa dos fechamentos para montagem dos trimestres [Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=702823607) para maiores detalhes.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Relatórios Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
