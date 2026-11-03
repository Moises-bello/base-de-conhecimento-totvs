---
article_id: 39423383538071
category: Encargos
content_hash: 9a968aa5716614e3d600b1d6baff1a2dbd77960c3fe7a90a39027ab835979385
fetched_at: '2026-06-28T22:46:52.171980+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP -  Como analisar o log do erro:  Não foi encontrado Agrupamento
  Contábil'
type: support-article
updated_at: '2026-04-01T16:58:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39423383538071-RH-RM-FOP-Como-analisar-o-log-do-erro-N%C3%A3o-foi-encontrado-Agrupamento-Cont%C3%A1bil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39423414797335) Tempo aproximado para leitura: 00**:08:14 min**  
  
**Dúvida**  
Como identificar a causa e analisar o log do erro abaixo, apresentado na geração de lançamentos contábeis (Encargos | Geração dos Lançamentos Contábeis) ?

**Não foi encontrado Agrupamento Contábil na seguinte parametrização:**  
**Código Encargo: xxx**  
**Grupo contábil: xxx**  
**Integração contábil: Sem preencher**  
**Integração funcionário: Sem preencher**  
**Conta Gestão Contábil: Sem preencher**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento  
  
**Solução**

Este erro ocorre devido à falta de parametrização contábil, e a própria mensagem de erro indicará o que está faltando ser preenchido. No entanto, antes disso, é necessário verificar qual é o tipo de contabilização utilizado: **por centro de custo, por seção ou por funcionário.**  
  
***Importante:***

Após identificar qual o tipo de contabilização é de extrema importância saber qual é a configuração utilizada pela empresa, se utilizam ou não integração contábil.  
  
A integração contábil aqui referida é:

Quando no processo de criação dos agrupamentos é definida a utilização de integração, poderão ser criados diversos agrupamentos para um mesmo grupo de conta, desde que a integração seja diferente.

A integração é utilizada quando um mesmo evento, ou encargo, deve ser lançado em contas diferentes, dependendo da seção ou centro de custo utilizado. Agrupa informações de uma mesma natureza ou procedência.

São três tipos de integração:

* **Por seção:** para quem não trabalha com cálculo por centro de custo relacionado ao funcionário;
* **Por Centro de custo:** para quem tem o centro de custo relacionado ao funcionário;
* **Por funcionário:** Cada funcionário tem sua integração.

Uma forma de identificar qual o tipo de contabilização que está sendo utilizado é através do log gerado no final da rotina **Encargos | Lançamentos contábeis** aba **Execução.**

No exemplo iremos utilizar uma contabilização por centro de custo com integração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39423414797975)

Veja que no cadastro do centro de custo abaixo utilizamos a integração contábil preenchida:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39423383514263)  
  
Como mencionado, a mensagem do erro sinaliza o que deve ser preenchido, veja:

Não foi encontrado Agrupamento Contábil na seguinte parametrização:

      Código Encargo: 001

      Grupo contábil: 213

      Integração contábil: Sem preencher***←  Aqui ele está validando a integração do agrupamento***

      Integração funcionário: Sem preencher

      Conta Gestão Contábil: Sem preencher

A integração do agrupamento estará localizada dentro do cadastro **Encargos | Cadastros contábeis | Agrupamentos:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39423414801175)

Caso utilize a integração por funcionário, a coluna preenchida será a **Código Integração por funcionário**. Essa parametrização é definida pela organização, sendo necessário a validação interna e o conhecimento de qual parametrização é praticada na organização.

O grupo contábil é a coluna **Grupo Conta**, localizado dentro do cadastro deste agrupamento que será informado a conta do Gestão contábil.

E é esse agrupamento que será informado dentro da aba dados contábeis do evento ou do encargo a ser contabilizado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39423383520535)

No exemplo apresentado, o erro ocorre porque a organização utiliza integração no centro de custo cadastrado em rateio fixo para a chapa. Nesse caso, a causa está na ausência da marcação da flag **“Tem Integração”** na aba **Dados Contábeis** do encargo. Essa marcação é necessária para que, no momento do lançamento, o sistema direcione corretamente para a integração “0”, conforme definido nas parametrizações do agrupamento da conta 213 a crédito.

Se a flag **“Tem Integração”** do grupo de conta crédito 213 (na aba Dados Contábeis do encargo) estiver desmarcada, ao gerar o lançamento o sistema irá buscar, em **Cadastros | Agrupamento Contábil**, um agrupamento com a conta 213 sem a informação de integração preenchida. Porém, como a empresa do exemplo utiliza integração, o ajuste correto não deve ser feito no cadastro do agrupamento, e sim na parametrização da aba **Dados Contábeis do encargo**.

Ao marcar a flag **“Tem Integração”**, o problema é corrigido. Ainda assim, o erro também pode ocorrer em outras situações, como:

* Ausência de cadastro do agrupamento contábil apontando para a integração “0”;
* Falta de preenchimento da informação de integração no cadastro do centro de custo.

É importante destacar que as validações devem ser realizadas conforme o tipo de parametrização contábil adotado:

* **Por seção**: verificar a aba **Dados Contábeis da seção**;
* **Por funcionário**: validar as informações no cadastro do funcionário, na aba **Dados Contábeis**.

Após a marcação da flag na aba **Dados Contábeis** do cadastro do encargo “001”, o erro deixa de ocorrer.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39423383521559)

Saiba mais:

[Parametrização para Contabilização - 11.0](https://tdn.totvs.com/pages/releaseview.action?pageId=110428888)

[RH - RM - FOP - Contabilização por centro de custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8895372319511-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o-por-centro-de-custo)

[RH - RM - FOP - Contabilização com integração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8770221333271-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o-com-integra%C3%A7%C3%A3o)

[RH - RM - FOP - Cadastro de código de integração contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8021819655447-RH-RM-FOP-Cadastro-de-c%C3%B3digo-de-integra%C3%A7%C3%A3o-cont%C3%A1bil)
