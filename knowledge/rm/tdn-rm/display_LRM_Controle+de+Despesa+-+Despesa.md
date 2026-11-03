---
content_hash: d3f6687fdd427f5d62347d8983738eb09e86b2f206c32d72346b2754f7e27320
fetched_at: '2026-06-29T00:09:55.516151+00:00'
page_id: '447090488'
product: rm
source: tdn-rm
title: Controle de Despesa - Despesa
type: documentation
url: https://tdn.totvs.com/display/LRM/Controle+de+Despesa+-+Despesa
version: 12
---

### Introdução

---

O Controle de Despesas foi criado para ser um cadastro único, que visa atender ao módulo de Incorporação, tanto no que tange a parte de vendas, quanto a parte de alugueis e controle de seguros.

O objetivo foi criar uma ferramenta que permita o agendamento do pagamento de despesas (através da geração de movimento) e quando necessária, a consequente solicitação de reembolso (através da geração de lançamentos a receber), ou seja, permita que seja cadastrada uma despesa que irá gerar um movimento a pagar, e também permita gerar lançamentos a receber, para que seja cobrado o reembolso do que foi pago (quando necessário).

Atualmente, a despesa é utilizada para:

* Despesas de aluguel
* Controle de Seguro

### Utilização

---

Para utilizar o controle de despesas, existem dois cadastros diretamente ligados à despesa que precisam ser feitos:

