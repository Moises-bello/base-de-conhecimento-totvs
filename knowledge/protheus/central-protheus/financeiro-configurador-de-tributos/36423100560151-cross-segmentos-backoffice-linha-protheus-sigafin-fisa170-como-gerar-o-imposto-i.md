---
article_id: 36423100560151
category: Financeiro - Configurador de Tributos
content_hash: 3ca3acc5aed2c31c3367180349729c7c3a1186a3e02eed3a4e9d60d206848a9f
fetched_at: '2026-06-28T22:37:45.882260+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como gerar
  o imposto ISS com a regra financeira no contas a receber?
type: support-article
updated_at: '2025-11-18T19:32:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36423100560151-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-o-imposto-ISS-com-a-regra-financeira-no-contas-a-receber
---

**Dúvida**  
Como gerar o imposto ISS com a regra financeira pelo configurador de tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Para definir a regra financeira do ISS ao **Contas a Receber** por meio do **Configurador de Tributos (FISA170)**, é necessário que os cadastros de **Regras Financeiras, Cliente e Natureza** estejam previamente criados.

Ressalta-se que os cadastros de cliente e **natureza** não devem conter parametrizações de impostos, uma vez que toda a configuração é realizada exclusivamente nas **Regras Financeiras**, conforme ilustrado no exemplo a seguir:

**1. FISA710 - Regras Financeiras > Regra do Título**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36423109423511)

Para esse cenário, crie a **regra de título** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* **Tipo de Movimento (Tp. Movto)**, selecionando a opção **abatimentos**
* **Código do participante** (fornecedor para o qual será gerado o título com base no município do débito;
* **C****arteira**, que neste caso deve ser definida como **receber**;
* **Código Participante** (deixar em branco)
* **N****atureza** previamente criada para vinculação do tributo;
* **Tipo de título**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36423100539799)  
  
**1.2 Regra de Cálculo - Títulos Financeiros**

Para esse cenário, crie a **regra de cálculo**considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **% Base**: 100%
* **% Alíquota**: conforme a necessidade.
* **Edita Cálculo**: Sim.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36423100540695)  
  
**1.3 Regra de Vencimento**

Para esse cenário, crie a **regra de vencimento** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Dia do Vencimento**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36423100541463)  
  
**1.4 Regra de retenção**

Para este cenário, crie a **regra de retenção** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Valor Mínimo de Retenção.**
* **Valor máximo de retenção.**
* **Demais campos**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36423100542103)

**1.5 Regra Financeira**  
Este cadastro tem como função definir a regra de retenção do tributo aplicado a títulos gerados diretamente no módulo Financeiro, consolidando outras regras como vencimento, cumulatividade, retenção, cálculo, etc.

Outra função deste cadastro é definir a qual tributo a regra se refere, ou seja, relacionar a regra financeira a um tributo definido por legislações federais, estaduais ou municipais.

Para este cenário, é necessário criar a regra financeira correspondente ao imposto na aba**Dados Gerais**, preenchendo os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Início de Vigência**: data inicial
* **Fim da Vigência**: data final
* **Fato Gerador:** 1 – **Competência (emissão)** | 2 – Caixa (baixa)
* **Aplica-se à Carteira**: (1 – Pagar ou 2 – Receber; neste caso, selecionar a opção ****receber****)
* **Valor do Título**: (1 – Subtrair, 2 – Somar ou 3 – Sem ação. Neste caso, selecionar a opção **Subtrair**)
* **Parcelamento**: opcional, conforme a necessidade.
* **Tributo**: imposto a ser cadastrado.
* **Classificação do tipo de imposto** (Principal)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36423100542743)

Na aba **Regras Gerais**, vincule todas as regras criadas anteriormente nas **regras financeiras**, considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Regra de Vencimento**
* **Regra de Título**
* **Regra de Cálculo**
* **Regra de Retenção**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36423100544023)

**2. Cadastro de Cliente**  
No **cadastro do Cliente**, criado sem configuração de impostos, vincule a **regra financeira** em **Outras Ações → Tipos de Retenções**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36423363367831)

Vincule o código da **Regra Financeira**conforme exemplo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36423109432215)  
  
**3. Cadastro da Natureza**  
No**cadastro de** **natureza,** criado sem parametrização de impostos, vincule a **regra financeira** em **"Tipo de retenção x natureza",**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36423363369495)  
  
Para o cálculo da retenção de ISS via documento de entrada ou saída, por meio do Configurador de Tributos, é necessário também cadastrar a respectiva regra fiscal.

**Saiba mais**  
[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras#01-01)  
[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular o ISS utilizando o Configurador de Tributos para notas de entrada e saída?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33675439757335-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-ISS-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda)
