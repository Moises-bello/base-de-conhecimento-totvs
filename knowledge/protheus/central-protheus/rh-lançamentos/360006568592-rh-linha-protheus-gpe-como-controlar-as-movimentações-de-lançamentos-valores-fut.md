---
article_id: 360006568592
category: RH - Lançamentos
content_hash: e1f362e64442912c2096d7d62aa8216ca575698db7279e3cdae82d15690a6d90
fetched_at: '2026-06-28T22:43:31.169731+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Como controlar as movimentações de Lançamentos
  Valores Futuros
type: support-article
updated_at: '2025-07-24T18:11:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006568592-RH-Linha-Protheus-GPE-Como-controlar-as-movimenta%C3%A7%C3%B5es-de-Lan%C3%A7amentos-Valores-Futuros
---

#### time.png Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Como controlar as movimentações dos lançamentos de Valores Futuros, tais como desconto efetuados de parcelas, solicitações, suspensões, cancelamentos ou exclusões de pagamentos?**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**A rotina **Conta Corrente Valores Futuros**é responsável por controlar as movimentações dos **Lançamentos de Valores Futuros**, tais como **baixa** de parcelas, **solicitações, suspensões, cancelamentos** ou **exclusões** de pagamentos.

Para cada lançamento de valor futuro de pagamento ou estorno incluído, o sistema **atualiza** as informações de **número de parcelas pagas,** valor **total** pago e **saldo.**

A **situação** do lançamento é atualizada de acordo com os **movimentos gerados** pelo sistema ou incluídos **manualmente** (movimento lançado para quitação do valor restante).

Quando ocorrer o pagamento através da **Folha de Pagamentos,** a rotina de **fechamento** atualizará a tabela de **Conta Corrente Valores Futuros** (RCK), possibilitando a consulta do usuário de todos os pagamentos efetuados em seus respectivos períodos.   
Na versão 12, dependendo da política de cada cliente, permitirá o **pagamento** e, consequentemente, a **baixa** de parcelas sem transitar na Folha de Pagamento, ou seja, a baixa das parcelas poderá ocorrer por esta rotina.

O controle de valores futuros possui o **histórico** de conta corrente dos pagamentos, possibilitando inclusive que o funcionário faça sua **quitação** diretamente no Financeiro/RH.

A situação do lançamento determina se os lançamentos de valores futuros serão **considerados** no **Cálculo da Folha de Pagamento** ou no **Fechamento do Período**.

A situação do lançamento pode ser classificada com:

* **Ativo**- Lançamento válido para cálculos.
* **Solicitado**- Lançamento aguardando aprovação de pagamento ou desconto.
* **Suspenso**- Lançamento não deve ser considerado em alguns períodos de cálculo, até que se tornem ativos.
* **Pago**- Lançamento de quitação.
* **Excluído**- Lançamento estornado.

A situação do lançamento é atualizada de acordo com os movimentos gerados pelo sistema ou através de interferência manual, obedecendo as seguintes regras:

• **De Solicitado para Ativo**: Um lançamento futuro pode ser cadastrado apenas como solicitação, aguardando aprovação de pagamento/desconto. Para ser considerado nos cálculos, deve ter sua situação alterada para Ativo.

• **De Ativo para Suspenso**: É possível suspender o lançamento por um ou mais períodos de cálculo. Quando sua situação é alterada para Suspenso, é registrada uma nova movimentação com o status da suspensão e não será considerado no cálculo, até que sua situação seja alterada para Ativo novamente.

• **De Suspenso para Ativo**: Ao tornar o lançamento Ativo ele passa a ser considerado no Cálculo da Folha.

No Fechamento do Período é gerada uma movimentação para registrar o pagamento/desconto da parcela e o sistema atualiza os campos referentes aos pagamentos.

**Importante:**O status Excluído deve ser utilizado apenas para estornar um movimento lançado indevidamente.  
  
Para tais alterações é necessário entrar na rotina de **Atualizações > Lançamentos > Conta Corrente Valores Futuros (GPEA415).  
  
Exemplos:**Lançamento Futuro lançado para as matrículas 000050, 000051, 000052, 000053, 000054 da seguinte forma:

**Matricula 000050 - Ativo**

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A50%3A50.png?version=1&modificationDate=1474377038000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A51%3A32.png?version=1&modificationDate=1474377038000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A52%3A1.png?version=1&modificationDate=1474377039000&api=v2)

**Matricula 000051 – Suspenso**

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A52%3A43.png?version=1&modificationDate=1474377039000&api=v2)  ![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A53%3A23.png?version=1&modificationDate=1474377039000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A53%3A49.png?version=1&modificationDate=1474377039000&api=v2)  
  
