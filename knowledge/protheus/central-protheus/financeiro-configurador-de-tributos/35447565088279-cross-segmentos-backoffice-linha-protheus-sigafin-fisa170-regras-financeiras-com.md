---
article_id: 35447565088279
category: Financeiro - Configurador de Tributos
content_hash: bcd02c572a68817e91fec19e6a00d4ca36a2bb0b9dad649c2e1327787e390e0e
fetched_at: '2026-06-28T22:37:46.158215+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos Backoffice Linha Protheus - SIGAFIN - FISA170 - Regras financeiras
  - Como criar regra financeira para o IRRF no Contas a Receber
type: support-article
updated_at: '2025-11-26T12:26:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35447565088279-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Regras-financeiras-Como-criar-regra-financeira-para-o-IRRF-no-Contas-a-Receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35447565051927) Tempo aproximado para leitura: **00:15 min**  
  
**Dúvida**  
Como criar regra financeira para o IR no Contas a Receber?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.2210  
  
**Solução**  
Para definir a regra financeira do **IRRF** no **Contas a Receber** por meio do **Configurador de Tributos (FISA170)**, é necessário que os cadastros de **Cliente e Natureza** estejam previamente criados.

Ressalta-se que os cadastros de **Cliente e Natureza** não devem conter parametrizações de impostos, uma vez que toda a configuração é realizada exclusivamente nas **Regras Financeiras**, conforme ilustrado no exemplo a seguir:

**1.  FISA710 - Regras Financeiras > Regra do Título**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35447575158679)

Para esse cenário, crie a **regra de título** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* O **Tipo de Movimento (Tp. Movto)**, selecionando a opção ****Abatimentos.****
* **O****código do participante** deve ser mantido em branco.
* A **carteira**, que neste caso deve ser definida como **Receber**;
* A **natureza** previamente criada para vinculação do tributo;
* O **tipo de título**, IR-

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35447575160343)

**1.2 Regra de Cálculo - Títulos Financeiros**

Para esse cenário, crie a **regra de cálculo**considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **% Base**: 100%
* **% Alíquota**: conforme a necessidade.
* **Edita Cálculo**: Sim.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35447565056535)

**1.3 Regra de Vencimento**

Para esse cenário, crie a **regra de cálculo** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Dia do Vencimento**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35447575162135)

**1.4 Regra de retenção**

Para este cenário, crie a **regra de retenção** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Cumulatividade**(conforme a necessidade; neste cenário, **não será cumulado**)
* **Valor Mínimo de Retenção.**
* **Valor máximo de retenção.**
* **Demais campos**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35447565058967)

**1.5 Regra Financeira**

Este cadastro tem como função definir a regra de retenção do tributo aplicado a títulos gerados diretamente no módulo Financeiro, consolidando outras regras como vencimento, cumulatividade, retenção, cálculo, etc.

Outra função deste cadastro é definir a qual tributo a regra se refere, ou seja, relacionar a regra financeira a um tributo definido por legislações federais, estaduais ou municipais.

Para este cenário, é necessário criar a regra financeira correspondente ao imposto na aba**Dados Gerais**, preenchendo os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Início de Vigência**: data inicial
* **Fim da Vigência**: data final
* **Fato Gerador:** **1 – Competência (emissão)** | 2 – Caixa (baixa) ; neste caso, selecionar a opção **competência.**
* **Aplica-se à Carteira**: (1 – Pagar ou 2 – Receber; neste caso, selecionar a opção ****Receber****)
* **Valor do Título**: (1 – Subtrair, 2 – Somar ou 3 – Sem ação. Neste caso, selecionar a opção **Subtrair**)
* **Parcelamento**: opcional, conforme a necessidade.
* **Tributo**: imposto a ser cadastrado.
* **Classificação do tipo de imposto** (Principal)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35447565061911)

Na aba **Regras Gerais**, vincule todas as regras criadas anteriormente nas **regras financeiras**, considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Regra de Vencimento**
* **Regra de Título**
* **Regra de Cálculo**
* **Regra de Retenção**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35447575165975)

**2. Cadastro de Cliente**  
No **cadastro do Cliente**, criado sem configuração de impostos, vincule a **regra financeira** em **Outras Ações → Tipos de Retenções**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35448102584983)

Vincule o código da **Regra Financeira**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35448071418903)

**3. Cadastro da Natureza**  
No**cadastro de** **natureza,** criado sem parametrização de impostos, vincule a **regra financeira** em **"Tipo de retenção x natureza",**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35448071420055)

**4.** Exemplo de inclusão de um título no **Contas a Receber**, utilizando a configuração da rotina **FINA170 – Configurador de Tributos**, com a geração dos impostos de **IRRF.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35448102589847)

**Saiba Mais**

[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
