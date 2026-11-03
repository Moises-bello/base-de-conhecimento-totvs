---
article_id: 360016553112
category: RH - Folha de Pagamento
content_hash: a5f7d801783cb8b0d228a2c746dc77a1515138d00d492eabb29f2626bab93b57
fetched_at: '2026-06-28T22:44:13.277116+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir os valores das bases de IR para regime
  caixa nos cálculo de adiantamento, folha, férias, 13º salário e Rescisão
type: support-article
updated_at: '2025-08-12T12:59:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016553112-RH-Linha-Protheus-GPE-Como-conferir-os-valores-das-bases-de-IR-para-regime-caixa-nos-c%C3%A1lculo-de-adiantamento-folha-f%C3%A9rias-13%C2%BA-sal%C3%A1rio-e-Rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26346284868759) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Como conferir os valores das bases de IR para regime caixa nos cálculo de adiantamento, folha, férias, 13º salário e Rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

**Conferência IR - Regime Competência**

**Folha de Pagamento:**

Base IR Folha = (Verbas com **S** para **IR Proventos** – Verbas com **S** para **IR desconto**) – Dedução Inss Base IR .  
IR Folha = Base IR Folha - Dedução de Dependentes – Pensão Alimentícia da Folha (se houver) \* Parcela % da Tabela de IR – Parcela a deduzir.

**Conferência IR - Regime Caixa**

**Adiantamento:**

Base IR Adiantamento = Verbas com **S** para **IR + Base IR Mês Anterior**  
**IR Adiantamento = Base IR Adiantamento - Dedução De dependentes – Pensão Alimentícia do Adiantamento (se houver) \* Faixa da Tabela de IR – Parcela a deduzir – IR. Mês Anterior.**

**Folha de Pagamento**Base IR Folha = Verbas com **S** para **IR – Adiantamento – Dedução De Inss Base IR**  
**IR Folha = Base IR – Ded. De Dependentes – Pensão alimentícia da Folha (se houver) \* Faixa IR – Parcela a Deduzir**

**Férias**Base de IR Férias = Verbas com **S** para férias e **S** para **IR – Ded. INSS da Base Férias**  
**IR Férias = Base IR Férias – Dedução Dependentes Férias – Pensão Alimentícia Férias (se houver) \*** **Alíquota****de IR – Parcela a deduzir.**

**13º Salário**Base IR 13º Salário = Verbas com “S” para 13º Salário e “S” para IR  
IR 13º Salário = Base IR 13º Salário – Ded. De Dependentes – Pensão Alimentícia do 13º Salário (se houver) \* Alíquota do IR – Parcela a Deduzir.

**Rescisão**Para conferir estes valores em rescisão contratual devem ser utilizadas as mesmas fórmulas acima.

Os IR's de cada fato gerador (Salário, Férias e 13º Salário) devem ser **conferidos individualmente**.

Para compor a **base de IR da Folha**, numa rescisão, são levadas em consideração as **verbas com S para IR** nas incidências das verbas e **NÃO** no campo **Ref. a Férias** e **Ref. a 13º**.

Para conferir as férias, as verbas com **S** para **IR** e **SIM** para **Ref. a Férias**, da mesma forma o 13º.

**Observações:**

Para conferência de **qualquer um dos valores**, indicamos o relatório de DARF/MENSAL.  
Nele constam os valores que irão para a DARF de acordo com a data do pagamento, já com a separação entre folha, adiantamento, férias, 13º salário e Rescisão Contratual.

Os valores que constarão na DARF, são os valores com**DATA DE PAGAMENTO**dentro do período de pagamento informado nos parâmetros de geração da DARF.

**Para Saber Mais:**

**Conceito de Regime Caixa e Competência**

**Regime Competência**O funcionário trabalha e recebe dentro do mesmo mês, ou seja, até o último dia do mês. Neste caso o calculo do IRRF será sempre na folha de pagamento.

**Regime Caixa**O funcionário trabalha em um mês e recebe até o 5º dia útil do mês subsequente, e provavelmente auferiu um adiantamento no dia 20. Neste caso teremos o cálculo do IRRF no Adiantamento de Salário e na Folha de Pagamento.  
  
**Configurações importantes para que o cálculo acima seja feito corretamente:**[RH - Linha Protheus - GPE - Como efetuar a configuração de Verbas IRRF no adiantamento (regime caixa)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006990952-RH-Linha-Protheus-GPE-Como-efetuar-a-configura%C3%A7%C3%A3o-de-Verbas-IRRF-no-adiantamento-regime-caixa-)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
