---
article_id: 20357137665815
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 61813c77c7e214412ff2e5a1b18366735417baa87f311bf2bc7d550b1b2e4714
fetched_at: '2026-06-28T22:37:56.256117+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA430 / FINA200 -
  Como funciona a gravação do registro totalizador do lote CNAB
type: support-article
updated_at: '2025-01-24T20:52:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20357137665815-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA430-FINA200-Como-funciona-a-grava%C3%A7%C3%A3o-do-registro-totalizador-do-lote-CNAB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20357137640343) Tempo aproximado para leitura: **00:10:00 min****Dúvida**  
Como funciona a gravação do registro totalizador do lote CNAB nas baixas via recepção de arquivo?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**O retorno de comunicação bancária contas a receber e pagar (FINA200/FINA430), tem como finalidade efetivar a baixa dos títulos com base no arquivo de retorno de recebimento disponibilizado pela instituição bancária. Esta rotina gera dois tipos de movimentações bancária, por **Lote**e por **Filial**  
  
O **registro único totalizador da movimentação bancária**, será gerado por **Lote** quando e somente se o parâmetro MV\_BXCNAB estiver configurado com  o conteúdo **S**, e as tabelas de cadastro de banco (SA6), saldo bancário (SE8) e movimentos (SE5) estiverem compartilhadas em **todos níveis, filial, unidade de negócio e empresa**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20357157692311)  
  
Quando não atendido **qualquer** um dos requisitos para gerar o registro totalizador da movimentação bancária por **Lote**, a rotina passará a gerar as movimentações bancária por **Filial.**Ou seja, para cada filial do arquivo de retorno de recebimento será criado um registro de movimentação bancária **VL.**

**Saiba mais**

#### **[Retorno de comunicação bancária contas a receber, gravação do registro totalizador tipo VL.](https://tdn.totvs.com/pages/viewpage.action?pageId=818452634)**
