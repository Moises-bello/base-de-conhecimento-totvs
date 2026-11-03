---
content_hash: 2a3f23f2336c9be98f0696078f78de4a0317ae2f6d14ba240aa635c9eb50bb3e
fetched_at: '2026-06-29T00:10:47.590301+00:00'
page_id: '559496971'
product: rm
source: tdn-rm
title: Composição dos valores da parcela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=559496971
version: 41
---

---

Consultando a Central Financeira no lado esquerdo da tela é possível avaliar quais os valores detalhados que á compõe a parcela, levando em consideração o cálculo por crédito das disciplinas, descontos de parcelas, descontos por antecipação, aproveitamento de conta corrente, detalhamento das bolsas condicionais e incondicionais entre outros.

Esta funcionalidade retorna de forma detalhada informações relacionadas aos valores que compõem o cálculo da parcela conforme as disciplinas matriculada, levando em consideração a parametrização que define como os crédito serão processados.

Disciplina

6
complete
**PARCELA DE VALOR FIXO**

Para o **Serviço** de uma parcela fixanão será gerado detalhamento do cálculo por disciplina.

5
complete
**PARCELA CALCULADA POR CRÉDITO**

No **Serviço** de uma parcela por crédito, quando se expande o serviço será apresentando os detalhes do cálculo das disciplinas (quando a parcela estiver parametrizada para calcular por crédito) , tais como valor da disciplina, n° crédito, valor do crédito, valor da disciplina no contrato, data de matricula, e quantidade de parcelas.

Em função da parametrização, podemos ter algumas particularidades no cálculo dos valores por disciplinas que poderão ser apresentadas como abatimentos ou acréscimos, neste caso o sistema vai destacar o item com um ícone de exclamação, ao passar o mouse sobre o ícone será apresentado uma descrição informando a que particularidade está relacionado o item de cálculo.

* **Parcelas calculadas por crédito, com abatimento (cancelamento de disciplina ou parcela fixa)**

* **Parcelas calculadas por crédito, com acréscimo (inclusão de disciplina)**

Informações

Para contratos legados que não exista o detalhamento do cálculo por crédito, o sistema não conseguirá montar um detalhamento que identifique quais parcelas a disciplina foi cobrada e qual o valor a ser devolvido por parcelas.

 Para saber como é feito a cobrança por crédito, **[clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=4815054)**

Desconto da parcela e antecipação

8
complete
**DESCONTO DA PARCELA (percentual ou fixo)**

9
complete
**DESCONTO POR****ANTECIPAÇÃO**

Será apresentando em colunas os valores de desconto para cada vencimento de acordo com a quantidade de itens cadastrado no desconto por antecipação associado ao aluno, para saber sobre as regras do desconto por antecipação, **[clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=325847718)**

* **Valor Auxiliar no Desconto por Antecipação**

Na tela também será apresentando os valores auxiliares do desconto por antecipação ao expandir a lina do detalhamento do desconto por antecipação, informações sobre o Valor Auxiliar, 

Bolsas Incondicionais e Condicionais

10
complete
**BOLSAS INCONDICIONAIS**

As bolsas incondicionais serão apresentadas na tela da composição dos valores da parcela aplicado o desconto fixo ou calculado por percentual, para calcular o desconto da bolsa incondicional deve se levar em consideração também os parâmetros que impactam o calculo da bolsa.  
  
Como por exemplo:

Parâmetros que possui no cadastro de Bolsa ou no Contrato:

* **Tipo da bolsa** (Somar Bolsas, Cascata, Aplicar Maior Bolsa)  e **Aplicar desconto por antecipação** (Antes ou Depois do cálculo da bolsa)

11
complete
**BOLSAS CONDICIONAIS**

As bolsas condicionais serão apresentadas na tela da composição dos valores da parcela aplicado o desconto fixo ou calculado por percentual, para calcular o desconto da bolsa condicional deve se levar em consideração também os parâmetros que impactam no calculo da bolsa ou perda.

