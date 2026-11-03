---
content_hash: 7d6ab592290bdb2cc5e5e5c368acc1c1c3f5fe079b2a9163f29ec4ba376a6715
fetched_at: '2026-06-29T00:09:47.791185+00:00'
page_id: '435105071'
product: rm
source: tdn-rm
title: Cadastrar Evento Financeiro Avulso
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastrar+Evento+Financeiro+Avulso
version: 81
---

**Cadastrar Evento Financeiro Avulso**

---

**Imóvel** |Cadastro de Imóvel]{\*}.\* \*2-\* Ter Cadastrado o [**Tipo de Evento Financeiro**|Tipo Evento Financeiro] que tenha a finalidade "Diversos". \*3-\* Ter incluído o [**Parâmetro de Integração Financeira**|Parâmetros de Integração Financeira - Aluguel] \*4-\* Ter incluído um Contrato de Locação com a situação [**"Efetivado"**|Processo - Efetivar Contrato de Locação]
\*Incluindo um Evento Financeiro Avulso\*
\*Passo  1-\* Acesse: TOTVS Incorporação/ Aluguel/ Evento Financeiro \*Passo  2-\* Clique em \[Incluir novo Evento Financeiro\]. \*Passo  3-\* Informe os campos  e clique no botão  \[Salvar\]:]]>

* **Data  do Evento:** Data qual o Evento corresponderá.
* **Valor do Evento:** Valor total do  Evento Financeiro.
* **Tipo de Evento Financeiro:** Informar  evento que atenda a pré-Condição 2.
* **Parâmetro de Integração:** Parâmetro responsável por gerenciar a criação dos tipos de documento a pagar e receber, além de centros de custos e naturezas financeiras.
* **Imóvel:** Imóvel qual o evento referenciará. Se for informado o código do Imóvel, o sistema permitirá selecionar apenas Contratos de Locação ou Administração vinculados a ele
* **Contrato de Locação:** Se for informado o Contrato de Locação, o sistema permitirá selecionar apenas imóveis  vinculados a ele.
  + ***Observação: Quando o Contrato de Locação é informado, o sistema habilita para seleção a ação para o locatário.***
    - **Nenhuma-**  O sistema não executa nenhuma ação financeira no contrato.
    - **A Pagar-**  O sistema  gera as parcelas e lançamentos para o Locatário do tipo Fornecedor. ***Obs: O locatário deve ser obrigatoriamente Fornecedor ou Ambos***
    - **A Receber**- O sistema  gera as parcelas e lançamentos para o Locatário do tipo Cliente. ***Obs: O locatário deve ser obrigatoriamente Cliente ou Ambos***

* **Data Primeiro Vencimento:** Ao gerar os lançamentos financeiros, o sistema gerará a primeira parcela  de acordo com a data informada.

**Passo 6-** O sistema Gera as parcelas, de acordo com as configurações estabelecidas no formulário e com a situação "Não integrada". **Passo 7-** Acesse: Processos Incluir Lançamento Financeiro para alterar a situação da parcela para "Integrada"  
   
   
Voltar
