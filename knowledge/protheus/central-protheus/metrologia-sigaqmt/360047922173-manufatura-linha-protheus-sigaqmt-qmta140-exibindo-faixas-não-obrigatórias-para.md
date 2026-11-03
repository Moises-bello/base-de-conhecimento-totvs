---
article_id: 360047922173
category: Metrologia (SIGAQMT)
content_hash: b852be0dd5f87ce6e8227431bdab0a42f7bdaef46165daf9efb8842468ce138a
fetched_at: '2026-06-28T22:42:24.870328+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - QMTA140 exibindo faixas não obrigatórias
  para calibração
type: support-article
updated_at: '2021-08-10T19:07:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047922173-Manufatura-Linha-Protheus-SIGAQMT-QMTA140-exibindo-faixas-n%C3%A3o-obrigat%C3%B3rias-para-calibra%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50 min**  
**Ocorrência**No módulo **SIGAQMT - Metrologia**, ao realizar a calibração de um instrumento na rotina **QMTA140 - Medições**, está exibindo faixas que foram definidas como não obrigatórias.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**Essa situação ocorre quando foi definida uma faixa como não obrigatória no cadastro do instrumento na rotina **QMTA010 - Instrumentos**, ou seja, com o campo **Cal. Obrigat?** como **Não**.  
  
**Solução**Ao parametrizar uma faixa como não obrigatória, indica que a mesma será exibida na calibração do instrumento na rotina **QMTA140**, porém não é necessário realizar o preenchimento das medições para que a calibração seja aprovada.  
Para que as faixas não sejam apresentadas na rotina **QMTA140** é necessário remover o vínculo das mesmas com o instrumento.
