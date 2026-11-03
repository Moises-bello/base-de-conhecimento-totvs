---
article_id: 32524692208535
category: Financeiro - Configurador de Tributos
content_hash: 62e298830ed1274165d4856f8859a9de83abd2b6f14bfde9867dd637469285e6
fetched_at: '2026-06-28T22:37:45.868990+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como gerar
  o imposto INSS com a regra financeira?
type: support-article
updated_at: '2025-09-24T20:18:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32524692208535-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-o-imposto-INSS-com-a-regra-financeira
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32524692152727) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como gerar o imposto INSS com a regra financeira pelo configurador de tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**  
Para definir a regra financeira do INSS ao **Contas a Pagar** por meio do **Configurador de Tributos (FISA170)**, é necessário que os cadastros de **Regras Financeiras, Fornecedor e Natureza** estejam previamente criados.

Ressalta-se que os cadastros de **fornecedor** e **natureza** não devem conter parametrizações de impostos, uma vez que toda a configuração é realizada exclusivamente nas **Regras Financeiras**, conforme ilustrado no exemplo a seguir:  
  
**1. FISA710 - Regras Financeiras > Regra do Título**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35174096814999)  
  
Para esse cenário, crie a **regra de título** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* O **Tipo de Movimento (Tp. Movto)**, selecionando a opção **Impostos**
* **O****código do participante** (fornecedor ou cliente) para o qual será gerado o título;
* A **carteira**, que neste caso deve ser definida como **Pagar**;
* A **natureza** previamente criada para vinculação do tributo;
* O **tipo de título**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35174069912599)  
  
**1.2 Regra de Cálculo**

Para esse cenário, crie a **regra de cálculo**considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **% Base**: 100%
* **% Alíquota**: conforme a necessidade.
* **Edita Cálculo**: Sim.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35174069915415)  
  
**1.3 Regra de Vencimento**

Para esse cenário, crie a **regra de cálculo** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Dia do Vencimento**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35174096818071)

**1.4 Regra de Retenção**

Para este cenário, crie a **regra de retenção** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Cumulatividade**
* **Valor Mínimo de Retenção.**
* **Valor máximo de retenção.**
* **Demais campos**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35174069918359)

**1.5 Regra Financeira**  
Este cadastro tem como função definir a regra de retenção do tributo aplicado a títulos gerados diretamente no módulo Financeiro, consolidando outras regras como vencimento, cumulatividade, retenção, cálculo, etc.

Outra função deste cadastro é definir a qual tributo a regra se refere, ou seja, relacionar a regra financeira a um tributo definido por legislações federais, estaduais ou municipais.

Para este cenário, é necessário criar a regra financeira correspondente ao imposto na aba **Dados Gerais**, preenchendo os campos indicados a seguir:

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
* **Classificação do tipo de imposto** (Principal)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35174096820759)

Na aba Regras Gerais, vincule todas as regras criadas anteriormente nas **regras financeiras**, considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Regra de Vencimento**
* **Regra de Título**
* **Regra de Cálculo**
* **Regra de Retenção**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35174096822679)

**2. Cadastro de Fornecedor**  
No **cadastro do fornecedor**, criado sem configuração de impostos, vincule a **regra financeira** em **Outras Ações → Tipos de Retenções**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35174069927319)  
  
 Vincule o código da **Regra Financeira**conforme exemplo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35174096826135)

**3. Cadastro da Natureza**   
No**cadastro de** **natureza,** criado sem parametrização de impostos, vincule a **regra financeira** em **"Tipo de retenção x natureza"**conforme exemplo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35174069930775)  
  
4. Demonstração da inclusão de um título no contas a pagar utilizando a configuração da rotina **FINA170** **- Configurador de tributos e gerando o imposto INSS.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35174096829719)

⚠️ Importante

Para o cálculo da retenção de PIS/COFINS/CSLL em notas de entrada e saída, por meio do Configurador de Tributos, é necessário também cadastrar a respectiva Regra Fiscal.

**Saiba mais**  
[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras#01-01)  
[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
