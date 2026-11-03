---
article_id: 5267914763287
category: RH - Rescisão
content_hash: 229761c218a1a175fa4d52de1d59687e014a44e006cd3891ad3351015ddf34e3
fetched_at: '2026-06-28T22:43:49.890366+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que não é possível editar data de demissão
  em rescisão complementar mesmo com o parâmetro MV_MDDTDEM = S
type: support-article
updated_at: '2025-04-16T18:52:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5267914763287-RH-Linha-Protheus-GPE-Por-que-n%C3%A3o-%C3%A9-poss%C3%ADvel-editar-data-de-demiss%C3%A3o-em-rescis%C3%A3o-complementar-mesmo-com-o-par%C3%A2metro-MV-MDDTDEM-S
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26570346066967) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que não é possível editar data de demissão em rescisão complementar mesmo com o parâmetro MV\_MDDTDEM = S?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Não é possível editar a data de demissão de rescisão complementar mesmo com o parâmetro MV\_MDDTDEM = S, devido o campo RG\_DATADEM estar como Visualizar em Propriedade na base de dados do Configurador:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5267868808087)

Altere via configurador SIGACFG o campo Propriedade para Alterar. Dessa forma a data de demissão poderá ser editada:![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5267900324887)

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo:

[RH - Linha Protheus - GPE - Qual a finalidade do parâmetro MV\_MDDTDEM = S](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411589885335-RH-Linha-Protheus-GPE-Qual-a-finalidade-do-par%C3%A2metro-MV-MDDTDEM-S?source=search)

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
