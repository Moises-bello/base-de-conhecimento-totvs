---
article_id: 360041905853
category: SIGAEST - PROCESSAMENTOS
content_hash: 642e56f27d3ad6efc8913d987d11fb18024696658f663c84479c647dd741d3d3
fetched_at: '2026-06-28T22:39:04.856921+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Arithmetic overflow
  error converting float to data type numeric
type: support-article
updated_at: '2025-10-22T19:01:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041905853-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Arithmetic-overflow-error-converting-float-to-data-type-numeric
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19876683772567) Tempo aproximado para leitura: 00:03:05 min**

**Dúvida**

Ao executar as rotinas Recálculo do **Custo Médio, Refaz Saldo, Virada de Saldo** ou outras rotinas que utilizam Stored Procedures apresentarem o erro de "**Arithmetic overflow error converting float to data type numeric"**  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

O erro "**Arithmetic overflow error converting float to data type numeric**" ocorre quando há uma tentativa de converter um valor de tipo `float` para o tipo `numeric` (ou `decimal`), e essa conversão resulta em um **estouro aritmético**. Este tipo de erro geralmente surge em linguagens de programação que suportam esses tipos de dados, como **SQL**, onde `float` representa números de ponto flutuante e `numeric` (ou `decimal`) representa números decimais com precisão fixa, **e na maioria dos casos ocorre com a utilização das Procedures relacionadas a cada rotina processada**.

**Contextualização do Erro:** A causa fundamental desse erro está na natureza das representações numéricas. O tipo `float` é usado para representar números de ponto flutuante, o que significa que ele tem uma precisão limitada e pode resultar em perda de precisão ao lidar com números muito grandes ou muito pequenos. Ao tentar converter um valor `float` para `numeric`, o sistema pode encontrar uma situação em que a magnitude do número excede a capacidade do tipo `numeric` para mantê-lo sem perda de precisão.

Ao apresentar esse erro, **desinstale a Procedure que a rotina está utilizando** e execute novamente a rotina, e valide se é apresentado algum outro erro, caso sim anexe a avaliação do suporte.

Pois quando a Procedure está instalada, ela não mostra qual é o campo que apresenta o problema.

**COMO REINSTALAR A PROCEDURE AQUI:**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel>

**Para o** **Erro** **Data width error****, temos a documentação abaixo que irá te auxiliar:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=271655678>

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como avaliar o erro Data width error em rotinas de processamento?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17995686483095?source=search)

Escrita e código de mais erros em diferentes bancos:

**SQL Server:**  
**Erro 8115:** "Arithmetic overflow error converting expression to data type [data\_type]."

**Oracle:**  
**ORA-01438:** "value larger than specified precision allowed for this column"

**PostgreSQL:**  
**ERRO:** "numeric field overflow"

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

*[Clique aqui e veja mais artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)*
