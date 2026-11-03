---
article_id: 11656471494295
category: Ativo Fixo - Aquisição por Transferência
content_hash: 564bd2e14b4408929ee984e4c99cdfa5078ac134951a10198c364ee49ae300e0
fetched_at: '2026-06-28T22:41:56.951257+00:00'
product: protheus
section_id: 1500001535341
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- ATFA251 - Configuração
  Lançamento padrão 835
type: support-article
updated_at: '2023-08-31T12:31:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11656471494295-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ATFA251-Configura%C3%A7%C3%A3o-Lan%C3%A7amento-padr%C3%A3o-835
---

**Dúvida**

Exemplo de configuração do Lançamento padrão 835 para que o sistema gere o Debito para a baixa e o crédito para a Inclusão  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 12.  
   
  
**Solução**

* Configurar  duas sequencias de LPs 835 com a condicional apontando para o tipo (N4\_TIPO)ou ocorrência ([N4\_OCORR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018328552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-N4-OCORR-tipos-de-movimentos-?source=search)) da tabela SN4
* Exemplo :
* Veja que no exemplo abaixo executamos a rotina Aquisição por transferência (ATFA251)
* Selecionamos dois bens

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11656308176279)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11656371643287)

* baixando dois bens ([N4\_OCORR = 15](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018328552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-N4-OCORR-tipos-de-movimentos-?source=search) ) e gerando um novo bem ([N4\_OCORR = 16](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018328552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-N4-OCORR-tipos-de-movimentos-?source=search))

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11656231539607)

Configuração Lançamento padrão:

* Debito Baixa : [N4\_OCORR = 15 Baixa por aquisição de transferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018328552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-N4-OCORR-tipos-de-movimentos-?source=search)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11656070967447)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11656132166423)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11656136264471)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11656163992983)

* Credito Aquisição : [N4\_OCORR = 16 Aquisição por transferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018328552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-N4-OCORR-tipos-de-movimentos-?source=search)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11656175836439)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11656169831703)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11656178017559)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11656179376791)

Sistema contabiliza

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11656412236055)
