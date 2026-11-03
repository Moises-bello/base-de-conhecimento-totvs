---
article_id: 4423729638039
category: PMS - Projetos
content_hash: ecf7f81995e0f75b1512dc6260e1e950f403e82f9e7f23e007b3676f874897cf
fetched_at: '2026-06-28T22:37:15.085070+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Empenho Financeiro
  com Gestão de Projetos
type: support-article
updated_at: '2022-02-14T18:53:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4423729638039-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAPMS-Empenho-Financeiro-com-Gest%C3%A3o-de-Projetos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Como é gerado o Empenho Financeiro com o Gestão de Projetos ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Todas as Versões

**Solução**

Quando existe a integração do projetos e titulo, são controlados os custos que serão referentes aos apontamentos amarrados ao projeto como documentos de entrada, remessas, requisições, apontamentos de recursos, títulos a pagar, movimentos internos, observando a data base do sistema.  
  
**Valor total de pagamentos**

Após gerar a Nota Fiscal, com a amarração no projeto, devem ser somado a este campo Valor Total de Pagamentos. Exemplo:  
Documento de entrada amarrado a um projeto ( AFN), onde a TES Gera Duplicata = Sim eF4\_MOVPRJ = Despesa, será gerado um Titulo a Pagar, assim que este titulo for baixado somará no Custo do Projeto.   
Título do Conta a Pagar, que foram incluídos manual e Amarrado ao Projeto através da tabela (AFR), não será computado no campo Valor total de pagamentos, somará apena na baixa.  
  
Saiba mais em :  **[Cross Segmentos/ Totvs BackOffice Protheus/Gestão de Projetos - PMS - Custo Realizado/ Custo Previsto e Saldo Realizado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011502862-Cross-Segmentos-Totvs-BackOffice-Protheus-Gest%C3%A3o-de-Projetos-PMS-Custo-Realizado-Custo-Previsto-e-Saldo-Realizado?source=search)**
