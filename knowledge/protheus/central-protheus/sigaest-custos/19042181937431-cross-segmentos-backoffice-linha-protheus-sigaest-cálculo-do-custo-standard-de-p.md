---
article_id: 19042181937431
category: SIGAEST - CUSTOS
content_hash: 13fecd88dcfc4a048ff88fc6967e8c4ed095c0122c3b320448f299e152c11994
fetched_at: '2026-06-28T22:39:02.430791+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAEST - Cálculo do Custo
  Standard de Produto do tipo "PA" por estrutura.
type: support-article
updated_at: '2023-11-17T12:09:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19042181937431-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAEST-C%C3%A1lculo-do-Custo-Standard-de-Produto-do-tipo-PA-por-estrutura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19042217879831) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como funciona o cálculo Cálculo do Custo Standard de Produto do tipo "PA" por estrutura?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**

Quando o produto é produzido dentro de sua empresa e ele faz parte de uma estrutura, a rotina de "Custo de Reposição" (MATA320) deve ser executada com a resposta "Estrutura"

**Exemplo**:

PA -  
       |\_MP1 QTD na estrutura = 20 itens e B1\_CUSTD 11,00  
       |\_MP2 QTD na estrutura = 200 itens e B1\_CUSTD 11,00

11 (B1\_CUSTD) \* 20 (Qtd na Estrutura) = 220,00  
11 (B1\_CUSTD) \* 200 (Qtd na Estrutura) = 2200

Ou seja, Quantidade Consumida \* Custo Standard de cada MP.

Ao executar a rotina “Custo Standard/Custo de Reposição” (MATA320), para formarmos o Custo Standard dos nossos PA's, selecionando a pergunta "Calcular os custos por?" = Estrutura, o valor a ser gravado no cadastro do produto PA, neste exemplo, será B1\_CUSTD = 2.420,00 (que basicamente é a soma do Custo Standard do MP1 e MP2, já que fazem parte da estrutura.

Saiba mais:

[Conceito de utilização da rotina MATA320 - Custo Standard/Custo de Reposição - B1\_CUSTD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013572791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-de-utiliza%C3%A7%C3%A3o-da-rotina-MATA320-Custo-Standard-Custo-de-Reposi%C3%A7%C3%A3o-B1-CUSTD)

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
