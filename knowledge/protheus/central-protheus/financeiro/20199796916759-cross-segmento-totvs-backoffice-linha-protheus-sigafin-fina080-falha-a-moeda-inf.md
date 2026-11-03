---
article_id: 20199796916759
category: Financeiro
content_hash: cd6578214c223f4c81b5900f28123fe3c9bf5c574e0bbb6cc38c72d8c022683d
fetched_at: '2026-06-28T22:38:01.159162+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAFIN - FINA080 - Falha:
  A moeda informada 03 esta zerada na data da baixa'
type: support-article
updated_at: '2023-12-29T19:25:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20199796916759-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Falha-A-moeda-informada-03-esta-zerada-na-data-da-baixa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20199781270551) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao tentar realizar a baixa do titulo aparece a mensagem: "A moeda informada 3 esta zerada na data da baixa"  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - FINANCEIRO - Todas as versões  
  
**Solução**Em um titulo que foi gerado em meses anteriores e que não é possível cancelar e reenviar novamente e quando é feita a tentativa de baixa ocorrer a mensagem: "A moeda informada 3 esta zerada na data da baixa" é necessário na data da baixa na moeda que estiver sendo informada colocar a cotação do dia da moeda 01 por exemplo para que o sistema entenda que não esta zera e realizar a baixa do titulo.
