---
content_hash: b140dbf86d022384096b1c0186bde238551272eca809388945ab79be8a95e128
fetched_at: '2026-06-29T00:09:33.884603+00:00'
page_id: '425459073'
product: rm
source: tdn-rm
title: Parcelas do Contrato Educacional
type: documentation
url: https://tdn.totvs.com/display/LRM/Parcelas+do+Contrato+Educacional
version: 33
---

---

Nesta tela se cadastra as Parcelas do contrato do aluno.

**Criação de parcelas de origem do Plano de Pagamento**

Ao informar um plano de pagamento ao contrato, caso o plano tenha as parcelas, as mesmas já serão automaticamente geradas, porém, existem outras situações que o contrato terá outras parcelas além das geradas pelo plano de pagamento.

Data de Vencimento da Parcela

A data de vencimento da parcela será a mesma data de vencimento definido nas parcela do plano de pagamento, no entanto o cadastro de parcela do plano de pagamento possui a opção "**Data de Vencimento Flexível**" que será aplicada quando a data de vencimento da parcela for menor que a data de inclusão do plano de pagamento no contrato do aluno.

Quando este cenário ocorrer e o campo "**Data de Vencimento Flexível**" estiver marcado a nova data de vencimento irá considerar a seguinte regra:

**Data inclusão plano pagamento contrato + Núm. de dias para acrescentar na Data Venc. Flexível na parcela** (o parâmetro pode ser acessado em ***Educacional | Tesouraria | Geral 2/2**)*

**Exemplo:**

→Data execução da matricula no portal  = 23/06/2021

→Parcela do Plano de Pagamento:

Data de Vencimento = 01/06/2021

Data de Vencimento Flexível  = Marcado

→Núm. de dias para acrescentar na Data Venc. Flexível na parcela = 5 dias 

Nova Data de Vencimento da Parcela: **28/06/2021 (**23/06/2021 + 5 dias **)**

Vencimento em dia não útil

A nova data de vencimento irá respeitar o parâmetro "**Vencimento em dia não útil**" que pode ser acessado em ***Educacional | Integração | Financeiro | Educacional | Geral 1/4***

**IMPORTANTE:** Essa funcionalidade está disponível somente à partir da versão 12.1.33 do sistema.

**Valor simulado da parcela**

Na visão de parcelas do contrato foi inserida, no contexto de ensino superior, a coluna Valor Simulado, que traz, caso a parcela seja marcada para ser gerado por créditos, o valor simulado original sem bolsas e sem desconto. Caso a parcela não seja marcada para ser gerada através dos créditos a coluna valor simulado traz o valor original da parcela.

Para saber mais  e verifique o subtítulo "Usar valor do crédito financeiro da matriz curricular do aluno".

**Anexo lançamentos / boletos da parcela**

Na tela de edição de parcela, o campo que exibia a referência para o lançamento foi retirado. Agora os lançamentos, bem como os boletos do lançamento, são exibidos através do anexo lançamentos / boletos da parcela.

Nesse anexo serão exibidos os dados mais relevantes e ao efetuar um duplo clique na visão, o registro é aberto para edição.

**Parcela gerada cancelada**

O sistema passou a permitir a edição de uma parcela gerada cancelada, mas com o parâmetro de "Permitir regerar lançamentos cancelados" marcado, o parâmetro pode ser acessado em ***Educacional | Integração | Financeiro | Educacional | Geral 1/4******.***

**Parcelas geradas por acordo financeiro**

O parâmetro de "Preenche mês/ano de competência da parcela com mês/ano do acordo", o parâmetro pode ser acessado em ***Educacional | Tesouraria | Geral 1/2***, quando preenchido, as parcelas geradas por acordo financeiro virão com a Data de Competência preenchida com a data do primeiro dia do mês que o acordo está sendo realizado.

Se desmarcar o parâmetro a Data de Competência virá em branco nas parcelas geradas pelo acordo.

**Geração de lançamentos com valor zerado**

O TOTVS Educacional, tem a  opção de verificar o parâmetro do TOTVS Gestão Financeira , que informa se é permitido a geração de lançamentos com valor zerado. Se este parâmetro estiver marcado, o o TOTVS Educacional  também vai permitir a geração desses lançamentos.

**Concessão de bolsa futura**

Toda e qualquer inserção/alteração no cadastro da parcela é verificado se existe  cadastrada. O sistema irá verificar o período da concessão e a data de vencimento da parcela. Se a data de vencimento estiver dentro do período da concessão, a  será cadastrada e o quando o lançamento for  o desconto será concedido para aquela parcela.

Como Fazer

---

[Gerar Lancamento](http://tdn.totvs.com/pages/viewpage.action?pageId=425459455)[Central Financeira](https://tdn.totvs.com/display/LRM/Central+Financeira)[(Detalhamento do Cálculo da Parcela)](https://tdn.totvs.com/display/LRM/Central+Financeira)  
[Detalhamento do cálculo da bolsa do aluno](https://tdn.totvs.com/pages/viewpage.action?pageId=531024083)
