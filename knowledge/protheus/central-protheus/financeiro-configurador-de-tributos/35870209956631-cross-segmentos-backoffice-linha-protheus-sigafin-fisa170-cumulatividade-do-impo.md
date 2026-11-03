---
article_id: 35870209956631
category: Financeiro - Configurador de Tributos
content_hash: b305c3e1b2c55d11b3cf2912c7033c47a4481319dbecdc79cda0e1b59eb25eab
fetched_at: '2026-06-28T22:37:46.007907+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Cumulatividade
  do imposto IRRF com a regra financeira para o contas a receber e pagar
type: support-article
updated_at: '2025-11-26T13:46:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35870209956631-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Cumulatividade-do-imposto-IRRF-com-a-regra-financeira-para-o-contas-a-receber-e-pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35870209925655) Tempo aproximado para leitura: **00:15 min**  
  
**Dúvida**  
Qual é o processo de cumulatividade para o IRRF?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da 12.1.2210.  
  
**Solução**  
Para definir a regra financeira do IRRF ao **Contas a Pagar** por meio do **Configurador de Tributos (FISA170)**, é necessário que os cadastros de **Regras Financeiras, Fornecedor e Natureza** estejam previamente criados.

Ressalta-se que os cadastros de **fornecedor** e **natureza** não devem conter parametrizações de impostos, uma vez que toda a configuração é realizada exclusivamente nas **Regras Financeiras**, conforme ilustrado no exemplo a seguir:  
  
**1. FISA710 - Regras Financeiras > Regra do Título**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35870209928599)**

Para esse cenário, crie a **regra de título** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* O **Tipo de Movimento (Tp. Movto)**, selecionando a opção****Impostos.****
* **O****código do participante** (fornecedor ou cliente) para o qual será gerado o título;
* A **carteira**, que neste caso deve ser definida como **Pagar**;
* A **natureza** previamente criada para vinculação do tributo;
* O **tipo de título**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35870209931031)

**1.2 Regra de Cálculo - Títulos Financeiros**  
Para esse cenário, crie a **regra de cálculo**considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **% Base**: 100%
* **% Alíquota**: conforme a necessidade.
* **Edita Cálculo**: Sim.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35870209932439)

**1.3 Regra de Vencimento**

Para esse cenário, crie a **regra de cálculo** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Dia do Vencimento**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35870209933079)

**1.4 Regra Financeira**  
Este cadastro tem como função definir a regra de retenção do tributo aplicado a títulos gerados diretamente no módulo Financeiro, consolidando outras regras como vencimento, cumulatividade, retenção, cálculo, etc.

Outra função deste cadastro é definir a qual tributo a regra se refere, ou seja, relacionar a regra financeira a um tributo definido por legislações federais, estaduais ou municipais.

Para este cenário, é necessário criar a regra financeira correspondente ao imposto na aba**Dados Gerais**, preenchendo os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Início de vigência**: data inicial
* **Fim da vigência**: data final.
* **Fato Gerador:** 1 – Competência (emissão) | 2 – Caixa (baixa)
* **Aplica-se à Carteira**: (1 – Pagar ou 2 – Receber; neste caso, selecionar a opção **Pagar**)
* **Valor do Título**: (1 – Subtrair, 2 – Somar ou 3 – Sem ação. Neste caso, selecionar a opção Subtrair)
* **Código de retenção**, conforme a necessidade.
* **Parcelamento**: opcional, conforme a necessidade.
* **Tributo**: imposto a ser cadastrado.
* **Classificação do tipo de imposto** (principal)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35870199558551)

Na aba **Regras Gerais**, vincule todas as regras criadas anteriormente nas **regras financeiras**, considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Regra de Vencimento**
* **Regra de Título**
* **Regra de Cálculo**
* **Regra de Retenção**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35870209934743)

**1.5 Regra de Cumulatividade**

Para este cenário, é necessário criar a regra de cumulatividade e vincular a **regra financeira**, considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Relacionar as regras financeiras para cumulatividade (PIS, COFINS e CSLL)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35870199560855)

**1.6 Regra de Retenção**

Para este cenário, crie a **regra de retenção** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Cumulatividade**(3 - Acumula por valor de imposto)
* **Valor Mínimo de Retenção.**
* **Valor máximo de retenção.**
* **Regra de cumulatividade** (vincular à regra de cumulatividade cadastrada anteriormente)
* **Demais campos**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35870209936279)

**2. Cadastro de fornecedor.**  
No **cadastro do fornecedor**, criado sem configuração de impostos, vincule a **regra financeira** em **Outras Ações → Tipos de Retenções**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35870199563031)

Vincule o código da **Regra Financeira**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35870209939095)

**3. Cadastro da natureza.**  
No**cadastro de** **natureza,** criado sem parametrização de impostos, vincule a **regra financeira** em **"Tipo de retenção x natureza",**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35870209941143)

**Para o cálculo da retenção de PIS/COFINS/CSLL em notas de entrada e saída, por meio do Configurador de Tributos, é necessário cadastrar a respectiva** [**Regra Fiscal**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28271950709399-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-PIS-COFINS-CSLL-reten%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda)**.**

**Saiba mais**  
[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/PROT/Configurador+de+Tributos+-+Regras+Financeiras#01-01)  
[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)  
[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular PIS/COFINS/CSLL retenção utilizando o Configurador de Tributos para notas de entrada e saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28271950709399-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-PIS-COFINS-CSLL-reten%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda)
