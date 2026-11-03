---
content_hash: a30e200a958f9ccbd08aca4a5e3e6c493b12b125858a5ceee530127d39ffa2e6
fetched_at: '2026-06-29T00:09:49.659484+00:00'
page_id: '435105341'
product: rm
source: tdn-rm
title: Controle de Despesa - Definição de Despesa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105341
version: 12
---

O cadastro de definição de despesas é um facilitador que o sistema está disponibilizando para o usuário incluir um volume grande de despesas para vários imóveis de uma só vez.  
Neste cadastro o usuário faz uma predefinição dos dados que as despesas terão em comum. Depois os dados particulares de cada despesa como por exemplo o valor e o número de documento poderão ser alterados.  
O cadastro consta com os seguintes campos:

* **Coligada:** Permite a seleção da coligada ao qual a definição de despesa irá gerar as despesas. Ressaltamos que, ao selecionar a coligada, todos os parâmetros abaixo serão da coligada selecionada.
* **Origem:** Campo preenchido automaticamente pelo sistema, podendo ser **Aluguel** ou **Venda**.
* **Código:** Campo que armazena o código da definição da despesa, o mesmo é preenchido automaticamente pelo sistema.
* **Descrição:** Descrição da despesa a ser cadastrada.
* **Tipo de despesa:** Campo usado para vincular Tipo de Despesa na Despesa. Para saber mais sobre Tipo de Despesa clique aqui.
* **Parâmetro de movimento:** Campo usado para vincular Parâmetro de tipo de movimento na Despesa. Para saber mais sobre Parâmetro de tipo de movimento clique aqui.
* **Cliente/Fornecedor:** Campo que deve ser informado o fornecedor responsável por gerar a despesa. Por exemplo, o usuário possui como despesa o IPTU. O fornecedor desta despesa é a prefeitura que gerou este tributo.
* **Tipo valor despesa:** Este campo possuí duas opções, são elas: **Valor à vista** e **Valor à prazo**. Caso seja selecionado o valor a prazo, serão habilitados os seguintes campos:
  + **Periodicidade despesa:** Define uma periodicidade para as parcelas da despesa. Ela pode ser mensal ou personalizada. A periodicidade personalizada permite ao usuário definir o intervalo de dias de sua preferência para a geração das parcelas.
  + **N° de parcelas:** Neste campo o usuário poderá informar o número de parcelas.
  + **Intervalo em dias:** Intervalo de dias entre as parcelas da despesa. Este campo será habilitado caso a periodicidade da despesa seja **"Personalizada".**
* **Gerar Despesa por Inscrição Municipal:** Define se será gerada uma despesa para cada inscrição municipal de cada imóvel.
* Caso o campo **Permite reembolso** for marcado, então os campos abaixo serão habilitados:
* **Regra de reembolso:** Campo usado para armazenar a regra de reembolso da despesa. Para maiores detalhes sobre Regra de Reembolso clique aqui.
* **Nº de parcelas reembolso:**Quantidade de parcelas que serão geradas para o reembolso da despesa.
* **Tipo valor reembolso:** Assim como o campo **Tipo Valor Despesa**, este campo possuí duas opções, são elas: **Valor à vista** e **Valor à prazo.** Caso o valor seja a prazo, serão habilitados os campos:
  + **Periodicidade reembolso:** Define uma periodicidade para as parcelas da despesa. Ela pode ser mensal ou personalizada. A periodicidade personalizada permite ao usuário definir o intervalo de dias de sua preferência para a geração das parcelas.
  + **N° de parcelas:** Neste campo o usuário poderá informar o número de parcelas de reembolso.
  + **Intervalo em dia reembolso:** Intervalo de dias entre as parcelas do reembolso. Este campo será habilitado caso a periodicidade da despesa seja **"Personalizada".**
* **Parâmetro integração financeiro:** Este campo é usado para armazenar o parâmetro de integração financeira de aluguel que será para a geração dos lançamentos de reembolso. Para saber mais sobre Parâmetros de Integração Financeira [clique aqui](http://wikihelp.totvs.com.brParâmetros de Integração Financeira - Aluguel).
* No quadro de **Associação de Imóveis** é possível associar imóveis cadastrados nas **Definições de Despesa**. Para adicionar novos imóveis, basta clicar no botão Incluir e utilizar os filtros necessários para encontrar os imóveis desejados.

Abaixo temos a tela de Definição de Despesa: 

Responsável pela Despesa.

As opções pelo pagamento de Despesas são:

* Cliente.
* Empresa.

Quando o responsável for o cliente, fica habilitado as seguintes opções abaixo:

* Data do contrato;
* Data de início da locação;
* Data a definir.

Caso a opção escolhida for:  "Data a definir", será habilitado um campo Data para que possa informar a data na qual será cobrada do cliente.

## **PARA MAIS INFORMAÇÃO SOBRE DESPESA : [CLIQUE AQUI !](https://tdn.totvs.com/pages/viewpage.action?pageId=725741976#Despesas-1590657733)**

**Figura 1 - Tela de definição de despesa com os campos preenchidos**

Recursos Adicionais

---
