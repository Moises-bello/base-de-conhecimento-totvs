---
content_hash: 9633070138683b350587cc5d0f9fb316c6e3dd9a76fbca0eebfaac73e7239677
fetched_at: '2026-06-29T00:09:16.323224+00:00'
page_id: '421385513'
product: rm
source: tdn-rm
title: Taxas
type: documentation
url: https://tdn.totvs.com/display/LRM/Taxas
version: 80
---

**Taxas**
Através do cadastro de taxas pode-se efetuar o cálculo da taxa do BDI do Projeto.
Deve-se inserir as despesas e as bonificações
Através do ícone "Novo registro" ou através da seta para baixo pode-se inserir uma nova taxa. Para cadastrar uma taxa é necessário informar a Descrição, o Tipo (Despesa ou Bonificação) e o Valor (%).
Através do ícone "Excluir registro" pode-se excluir as taxas cadastradas.
 
\* Atenção:\*
Caso o somatório de Despesas e Bonificações seja maior ou igual a 100%, o cálculo do BDI resultará em um valor negativo.
 
\*Resumo\*
Despesas:
Somatório das Taxas de Despesas cadastradas.
Bonificação:
Somatório das Taxas de Bonificações cadastradas.
BDI Taxas/Bonif.:
Nesse campo é feito o seguinte cálculo: \[1/(1-(somatório das despesas e das bonificações/100))\].
Total Direto:
Somatório do valor parcial dos serviços de custo direto.
Total Indireto:
Somatório do valor parcial dos serviços de custo indireto. Para filtrar a listagem das tarefas, visualizando somente serviços de custo indireto, utilize o botão e escolha a opção ''Indiretos, dessa forma, os valores dos mesmos ficam visíveis.
BDI Calculado:
Para se chegar ao Preço de Venda (PV), soma-se o CD (Custo direto) e o CI (Custo Indireto). Nesse resultado aplica-se o BDI Taxas/Bonif..
Com o preço de venda calculado, é feito o cálculo dos percentuais. A soma destes percentuais irá gerar o BDI do projeto.
Encontra-se a relação entre o custo direto e o custo indireto (CD / CI).
Encontra-se o valor absoluto das taxas e bonificações (BDI Taxas/Bonif. / 100 \* PV).
Encontra-se a relação enter o valor absoluto das taxas e bonificações e o custo direto (BDI Taxas/Bonif. /100 \* PV) / CD.
O BDI do projeto é a soma da relação entre o custo direto e o custo indireto (CI / CD), com a relação entre o valor absoluto das taxas e bonificações e o custo indireto (BDI Taxas/Bonif. / 100 \* PV) / CD e com o valor unitário (1).
O BDI do projeto calculado é transferido para a subpasta BDI - Fator K, campo Taxa.
\* Exemplo:\*
Considere,
CD = 582.786,06
CI = 218.965,99
Taxas:  Incidência Matriz = 5%
Impostos = 10,6%
Bonificações = 15%
åTaxas = 30,6% (5+10,6+15)
O BDI Taxas/Bonif. (BDI Parcial) é calculado através da fórmula \[1/(1-(somatório das despesas e das bonificações/100))\].
BDI Taxas/Bonif. = 1 / (1-0,306) = 1,4409
Logo, o PV = (CD+CI) \* BDI Taxas/Bonif. = (582.786,06+218.965,99)\* 1,4409 = 1.155.244,53
Encontrando a relação entre o custo direto e o custo indireto:
%CI = CI / CD = 218.965,99 / 582.786,06 = 0,3757 (37,57%)
Encontrando o valor absoluto das taxas e bonificações:
TX absoluto = ∑Taxas /100 \* PV = 0,306 \* 1.155.244,53 = 353.504,83
Encontrando a relação entre o valor absoluto das taxas e bonificações e o custo direto:
%TX = TX absoluto / CD = 353.504,83 / 582.786,06 = 0,6066 (60,66%)
BDI do Projeto = 1 + 0,3757 + 0,6066 = 1,9823
 
Comprovando o valor do BDI:
O valor CD = 582.786,06, CI = 218.965,99
Taxas = 0,306 \* 1.155.256,81 = 353.508,58
Total = 1.155.260,64 (582.786,06 + 218.965,99 + 353.508,58)
Os valores não batem exatamente, devido aos arredondamentos.]]>
