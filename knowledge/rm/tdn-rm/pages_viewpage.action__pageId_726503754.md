---
content_hash: bd3fd0fef93efed4c480cf8fbfcc757f98fce678b411741aef383c4d0ac7b377
fetched_at: '2026-06-29T00:11:27.533659+00:00'
page_id: '726503754'
product: rm
source: tdn-rm
title: Venda Despesa - Definição de Despesa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=726503754
version: 11
---

**Definição de Despesa**

O Objetivo deste processo: Gerar despesas para todas as subunidades (ou imóveis) associados a uma determinada definição.

O cadastro de definição de despesas é um facilitador que o sistema está disponibilizando para o usuário incluir um volume grande de despesas para vários imóveis de uma só vez.  
Neste cadastro o usuário faz uma pré-definição dos dados que as despesas terão em comum. Depois os dados particulares de cada despesa como por exemplo o valor e o número de documento poderão ser alterados.  
O cadastro consta com os seguintes campos:

* **Origem:** Campo preenchido automaticamente pelo sistema, podendo ser **Aluguel** ou **Venda**.
* **Código:** Campo que armazena o código da definição da despesa, o mesmo é preenchido automaticamente pelo sistema.
* **Descrição:** Descrição da despesa a ser cadastrada.
* **Tipo de despesa:** Campo usado para vincular Tipo de Despesa na Despesa. Para saber mais sobre Tipo de Despesa [clique aqui](https://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&title=Controle+de+Despesa+-+Tipo+de+Despesa&linkCreation=true&fromPageId=435105341).
* **Parâmetro de movimento:** Campo usado para vincular Parâmetro de tipo de movimento na Despesa. Para saber mais sobre Parâmetro de tipo de movimento [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=435105352).

Importante!

Ao selecionar o Tipo de Pagamento para "*Gerar Movimento de Faturamento*" na configuração de uma despesa, o sistema ir exibir o campo de *Data de Entrega*, que será replicado diretamente para o Movimento definido nos Parâmetros de Movimento da Definição da Despesa.

Já ao selecionar o Tipo de Pagamento "*Gerar Lançamento Financeiro*", o campo de data do *Primeiro Vencimento* será apresentada. Isso permite que o lançamento seja gerado com a data de vencimento determinada durante essa parametrização.

* **Fornecedor:** Campo que deve ser informado o fornecedor responsável por gerar a despesa. Por exemplo, o usuário possui como despesa o IPTU. O fornecedor desta despesa é a prefeitura que gerou este tributo.
* **Tipo valor despesa:** Este campo possuí duas opções, são elas: **Valor à vista** e **Valor à prazo**. Caso seja selecionado o valor a prazo, serão habilitados os seguintes campos:
  + **Periodicidade despesa:**Define uma periodicidade para as parcelas da despesa. Ela pode ser mensal ou personalizada. A periodicidade personalizada permite ao usuário definir o intervalo de dias de sua preferência para a geração das parcelas.
  + **N° de parcelas:** Neste campo o usuário poderá informar o número de parcelas.
  + **Intervalo em dias:** Intervalo de dias entre as parcelas da despesa. Este campo será habilitado caso a periodicidade da despesa seja **"Personalizada".**
* **Gerar Despesa por Inscrição Municipal:** Define se será gerada uma despesa para cada inscrição municipal de cada imóvel.
* Caso o campo **Permite reembolso** for marcado, então os campos abaixo serão habilitados:
* **Regra de reembolso:** Campo usado para armazenar a regra de reembolso da despesa. Para maiores detalhes sobre Regra de Reembolso [clique aqui](https://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&title=Controle+de+Despesa+-+Regra+de+Reembolso&linkCreation=true&fromPageId=435105341).
* **Nº de parcelas reembolso:**Quantidade de parcelas que serão geradas para o reembolso da despesa.
* **Tipo valor reembolso:** Assim como o campo **Tipo Valor Despesa**, este campo possuí duas opções, são elas: **Valor à vista** e **Valor à prazo.**Caso o valor seja a prazo, serão habilitados os campos:
  + **Periodicidade reembolso:**Define uma periodicidade para as parcelas da despesa. Ela pode ser mensal ou personalizada. A periodicidade personalizada permite ao usuário definir o intervalo de dias de sua preferência para a geração das parcelas.
  + **N° de parcelas:** Neste campo o usuário poderá informar o número de parcelas de reembolso.
  + **Intervalo em dia reembolso:** Intervalo de dias entre as parcelas do reembolso. Este campo será habilitado caso a periodicidade da despesa seja **"Personalizada".**
* **Parâmetro integração financeiro:** Este campo é usado para armazenar o parâmetro de integração financeira de aluguel que será para a geração dos lançamentos de reembolso. Para saber mais sobre Parâmetros de Integração Financeira [clique aqui](http://wikihelp.totvs.com.xn--brparmetros%20de%20integrao%20financeira%20-%20aluguel-foe1f3l/).
* No quadro de **Associação de Imóveis** é possível associar imóveis cadastrados nas **Definições de Despesa**. Para adicionar novos imóveis, basta clicar no botão Incluir e utilizar os filtros necessários para encontrar os imóveis desejados.

Abaixo temos a tela de Definição de Despesa: 

**Tela de Definição de Despesa** .

**Descrição** : Descrição que usuário irá inserir na nova Definição de Despespesa.

**Periodicidade**:

* Nenhum
* Mensal
* Bimestral
* Trimestral
* Semestral
* Anual
* Outra  ( Esta opção selecionada : cliente pode colodar : quinzenal, ou de 10 em 10 dias, ou 20 em 20 dias por exemplo.

**Tipo de Despesa**:  Cadastro do Tipo de Despesa

**Pode ser despesa de** :

1. IPTU
2. ITBI
3. Outros ( Outro tipo de Despesa conforme cliente desejar cobrar ).

**Tipo de Pagamento** : Pode ser configurado para se gerar um Movimento para o TOTVS Compras Estoque e Faturamento ou gerar Financeiro para o TOTVS Gestão Financeira.

Após selecionar o tipo de pagamento desejado , o cliente informa o Parametro Financeiro ou de Movimento.

## **Processo para Gerar Despesa**

Selecionado os Imóveis e em seguida : Processo |**Gerar Despesa**

Neste caso que foi selecionado o **tipo de Despesa** IPTU - A **Desepesa será gerada para codigo da Prefeitura** nas **SubUnidades selecionadas**.

No caso se fosse **Outro** - O **Código do Fornecedor** ficaria **habilitado** para que pudesse inserir um e assim , gerar a Despesa para um determinado Cli/For.

Na tela de **Definição de Despesa**, foi disponibilizado o processo de **Gerar Despesa**, para gerar despesas destinadas para um ou mais imóveis.  
A tela do processo de Gerar despesa possuí as seguintes características:

* Os campos Ano exercício e Competência são preenchidos automaticamente com o mês e ano corrente, mas é permitida a edição dos mesmos;
* O campo **Primeiro vencimento despesa** é preenchido automaticamente buscando essa informação da **Definição de Despesa** que está sendo usada na geração da Despesa;
* O campo **Primeiro vencimento reembolso** é preenchido automaticamente buscando essa informação da **Definição de Despesa** que está sendo usada na geração da Despesa;
* Os campos Valor à vista e Valor a prazo devem ser preenchidos, pois estes valores serão usados no preenchimento das Despesas a serem criadas;
* Após preencher os campos **Ano exercício**, **Competência**, **Primeiro vencimento despesa**, **Primeiro vencimento reembolso**(se houver reembolso)**,****Valor à vista** e **Valor à prazo**, basta então selecionar as Despesas que deseja criar, e clicar no botão **Aplicar**;
* As informações exibidas nas colunas Código, Endereço e  colunas referentes à Inscrição Municipal não podem ser editadas;
* As colunas referentes à Inscrição Municipal do imóvel são exibidas quanto o campo Gerar Despesa por Inscrição Municipal na Definição de Despesa está marcado;
* As colunas **Nº documento**, **Ano exercício**, **Competência**, **Primeiro vencimento despesa**, **Primeiro vencimento reembolso**(se houver reembolso)**, Valor à vista** e **Valor à prazo** podem ser editadas para a geração da Despesa e seus valores;
* Ao executar o processo, o sistema irá gerar a despesa para todos os imóveis selecionados. Caso nenhum imóvel for selecionado, então por padrão o sistema irá gerar para todos os imóveis listados.