* **Cadastro de Tipo de Despesa**: O tipo de despesa é utilizado para agrupar e para definir a natureza financeira a pagar e receber. Para conhecer mais sobre Tipo de Despesa, [clique aqui](http://tdn.totvs.com/display/LRM/Controle+de+Despesa+-+Tipo+de+Despesa).
* **Cadastro de Regra de Reembolso**: Este cadastro possui as definições que serão usadas para se gerar os lançamentos de reembolso (quando houver), como por exemplo a ordem de prioridade de cobrança. Para conhecer mais sobre Regra de Reembolso, [clique aqui](http://tdn.totvs.com/display/LRM/Controle+de+Despesa+-+Regra+de+Reembolso).

Para realizar a criação das despesas, é possível cadastrar de forma individual, através do **cadastro de despesas.**

Para o módulo de alugueis, é possível criar despesas em lote, para vários imóveis simultaneamente. Para isto, é possível criar uma definição de despesa, onde são informados os parâmetros a serem utilizados para o processamento que irá gerar uma despesa para cada imóvel associado. Para conhecer melhor a **Definição de Despesa**, .

A criação das despesas é feita através de um cadastro simples, que possui particularidades conforme o tipo de despesa.

#### **Campos referentes à Despesa:**

---

* **Coligada:** Permite que seja selecionada a coligada a qual a despesa será cadastrada. É importante notar que, ao selecionar a coligada, todos os parâmetros abaixo serão da coligada da despesa e não da coligada do contexto. Exemplo: Se estou na coligada 7 e estou cadastrando uma despessa na coligada 1, todos os cadastros desta despesa serão da coligada 1. Todos os lançamentos e movimentos serão também gerados na coligada da despesa.
* **Origem:** Este campo é definido internamente pelo sistema, de acordo com o local que é feita sua chamada, podendo ser **Aluguel** ou **Seguro**.
* **Status:** Este campo é preenchido automaticamente pelo sistema. Os status utilizados são:

* + **Não Integrado:** É o status inicial, que é definido por default quando a despesa é criada.
  + **Integrado**: Ao gerar os movimentos e os lançamentos financeiros da despesa, esta tem seu status alterado para "Integrado".
  + **Parcialmente Integrado:**Ao gerar **apenas** os movimentos **ou** os lançamentos financeiros da despesa, esta tem seu status alterado para "Parcialmente Integrado".

* **Ano base:** Ano de referência da cobrança da despesa. Utilizado para ajudar nos filtros do usuário.
* **Competência:** Define a competência da despesa. Por exemplo, uma despesa pode ter vencimento em julho, mas ser referente à competência de junho.
* **Código:** Campo chave do cadastro, que não pode ser repetido. É definido automaticamente pelo sistema de forma incremental.
* **Descrição:** Campo de texto livre, com tamanho máximo de 50 caracteres, para que o usuário defina a descrição da forma que lhe facilite as consultas e busca de despesas. Exemplo: Despesa de IPTU.
* **Número documento:** Número da guia a ser paga como despesa, a mesma deve ser informada nesse campo. Geralmente é informada o mesmo número da guia que consta no documento de cobrança.
* **Tipo de despesa:** Define o Tipo de Despesa da Despesa cadastrada. O tipo de despesa é utilizado para agrupar e para definir a natureza financeira a pagar e receber.
* **Tipo de Pagamento:** Define o Tipo de Pagamento que será utilizado para o processo de geração das parcelas integradas ao movimento que será gerado ou ao lançamento financeiro diretamente.
  + **Parâmetros de movimento:** Define o Tipo de movimento da Despesa. Ele é quem definirá as configurações a serem consideradas no movimento que será gerado pela despesa. Para saber mais sobre Parâmetro de tipo de movimento [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=435105352).
  + **Parâmetros financeiros:**  Define os parâmetros que foram configurados a serem considerados na geração dos lançamentos financeiros que será gerado pela despesa.  Para saber mais sobre parâmetros financeiros [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=435105050).
* **Imóvel:** Imóvel para o qual a despesa será gerada. Uma despesa pode ter apenas um imóvel associado. Este campo apenas é utilizado quando a Origem da despesa está definida como "Aluguel".
  + **Observação:** Caso seja feito o encerramento ou rescisão no **contrato de locação** vinculado ao imóvel da despesa, os lançamentos financeiros de reembolso com data de vencimento posterior ao encerramento ou rescisão serão cancelados.
* **Empreendimento/Unidade/Subunidade:** Define a associação da Subunidade para a qual a despesa será gerada. Uma despesa pode ter apenas uma Subunidade associada. Este campo apenas é utilizado quando a Origem da despesa está definida como "Venda".
  + **Observação:** Caso a Subunidade esteja **vendida** e exista a necessidade de realizar **Distrato, ou Aditivos de Troca de Subunidade ou Troca de Comprador** no contrato, estes só poderão ser efetivados se não existir nenhum lançamento de **Reembolso da Despesa aberto**.
* **Inscrição municipal:** Define a associação da despesa com a Inscrição municipal do imóvel selecionado.
* **Cliente/Fornecedor:** Neste campo é definido o fornecedor para o qual será gerado o movimento da despesa. Caso o Tipo de Despesa informado seja de **IPTU** ou **ITBI** o Cliente/Fornecedor será buscado do cadastro da Subunidade no campo código da prefeitura que é informado em **Controle de IPTU/Registro**.

#### **Campos do Responsável pela Despesa:**

---

* **Responsável pela Despesa:**Define o Responsável como Cliente ou Empresa.
* **Responsável a Partir:**Caso seja definido que o responsável é o cliente o sistema permite a seleção de datas para informar em qual momento a obrigação passou a ser do cliente

#### **Campos de Valor Despesa:**

---

* **Tipo valor despesa:** Este campo possuí duas opções, são elas: **Valor à vista** e **Valor à prazo**. Quando for marcada a opção **Valor à vista** os campos **Nº de parcela(s)** e **Intervalo em dias** ficarão desabilitados impossibilitando a edição dos mesmos. Já marcando a opção **Valor à prazo,** os campos de **Nº de parcela(s)** e **Intervalo em dias** ficarão habilitados, permitindo que as informações seja inseridas.

* + **Valor a vista:** Campo usado para informar o valor a vista para a despesa a ser gerada.
  + **Valor a prazo:** Campo usado para informar o valor a prazo para a despesa a ser gerada.

* **Primeiro vencimento:** Neste campo o usuário deve informar o primeiro vencimento da despesa a ser gerada.
* **N° de parcela(s):** Permite ao usuário informar o número de parcelas que serão geradas para o despesa.
* **Periodicidade**: Define a periodicidade das parcelas a partir da data de **Primeiro vencimento**
  + **Mensal** : As parcelas serão mensais, ou seja, vencerão todas no mesmo dia variando apenas os meses entre elas
  + **Personalizada**: As parcelas terão um intervalo de dias fixo entre elas
* **Intervalo em dias:** Permite ao usuário informar o intervalo em dias de uma parcela de despesa para outra quando a **Periodicidade** é definida como **Personalizada**.

#### **Campos referentes ao Reembolso:**

---

* **Permite reembolso:** Marcando este parâmetro todos os outros campos da tela serão habilitados para preenchimento.
* **Regra de reembolso:** Campo usado para armazenar a regra de reembolso da despesa. Para maiores detalhes sobre Regra de Reembolso [clique aqui](https://tdn.totvs.com/display/LRM/Controle+de+Despesa+-+Regra+de+Reembolso).
* **Tipo valor reembolso:** Assim como o campo **Tipo Valor Despesa**, este campo possuí duas opções, são elas: **Valor à vista** e **Valor à prazo**. Quando for marcada a opção **Valor à vista** os campos **Nº de parcela(s)** e **Intervalo em dias reembolso** ficarão desabilitados impossibilitando a edição dos mesmos. Já a opção **Valor à prazo, quando estiver marcada, os campos de Nº de parcela(s)** e **Intervalo em dias reembolso** ficarão habilitados, permitindo que as informações seja inseridas.
* **Primeiro vencimento reembolso:** Neste campo o usuário deve informar o primeiro vencimento da parcela de reembolso a ser gerada.
* **Nº de parcela(s):** Permite ao usuário informar o número de parcelas que serão geradas para o Reembolso.
* **Periodicidade reembolso**: Define a periodicidade das parcelas de reembolso a partir da data de **Primeiro vencimento reembolso**
  + **Mensal** : As parcelas serão mensais, ou seja, vencerão todas no mesmo dia variando apenas os meses entre elas
  + **Personalizada**: As parcelas terão um intervalo de dias fixo entre elas
* **Intervalo em dias reembolso:** Permite ao usuário informar o intervalo em dias de uma parcela de reembolso para outra. quando a **Periodicidade de reembolso** é definida como **Personalizada**
* **Código parâmetro integração financeiro:** Este campo é usado para armazenar o parâmetro de integração financeira de aluguel que será para a geração dos lançamentos de reembolso. Para saber mais sobre Parâmetros de Integração Financeira [clique aqui](http://wikihelp.totvs.com.xn--brparmetros%20de%20integrao%20financeira%20-%20aluguel-foe1f3l/).

Clicando no botão **Salvar**, o sistema irá gravar as parcelas vinculadas à despesa.

**Importante:**

* Não será possível integrar uma despesa, isto é, gerar movimentos de despesa ou lançamentos de reembolso, caso o seguro associado não esteja com o status de "Efetivado".
* Na geração de lançamentos de reembolso, caso o parâmetro integração financeira não estiver configurado com algum valor para o campo "Centro de Custo" o sistema irá automaticamente buscar o centro de custo cadastrado no imóvel associado a despesa;
* Caso o imóvel possua áreas fracionadas, o sistema irá utilizar os centros de custo cadastrados na área do imóvel para realizar os rateios dos lançamentos de reembolso.
* Caso o imóvel possua áreas fracionadas mas sem a informação de centro de custo, o sistema continuará buscando o centro de custo cadastrado no imóvel ou nos parâmetros de integração financeira da despesa para compor os devidos rateios.

Informações Complementares

---

* [Despesa - Anexo - Parcela de Despesa](https://tdn.totvs.com/display/LRM/Despesa+-+Anexo+-+Parcela+de+Despesa)
* [Despesa - Anexo - Parcela de Reembolso](https://tdn.totvs.com/display/LRM/Despesa+-+Anexo+-+Parcela+de+Reembolso)

Recursos Adicionais

---

* [Definição de Despesas de Vendas](https://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&title=Defini%C3%A7%C3%A3o+de+Despesas+de+Vendas&linkCreation=true&fromPageId=599367719)
* [Parcela de Reembolso - Processo - Gerar Lançamentos de Reembolso](https://tdn.totvs.com/pages/viewpage.action?pageId=435105323)
* [Parcela de Reembolso - Processo - Cancelar Lançamentos Financeiros](https://tdn.totvs.com/pages/viewpage.action?pageId=435105350)
* [Parcela de Despesa - Processo - Gerar Movimento de Despesa](https://tdn.totvs.com/display/LRM/Parcela+de+Despesa+-+Processo+-+Gerar+Movimento+de+Despesa)
* [Parcela de Despesa - Processo - Cancelar Integração de Despesa](https://tdn.totvs.com/pages/viewpage.action?pageId=435105282)
