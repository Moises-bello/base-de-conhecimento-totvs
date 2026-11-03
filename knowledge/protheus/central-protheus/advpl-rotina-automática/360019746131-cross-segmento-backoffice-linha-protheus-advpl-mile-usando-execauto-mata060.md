---
article_id: 360019746131
category: ADVPL - Rotina Automática
content_hash: 0be1ef9b45ddc22790c8cee6530aae1e6e02115d86f6996c6a55e9f3410e8b00
fetched_at: '2026-06-28T22:40:24.139542+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ADVPL - MILE USANDO EXECAUTO
  MATA060 '
type: support-article
updated_at: '2021-12-29T18:58:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019746131-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-MILE-USANDO-EXECAUTO-MATA060
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**MILE USANDO EXECAUTO MATA060 ou MATA061?

**Ambiente**Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**A rotina correta é MSExecauto MATA060

Segue exemplo de Layout

* Defina Layout, Descrição, Tipo Adpter, Adpter (Rotina), Tabela Principal e ordem

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015338451/mceclip2.png)

* Na formatação pode ser definido ponto de virgula ou Pipe para definir o Arquivo TXT.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015338571/mceclip3.png)

* Na seção adatptes de Rotina Automatica defina a MSExecauto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015289212/mceclip4.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015338691/mceclip5.png)

* Na seção Canais é necessário nomear um Canal e referencia a Tabela Master ou Detail.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015338751/mceclip6.png)

* Defina os campos que identificara o arquivo TXT.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015339491/mceclip0.png)

* Layout do arquivo TXT conforme exemplo ( |PROD00000000000|UNIAO |00|)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015290452/mceclip0.png)

**Saiba Mais**

* [MILE - Model Integrator Layout Engine](MILE+-+Model+Integrator+Layout+Engine)
