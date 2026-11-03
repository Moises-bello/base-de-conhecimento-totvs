---
article_id: 9162954029591
category: Financeiro - Contabilização
content_hash: 420f9c9475decc231a59a05396e5205eb326a5163ee7810eeb64df6088add747
fetched_at: '2026-06-28T22:38:05.539287+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN- CTBAFIN - Foi encontrado
  um registro no arquivo SE5 que não possui Correspondência.
type: support-article
updated_at: '2024-08-26T21:09:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9162954029591-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Foi-encontrado-um-registro-no-arquivo-SE5-que-n%C3%A3o-possui-Correspond%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24344070619287) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**No módulo Financeiro, ao realizar a contabilização off-line pela rotina CTBAFIN, aparece a mensagem abaixo:  
![mensagem_Ctbafin_n_o_encontrado.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9162874562839)**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro (SIGAFIN) - Todas as versões  
  
**Causa**Esta mensagem poderá ser apresentada quando se efetua a tentativa de contabilização de registros que possuem contabilizações exclusivamente online, após a limpeza do flag contábil, por exemplo ( E5\_LA), visto que poderão ter alterações nas tabelas de movimentos bancários (SE5) após a exclusão, como por  exemplo os casos dos adiantamentos do contas a pagar (PA) ou do contas a receber (RA), onde após a exclusão ou estorno, os títulos tem os campos chaves limpos para evitar duplicidade de movimentos, sendo a mensagem mostrada pois realmente não há referência nas tabelas de contas a pagar ou receber, já que não há campos para rastreamento.

**Exemplo:**  
![mensagem_Ctbafin_n_o_encontrado-se5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9163059305623)  
  
**Solução**Ao invés de limpeza do flag manual, poderá ser efetuada a exclusão do lote contábil. No caso de customizações para limpeza do flag contábil, filtrar os documentos que não podem os campos chaves preenchidos como no exemplo da imagem acima.
