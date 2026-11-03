---
article_id: 37535417591319
category: SIGAEST - CUSTOS
content_hash: 9ffbb0f76a54e50f1b7d7eafc89322f68253725cd56fcfdd4d89a1942c0f6bb2
fetched_at: '2026-06-28T22:39:00.760091+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como identificar impostos
  do Configurador de Tributos nas Notas Fiscais?
type: support-article
updated_at: '2026-01-08T18:44:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37535417591319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-identificar-impostos-do-Configurador-de-Tributos-nas-Notas-Fiscais
---

Para identificar a Regra de Cálculo aplicada a uma Nota Fiscal no Configurador de Tributos (FISA170), verifique a aba "Tributos Genéricos - Por Item" na Nota Fiscal, onde o campo "Sigla" indica o código da regra. Alternativamente, consulte os campos D2\_IDTRIB (SD2) ou D1\_IDTRIB (SD1), localize o ID na tabela F2D e, por fim, filtre na tabela F2B para encontrar a regra aplicada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37535417560983) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como identificar qual Regra de Cálculo do Configurador de Tributos (FISA170) foi aplicada à uma Nota Fiscal?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**  
A forma mais simples de identificar o tributo seria validar a aba "Tributos Genéricos - Por Item" na Nota Fiscal, onde o campo "Sigla" indica qual o código da "Regra de Cálculo - Documentos Fiscais" que foi aplicada.

Exemplo:

**Documento de Entrada (MATA103):**

![CFG 01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37535417564695)

***Regra de Cálculo - Documentos Fiscais:***

![CFG 02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37535417565975)

### Se por algum motivo a regra não puder ser identificada dessa forma, há como identificar através dos registros nas tabelas **F2D - Calculo do Tributo** e **CJ3 - Valores dos Tributos**:

1. Consulte o ID que o sistema registra nas tabelas **SD2 (Notas Fiscais de Saída)** no campo **D2\_IDTRIB** e na tabela **SD1 (Notas Fiscais de Entrada)** no campo **D1\_IDTRIB**:

![CFG 03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37535433264791)

2. O ID que consta no campo **D2\_IDTRIB / D1\_IDTRIB**, pode ser identificado na tabela F2D no campo F2D\_IDREL

![CFG 04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37535417569175)

3. O campo F2D\_TRIB registra o código do tributo que pode ser identificado no Configurador de Tributos (FISA170) registrado na tabela **F2B** no campo **F2B\_REGRA**:

![CFG 02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37535417565975)

Filtrando na tabela F2B:  
![CFG 05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37535433266071)

***Saiba mais:***

[SIGAEST - Como configurar o custo de entrada com impostos na TES?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19509172274455-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-configurar-o-custo-de-entrada-com-impostos-na-TES)

[Configurador de Tributos - Regras de Custo (MATA041)](https://tdn.totvs.com/x/ZM-HNg)
