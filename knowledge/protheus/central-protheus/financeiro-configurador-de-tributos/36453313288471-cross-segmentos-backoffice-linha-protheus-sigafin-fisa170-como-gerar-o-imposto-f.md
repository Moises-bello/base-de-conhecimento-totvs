---
article_id: 36453313288471
category: Financeiro - Configurador de Tributos
content_hash: 0bc9e12537ea9b12a7a82f3f7420f6a54ba4102b2524dedff9b695190f2420e2
fetched_at: '2026-06-28T22:37:46.210829+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como gerar
  o imposto FUNRURAL com a regra financeira para o receber?
type: support-article
updated_at: '2025-11-21T16:23:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36453313288471-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-o-imposto-FUNRURAL-com-a-regra-financeira-para-o-receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36453313243287) Tempo aproximado para leitura: **00:09 min**  
  
**Dúvida**  
Como gerar o imposto FUNRURAL com a regra financeira para o receber?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
**1.  FISA710 - Regras Financeiras > Regra do Título**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36453313243799)

Para esse cenário, crie a **regra de título** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* O **Tipo de Movimento (Tp. Movto)**, selecionando a opção****Impostos.****
* **O****código do participante** (fornecedor ou cliente) para o qual será gerado o título;
* A **carteira**, que neste caso deve ser definida como **Receber**;
* A **natureza** previamente criada para vinculação do tributo;
* O **tipo de título**, aplicável aos três impostos.

**Exemplo aplicado ao SENAR, devendo ser replicado para os demais tributos de GILRAT e INSS.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36492590281751)

**1.2 Regra de Cálculo - Títulos Financeiros**

Para esse cenário, crie a **regra de cálculo**considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **% Base**: 100%
* **% Alíquota**: conforme a necessidade.
* **Edita Cálculo**: Sim.

**Exemplo aplicado ao SENAR, devendo ser replicado para os demais tributos de GILRAT e INSS.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36453313246103)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36492602818967)

**1.3 Regra de Vencimento**

Para esse cenário, crie a **regra de vencimento** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Dia do Vencimento**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36453313246999)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36492590286615)

**1.4 Regra de retenção**

Para este cenário, crie a **regra de retenção** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Cumulatividade**(conforme a necessidade; neste cenário, não será cumulado)
* **Valor Mínimo de Retenção.**
* **Valor máximo de retenção.**
* **Demais campos**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36492590286999)

**1.5 Regra Financeira**

Este cadastro tem como função definir a regra de retenção do tributo aplicado a títulos gerados diretamente no módulo Financeiro, consolidando outras regras como vencimento, cumulatividade, retenção, cálculo, etc.

Outra função deste cadastro é definir a qual tributo a regra se refere, ou seja, relacionar a regra financeira a um tributo definido por legislações federais, estaduais ou municipais.

Para este cenário, é necessário criar a regra financeira correspondente ao imposto na aba**Dados Gerais**, preenchendo os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Início de Vigência**: data inicial
* **Fim da Vigência**: data final
* **Fato Gerador:** 1 – Competência (emissão) | 2 – Caixa (baixa)
* **Aplica-se à Carteira**: (1 – Pagar ou 2 – Receber; neste caso, selecionar a opção **Pagar**)
* **Valor do Título**: (1 – Subtrair, 2 – Somar ou 3 – Sem ação. Neste caso, selecionar a opção Subtrair)
* **Parcelamento**: opcional, conforme a necessidade.
* **Tributo**: imposto a ser cadastrado.
* **Classificação do tipo de imposto** (Principal)

**Exemplo aplicado ao SENAR, devendo ser replicado para os demais tributos de GILRAT e INSS.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36453303637783)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36492602822807)

Na aba **Regras Gerais**, vincule todas as regras criadas anteriormente nas **regras financeiras**, considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Regra de Vencimento**
* **Regra de Título**
* **Regra de Cálculo**
* **Regra de Retenção**

**Exemplo aplicado ao SENAR, devendo ser replicado com os cadastros correspondentes para os demais tributos de GILRAT e INSS.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36492590289175)

**A aba contábil não contém nenhum preenchimento.**

**⚠️Importante: Configuração de Regras Financeiras e Tributos.**

As regras financeiras **NÃO**possuem a funcionalidade de vínculo do **IDTOTVS**, sendo assim, para o correto cálculo dos impostos do legado no cadastro da regra financeira, deve ser informada a sigla do imposto legado, conforme é demonstrado na seção de detalhes da Regra Financeira no grid **Tributo**.

Por exemplo, em uma configuração de regra fiscal em que seja informado o tributo SENAR vinculado ao IDTOTVS do SENAR e nesta regra, seja vinculada a uma regra financeira para ser gerada a retenção do imposto, a regra financeira deve estar cadastrada indicando o tributo como **SENAR (sigla do legado) / INSS (sigla do legado) ou FUNRUR (sigla do legado).**

Caso a Regra Financeira seja cadastrada como **SENAR** por exemplo**,**o sistema irá interpretá-la como um novo tributo, o que poderá gerar diferenças nos valores calculados e impactar a geração das obrigações fiscais.

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36492602825239)

**2. Cadastro de Cliente**  
No **cadastro do cliente**, criado sem configuração de impostos, vincule a **regra financeira** em **Outras Ações → Tipos de Retenções**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36453313259415)

Vincule o código da **Regra Financeira**conforme exemplo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36453313261079)

**3. Cadastro da natureza**  
No**cadastro de** **natureza,** criado sem parametrização de impostos, vincule a **regra financeira** no grid **"Tipo de retenção x natureza",**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36453313262103)

**4.** Exemplo de inclusão de um título no **Contas a Receber**, utilizando a configuração da rotina **FISA170 – Configurador de Tributos**, com a geração dos impostos **SENAR, INSS e GILRAT**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36453303648023)

**Ao acessar o título NF > Outras ações > Consulta de Retenções**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36453303649431)

**É demonstrada a tela a seguir:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36453313271063)

**⚠️ Importante**

Para o cálculo da retenção de SENAR/GILRAT/INSS em notas de entrada e/ou saída, por meio do Configurador de Tributos, é necessário também cadastrar a respectiva [Regra Fiscal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28271950709399-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-PIS-COFINS-CSLL-reten%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda).

**Saiba mais**

[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/PROT/Configurador+de+Tributos+-+Regras+Financeiras#01-01)  
[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
