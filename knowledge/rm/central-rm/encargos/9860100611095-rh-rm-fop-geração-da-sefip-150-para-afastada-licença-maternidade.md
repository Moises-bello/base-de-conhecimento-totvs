---
article_id: 9860100611095
category: Encargos
content_hash: ac33617f34ce2c09254e3efc053bf952ee2db4f19cb63d3aec4a759c9ecfadb6
fetched_at: '2026-06-28T22:46:52.412525+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração da SEFIP 150 para afastada licença maternidade
type: support-article
updated_at: '2025-03-11T10:46:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9860100611095-RH-RM-FOP-Gera%C3%A7%C3%A3o-da-SEFIP-150-para-afastada-licen%C3%A7a-maternidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como gerar a SEFIP para afastadas de licença maternidade no tomador de serviço, Sefip 150?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**Para que as informações da afastada por licença maternidade sejam levadas no tomador que está alocado, para o SEFIP é necessário verificar, o tomador não poderá ter CEI e a mesma não é levada no SEFIP 155, verifique a parametrização utilizada em Configurações | parametrizador| folha normal | tomadores de serviço:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859194836247)

Incluir na funcionária em anexos | folha de pagamento | Rateio tomador:

Caso no afastamento, não for informado o tomador será levado o do parametrizador como default:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859308111383)

Verificar no tomador se o mesmo é cessão mão de obra:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859312433175)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859349255831)

Cadastrar o afastamento da funcionária e informar o tomador que será levado:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859409123863)

Realizar o lançamento da folha:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859415862935)

Liberar flags do FGTS em encargos | SEFIP:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859453787799)

Distribuir o SEFIP:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859490141975)

Verifique na edição da distribuição do SEFIP:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859512092055)

Geração do SEFIP:

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859579755031)

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859656278295)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859578569239)

O arquivo será gerado no caminho informado:

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859755332631)

Esse arquivo será importado no validador do SEFIP:

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9859993794071)
