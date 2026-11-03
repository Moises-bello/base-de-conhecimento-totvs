---
content_hash: 197eee85aed654af77d0d366fe216cafd17d9e0153644953efc08be4230dab75
fetched_at: '2026-06-29T00:09:49.721497+00:00'
page_id: '435105352'
product: rm
source: tdn-rm
title: Cadastros - Parâmetro de Movimento Aluguel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105352
version: 38
---

---

![Reforma Tributária](https://tdn.totvs.com/download/attachments/1025239488/1025239500/ReformaTributaria.png)


# Parâmetro de Movimento Aluguel

Reforma tributária
Gestão de Imóveis

Este cadastro permite gerar e integrar movimentos com o
**TOTVS Gestão de Estoque, Compras ou Faturamento**.

Está localizado em: **TOTVS Incorporação > Aluguéis > Cadastros > Cadastros Alugueis >
Parâmetro de Movimento Aluguel**

## 🧾 Aba Identificação

**Código**  
Código identificador do parâmetro que está sendo criado ou editado.

**Tipo de Geração**  
Define a finalidade de utilização do parâmetro. Os tipos disponíveis são:

* Administração de Aluguel
* Despesa de Aluguel
* **Locação de imóvel** *(implementado)*

O tipo **Locação de imóvel** será utilizado para
**gerar o movimento destinado à emissão de nota fiscal**,
em atendimento à **reforma tributária**.

**Coligada Origem do Cadastro**  
Coligada à qual pertence o cadastro destes parâmetros.

**Descrição**  
Campo destinado à descrição dos parâmetros que estão sendo gerados ou editados.

**Coligada do Movimento**  
Coligada à qual pertence o movimento definido no parâmetro.

### 📄 Tipo de Movimento

* Quando o **Tipo de Geração** for
  **Administração de Aluguel**, o sistema permite apenas
  **Pedidos de Venda**.
* Quando o **Tipo de Geração** for
  **Locação de imóvel**, o tipo de movimento deve pertencer
  obrigatoriamente ao **grupo 2.1**.

**Produto**  
Define qual produto será associado ao movimento no momento da geração.

### 🏢 Filial

**Buscar Filial**  
Campo desabilitado para o usuário.

* Para **Locação de imóvel**, a filial é definida exclusivamente
  via **Parâmetro**.

**Filial**  
Filial que será utilizada no movimento no momento da geração.

### 💰 Natureza Financeira

**Buscar Natureza**  
Define como a Natureza Financeira será informada no movimento gerado.

* **Despesa de Aluguel**:
  + Parâmetro
  + Não se aplica
  + Tipo de despesa
* **Locação de imóvel**:
  + Parâmetro
  + Não se aplica

**Natureza Financeira**  
Habilitado quando selecionada a opção **Parâmetro**
no campo Buscar Natureza.

### 🏷️ Centro de Custo

**Buscar Centro de Custo**  
Define como o Centro de Custo será informado no movimento gerado.

* **Não se aplica**
* **Parâmetro**
* **Imóvel**

**Centro de Custo**  
Habilitado quando selecionada a opção **Parâmetro**.

### 📊 Rateio de Centro de Custo

**Busca Rateio Centro de Custo**

* **Despesa de Aluguel**:
  + Parâmetro
  + Imóvel
* **Administração de Aluguel**:
  + Não se aplica
  + Imóvel
* **Locação de imóvel**:
  + Imóvel
  + Parâmetro
  + Não se aplica

**Informe o rateio de centro de custo**  
Disponível quando o Tipo de Geração for
**Despesa de Aluguel** ou **Locação de Imóvel**
e a Busca Rateio Centro de Custos estiver como **Parâmetro**.

![Rateio de Centro de Custo](https://tdn.totvs.com.br/download/attachments/435105352/image-2025-12-19_17-33-8.png)

**Não permitir alterações dos parâmetros default no processo**  
Define se os dados poderão ser alterados durante a execução do processo.

## 🕒 Histórico

O campo Histórico permite a utilização de **mnemônicos**
para complementar as informações do movimento gerado.

Mnemônicos disponíveis para **Locação de imóvel**:

* [CLI] – Cliente/Fornecedor
* [TEL] – Telefone
* [IM] – Inscrição Municipal
* [IMOV] – Código do imóvel
* [DIMO] – Descrição do imóvel
* [TLG] – Tipo de logradouro
* [LGR] – Logradouro
* [NRO] – Número
* [CPL] – Complemento
* [BRR] – Bairro
* [MUN] – Município
* [CEP] – CEP
* [UF] – UF
* [CADM] – Código do contrato de administração
* [NUMADM] – Número do contrato de administração
* [CALG] – Código do contrato de locação
* [NUMLOC] – Número do contrato de locação

Para visualizar os mnemônicos, selecione o **Tipo de Geração**
e clique com o botão direito no campo **Histórico**.

![Histórico - Mnemônicos disponíveis](https://tdn.totvs.com.br/download/attachments/435105352/image-2025-12-19_17-38-6.png)

]]>
