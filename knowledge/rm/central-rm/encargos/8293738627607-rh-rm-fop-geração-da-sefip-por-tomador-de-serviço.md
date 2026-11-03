---
article_id: 8293738627607
category: Encargos
content_hash: a8b0e822207295458b59a9fc4cc93b0b9c09f9caf1eb8b9360a5e433974a2a37
fetched_at: '2026-06-28T22:46:52.453721+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração da SEFIP por tomador de serviço
type: support-article
updated_at: '2024-10-11T19:53:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8293738627607-RH-RM-FOP-Gera%C3%A7%C3%A3o-da-SEFIP-por-tomador-de-servi%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como gerar a SEFIP para tomador de serviço, Sefip 150?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**Verificar se o sistema está parametrizado para utilizar tomador de serviço em: **Configurações Parametrizador| Folha Normal | Tomador de Serviços:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8768343845527/mceclip1.png)

Esse tomador informado no parametrizador será o administrativo.

No funcionário informar em Histórico | rateio de tomador, o tomador do funcionário:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8768515929879/mceclip2.png)

Feito isso distribua a SEFIP em **Encargos | Sefip | Distribuir SEFIP**:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8768575830551/mceclip3.png)

Poderá verificar a distribuição em **Encargos | Sefip | Edição do movimento** se foi distribuído corretamente:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8768703254679/mceclip4.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8768719528471/mceclip5.png)

**Importante**

Para que seja considerado o tomador do cadastro do funcionário no rateio de tomadores, todos os eventos devem possuir a flag **Segue rateio de tomadores marcado.** Pois caso contrario, será considerado o tomador do parametrizador.

![](https://totvssuporte.zendesk.com/attachments/token/6qj14jpTaUQDoUQzwNrUdjR1w/?name=image.png)

Gerar o SEFIP com o código de recolhimento necessário:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8768776013591/mceclip6.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8768802767895/mceclip7.png)

Dessa forma será gerado e poderá importar o arquivo do SEFIP no validador:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8768855675799/mceclip8.png)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8293511290775/mceclip8.png)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8769245937559/mceclip9.png)

**Saiba mais**  
[Geração de SEFIP com tomadores de serviço.](https://tdn.totvs.com/pages/releaseview.action?pageId=146182119)
