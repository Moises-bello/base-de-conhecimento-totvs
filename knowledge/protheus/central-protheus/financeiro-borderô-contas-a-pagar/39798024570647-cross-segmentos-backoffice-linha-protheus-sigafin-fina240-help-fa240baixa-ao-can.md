---
article_id: 39798024570647
category: 'Financeiro - Borderô contas a Pagar '
content_hash: b18afbcc8f100f515bb4b1d2e4e49e800f7402e0d7961176fb0e9a2843cb0e94
fetched_at: '2026-06-28T22:37:34.949017+00:00'
product: protheus
section_id: 35057529029143
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA240 - HELP FA240BAIXA
  ao cancelar borderô
type: support-article
updated_at: '2026-04-16T18:01:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39798024570647-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA240-HELP-FA240BAIXA-ao-cancelar-border%C3%B4
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39798024558359) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência:**  
Ao tentar realizar o cancelamento de um borderô, o sistema apresenta a mensagem HELP FA240BAIXA

![WhatsApp-Image-2026-04-16-at-10.52.10.jpeg](https://totvssuporte.zendesk.com/attachments/token/L8UR68a4VoN0k0stZ0Oxm8QdB/?name=WhatsApp-Image-2026-04-16-at-10.52.10.jpeg&lotus_request=true)  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2310  
  
**Solução**  
O HELP FA240BAIXA é exibido pois não é permitido realizar o cancelamento de um borderô que possua um ou mais títulos já baixados. Para que o cancelamento seja concluído, é obrigatório realizar previamente a remoção dos títulos vinculados ao borderô através da rotina de Manutenção de Borderôs.

Passos

1. Acesse o módulo Financeiro (SIGAFIN).
2. Vá em Atualizações / Contas a Pagar / Manutenção de Borderôs (FINA590).
3. Localize e selecione o borderô em questão.
4. Remova os títulos vinculados ao borderô que apresentam baixa.
5. Após a remoção dos títulos, prossiga com a rotina de cancelamento do borderô.

Saiba mais: [Borderô Pagamentos - FINA240 - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=236605212)
