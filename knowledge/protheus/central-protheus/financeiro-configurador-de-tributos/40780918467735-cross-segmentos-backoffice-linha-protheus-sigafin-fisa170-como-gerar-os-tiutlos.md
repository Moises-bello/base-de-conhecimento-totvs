---
article_id: 40780918467735
category: Financeiro - Configurador de Tributos
content_hash: d9c35d6fffe1d1041ac3e70593f8387fcacf342d0956b007c10134bd6b9edc8b
fetched_at: '2026-06-28T22:37:45.947538+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como gerar
  os tiutlos de pis, cofins e csll do contas a receber para o contas a pagar?
type: support-article
updated_at: '2026-05-29T14:14:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40780918467735-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-os-tiutlos-de-pis-cofins-e-csll-do-contas-a-receber-para-o-contas-a-pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40780918449175) Tempo aproximado para leitura: **15:00 min**  
  
**Dúvida**  
Como gerar os títulos de PIS, COFINS e CSLL do contas a receber para o contas a pagar?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Para definir a regra financeira do PIS, COFINS e CSLL do **Contas a receber para o Contas a pagar** por meio do **Configurador de Tributos (FISA170)**, é necessário que os cadastros de **Cliente** **e Natureza** estejam previamente criados.

Ressalta-se que os cadastros de **cliente**e **natureza** não devem conter parametrizações de impostos, uma vez que toda a configuração é realizada exclusivamente nas **Regras Financeiras**, conforme ilustrado no exemplo a seguir:

**1)** FISA710 - **Regras Fiscais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40808584842391)

**Perfis** > **Perfil do Produto**

Para esse cenário, crie o **Perfil do Produto**, considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* **Código do produto:** código do produto que deverá ser vinculado à regra. **Observação: não deve conter configuração de imposto no cadastro.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40823321047191)

**2) Perfis** > **Perfil de Participante**

Para esse cenário, crie o **Perfil do Participante**, considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* **Tipo:** (cliente ou fornecedor) Neste caso, **cliente.**
* **Código do participante:** código do participante que deverá ser vinculado à regra. **Observação: não deve conter configuração de imposto no cadastro.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40823321050007)

**3)** **Regras Fiscais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40808545703959)

**Regras de Cálculo do Documento Fiscal** > **Regra de Base de Cálculo**

Para esse cenário, crie **a** **Regra de Base de Cálculo**, considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* **Valor de Origem:** (01 - Valor da Mercadoria)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40808545706647)

**4)** **Regras de Cálculo Documento Fiscal** >**Regra de Alíquota**

Para esse cenário, crie a **Regra de Alíquota**, considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* **Valor de Origem:** (04 - Alíquota informada manualmente)
* **Tipo de alíquota**: (01 - Porcentual)
* **Alíquota**

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40808661631255)

**5) Regras de Cálculo Documento Fiscal > Regras de Cálculo - Documento Fiscais**

Para esse cenário, crie a **Regra de Alíquota**, considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código regra**
* **Descrição**
* **Tributo**
* **Data de início (período que será validado a regra)**
* **Data Final (período que será validado a regra)**
* **Status**
* **Base de cálculo**
* **Alíquota**
* **Regra Financeira**

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40820723769239)

**Em Definição dos Perfis**

* **Origem/Destino**
* **Participante** (participante criado no passo inicial)
* **Operação**
* **Produto** (produto criado no passo inicial)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40823300998295)

**6) Regras Financeiras**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40807942120599)

**Regras Financeiras** > **Regra de Título**

Para esse cenário, crie a **regra de título** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* O **Tipo de Movimento (Tp. Movto)**, selecionando a opção***Impostos.***
* **O****código do participante** (**fornecedor)** para o qual será gerado o título;
* A **carteira**, que neste caso deve ser definida como ***pagar***;
* A **natureza** previamente criada para vinculação do tributo;
* O **tipo de título**, aplicável aos três impostos (**TX**)

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40820674421399)

**7) Regras Financeiras** > **Regra de Cálculo - Títulos Financeiros**

Para esse cenário, crie a **regra de cálculo**considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **% Base**: 100%
* **% Alíquota**: conforme a necessidade.
* **Edita Cálculo**: Sim.

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40820723771927)

**8) Regras Financeiras** > **Regra de Vencimento**

Para esse cenário, crie a **regra de cálculo** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Dia do Vencimento**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40807958583063)

**9) Regras Financeiras** > **Regra de Retenção**

Para este cenário, crie a **regra de retenção** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Cumulatividade**(conforme a necessidade; neste cenário, **não será cumulado**)
* **Valor Mínimo de Retenção.**
* **Valor máximo de retenção.**
* **Demais campos**: conforme a necessidade.

**Exemplo aplicado ao PCC, sem cumulatividade:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40807942125719)

**10)** **Regras Financeiras** > **Regras Financeiras**

Este cadastro tem como função definir a regra de retenção do tributo aplicado a títulos gerados diretamente no módulo Financeiro, consolidando outras regras como vencimento, cumulatividade, retenção, cálculo, etc.

Outra função deste cadastro é definir a qual tributo a regra se refere, ou seja, relacionar a regra financeira a um tributo definido por legislações federais, estaduais ou municipais.

Para este cenário, é necessário criar a regra financeira correspondente ao imposto na aba**Dados Gerais**, preenchendo os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Início de Vigência**: data inicial
* **Fim da Vigência**: data final
* **Fato Gerador:** 1 – Competência (emissão) | 2 – Caixa (baixa) ; neste caso, selecionar a opção **Caixa (baixa).**
* **Aplica-se à Carteira**: (1 – Pagar ou 2 – Receber) neste caso, selecionar a opção ***Pagar***
* **Valor do Título**: (1 – Subtrair, 2 – Somar ou 3 – Sem ação. Neste caso, selecionar a opção **Sem Ação**)
* **Código de retenção** (conforme a necessidade)
* **Parcelamento**: opcional, conforme a necessidade.
* **Tributo**: imposto a ser cadastrado.
* **Classificação do tipo de imposto** (principal)

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40820674422679)

Na aba **Regras Gerais**, vincule todas as regras criadas anteriormente nas **regras financeiras**, considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Regra de Vencimento**
* **Regra de Título**
* **Regra de Cálculo**
* **Regra de Retenção**

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40808545708439)

Desta forma, serão gerados o PIS, COFINS e CSLL no contas a pagar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40823321052823)