Como por exemplo:

Parâmetros que possui no cadastro de Bolsa ou no Contrato:

* **Tipo da bolsa** (Somar Bolsas, Cascata, Aplicar Maior Bolsa)  e **Aplicar desconto por antecipação** (Antes ou Depois do cálculo da bolsa)

Parâmetros do Educacional:

* Mantém fórmula para valor opcional / Integração de bolsas condicionais
* O Calculo das bolsas condicionais levará em consideração o desconto por antecipação aplicado no momento da baixa do lançamento financeiro.

Para mais detalhes sobre os cálculos das bolsas, **[clique aqui.](https://tdn.totvs.com/display/LRM/Bolsa+do+contrato)**

* **Valores Auxiliares nas Bolsas**

Na tela também será apresentando os valores auxiliares das bolsas ao expandir a linha do detalhamento das bolsas, informações sobre o Valor Auxiliar, 

Pagamento a Maior e Menor

12
complete
**PAGAMENTO A MAIOR**

Quando o responsável financeiro realiza o pagamento do boleto com valor maior que o valor liquido será considerado no sistema o pagamento a maior e esse valor será incluído na conta corrente do aluno e na tela será mostrado na tela de Resumo do cálculo.

13
complete
**PAGAMENTO A MENOR**

Quando o responsável financeiro realiza o pagamento do boleto com valor menor que o valor liquido será considerado no sistema o pagamento a menor e esse valor será incluído na conta corrente do aluno e na tela será mostrado na tela de Resumo do cálculo.

Para mais detalhes sobre os pagamento a maior ou menor, **[clique aqui.](https://tdn.totvs.com/display/LRM/Conta+Corrente+do+aluno)**

Bolsas Retroativas

18
complete
**INCLUSÃO DE BOLSA****RETROATIVA**

Quando existe a inclusão da bolsa retroativa será apresentado na parcela que foi aproveitado o crédito uma linha com o Valor de devolução da bolsa retroativa.

19
complete
**EXCLUSÃO DE BOLSA****RETROATIVA**

Já para exclusão da bolsa será criado uma nova parcela será criada no contrato e será apresentado no detalhamento somente com o valor da parcela. 

Para mais detalhes sobre bolsa retroativa, **[clique aqui.](https://tdn.totvs.com/display/LRM/Bolsa+do+contrato)** 

Aproveitamento de Conta Corrente

Quando existe algum valor na conta corrente do aluno seja ele gerado pelo pagamento a maior ou menor, ou gerado pela bolsa retroativa ao aproveitar esses valores no lançamento será mostrado na tela de Composição e Resumo do cálculo. 

Para mais detalhes sobre os pagamento a maior ou menor, **[clique aqui.](https://tdn.totvs.com/display/LRM/Conta+Corrente+do+aluno)**

Valores de Integração - TOTVS Financeira

Nas parcelas com lançamentos gerados serão apresentados também os Valores de Integração Financeira. 

Campos que serão disponibilizados no TOTVS Financeiro para cadastro de valores de integração direto no financeiro, podendo definir uma fórmula. Para saber mais sobre esses campos,  e acesse o tópico de **Valores de Integração do TOTVS Financeira.**

Resumo do cálculo

No resumo do cálculo serão detalhados todos os valores que impactam no valor líquido do lançamento do aluno, com suas bolsas, descontos, aproveitamento de conta corrente, pagamento a maior e menor, créditos de bolsa retroativa, multas, juros, Valores de Integração do TOTVS Financeiro entre outros.

Simulação do cálculo de baixa

Simulação das parcelas geradas e que estão em aberto informando a “Data de previsão de baixa”.

 Como Fazer

---

[Detalhamento do Cálculo da Parcela por Disciplina](http://tdn.totvs.com/pages/viewpage.action?pageId=412886824)[Detalhamento dos Valores da Parcela do Contrato via Webservice](http://tdn.totvs.com/x/o8gBGQ)
