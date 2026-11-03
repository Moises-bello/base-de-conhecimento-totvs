---
article_id: 34977506568599
category: Financeiro - Configurador de Tributos
content_hash: 4ba39186983247db8d0bd6720ea4e1be5778300208a1d71acd6f6bd80ca9faf0
fetched_at: '2026-06-28T22:37:45.962835+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como gerar
  retenção de PIS, Cofins e Csll Contas a Receber?
type: support-article
updated_at: '2026-05-28T20:01:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34977506568599-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-reten%C3%A7%C3%A3o-de-PIS-Cofins-e-Csll-Contas-a-Receber
---

**Dúvida:**  
Como gerar um título PCC com abatimento no financeiro?  
  
**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução:**  
Para definir a regra financeira do PIS, COFINS e CSLL ao **Contas a receber** por meio do **Configurador de Tributos (FISA170)**, é necessário que os cadastros de **Fornecedor e Natureza** estejam previamente criados.

Ressalta-se que os cadastros de **cliente**e **natureza** não devem conter parametrizações de impostos, uma vez que toda a configuração é realizada exclusivamente nas **Regras Financeiras**, conforme ilustrado no exemplo a seguir:

**1.  FISA710 - Regras Financeiras > Regra do Título**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35443429595543)

Para esse cenário, crie a **regra de título** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* O **Tipo de Movimento (Tp. Movto)**, selecionando a opção***Abatimentos.***
* **O****código do participante** (cliente) para o qual será gerado o título;
* A **carteira**, que neste caso deve ser definida como ***receber***;
* A **natureza** previamente criada para vinculação do tributo;
* O **tipo de título**, aplicável aos três impostos (**PIS = PI-, COFINS = CF-, CSLL = CS-**)

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35443411717015)

**1.2 Regra de Cálculo - Títulos Financeiros**

Para esse cenário, crie a **regra de cálculo**considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **% Base**: 100%
* **% Alíquota**: conforme a necessidade.
* **Edita Cálculo**: Sim.

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35443429601687)

**1.3 Regra de Vencimento**

Para esse cenário, crie a **regra de cálculo** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Dia do Vencimento**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35443429602711)

**1.4 Regra de retenção**

Para este cenário, crie a **regra de retenção** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Cumulatividade**(conforme a necessidade; neste cenário, **não será cumulado**)
* **Valor Mínimo de Retenção.**
* **Valor máximo de retenção.**
* **Demais campos**: conforme a necessidade.

**Exemplo aplicado ao PCC, sem cumulatividade:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40509478126103)

**1.5 Regra Financeira**

Este cadastro tem como função definir a regra de retenção do tributo aplicado a títulos gerados diretamente no módulo Financeiro, consolidando outras regras como vencimento, cumulatividade, retenção, cálculo, etc.

Outra função deste cadastro é definir a qual tributo a regra se refere, ou seja, relacionar a regra financeira a um tributo definido por legislações federais, estaduais ou municipais.

Para este cenário, é necessário criar a regra financeira correspondente ao imposto na aba**Dados Gerais**, preenchendo os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Início de Vigência**: data inicial
* **Fim da Vigência**: data final
* **Fato Gerador:** **1 – Competência (emissão)** | 2 – Caixa (baixa) ; neste caso, selecionar a opção **competência.**
* **Aplica-se à Carteira**: (1 – Pagar ou 2 – Receber; neste caso, selecionar a opção ***Receber***)
* **Valor do Título**: (1 – Subtrair, 2 – Somar ou 3 – Sem ação. Neste caso, selecionar a opção **Subtrair**)
* **Parcelamento**: opcional, conforme a necessidade.
* **Tributo**: imposto a ser cadastrado.
* **Classificação do tipo de imposto** (Principal)

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35443429604887)

Na aba **Regras Gerais**, vincule todas as regras criadas anteriormente nas **regras financeiras**, considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Regra de Vencimento**
* **Regra de Título**
* **Regra de Cálculo**
* **Regra de Retenção**

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35443411723287)

⚠️Importante: **Configuração de Regras Financeiras e Tributos.**

As regras financeiras **NÃO**possuem a funcionalidade de vínculo do **IDTOTVS**, sendo assim, para o correto cálculo dos impostos do legado no cadastro da regra financeira, deve ser informada a sigla do imposto legado, conforme é demonstrado na seção de detalhes da Regra Financeira na aba **Tributos**.

Por exemplo, em uma configuração de regra fiscal em que seja informado o tributo PISRET vinculado ao IDTOTVS do PIS e nesta regra, seja vinculada a uma regra financeira para ser gerada a retenção do imposto, a regra financeira deve estar cadastrada indicando o tributo como **PIS (sigla do legado) / COF (sigla do legado)**

Caso a Regra Financeira seja cadastrada como **PISRET,**o sistema irá interpretá-la como um novo tributo, o que poderá gerar diferenças nos valores calculados e impactar a geração das obrigações fiscais.

**2. Cadastro de Cliente**  
No **cadastro do Cliente**, criado sem configuração de impostos, vincule a **regra financeira** em **Outras Ações → Tipos de Retenções**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35443429606807)

Vincule o código da **Regra Financeira**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35443429607703)

**3. Cadastro da natureza**  
No**cadastro de** **natureza,** criado sem parametrização de impostos, vincule a **regra financeira** em **"Tipo de retenção x natureza",**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35443411727127)

**4.** Exemplo de inclusão de um título no **Contas a Receber**, utilizando a configuração da rotina **FINA170 – Configurador de Tributos**, com a geração dos impostos **PIS, COFINS e CSLL**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35443429612439)

⚠️ **Importante**

Para o cálculo da retenção de PIS/COFINS/CSLL em notas de entrada e saída, por meio do Configurador de Tributos, é necessário também cadastrar a respectiva [Regra Fiscal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28271950709399-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-PIS-COFINS-CSLL-reten%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda).

**Saiba Mais**

[SIGAFIN - Configurador de Tributos - How to](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33852958399767-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Configurador-de-Tributos-How-to)

[SIGAFIN - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
