---
content_hash: 6229783149f255c354b81ea6deca118146dedefebdca2fd4e19063d7c00615da
fetched_at: '2026-06-29T00:10:30.981055+00:00'
page_id: '520659198'
product: rm
source: tdn-rm
title: Contrato de Locação - Dados Gerais - Garantias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520659198
version: 12
---

# 🔐 Garantias do Contrato de Locação

Anexo do Contrato de Locação responsável por vincular Garantias Contrato.

---

# 📋 Pré-Condições

* Ter incluído uma Instituição (Cliente/Fornecedor/ambos);
* Ter incluído um Contrato de Locação com a situação **Em Preparação**.

---

# 🧾 Vincular uma Garantia a um Contrato de Locação

1. Selecione o Contrato de Locação e acesse: **Anexos / Garantia**.
2. Clique em **Incluir Garantia**.
3. O formulário responsável por vincular a Garantia ao Contrato de Locação será exibido.

## 📝 Campos do formulário

* Garantia
* Situação da Garantia
* Código da Instituição
* Número Garantia
* Tipo de Garantia *(ver informação complementar abaixo)*
* Valor Total
* Data Pagamento
* Validade Inicial
* Validade Final
* Observações

Após informar os campos, clique em **Salvar**.

---

# 🔄 Vínculo com o valor do contrato

Quando este parâmetro estiver habilitado, o sistema passará a controlar automaticamente a necessidade de atualização da garantia sempre que houver alterações nos imóveis do contrato de locação.

Assim, ao efetivar um aditivo de alteração de imóvel — seja para alteração de valores, inclusão de um novo imóvel ou exclusão de um imóvel — o sistema exigirá a existência de um aditivo de garantia em preparação para aplicação.

Esse aditivo de garantia será efetivado automaticamente junto com o aditivo de alteração de imóvel.

## 🎯 Objetivo do controle

Garantir que a garantia do contrato seja revisada e ajustada sempre que houver alterações que impactem o valor ou as condições vinculadas ao contrato.

---

# ⚠️ Regras Importantes

## Garantias da mesma modalidade

Não é possível cadastrar garantias de modalidades diferentes. Após cadastrar a primeira garantia, caso deseje cadastrar outras antes de efetivar o contrato de locação, elas deverão ser da mesma modalidade da primeira garantia cadastrada.

## Garantias e fiadores

Não é possível efetivar um contrato de locação com garantias e fiadores informados.

Uma vez que uma garantia seja informada, caso também seja informado um fiador, o processo de efetivação não será realizado.

---

# ℹ️ Informação Complementar

A partir da versão **12.1.2306**, ao acessar o campo **Tipo de Garantia** e selecionar a opção **Seguro Fiança**, será apresentado logo abaixo o campo **Seguro**, para que ele possa ser preenchido com a informação respectiva ao tipo de seguro que será utilizado para esta garantia selecionada.

> Este campo é apresentado apenas na seleção de **Seguro Fiança**.
