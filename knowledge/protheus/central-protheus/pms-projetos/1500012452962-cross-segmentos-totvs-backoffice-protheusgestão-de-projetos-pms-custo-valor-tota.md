---
article_id: 1500012452962
category: PMS - Projetos
content_hash: 47deb43a688c69166dfb4bdab77a23cd0dc35c277d32d0c8be55c783d7ef2de1
fetched_at: '2026-06-28T22:37:14.981690+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos/ Totvs BackOffice Protheus/Gestão de Projetos - PMS - Custo
  - Valor Total de Pagamento
type: support-article
updated_at: '2021-05-31T18:13:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012452962-Cross-Segmentos-Totvs-BackOffice-Protheus-Gest%C3%A3o-de-Projetos-PMS-Custo-Valor-Total-de-Pagamento
---

**Dúvida**

Como é somado o Valor Total de Pagamento, na planilha do Projeto?

![pamento.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019852281/pamento.PNG)  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Projetos - Todas as versões

**Solução**

O campo Total de Pagamento é composto pela soma de todos os títulos que foram baixados com amarração no projeto,  Exemplo:

* Documento de entrada amarrado a um projeto ( **AFN**), onde a TES **Gera Duplicata = Sim** e **F4\_MOVPRJ = Despesa,**será gerado um Titulo a Pagar, assim que este **titulo** for**baixado** somará no Custo do Projeto.
* Títulos do Contas a Pagar, que foram incluídos manual e Amarrado ao Projeto através da tabela (**AFR**), não será computado no campo **Valor total de pagamentos,**somará apenas na baixa.
* Títulos de Pagamento Antecipado - Serão somado ao **Valor total de pagamentos,**no ato da inclusão. Lembrando que, devem estar amarrados ao projeto através da tabela AFR.

**Observação:**

Valores de impostos não são considerados no Custo.

Exemplo: ICMS retido no custo D1\_CUSTO não é somado no custo do projeto, apenas o valor total de pagamento. 

**Saiba mais sobre os outros Custos do Projeto: [PMS0033 - Custos do projeto na visualização em planilha do projeto](https://tdn.totvs.com/pages/viewpage.action?pageId=520666570)**

#
