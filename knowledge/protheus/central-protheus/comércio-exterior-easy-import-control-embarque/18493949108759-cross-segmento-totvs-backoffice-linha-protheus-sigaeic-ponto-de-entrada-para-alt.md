---
article_id: 18493949108759
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: ed3e94a2a7083b54f2b54153b454b77929059ade4381806ad7e7ac5754dd2e4b
fetched_at: '2026-06-28T22:39:48.858741+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ponto de Entrada
  para Alteração e Validação do Lote de Importação.
type: support-article
updated_at: '2023-10-23T15:39:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18493949108759-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-Entrada-para-Altera%C3%A7%C3%A3o-e-Valida%C3%A7%C3%A3o-do-Lote-de-Importa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18493960176663) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Existe algum Ponto de Entrada para Alterar ou Validar o Lote de Importação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  –*Easy Import Control*– Todas versões.  
  
**Solução**É possível utilizar o Ponto de Entrada da função "**EICDI500"**, parâmetro **"DI500LOTEVAL\_VALLOTE"**, modificando o array **lValLote.**

|  |  |  |  |
| --- | --- | --- | --- |
| Nome | Tipo | Descrição | Referência |
| **DI500LOTEVAL\_VALLOTE** | Lógico | Variável utilizada para validação do número do lote na inclusão. Deve-se usar a variável private cValCampo para a identificação do campo que está sendo validado, no caso do número do lote (e da data de validade) a variável estará com o conteúdo “LOTE”, use a variável lValLote para identificar se a validação está correta ou não (.T., para correto, e .F., para incorreto). A criação do ponto de entrada adicionará novas validações ao sistema, ou seja, as validações já existentes no padrão do sistema continuarão sendo executadas. | lValLote |

**Saiba mais****[Ponto de entrada EICDI500](https://tdn.totvs.com/pages/releaseview.action?pageId=571998687)**
