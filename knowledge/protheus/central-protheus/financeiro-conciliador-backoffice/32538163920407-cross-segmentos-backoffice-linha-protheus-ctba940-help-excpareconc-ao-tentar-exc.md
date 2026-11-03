---
article_id: 32538163920407
category: Financeiro - Conciliador Backoffice
content_hash: 8c0764269ee65e604d76a35121fa1448332caae06942e371bc6215958d1b1c72
fetched_at: '2026-06-28T22:37:47.097636+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - CTBA940 - HELP: EXCPARECONC
  ao tentar excluir PA'
type: support-article
updated_at: '2025-06-02T21:02:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32538163920407-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-HELP-EXCPARECONC-ao-tentar-excluir-PA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32538163910551) Tempo aproximado para leitura: **00:05 min** **Dúvida**Ao excluir o PA é apresentado o HELP: EXCPARECONC, o que fazer?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – Todas as versões  
  
**Solução**  
O erro ocorre devido à configuração do parâmetro `MV_BXCONC` com o valor "2", o qual impede a exclusão do pagamento antecipado (PA) quando o título está conciliado. Para viabilizar o cancelamento, é necessário primeiramente desfazer a conciliação (cancelar o match).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32538149611031)

Para cancelar a conciliação, basta localizar o registro, sobre o título, clicar nos três pontos e selecionar a opção **Cancelar Match.**

![Gravar_2025_06_02_17_54_29_616.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32538163911447)

**Saiba mais**

[Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Cancelar Conciliação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28945869513879-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Cancelar-Concilia%C3%A7%C3%A3o)
