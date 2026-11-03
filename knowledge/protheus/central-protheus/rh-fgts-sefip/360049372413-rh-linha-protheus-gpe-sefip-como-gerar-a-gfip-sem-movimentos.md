---
article_id: 360049372413
category: RH - FGTS / SEFIP
content_hash: 06994aa105d70e50ca57b129491d0fa8a680b3c5c4ba9d1b5ce2b6587526d74f
fetched_at: '2026-06-28T22:43:41.490221+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - SEFIP - Como gerar  a GFIP sem movimentos
type: support-article
updated_at: '2025-08-19T12:18:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049372413-RH-Linha-Protheus-GPE-SEFIP-Como-gerar-a-GFIP-sem-movimentos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34187253512343) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**Como gerar a GFIP sem movimentos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução:**Para geração do **SEFIP** sem movimento deve ser lançado diretamente no **SEFIP** conforme demonstrado abaixo, pois no *layout* da Sefip não há instrução para geração de arquivo para esse tipo de movimentação, tem apenas a informação abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001902442)

Inexistindo recolhimento ao FGTS e informações à Previdência Social, o empregador/contribuinte deve transmitir pela Conectividade Social um arquivo da **SEFIP em branco** no qual foi incluído manual com indicativo de ausência de fato gerador (sem movimento), que é assinalado na tela de abertura do movimento, **para o código 115**.

O arquivo deve ser transmitido para a primeira competência da ausência de informações, dispensando-se a transmissão para as competências subsequentes até a ocorrência de fatos determinantes de  recolhimento ao FGTS e/ou fato gerador de contribuição previdenciária.

![Ausência do fato gerador SEFIP_1.png](https://tdn.totvs.com/download/attachments/190513772/Aus%C3%AAncia%20do%20fato%20gerador%20SEFIP_1.png?version=1&modificationDate=1434746584000&api=v2)

**Imagem 1** – Opção da SEFIP para ser marcada quando existir a inexistência do movimento.

**Saiba mais**:   
[FGTS](https://tdn.totvs.com/display/public/PROT/FGTS)

[RH - FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
