---
article_id: 360011618932
category: RH - Folha de Pagamento
content_hash: 2f3972840b6acc6839c7be95d554bd9f1aa7d8a2778a4de88511a5614eea48e2
fetched_at: '2026-06-28T22:44:13.270532+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir os valores das bases de IR de adiantamento,
  folha, férias, 13º salário e rescisão?
type: support-article
updated_at: '2025-08-22T18:29:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011618932-RH-Linha-Protheus-GPE-Como-conferir-os-valores-das-bases-de-IR-de-adiantamento-folha-f%C3%A9rias-13%C2%BA-sal%C3%A1rio-e-rescis%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19426657257751)*** Tempo aproximado para leitura**:** **00:02:00 min****Dúvida**Como conferir os valores das bases de Imposto de Renda de adiantamento, folha de pagamento, férias, 13º salário e rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

**Conceito de Regime Caixa e Competência**

- Regime Competência:

O funcionário trabalha e recebe dentro do mesmo mês, ou seja, até o último dia do mês. Neste caso o calculo do IRRF será sempre na folha de pagamento.

- Regime Caixa:

O funcionário trabalha em um mês e recebe até o 5º dia útil do mês seqüente, e provavelmente auferiu um adiantamento no dia 20. Neste caso teremos o cálculo do IRRF no Adiantamento de Salário e na Folha de Pagamento.

**Conferência IR - Regime Competência**

- Folha de Pagamento:

Base IR Folha = (Verbas com “S” para IR Proventos – Verbas com “S” para IR desconto e com Não nos campos Ref 13º e Ref Ferias) – Ded. Inss Base IR .  
IR Folha = Base IR Folha - Ded. de Dependentes – Pensão Alimentícia da Folha (se houver) \* Parcela % da Tabela de IR – Parcela a deduzir.

**Conferência IR - Regime Caixa**

- Adiantamento:

Base IR Adiantamento = Verbas com “S” para IR + Base IR Mês Anterior  
IR Adiantamento = Base IR Adiantamento - Ded. De dependentes – Pensão Alimentícia do Adiantamento (se houver) \* Faixa da Tabela de IR – Parcela a deduzir – IR. Mês Anterior.

- Folha de Pagamento:

Base IR Folha = Verbas com “S” para IR  e com Não nos campos Ref 13º e Ref Ferias – Adiantamento – Ded. De Inss Base IR  
IR Folha = Base IR – Ded. De Dependentes – Pensão alimentícia da Folha (se houver) \* Faixa IR – Parcela a Deduzir.

**Conferência IR nas Férias:**

Base de IR Férias = Verbas com “S” para férias e “S” para IR – Ded. INSS da Base Férias  
IR Férias = Base IR Férias – Ded. Dependentes Férias – Pensão Alimentícia Férias (se houver) \* Alíquota de IR – Parcela a deduzir.

**Conferência IR no 13º Salário:**

Base IR 13º Salário = Verbas com “S” para 13º Salário e “S” para IR  
IR 13º Salário = Base IR 13º Salário – Ded. De Dependentes – Pensão Alimentícia do 13º Salário (se houver) \* Aliquota do IR – Parcela a Deduzir.

**IR na Rescisão:**

Para conferir estes valores em rescisão contratual devem ser usadas as mesmas fórmulas acima.

Os IRs de cada fato gerador (Salário, Férias e 13º Salário) devem ser conferidos individualmente.

Para compor a base de IR da Folha, numa rescisão, são levadas em consideração as verbas com "S" para IR nas incidências das verbas e "NÃO" no campo "Ref. a Férias" e "Ref. a 13º".

Para conferir as férias, as verbas com "S" para IR e SIM para "Ref. a Férias", da mesma forma o 13º.

Para conferência de qualquer um dos valores, indicamos o relatório de DARF/MENSAL, nele constam os valores que irão para a DARF de acordo com a data do pagamento, já com a separação entre folha, adiantamento, férias, 13º salário e Rescisão Contratual.

Os valores que constarão na DARF, são os valores com**DATA DE PAGAMENTO**dentro do período de pagamento informado nos parâmetros de geração da DARF.

**IMPORTANTE:** Caso o cálculo do IR seja no modelo simplificado, não terá as deduções legais da base de IR (INSS, dependente, pensão e previdência privada), então deve ser considerada apenas as verbas de provento e desconto para montar a s bases.

**O sistema valida os percentuais informados nas tabelas S001** (tabela de INSS) **e S002** (tabela de imposto de renda).

[RH - Linha Protheus - GPE - Como cadastrar ou atualizar a tabela de INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043059473-RH-Linha-Protheus-GPE-Como-cadastrar-ou-atualizar-a-tabela-de-INSS)

[RH - Linha Protheus - GPE - Como cadastrar ou alterar a tabela S002 - Tabela Imposto de Renda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21864295842327-RH-Linha-Protheus-GPE-Como-cadastrar-ou-alterar-a-tabela-S002-Tabela-Imposto-de-Renda)

**Saiba Mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[PSIGAGPE0118 - GPEA040 - Como parametrizar as verbas para o cálculo do adiantamento?](http://tdn.totvs.com/pages/viewpage.action?pageId=223904764)

[RH - Linha Protheus - GPE - MP-1.171/2023 - Como configurar a nova forma de cálculo de IR no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14626756121367)

[FAQ da Consultoria de Segmentos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=758481181)

[Espaço Fiscal - Totvs](https://www.totvs.com/blog/fiscal-clientes/novo-calculo-de-imposto-de-renda/)
