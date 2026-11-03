---
article_id: 6302001891991
category: Faturamento - Cadastros
content_hash: 69825f90418844b5e97ea8f574fae559233e9e37cb9268bc7a73b317c6af149a
fetched_at: '2026-06-28T22:38:35.563872+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: 'Cross Segmentos - TOTVS BackOffice (Linha Protheus) - SIGAFAT – HELP: A1_TPFRET,
  Problema: Descrição da Regra de Base de Cálculo - Todas as versões'
type: support-article
updated_at: '2022-05-24T20:08:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6302001891991-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-SIGAFAT-HELP-A1-TPFRET-Problema-Descri%C3%A7%C3%A3o-da-Regra-de-Base-de-C%C3%A1lculo-Todas-as-vers%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00min**

**Dúvida**Por que ao colocar um tipo de frete em um cliente no campo A1\_TPFRET, ao retornar para a opção do frete em branco ele não permite?

**Ambiente**Cross Segmentos - TOTVS BackOffice (Linha Protheus) - SIGAFAT – Todas as versões

**Solução**

Qualquer campo no formato de opção de escolha, como por exemplo, o A1\_TPFRETE em questão, possuem uma opção em branco e a demais opções de escolha para que aquele campo,  que possui o mesmo valor de como se estivesse em branco.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6301745324823/mceclip1.png)

Ao não selecionar uma opção das disponibilizadas e, manter o campo em branco, o sistema segue os processos normalmente e é possível concluir as operações.

Caso haja alteração de um campo em branco para uma opção disponível, não é possível voltar o status anterior do campo (escolher a última opção em branco).

Com base no exemplo acima, a melhor opção que equivale ao comportamento da opção em branco (última) é a opção "**S - Sem frete**".

Uma vez feito a escolha de uma das opções, caso tente retornar para a opção em branco, o sistema  não permitirá e apresentará algum **HELP**.  No caso do **campo A1\_TPFRET**, apareceu este **HELP:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6301725632279/mceclip0.png)

O HELP é referente apenas a escolha da opção em branco, já a descrição do problema se dá ao fato de que o sistema está utilizando todas as variáveis recebidas para fazer o cálculo geral dos valores da tabela **SA1 - Cadastro de Clientes**, desta forma,  o sistema não aceitará o retorno da opção em branco após ter selecionado uma das opções disponíveis para o preenchimento do campo.
