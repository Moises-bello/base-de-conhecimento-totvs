---
article_id: 27276310526231
category: Financeiro
content_hash: 9387102e0a99fb859c2ad9a9480582b280fc4605800af45c1663a1e767d27fd4
fetched_at: '2026-06-28T22:38:03.045808+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA474 - Conciliação
  Automática com data diferente configurada do arquivo
type: support-article
updated_at: '2024-10-23T19:39:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27276310526231-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA474-Concilia%C3%A7%C3%A3o-Autom%C3%A1tica-com-data-diferente-configurada-do-arquivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27276301302807) Tempo aproximado para leitura: **00****:03:00 min** **Dúvida**Porque a conciliação automática está trazendo data diferente da configurada no arquivo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da 12.1.2310  
  
**Solução**Neste caso deve validar a configuração deste banco na rotina **FINA130** no campo **EE\_TIPODAT**, para a data que está no arquivo, por exemplo, arquivo a data é **dd/mm/aaaa**, então tenho que configurar o **formato 4** igualmente ao print a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27276301304215)

**Saiba mais:**

[FINA474 - Manutenção de Extratos Bancários](https://tdn.totvs.com/pages/releaseview.action?pageId=721003882)

[FINA130 - Parâmetros de Bancos](https://tdn.totvs.com/pages/releaseview.action?pageId=624116777)
