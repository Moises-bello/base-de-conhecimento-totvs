---
article_id: 1500012162102
category: Financeiro - Consultas / Relatórios
content_hash: 89e83437c2f425e4bc043aa8caeae176de1fda64727455438cf167795dadbe7c
fetched_at: '2026-06-28T22:37:58.426881+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINR721 - Correta configuração
  para que o relatório apresente dados Orçados x reais mês por centro de custo
type: support-article
updated_at: '2023-01-25T23:02:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012162102-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINR721-Correta-configura%C3%A7%C3%A3o-para-que-o-relat%C3%B3rio-apresente-dados-Or%C3%A7ados-x-reais-m%C3%AAs-por-centro-de-custo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:09:00 min  
  
Dúvida**  
Como executar a correta configuração para que o relatório apresente os dados Orçados x reais mês por centro de custo?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. As **Naturezas** devem estar classificadas como **Receita** ou **Despesas** corretamente., pois se trata de um relatório comparativo entre valores rateados. Será necessário a criação de um cadastro de **Naturezas** **SED** estruturado, (as naturezas devem ser ordenadas em grupos de **Receita** ou **Despesa**, conforme finalidade) em sequencia cadastradas como entrada e saída

**Exemplo**Natureza de Entrada :  01 a 05  
Natureza de Saída : 06 a 10

**Importante**  
Este cadastro será necessário o preenchimento das perguntas 01, 02, 03 e 04 do Relatório

![](https://tdn.totvs.com/download/attachments/244935020/image2016-8-30%2010%3A50%3A6.png?version=1&modificationDate=1472567912000&api=v2)

2. Os **Orçamentos** devem estar cadastrados e rateados por **centro de custo** mensalmente para que sejam considerados, além do **orçamento** por **natureza**, é necessário informar o **rateio** por **centro de custo**. Desse modo será definido o quanto do **orçamento** da **natureza** será destinado ao **centro de custo**

**Importante**  
Para cadastrar o **Orçamento**, acesse rotina **FINA020** e após preencher os campos correspondentes aos períodos cadastrados, posicione no mês que desejar ratear e clique em **Outras Ações > Rateio**

![](https://tdn.totvs.com/download/attachments/244935020/image2016-8-30%2010%3A56%3A18.png?version=1&modificationDate=1472567914000&api=v2)

3. A Inclusão de títulos somente será considerada no relatório se **(título Pagar** ou **Receber)** for incluído por **Múltiplas Naturezas de Centro de Custo**, selecionando a **opção 1 = Sim na guia Administrativo**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019559141/mceclip0.png)

Na tela de **Rateio**, a opção **Rat.C.Custo** deverá ser preenchida como **Sim**

![](https://tdn.totvs.com/download/attachments/244935020/image2016-8-30%2011%3A2%3A19.png?version=1&modificationDate=1472567917000&api=v2)

Para que o campo **Múltiplas Naturezas** esteja disponível, deverá ser habilitado no **Configurador** os parâmetros **MV\_MULNATP** e **MV\_MULNATR**

4. A **Baixa de títulos** somente será considerada no relatório se (**título Pagar ou Receber**) for selecionado a opção **Rateio Mul.Naturezas**, para que seja apresentado a tela de distribuição do **rateio**.

![](https://tdn.totvs.com/download/attachments/244935020/image2016-8-30%2011%3A4%3A54.png?version=1&modificationDate=1472567918000&api=v2)

Abaixo segue tabelas consultadas pelo relatório **FINR721**

**SE1** – Contas a Receber

**SE2** – Contas a Pagar

**SE5** – Movimentação Bancária

**SED** – Naturezas

**CTT** – Centros de Custo

**SEF** - Cheques

**SEZ** – Distribuição das Naturezas em Centros de Custo

**SEW** – Rateio para Orçamentos

**SA6** – Bancos
