---
content_hash: c34e3888d0cb6ea21256fe29f41e004c5fc0aed81c8ab27403d67ea26023bd76
fetched_at: '2026-06-29T00:11:25.705199+00:00'
page_id: '715139289'
product: rm
source: tdn-rm
title: Controle de Despesa Venda
type: documentation
url: https://tdn.totvs.com/display/LRM/Controle+de+Despesa+Venda
version: 3
---

***Despesas de Venda***

Controle de Despesa ( Venda )Cokpit - Cliente ,360 ( Despesa )Funcionalidade disponível na versão 12.1.2302 em diante !!!!

## **Funcionalidade disponível na versão 12.1.2302 em diante !!!!**

Para saber mais sobre esta fucnionalidade, [CLIQUE AQUI !](https://tdn.totvs.com/pages/viewpage.action?pageId=709413990)

Tipo de Despesa |

Este cadastro permite cadastrar os tipos de despesas necessárias, podendo assim agrupar despesas que possuam um mesmo objetivo e características. Para acessar este cadastro basta acessar Outros/ Tipo de Despesa.

**Figura 1 - Cadastro de tipo de despesa aluguel**

**Figura 2 - Cadastro de tipo de despesa venda**

Os campos presentes nestes cadastros são:

* **Código do Tipo Despesa:** Código que identifica o Tipo de Despesa cadastrado. Campo preenchido automaticamente pelo sistema;
* **Tipo Rateio:** Define se o rateio da despesa será realizado por M² ou CRD.
  + Importante: Quando o tipo de rateio é definido por CRD, não será possível gerar despesas para os imóveis que possuem áreas fracionadas.
* **Descrição:** Descrição do Tipo de Despesa cadastrado.
* **Tipo despesa:** Informa se a despesa é de IPTU, ITBI ou outros. Esse campo será utilizado na geração de despesa para especializar parte do processo, quando as despesas foram de IPTU e ITBI. Eles só devem ser informados durante a inclusão, após isso o campo será bloqueado.
* **Natureza Financeira a pagar:** Neste campo é possível determinar a Natureza Financeira dos lançamentos a pagar da Despesa que estiver associada ao Tipo de despesa cadastrada;
* **Natureza Financeira a receber:** Neste campo é possível determinar a Natureza Financeira dos lançamentos a receber da Despesa que estiver associada ao Tipo de despesa cadastrada.
Definição de Despesas de Venda |

**Definição de Despesas**

---

Foi  criado associar subunidades à definição das despesas, para que o processo de geração de despesas possa ser realizado automaticamente.   
Essa associação deve ser possível através da própria subunidade, ou através da unidade para todas as subunidades daquela unidade, ou através do empreendimento para todas as subunidades daquele empreendimento.  
   
    
   
Dar permissão ao usuário no Processo ( Definição de Despesas )  
Serviços Globais | Segurança | Perfis : Sistema = Incorporação  
01.02.08.08 – Permitir acesso ao usuário.  
   
   
   
   
   
Despesas | Definição de Despesas  
   
    
   
 

Responsável pelas Despesas.

As opções de Responsáveis pelas Despesas:

* Cliente.
* Empresa.

Quando o responsável for o cliente.

As opções são as seguintes:

Despesa de venda:

* Data da venda;
* Data do habite-se;
* Data da entrega de chaves;
* Data da assinatura;
* Data informada na subunidade para despesa de IPTU;
* Data a definir.

Caso a opção escolhida seja "Data a definir", deverá ser informada uma data a partir da qual a despesa será cobrada do cliente e o sistema irá abrir campo de data.

   
**Origem:** Campo preenchido automaticamente pelo sistema, podendo ser Aluguel ou Venda.  
   
**Código :** Campo que armazena o código da despesa, o mesmo é preenchido automaticamente pelo sistema.  
   
Descrição : Descrição da definição de despesa a ser cadastrada.  
   
**Periodicidade:**  
·          **Nenhuma**  
·          **Mensal**  
·          **Bimestral**  
·          **Trimestral**  
·          **Semestral**  
·          **Anual**  
·          **Outra**  
   
**Tipo de Despesa:** Campo usado para vincular Tipo de Despesa na Despesa. Para saber mais sobre Tipo de Despesa [clique](https://tdn.totvs.com/display/LRM/Controle+de+Despesa+-+Tipo+de+Despesa)

**Tipo de Pagamento**: Campo utilizado para informar se será gerado um movimento de Faturamento ou um Lançamento financeiro.  
   
**Parâmetro de Movimento/Parâmetros Financeiros:** Campo usado para vincular Parâmetro de tipo de movimento na Despesa. Para saber mais sobre Parâmetro de tipo de movimento [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=435105038). Caso não seja utilizado Movimento deve ser informado o parâmetro financeiro.  
   
**Código Fornecedor** : Campo que deve ser informado o fornecedor, sendo que a despesa será gerada para o mesmo.  
   
**Tipo valor despesa** : Este campo possuí duas opções, são elas: **Valor à vista** e **Valor à prazo**.  
   
   
  
**Associação de:**  ( Nome é informado no Parametrizador do TIN )  
   
    
   
   
Ambiente | Parâmetros | TOTVS Incorporação | 22.01.02  - Empreendimento  
   
    
   
   
Nome é informado pelo Parâmetro : Nome da Sub-Unidade.  
 

* Processo de : Gerar Despesas  
     
     
    
     
     
  Detalhes sobre o Processo de Gerar Despesas, [Clique Aqui.](https://tdn.totvs.com/display/LRM/Gerar+Despesa+Venda)
Cadastro Individual de Despesas |

A criação das despesas é feita através de um cadastro simples, que possui particularidades conforme o tipo de despesa.

**Campos referentes à Despesa:**

* **Origem:** Este campo é definido internamente pelo sistema, de acordo com o local que é feita sua chamada, podendo ser **Aluguel**, **Venda** ou **Seguro**.
* **Status:** Este campo é preenchido automaticamente pelo sistema. Os status utilizados são:

* + **Não Integrado:** É o status inicial, que é definido por default quando a despesa é criada.
  + **Integrado**: Ao gerar os movimentos e os lançamentos financeiros da despesa, esta tem seu status alterado para "Integrado".
  + **Parcialmente Integrado:**Ao gerar **apenas** os movimentos **ou** os lançamentos financeiros da despesa, esta tem seu status alterado para "Parcialmente Integrado".

* **Ano base:** Ano de referência da cobrança da despesa. Utilizado para ajudar nos filtros do usuário.
* **Competência:** Define a competência da despesa. Por exemplo, uma despesa pode ter vencimento em julho, mas ser referente à competência de junho.
* **Código:** Campo chave do cadastro, que não pode ser repetido. É definido automaticamente pelo sistema de forma incremental.
* **Descrição:** Campo de texto livre, com tamanho máximo de 50 caracteres, para que o usuário defina a descrição da forma que lhe facilite as consultas e busca de despesas. Exemplo: Despesa de IPTU.
* **Número documento:** Número da guia a ser paga como despesa, a mesma deve ser informada nesse campo. Geralmente é informada o mesmo número da guia que consta no documento de cobrança.
* **Tipo de despesa:** Define o Tipo de Despesa da Despesa cadastrada. O tipo de despesa é utilizado para agrupar e para definir a natureza financeira a pagar e receber. Para saber mais sobre Tipo de Despesa [clique aqui](https://tdn.totvs.com/display/LRM/Controle+de+Despesa+-+Tipo+de+Despesa).
  + **Importante**: quando o tipo de despesa tem um tipo de rateio por CRD a despesa será gerada por empreendimento e não por imóvel. Desta forma, o campo imóvel passa a se chamar **"Empreendimento".**
* **Parâmetro de movimento:** Define o Tipo de movimento da Despesa. Ele é quem definirá as configurações a serem consideradas no movimento que será gerado pela despesa. Para saber mais sobre Parâmetro de tipo de movimento [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=435105352).
* **Imóvel / Empreendimento :** Imóvel ou Empreendimento (quando o tipo de rateio é por CRD) para o qual a despesa será gerada. Uma despesa pode ter apenas um imóvel ou empreendimento associado. Este campo apenas é utilizado quando a Origem da despesa está definida como "Aluguel".
  + **Observação:** Caso seja feito o encerramento ou rescisão no **contrato de locação** vinculado ao imóvel da despesa, os lançamentos financeiros de reembolso com data de vencimento posterior ao encerramento ou rescisão serão cancelados.
* **Empreendimento/Unidade/Subunidade:** Define a associação da Subunidade para a qual a despesa será gerada. Uma despesa pode ter apenas uma Subunidade associada. Este campo apenas é utilizado quando a Origem da despesa está definida como "Venda".
  + **Observação:** Caso a Subunidade esteja **vendida** e exista a necessidade de realizar **Distrato, ou Aditivos de Troca de Subunidade ou Troca de Comprador** no contrato, estes só poderão ser efetivados se não existir nenhum lançamento de **Reembolso da Despesa aberto**.
* **Inscrição municipal:** Define a associação da despesa com a Inscrição municipal do imóvel selecionado.
* **Cliente/Fornecedor:** Neste campo é definido o fornecedor para o qual será gerado o movimento da despesa.

**Campos de Valor Despesa:**

* **Tipo valor despesa:** Este campo possuí duas opções, são elas: **Valor à vista** e **Valor à prazo**. Quando for marcada a opção **Valor à vista** os campos **Nº de parcela(s)** e **Intervalo em dias** ficarão desabilitados impossibilitando a edição dos mesmos. Já marcando a opção **Valor à prazo,** os campos de **Nº de parcela(s)** e **Intervalo em dias** ficarão habilitados, permitindo que as informações seja inseridas.

* + **Valor a vista:** Campo usado para informar o valor a vista para a despesa a ser gerada.
  + **Valor a prazo:** Campo usado para informar o valor a prazo para a despesa a ser gerada.

* **Primeiro vencimento:** Neste campo o usuário deve informar o primeiro vencimento da despesa a ser gerada.
* **N° de parcela(s):** Permite ao usuário informar o número de parcelas que serão geradas para o despesa.
* **Periodicidade**: Define a periodicidade das parcelas a partir da data de **Primeiro vencimento**
  + **Mensal** : As parcelas serão mensais, ou seja, vencerão todas no mesmo dia variando apenas os meses entre elas
  + **Personalizada**: As parcelas terão um intervalo de dias fixo entre elas
* **Intervalo em dias:** Permite ao usuário informar o intervalo em dias de uma parcela de despesa para outra quando a **Periodicidade** é definida como **Personalizada**.

**Campos referentes ao Reembolso:**

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

Importante!

* Na geração de lançamentos de reembolso, caso o parâmetro integração financeira não estiver configurado com algum valor para o campo "Centro de Custo" o sistema irá automaticamente buscar o centro de custo cadastrado no imóvel associado a despesa;
* Caso o imóvel possua áreas fracionadas, o sistema irá utilizar os centros de custo cadastrados na área do imóvel para realizar os rateios dos lançamentos de reembolso.
* Caso o imóvel possua áreas fracionadas mas sem a informação de centro de custo, o sistema continuará buscando o centro de custo cadastrado no imóvel ou nos parâmetros de integração financeira da despesa para compor os devidos rateios.

Abaixo temos a tela de despesas aba Identificação:

**Figura 1 - Tela do Cadastro de Despesas de Aluguel**

**Figura 2 - Tela do Cadastro de Despesas de Venda**

Clicando no botão **Salvar**, o sistema irá gravar as parcelas vinculadas à despesa.

Importante: Não será possível integrar uma despesa, isto é, gerar movimentos de despesa ou lançamentos de reembolso, caso o seguro associado não esteja com o status de "Efetivado".

Informações Complementares

---

* [TOTVS Construção Gestão de Imóveis - Controle de Despesas](https://tdn.totvs.com/pages/viewpage.action?pageId=435105347)
* [Despesa - Visão|Anexo - Parcela de Reembolso](https://tdn.totvs.com/pages/viewpage.action?pageId=435105348)

Recursos Adicionais

---

* [Parcela de Reembolso - Processo - Gerar Lançamentos de Reembolso](https://tdn.totvs.com/pages/viewpage.action?pageId=435105323)
* [Parcela de Reembolso - Processo - Cancelar Lançamentos Financeiros](https://tdn.totvs.com/pages/viewpage.action?pageId=435105350)
* [Parcela de Despesa - Processo - Gerar Movimento de Despesa](https://tdn.totvs.com/display/LRM/Parcela+de+Despesa+-+Processo+-+Gerar+Movimento+de+Despesa)
* [Parcela de Despesa - Processo - Cancelar Integração de Despesa](https://tdn.totvs.com/pages/viewpage.action?pageId=435105282)
Regra de Reembolso 

O cadastro de Regras de Reembolso permite criar definições de como serão gerados os lançamentos financeiros de reembolso.  
Este cadastro é composto pelas campos abaixo:

* **Código:** Campo que guarda o código da regra de reembolso.
* **Descrição:** Campo usado para guardar a descrição da regra de reembolso cadastrada.
* **Utiliza cálculo pro-rata dia:** Quando este parâmetro está marcado indica que a despesa será calculada de forma pro-rata dia. Para o cálculo das parcelas Inicial e Final será utilizado o **Mês Civil.**
* **O que é Mês Civil?**
  + **Mês Civil:** Expressão existente no mercado financeiro e administrativo que considera todos os dias do mês, da forma real mesmo. Por exemplo, em fevereiro teremos 28 ou 29 dias. Sendo assim, o Ano Civil é considerado com 365 dias.
  + Segue um exemplo de um cálculo pró-rata:
    - **Despesa:**
      * **Primeiro Vencimento:**01/01/2018
      * **Nº de parcelas de reembolso:** 10
      * **Valores das parcelas de reembolso:** R$ 310,00
    - **Contrato de locação:**
      * **Data inicio de Locação:** 15/01/2018
      * **Data final de Locação:** 31/12/2018
    - **Cálculo Pro-rata:**
      * Na primeira parcela de Reembolso da despesa o valor a ser calculado para o locatário será:
      * **Dias civil do mês de janeiro:** 31
      * **Parcela / dias civil :** 310/31 = R$ 10,00
      * **Dias em que o locatário é responsável pelo pagamento da despesa:** 17
      * **(Parcela / dias civil) \* Dias em que o locatário é responsável pelo pagamento da despesa** = (310/31) \* 17 = R$ 170,00
    - Nesse caso o Locatário irá pagar o valor de R$ 170,00 na primeira parcela, e o valor integral de R$ 310,00 nas demais parcelas

**Informações específicas para quando a Origem for Aluguel**

---

* **Prioridade de Cobrança:** Neste o usuário define, qual será a prioridade de cobrança das despesas, podendo escolher entre Locatário e/ou Locador, para isso basta marcar o item desejado e definir a prioridade usando as setas para cima ou para baixo:
  + Se locatário e locador estiverem desmarcados, as despesas não serão cobradas;
  + Se locatário e locador estiverem marcados, o sistema irá buscar o que se encontra com a primeira prioridade, caso não exista, irá buscar o de segunda prioridade;
* **Cancelar Lançamento no encerramento/rescisão do contrato:** Quando esse parâmetro está marcado, ele indica que os Lançamentos Financeiros de Reembolso da Despesa serão cancelados, quando o Contrato de Locação associado ao Imóvel da Despesa for rescindido ou encerrado. Os lançamentos que serão cancelados, são os que possuem data de vencimento posterior a data de Encerramento/Rescisão. Os lançamentos só serão cancelados caso seu status no financeiro seja "Em Aberto".
  + **Observações:**
    - Caso possua algum lançamento de reembolso baixado com vencimento posterior a data de Encerramento/Rescisão do Contrato de Locação, o sistema irá criar um lançamento financeiro a pagar com o valor baixado dos lançamentos que se encontram nessa situação;
    - O sistema não permite marcar esse parâmetro juntamente com o parâmetro "Cobrar o reembolso agregado ao aluguel", pois dessa forma para excluir os lançamentos de despesas deverá ser excluídos os lançamentos do Contrato de Locação.
* **Cobrar o reembolso agregado ao aluguel:** Quando esse parâmetro está marcado, indica que os valores financeiros de reembolso, serão gerados na forma de valores de integração dos Lançamentos do Contrato de Locação associado ao Imóvel da Despesa. Dessa forma, eles serão gerados juntamente com a geração dos Lançamentos do Contrato de Locação.
  + **Observações:**
    - O sistema não permite marcar esse parâmetro juntamente com o parâmetro "Cancelar Lançamento no encerramento/rescisão do contrato", pois dessa forma para excluir os lançamentos de despesas deverá ser excluídos os lançamentos do Contrato de Locação;
    - Ao marcar esse parâmetro é obrigatório que seja informado qual o **valor de integração a somar** será utilizado.
* **Valor de Integração:** Neste campo o usuário informa o valor de integração que será utilizado na geração dos valores de reembolso da despesa junto as parcelas do contrato de locação;
  + **Observações:**
    - Este campo só é habilitado quando a opção **Cobrar o reembolso agregado ao aluguel está marcada.**

**Figura 1 - Tela de Regra de Reembolso Origem Aluguel**

**Informações específicas para quando a Origem for Venda**

---

* Somente podem ser gerados reembolsos para Despesas que estejam vinculadas a Subunidades vendidas, ou seja, devem estar em um contrato de venda com a situação **Efetivado**.
* Os lançamentos de reembolso serão gerados para o **Comprador Principal do Contrato de Venda**.
* Caso seja necessário **Distratar ou realizar Aditivo de Troca de Subunidade ou Troca de Comprador**, estes só poderão ser efetivados se não existir nenhum lançamento de Reembolso em aberto.

**Figura 2 - Tela de Regra de Reembolso Origem Venda**
