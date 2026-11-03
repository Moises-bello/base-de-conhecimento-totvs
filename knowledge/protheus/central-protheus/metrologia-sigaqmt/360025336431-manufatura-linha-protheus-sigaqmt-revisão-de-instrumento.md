---
article_id: 360025336431
category: Metrologia (SIGAQMT)
content_hash: 86c410f01c1efda7be002759f89cb956e1f0e9d98e5828d2494928328becbfbf
fetched_at: '2026-06-28T22:42:24.899303+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - Revisão de instrumento
type: support-article
updated_at: '2021-09-08T12:58:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025336431-Manufatura-Linha-Protheus-SIGAQMT-Revis%C3%A3o-de-instrumento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Na rotina de **Cadastro de Instrumentos -** **QMTA010**, existe a possibilidade de gerar uma nova revisão automaticamente, sempre que um instrumento for alterado?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Solução**Sim, ao alterar e salvar o instrumento, será apresentada a mensagem **Esta alteração criará uma nova revisão. Confirma?**Entretanto, esta mensagem será apresentada apenas nas situações listadas abaixo:  
1. O instrumento precisa ter pelo menos uma calibração, gerando registro na tabela **QM6 - Cabeçalho de Calibração.**Caso contrário, qualquer alteração de instrumento ainda não calibrado, continuará na revisão atual;  
2. O campo a ser alterado não pode constar no parâmetro **MV\_QNGREV - Digite os campos que não serão considerados para a geração de revisão de instrumentos**. Neste parâmetro são informados todos os campos que podem ser alterados, sem gerar uma nova revisão.
