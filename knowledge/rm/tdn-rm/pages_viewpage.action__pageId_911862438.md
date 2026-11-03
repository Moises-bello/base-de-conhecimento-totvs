---
content_hash: d56f5019575ab764a9610113d9e65da9936b112d5bef93613a7f53c7b54be598
fetched_at: '2026-06-29T00:12:03.596271+00:00'
page_id: '911862438'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Individualizado - Cálculos - Orçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=911862438
version: 2
---

Ao calcular o fechamento com a opção "Orçamento" marcada, o processo utilizará os orçamentos cadastrados para compor o valor total dos lançamentos que serão gerados para cobrança de condomínio.

Para que a apuração do fechamento funcione corretamente, é necessário seguir as seguintes premissas:

No **TOTVS Gestão de Estoque, Compras e Faturamento**, Menu Orçamento, Cadastro dos Valores Orçados, é necessário haver pelo menos um Cadastro de Orçamento.

Para entender como cadastrar um orçamento dentro deste módulo, com suas particularidades, consulte a documentação a seguir 

Este orçamento deverá possuir um período que compreenda a competência em que se deseja executar o fechamento utilizando orçamentos. Além disso também deve possuir uma Natureza Orçamentária/Financeira e um Centro de Custo. Ao informar o período desejado, serão mostrados no grid logo abaixo, os respectivos itens de período com data inicial e final. Para cada item, deve-se informar qual o valor orçado. Este valor será utilizado para a geração de lançamentos do fechamento.

No TOTVS Construção Gestão de Imóveis, no menu Condomínio / Cobrança por Orçamento, deverá existir pelo menos um registro cadastrado, que por sua vez possuirá um item de cobrança associado. Este item de cobrança deverá possuir uma Natureza Orçamentária/Financeira (cadastro anexo) associada, que deverá, obrigatoriamente ser do tipo "A Receber" ou "Ambas".

Para orçamentos que irão compor uma apuração de condomínio, deverão ser do tipo "Despesa". E sua natureza orçamentária financeira do tipo "A Pagar" ou "Ambas". Veja mais sobre essa regra logo abaixo.

**Anexos - Natureza Orçamentária/Financeira**

---

O orçamento classificado como "Despesa" no TOTVS Gestão de Estoques, Compras e Faturamento só pode ser associado à uma natureza orçamentária financeira do tipo "A Pagar" ou "Ambas".

Desta forma, para que o processo de Cobrança por Orçamento no módulo de Condomínio realize os cálculos para este Orçamento durante uma apuração, devemos consultar e cadastrar essa mesma Natureza "A Pagar" ou "Ambas" no anexo de Natureza Orçamentária Financeira presente em *Condomínio / Cobrança por Orçamento / Anexos / Natureza Orçamentária Financeira.*Não é possível associar Naturezas do tipo "A Receber" neste cadastro, visto que os Orçamentos de Condomínio devem ser sempre do tipo "Despesa".

Ao associar no cadastro de Cobrança por Orçamento a mesma Natureza cadastrada no Orçamento de Despesa do TOTVS Gestão de Estoques, Compras e Faturamento o sistema estará pronto para realizar este cálculo.

É importante também que, o Empreendimento que fará parte do cálculo do Orçamento possua o mesmo Centro de Custo cadastrado no Orçamento.

A Natureza Orçamentária "A Receber" deve ser associada ao Item de Cobrança associado a Cobrança por Orçamento. Neste Item de Cobrança só serão permitidas Naturezas do tipo "A Receber" visto que utilizamos esta Natureza para realizar os devidos rateios nos lançamentos a receber do Condomínio.

No cadastro do Item de cobrança também será necessário informar um Modelo de Cálculo de Rateio. As opções são:

* V[alor Fixo](http://tdn.totvs.com/pages/viewpage.action?pageId=435105104)
* [Rateio por CRD](http://tdn.totvs.com/pages/viewpage.action?pageId=435105196)
* [Rateio por Fração Ideal](http://tdn.totvs.com/pages/viewpage.action?pageId=435105183)
* [Rateio por M² Construído](http://tdn.totvs.com/pages/viewpage.action?pageId=435105299)
* [Rateio por M² Locado](http://tdn.totvs.com/pages/viewpage.action?pageId=435105202)
* [Rateio Linear por Total de Subunidade do Empreendimento](http://tdn.totvs.com/pages/viewpage.action?pageId=435105092)
* [Rateio Linear por Total de Subunidade da Unidade](http://tdn.totvs.com/pages/viewpage.action?pageId=435105215)
* [Rateio Linear por Total de Subunidades](http://tdn.totvs.com/pages/viewpage.action?pageId=435105093)

Observações

Para que o fechamento funcione corretamente, a opção "Rateio Linear por Total de Subunidades" deverá ser selecionada neste campo, para vincular cobranças diretamente às subunidades.  
E também um Tipo de Valor. As opções são: Valor Orçado, Valor Realizado.

É importante ressaltar que caso um empreendimento pertença a um centro de custo pai, todos os centro de custo filhos irão participar da cobrança por orçamento. Exemplo: O Empreendimento pertence ao centro de custo 01. Logo, todas as cobranças de orçamento, cadastradas para os centro de custo 01.01, 01.02, 01.03 e assim por diante, irão participar da cobrança por orçamento deste empreendimento.

A cobrança cadastrada poderá ser associada ao empreendimento ou à unidade. Para tanto, deve-se seguir as seguintes regras, respectivamente.

No anexo "Associação de Cobrança por Orçamento" do Empreendimento deverá existir pelo menos um registro cadastrado, que por sua vez deverá estar associado com a Cobrança por Orçamento cadastrada anteriormente. Já no cadastro do Empreendimento, na aba "Gestão Financeira", os campos "Centro de Custo" e "Natureza Orçamentária a receber" devem possuir os mesmos valores informados no Cadastro de Orçamento anteriormente. Ou;

No anexo "Associação de Cobrança por Orçamento" da Unidade deverá existir pelo menos um registro cadastrado, que por sua vez deverá estar associado com a Cobrança por Orçamento cadastrada anteriormente. Já no cadastro da Unidade, o campo "Centro de Custo" deve possuir o mesmo valor informado no Cadastro de Orçamento anteriormente. Neste caso, não é possível associar uma Natureza Financeira/Orçamentária à unidade, sendo assim é indiferente o valor que se informa para este campo no cadastro do Empreendimento, só é importante garantir que os valores deste campo sejam iguais no cadastro de orçamento e no anexo do item de cobrança.

Após ter preenchido todos estes dados, já é possível executar a Apuração, selecionando o processo "Orçamento" e marcando as subunidades que farão parte do processo.

**Veja mais**

---
