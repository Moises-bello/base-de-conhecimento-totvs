---
article_id: 360042928933
category: Financeiro - Contabilização
content_hash: 6ec13535c15695ef39e43a56b8d74d8d91a8cfb8fc034eabe63f6409c096022e
fetched_at: '2026-06-28T22:38:05.258074+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Cancelamento
  lançamento contábil
type: support-article
updated_at: '2024-08-30T14:30:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042928933-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Cancelamento-lan%C3%A7amento-cont%C3%A1bil
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26021768785943)****Tempo aproximado para leitura: ****00:03:00 min****

**Dúvida**  
Qual processo para efetuar um cancelamento do lançamento contábil?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**O correto e efetuar o cancelamento do lote contábil pelo módulo da **Contabilidade** (34), com o parâmetro **mv\_ctbapla** = a limpar os flag´s no **Financeiro**.

**Importante**  
O parâmetro **MV\_CTBAPLA** indica se o **Contabilidade Gerencial** (**SIGACTB**) limpará os flags de **Contabilizacao** (**\_LA/\_DTLANC**) ao **excluir lançamentos: 1=Não 2=Perguntar 3=Sim c/alertas 4=Sim s/ alertas.**  
Assim o cancelamento do lote contábil faz a limpeza dos campos **LA´s** e exclusão de dados das tabelas envolvidas no processo.
