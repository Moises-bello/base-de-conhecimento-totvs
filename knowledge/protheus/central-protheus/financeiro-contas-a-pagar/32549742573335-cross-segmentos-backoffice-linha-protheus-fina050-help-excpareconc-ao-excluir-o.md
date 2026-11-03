---
article_id: 32549742573335
category: Financeiro - Contas a Pagar
content_hash: 9f445ac8dab75208ac539d6611c92684ea67d835847229c8939d28779d07eeb1
fetched_at: '2026-06-28T22:38:07.032107+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA050 - HELP EXCPARECONC ao  excluir
  o PA
type: support-article
updated_at: '2025-09-18T13:55:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32549742573335-Cross-Segmentos-Backoffice-Linha-Protheus-FINA050-HELP-EXCPARECONC-ao-excluir-o-PA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32549742560407) Tempo aproximado para leitura: **00:05 min** **Dúvida**

HELP EXCPARECONC ao excluir o PA, o que fazer?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - a partir da release 12.1.2210  
  
**Solução**

O erro ocorre devido à configuração do parâmetro MV\_BXCONC com o valor "2", o qual impede a exclusão do pagamento antecipado (PA) quando o título está conciliado. Para viabilizar o cancelamento, é necessário desfazer primeiramente a conciliação (cancelar o match).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32549742560791)

Para cancelar a conciliação, basta localizar o registro, sobre o título, clicar nos três pontos e selecionar a opção Cancelar Match.

![Gravar_2025_06_02_17_54_29_616.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32549789107607)

**Saiba mais**

[Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Cancelar Conciliação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28945869513879-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Cancelar-Concilia%C3%A7%C3%A3o)
