---
article_id: 33858224342167
category: Financeiro - Configurador de Tributos
content_hash: df611f283dcd22acd3b60cf78e4320e76c86dcb4c26019daff479b249a034d31
fetched_at: '2026-06-28T22:37:45.983024+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como incluir
  a retenção dos impostos PCC com a cumulatividade entre Filiais com a mesma raiz
  de CNPJ
type: support-article
updated_at: '2025-09-24T20:12:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33858224342167-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-incluir-a-reten%C3%A7%C3%A3o-dos-impostos-PCC-com-a-cumulatividade-entre-Filiais-com-a-mesma-raiz-de-CNPJ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33858224276247) Tempo aproximado para leitura: **00:15 min**  
  
**Dúvida**  
Como incluir a retenção dos impostos PCC com a cumulatividade entre filiais com a mesma raiz de CNPJ no Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**

Para definir a regra financeira do PCC ao **Contas a Pagar** por meio do **Configurador de Tributos (FISA170)**, é necessário que os cadastros de **Regras Financeiras, Fornecedor e Natureza** estejam previamente criados.

Ressalta-se que os cadastros de **fornecedor** e **natureza** não devem conter parametrizações de impostos, uma vez que toda a configuração é realizada exclusivamente nas **Regras Financeiras**, conforme ilustrado no exemplo a seguir:

Para solucionar essa dúvida, é necessário:

-  Ter duas filiais com a mesma raiz de CNPJ, ou seja, os primeiros 8 dígitos iguais.

- Realizar os seguintes cadastros no Configurador de Tributos:  
  
**1. Regra do Título**

Para esse cenário, crie a **regra de título** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* O **Tipo de Movimento (Tp. Movto)**, selecionando a opção **Impostos**
* **O****código do participante** (fornecedor ou cliente) para o qual será gerado o título;
* A **carteira**, que neste caso deve ser definida como **Pagar**;
* A **natureza** previamente criada para vinculação do tributo;
* O **tipo de título**, aplicável aos três impostos.

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35175417846295)  
  
  
**2.** **Regra de Cálculo - Títulos Financeiros**

Para esse cenário, crie a **regra de cálculo**considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **% Base**: 100%
* **% Alíquota**: conforme a necessidade.
* **Edita Cálculo**: Sim.

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35175417847959)  
  
**3.** **Regra de Vencimento**

Para esse cenário, crie a **regra de cálculo** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Dia do Vencimento**: conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35175440998039)  
  
**4.** **Regra de Cumulatividade**

Para esse cenário, crie a **regra de cumulatividade** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Relacione as regras financeiras para cumulatividade** (vinculando os impostos correspondentes a serem acumulados)

Neste cadastro, é necessário vincular os três impostos que compõem a cumulatividade. Por exemplo, na regra do PIS deve incluir, em sua configuração, a associação ao CSLL e ao COFINS, conforme ilustrado a seguir:

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35175441008151)

Exemplo dos cadastros de **Cofins e CSLL.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35175417853847)

**5.** **Regra de Retenção**

Para este cenário, crie a **regra de retenção** considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Código**
* **Descrição**
* **Cumulatividade**
* **Valor Mínimo de Retenção.**
* **Valor máximo de retenção.**
* **Acumula Por** (4 - Raiz do CNPJ|)
* **Acum. Filial** (3 - Filiais com mesma raiz de CNPJ)
* **Regra de Cumulatividade** (Regra criada anteriormente)

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35175417857687)  
  
  
**6.** **Regras Financeira**

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

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35177065697047)

Na aba Regras Gerais, vincule todas as regras criadas anteriormente nas **regras financeiras**, considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Regra de Vencimento**
* **Regra de Título**
* **Regra de Cálculo**
* **Regra de Retenção**

**Exemplo aplicado ao PIS, devendo ser replicado para os demais tributos de Cofins e CSLL.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35177065698199)  
  
**7.**  **Cadastro de Fornecedor**

No **cadastro do fornecedor**, criado sem configuração de impostos, vincule a **regra financeira** em **Outras Ações → Tipos de Retenções**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35177039896343)

Vincule o código da **Regra Financeira**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35177065701399)  
  
  
**8.** **Cadastro da Natureza**

No**cadastro de** **natureza,** criado sem parametrização de impostos, vincule a **regra financeira** em **"Tipo de retenção x natureza",**conforme exemplo.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35177039899543)  
  
**Exemplo**  
  
1º título incluído com o valor de R$ 200, sem gerar a retenção.  
2º título incluído com o valor de R$ 250, gerando a retenção acumulada.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33858269186199)

**Importante**

Para o cálculo da retenção de PIS/COFINS/CSLL em notas de entrada e saída, por meio do Configurador de Tributos, é necessário também cadastrar a respectiva [Regra Fiscal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28271950709399-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-PIS-COFINS-CSLL-reten%C3%A7%C3%A3o-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda).

**Saiba Mais**  
[Compartilhamento de tabelas do Configurador de Tributos (Regras Financeiras)](https://tdn.totvs.com/pages/releaseview.action?pageId=969991293)
