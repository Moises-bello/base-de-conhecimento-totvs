---
article_id: 360021517971
category: SIGAEST - RELATORIOS
content_hash: 183841597387752e8d47136b62e056ea4fd9c917461d10a1f78bbad3191ed77f
fetched_at: '2026-06-28T22:39:06.244092+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Relatório MATR320
  -  Conceito e Condições
type: support-article
updated_at: '2025-12-12T12:34:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021517971-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Relat%C3%B3rio-MATR320-Conceito-e-Condi%C3%A7%C3%B5es
---

O relatório MATR320 exibe um resumo por tipo de produto das entradas e saídas, onde a coluna "Saldo Inicial" é calculada a partir das outras colunas, não representando o saldo cadastrado no sistema. O parâmetro MV\_PAR09 "Saldo a Considerar" define se o saldo é Atual, Fechamento ou por Movimento, influenciando o cálculo do saldo no relatório. Para comparar com o MATR260, deve-se usar "Saldo a Considerar" = Movimento e ajustar a data.

**Dúvida**

Qual o conceito e quais condições que o relatório MATR320 (Entradas e Saídas) utilizam para sua extração?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

O relatório MATR320 permite visualizar um resumo, **por tipo de produto**, todas as suas entradas e saídas.  No relatório, **a coluna** ***Saldo Inicial*** **é o resultado das outras colunas do relatório, e** **não o Saldo Inicial** **cadastrado para cada item no sistema**. Veja no link abaixo mais detalhes sobre o cálculo para apresentar o Saldo Inicial no relatório.

Um exemplo sobre o cenário acima é o caso de **"produtos Mão de Obra (MOD)** ***com*** **Integração Contábil" (**[*link*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402062082071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-de-configura%C3%A7%C3%A3o-de-MOD-e-GGF-com-e-sem-integra%C3%A7%C3%A3o-cont%C3%A1bil)**)**, onde a coluna Saldo Inicial é representada pelo Valor que foi importado para o Centro de Custo dentro do período de processamento, dessa forma é raro que o Saldo Atual do período seja exatamente o mesmo do período anterior.

[***RELATÓRIO DE ENTRADA E SAÍDAS***](https://tdn.totvs.com/x/yQ6aHg)

[***https://tdn.totvs.com/x/yQ6aHg***](https://tdn.totvs.com/x/yQ6aHg)

**Condições do Relatório MATR320 – Entradas/Saídas -** **Pergunta chave:** **"Saldo a Considerar" O parâmetro MV\_PAR09** **"Saldo a Considerar"****, apresenta o resultado conforme as instruções abaixo:**

|  |  |
| --- | --- |
| **Atual** | **Considera a quantidade e valor atual (****B2\_QATU, B2\_VATU****).** |
| **Fechamento** | **Considera a quantidade e valor final (****B2\_QFIM, B2\_VFIM****)** |
| **Por Movimento** | **Considera a função calcest() para calcular o saldo dos movimentos até a data presente (pela data do último fechamento do SB9) descontando todas as movimentações do SD1 e SD2** |

![MATR320 02.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/29630837392663)

Coluna de Saldo Atual e Saldo Inicial do Relatório:

**1)** **Saldo Atual:** Dependendo a opção que escolher no Parâmetro, "Saldo a Considerar":

**Saldo ATUAL** => Saldo com todos os movimentos incluídos no sistema (independentemente da data). É gravado nos campos **B2\_QATU e B2\_VATU1 a B2\_VATU5**

**Saldo FINAL**=> Saldo com os valores calculados conforme data do último processamento do CUSTO MÉDIO (independe da data). Ou seja, é gravado os campos **B2\_QFIM e B2\_VFIM1 a B2\_VFIM5**

**Saldo por MOVIMENTO** => Saldo com os **valores calculados de acordo** **com os movimentos** cadastrados e com a **data informada para referência**. É calculado através da função CALCEST.

**Como parametrizar o relatório de Entradas e Saídas para ver meu saldo resultante dos movimentos do dia a dia?**

Caso queira comparar as entradas e saídas com o relatório "Posição de Estoque" (MATR260), deverá parametrizar, no MATR320, o **"Saldo a Considerar" = Movimento** e colocar a data desejada para deixar pareado com o relatório MATR260. [Caso queira saber como parametrizar o MATR260 corretamente, clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016177632-MP-SIGAEST-Como-parametrizar-o-relat%C3%B3rio-MATR260-corretamente-?source=search)

**Calculo que cada coluna do MATR320 realiza para compor o resultado:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4436082259607)

**OBS: Alteração no calculo da coluna " Requisições para produção" do MATR320 é:**

Somatória das requisições com D3\_TM >= 500 com D3\_OP preenchido  
**MENOS**  
Somatória das requisições com D3\_TM =< 499 com D3\_OP preenchido

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Relatórios no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)