**Matricula 000052 – Lançamento a ser quitado**

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A54%3A19.png?version=1&modificationDate=1474377039000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A54%3A44.png?version=1&modificationDate=1474377039000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A55%3A12.png?version=1&modificationDate=1474377039000&api=v2)  
  
**Matricula 000053 – Solicitado**   
  
![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A55%3A43.png?version=1&modificationDate=1474377039000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A56%3A16.png?version=1&modificationDate=1474377039000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A56%3A49.png?version=1&modificationDate=1474377039000&api=v2)

**Matricula 000054 – Ativo**  
  
![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A57%3A33.png?version=1&modificationDate=1474377039000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A58%3A1.png?version=1&modificationDate=1474377039000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A58%3A27.png?version=1&modificationDate=1474377039000&api=v2)

Agora, fecharemos o período e fazer alterações.

Matricula 000050 – **Ativo**. Essa matricula **não** será alterada, pois deverá ser descontado esses R$ 200,00 mensalmente  
  
![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A59%3A3.png?version=1&modificationDate=1474377039000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%209%3A59%3A28.png?version=1&modificationDate=1474377039000&api=v2)  
  
Matricula 000051 – **Suspenso -> Ativo**. Iremos **Alterar** de Suspenso para Ativo para que a primeira parcela possa ser descontada e dar início ao seu pagamento. O suspenso poderá ser efetuado no meio dos pagamentos das parcelas.

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A0%3A47.png?version=1&modificationDate=1474377038000&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A1%3A24.png?version=1&modificationDate=1474377038000&api=v2)

Após salvar, a informação de baixo será alterada de Suspenso para Ativo

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A1%3A51.png?version=1&modificationDate=1474377038000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A2%3A15.png?version=1&modificationDate=1474377038000&api=v2)  
  
Matricula 000052 – **Quitado** (não irá mais descontar). Como já quitamos esse valor, a verba 502 não irá mais aparecer no recibo do funcionário. Na informação abaixo, a situação fica como Pagamento.   
  
![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A2%3A47.png?version=1&modificationDate=1474377038000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A3%3A12.png?version=1&modificationDate=1474377038000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A3%3A36.png?version=1&modificationDate=1474377038000&api=v2)  
  
Matrícula 000053 – **Solicitado -> Ativo**. Iremos **Alterar** de Solicitado para Ativo para que a primeira parcela possa ser descontada e dar início ao seu pagamento. O solicitado somente poderá ser efetuado no cadastramento da verba.   
  
![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A4%3A17.png?version=1&modificationDate=1474377038000&api=v2)  
  
Após salvar, a informação de baixo será alterada de Solicitado para Ativo   
  
![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A5%3A20.png?version=1&modificationDate=1474377038000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A5%3A49.png?version=1&modificationDate=1474377038000&api=v2)   
Matricula 000054 - **Ativo -> Exclusão**. Esse lançamento será excluído para que ele seja estornado do recibo do funcionário.

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A6%3A29.png?version=1&modificationDate=1474377038000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A7%3A12.png?version=1&modificationDate=1474377038000&api=v2)

Após salvar, o lançamento abaixo fica com o mesmo status da parte de cima. Como utilizei suspenso, ele não aparece no cálculo do funcionário.   
  
![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A7%3A54.png?version=1&modificationDate=1474377038000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A8%3A25.png?version=1&modificationDate=1474377038000&api=v2)

![](https://tdn.totvs.com/download/attachments/256316042/image2016-9-20%2010%3A8%3A47.png?version=1&modificationDate=1474377038000&api=v2)

**Obs: Caso o sistema não esteja permitindo alterar o campo Status no cabeçalho da rotina Conta Corrente Valores Futuros (SRK), deve verificar se este campo está como Alterar nesta tabela.**

**Acesse o configurador SIGACFG > Base de Dados > Dicionário > Base de Dados > Campos:**  
**Tabela SRK**  
![](https://totvssuporte.zendesk.com/attachments/token/vHUwNBxtqsTxBDouzyCqitKfB/?name=inline-722483864.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/ppC3iamciseEkEszJn3cVRROw/?name=inline1097934808.png)​  
  
**Tabela RCK**  
![](https://totvssuporte.zendesk.com/attachments/token/o9kiVWNiVr3OYkUTkBOJjmLIh/?name=inline202429472.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/dHduBqhkNsdHL8oNiPNHDZ4jG/?name=inline1960097221.png)

**Saiba mais:**

[RH - Lançamentos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781734-RH-Lan%C3%A7amentos)
