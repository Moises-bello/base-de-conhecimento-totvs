---
article_id: 11269334606359
category: RH - Rescisão
content_hash: 60ca4163051f861a686aa5372ee7c08d7fdb341cee5cd45681b521748dc55a2c
fetched_at: '2026-06-28T22:43:48.395500+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE -  Por que ao confirmar cálculo de rescisão é apresentada
  mensagem: O campo Atestado de Óbito só deverá ser preenchido se o motivo de desligamento
  for igual a A'
type: support-article
updated_at: '2025-09-09T15:10:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11269334606359-RH-Linha-Protheus-GPE-Por-que-ao-confirmar-c%C3%A1lculo-de-rescis%C3%A3o-%C3%A9-apresentada-mensagem-O-campo-Atestado-de-%C3%93bito-s%C3%B3-dever%C3%A1-ser-preenchido-se-o-motivo-de-desligamento-for-igual-a-A
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34809950287767) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que ao confirmar cálculo de rescisão é apresentada mensagem: O campo Atestado de Óbito só deverá ser preenchido se o motivo de desligamento for igual a A. Selecione um tipo de rescisão que o motivo seja diferente de desligamento devido a morte.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11269135101207)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**Ao calcular rescisão por falecimento onde o motivo E-social for igual a A (definido em tabela S043 tipos de rescisão), para a mensagem não ser apresentada o campo RG\_OBITO (tabela SRG cabeçalho rescisão), deve ser configurado em propriedades como Alterar, deste modo o campo poderá ser preenchido

**Módulo SIGACFG**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11269307681431)

Pesquise pela tabela **SRG**, e escolha a opção **Campos:**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11269311605271)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11269238298519)

Após ajuste, salve a alteração no diquete em modo exclusivo no sistema, assim ao calcular a rescisão, será possível deixar o campo sem preenchimento.

Saiba mais:

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
