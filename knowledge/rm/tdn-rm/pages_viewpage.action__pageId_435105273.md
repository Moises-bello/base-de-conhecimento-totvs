---
content_hash: 80563ca162b7c2c8064519bb75d6dd5b99a1ce2ee03fe6008ee48deffba32291
fetched_at: '2026-06-29T00:09:49.275812+00:00'
page_id: '435105273'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Aluguel - Evento Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105273
version: 34
---

---

# Evento Financeiro

O **Evento Financeiro** é uma funcionalidade do módulo de
**Gestão de Aluguel** do sistema **TOTVS Incorporação**,
que possibilita a gestão, parcelamento e distribuição de valores financeiros
cobrados de **locadores**, **locatários** ou de ambos,
na utilização ou administração de um imóvel.

Ele é utilizado, por exemplo, para registrar despesas de manutenção,
despesas geradas por contratos de locação (como *luvas*),
permitindo também a **integração com os lançamentos financeiros**
do módulo de Gestão Financeira da linha **RM** e **Protheus**.

## 📌 Identificação do Evento Financeiro

* **Código do evento:** Código único gerado automaticamente pelo sistema.
* **Data do evento:** Data em que o evento financeiro foi gerado.
* **Situação do evento:**
  + **Não Integrado:** Não possui lançamentos financeiros associados.
  + **Integrado:** Todas as parcelas possuem lançamentos financeiros associados.
  + **Parcialmente Integrado:** Apenas parte das parcelas possui lançamentos associados.

## 💰 Tipo de Cobrança do Evento

Define o comportamento do lançamento financeiro integrado ao evento.

* [**Avulso:**](https://tdn.totvs.com/display/LRM/Cadastrar+Evento+Financeiro+Avulso)
  Gera lançamentos financeiros desvinculados dos lançamentos mensais
  do contrato de locação (aluguel e repasse).
* **Agregado:** Gera lançamentos financeiros junto ao lançamento mensal
  (aluguel, repasse ou ambos).

**⚠️ Observação:**  
Para eventos financeiros do tipo **Pós Rescisão**, o tipo de cobrança
não pode ser definido como **Agregado**, pois os lançamentos ocorrem
somente após a rescisão do contrato.

### Tipo de Agregação

Disponível apenas quando o tipo de cobrança é **Agregado**.
Define a referência de data para agregação das parcelas.

* **Data de Vencimento:** A parcela do evento será agregada à parcela
  do contrato cujo vencimento seja menor ou igual.
* **Período da Parcela:** A agregação considera o período (competência)
  do contrato de locação.

## 🏷️ Tipo de Evento Financeiro

Utilizado para classificar os eventos financeiros do módulo de aluguel.
Cadastro localizado em:
**Aluguel | Cadastros | Tipo de Evento Financeiro**.

* **Diversos:** Eventos cadastrados manualmente.
* **Rescisão:** Gerados pelo processo de rescisão do contrato
  ([saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=435105386)).
* **Locação:** Gerados pela geração de lançamento do contrato
  ([saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=435105008)).
* **Luva:** Eventos cadastrados manualmente.
* **Locação Complementar:** Gerados pelo processo de aluguel complementar
  ([saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=520659271)).
* **Aditivo de Exclusão de Imóvel:** Gerados quando há multa configurada
  ([saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=435104951)).
* **Fundo Promocional:** Utilizado quando o aluguel complementar considera fundo promocional.
* **Pós Rescisão:** Eventos criados para contratos já rescindidos.

**Observação:**  
Eventos com finalidade **Rescisão, Locação, Locação Complementar** e
**Aditivo de Exclusão de Imóvel** só podem ser criados ou alterados
pelos seus respectivos processos.

## 🔗 Parâmetros e Associações

* **Parâmetros de Integração:** Utilizados para gerar informações financeiras
  para Gestão Financeira e Protheus.
* **Imóvel:** Deve estar associado a um contrato de administração ou locação.
* **Contrato de Administração:** Utilizado para gerar parcelas ao locador.
* **Contrato de Locação:** Utilizado para gerar parcelas ao locatário.

## ⚙️ Ações Financeiras

## 👤 Ações para o Locatário

| Ação | Descrição | Exemplo |
| --- | --- | --- |
| **Nenhuma** | Não será gerado nenhum lançamento financeiro. | — |
| **A Receber** | Gera lançamentos financeiros de natureza **a receber** do locatário para a empresa que gerencia os aluguéis. | Parcelas de aluguéis |
| **A Pagar** | Gera lançamentos financeiros de natureza **a pagar** da empresa que gerencia os aluguéis para o locatário. | Algum ressarcimento ou reembolso |

  


## 🏢 Ações para o Locador

| Ação | Descrição | Exemplo |
| --- | --- | --- |
| **Nenhuma** | Não será gerado nenhum lançamento financeiro. | — |
| **A Receber** | Gera lançamentos financeiros de natureza **a receber** do locador para a empresa que gerencia os aluguéis. | Recebimento vindo do locador |
| **A Pagar** | Gera lançamentos financeiros de natureza **a pagar** da empresa que gerencia os aluguéis para o locador. | Repasse de aluguéis recebidos |

## 🧾 Campo Compõe IVA

Indica se os valores do evento financeiro devem compor a base de cálculo
do **Imposto sobre Valor Agregado (IVA)**, considerando
**IBS** e **CBS**.

Quando habilitado, os lançamentos financeiros terão automaticamente
a base de cálculo preenchida, permitindo o cálculo correto dos impostos.

## 📅 Parcelamento

* **Data do 1º vencimento:** Primeiro vencimento das parcelas.
* **Quantidade de parcelas:** Total de parcelas geradas.
* **Periodicidade:** Define o intervalo das parcelas.
* **Mês/Ano:** Define se a geração ocorre mensal ou anual.
* **Valor da parcela:** Valor de cada parcela.
* **Adicionar Parcelas:** Botão utilizado para gerar as parcelas.

]]>

Como Fazer

---
