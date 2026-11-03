---
article_id: 29968281466903
category: Financeiro - Contas a Receber
content_hash: 28c27bec599bb258ea576684d35e7778dfa17acf14c801c220c05d2fd464f555
fetched_at: '2026-06-28T22:38:12.563550+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - FINR721 - Conceito
  e Configurações do relatório FINR721
type: support-article
updated_at: '2025-02-14T11:04:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29968281466903-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-FINR721-Conceito-e-Configura%C3%A7%C3%B5es-do-relat%C3%B3rio-FINR721
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29968273525527) Tempo aproximado para leitura: **00:10:00 min****Dúvida**

Como configurar os movimentos para a geração de informações no relatório **FINR721**.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Este relatório tem como objetivo apresentar, de forma comparativa, os lançamentos rateados por **Múltiplas Naturezas** e **Centro de Custo**, considerando as dimensões **Orçamento**, **A Realizar** e **Realizado**.

**Pré-Requisito (Configurações necessárias)**

**Mapa de Natureza (As naturezas devem estar classificadas como Receita ou Despesas corretamente)**

Por se tratar de um relatório comparativo entre valores rateados, é necessária uma configuração específica dos cadastros para seu correto funcionamento.

A primeira exigência é um **cadastro estruturado de Naturezas**, onde as naturezas estejam corretamente ordenadas dentro de seus respectivos grupos de **Despesa** e **Receita**, conforme suas finalidades. Além disso, as naturezas de **Entrada** e **Saída** devem ser cadastradas de forma sequencial.

**Exemplo:**

* **Naturezas de Entrada:** 01 a 05
* **Naturezas de Saída:** 06 a 10"

**Observação:** Este cadastro será necessário no momento do preenchimento das perguntas **01, 02, 03 e 04** do relatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29968273528599)

**Orçamentos (Os orçamentos devem estar cadastrados e rateados por centro de custo mensalmente)**

Para que os **Orçamentos** sejam considerados, além do orçamento por **Natureza**, é necessário informar o **rateio por Centro de Custo**. Isso determina quanto do orçamento da **Natureza** será destinado a cada **Centro de Custo**.

**Observação:** Para cadastrar o orçamento, acesse a rotina **FINA020**. Após preencher os campos correspondentes aos períodos cadastrados, posicione-se no mês desejado para o rateio e clique em **Outras Ações > Rateio**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29968281450263)

**Registros A Realizar**

Somente são consideradas as inclusões de títulos com **Múltiplas Naturezas por Centro de Custo**.

Dessa forma, ao incluir um título **A Receber** ou **A Pagar**, o campo **Mult.Natureza** deve ser preenchido

com **"1 - Sim"**. Além disso, na tela de **Rateio**, a opção **Rat.C.Custo** também deve ser marcada como **"Sim.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29968281453079)**

Para que o campo **Múltiplas Naturezas** esteja disponível, é necessário habilitar os seguintes parâmetros no **Configurador**:

* **MV\_MULNATP**
* **MV\_MULNATR**

**Registros Realizados.**

No momento da **baixa do título**, a opção **"Múltiplas Naturezas"** deve ser selecionada para que a tela de distribuição do **Rateio** seja exibida. Essa distribuição será registrada nas tabelas correspondentes e, posteriormente, apresentada no relatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29968273533463)

### **Parâmetros para Impressão do Relatório**

#### **- Naturezas de Entrada e Saída**

As **naturezas de Entrada (Receita)** e **Saída (Despesa)** devem ser preenchidas corretamente, seguindo a ordem e classificação adequada.

**Exemplo:**

* **Natureza de Entrada:** 01 a 05
* **Natureza de Saída:** 06 a 10

#### **- Considera Regime**

* **Caixa:** O relatório utilizará o campo **E5\_DATA** para apresentar os registros realizados.
* **Competência:** O relatório considerará o campo **E5\_DTDIGIT** para apresentar os registros dentro do período informado.

#### **- Moeda**

Define a moeda dos registros de **Contas a Receber**, **Contas a Pagar** e **Orçamentos** que serão considerados no relatório.

#### **- Imprime Acumulados**

* **Sim:** Acumula os valores dos orçamentos de todo o ano até o mês analisado.
* **Não:** Considera apenas o saldo do mês vigente.

#### **- Data de Referência**

Define o mês a ser considerado no relatório.

#### **- Outras Moedas**

Indica se os valores devem ser convertidos em caso de múltiplas moedas.

#### **- Considera Provisórios**

Define se os títulos do tipo **"PR – Provisórios"** serão incluídos no relatório.

#### **- Do Centro de Custo Até o Centro de Custo**

Especifica a sequência dos **Centros de Custo** que deverão ser considerados.

#### **- Seleciona Situações de Cobrança?**

* **Sim:** Permite selecionar quais situações de cobrança dos títulos serão consideradas na emissão do relatório.
* **Não:** Todas as situações de cobrança serão incluídas no relatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29968281455255)

**As tabelas que serão consultadas pelo FINR721.**  
  
SE1 – Contas a Receber

SE2 – Contas a Pagar

SE5 – Movimentação Bancária

SED – Naturezas

CTT – Centros de Custo

SEF - Cheques

SEZ – Distribuição das Naturezas em Centros de Custo

SEW – Rateio para Orçamentos

SA6 – Bancos

**Saiba mais**

**[Conceito e Configurações FINR721](https://tdn.totvs.com/display/public/PROT/FIN0031_CREL_Configuracoes_FINR721)**

**[Como utilizar rateio de múltiplas naturezas por Centro de Custo](https://tdn.totvs.com/pages/releaseview.action?pageId=229147656)**

**[Integração de Rateio por Centro Custo com o módulo Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=659589143#tabs-passo05)**
