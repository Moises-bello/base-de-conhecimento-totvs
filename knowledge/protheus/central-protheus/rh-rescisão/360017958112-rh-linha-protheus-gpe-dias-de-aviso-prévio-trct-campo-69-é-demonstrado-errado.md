---
article_id: 360017958112
category: RH - Rescisão
content_hash: 96011bfd6337f70cb00867792a08dbe8f862c67541b1603a3969a18371bc1082
fetched_at: '2026-06-28T22:43:49.682881+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Dias de Aviso Prévio TRCT (campo 69) é demonstrado
  errado
type: support-article
updated_at: '2025-07-14T19:04:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017958112-RH-Linha-Protheus-GPE-Dias-de-Aviso-Pr%C3%A9vio-TRCT-campo-69-%C3%A9-demonstrado-errado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33462315751191) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No módulo Gestão de Pessoal, os dias de **Aviso Prévio** TRCT (campo 69) é demonstrado errado quando a verba de aviso prévio é rateada ou quando as médias não são impressas separadamente no TRCT.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) – Gestão de Pessoal – A partir da versão 12.  
  
**Causa**Quando a **verba de aviso prévio é rateada** e o parâmetro **MV\_RATPROV** está com conteúdo S o sistema não carrega corretamente os dias de aviso prévio, para o campo 69 do TRCT, ou quando na impressão do TRCT a pergunta Imp.Medias Separadas? fica com Não, no TRCT o campo 69 é duplicado.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Faça o *backup* prévio;  
2. Compile o pacote IMPRESH.PRW referente a sua versão (deverá ser usado o include IMPRESH.CH anexo);   
3. Refaça o teste.

**OBS.:** O fonte IMPRESH.PRW deve ser **compilado**, nos links abaixo não há pacote a ser aplicado e sim **compilado**, no link Baixe o impresh.prw AQUI, acesse a pasta FOLHA para download do fonte.  
  
**Saiba Mais:**

**[BAIXE O IMPRESH.PRW AQUI](https://suporte.totvs.com/portal/p/10098/download#detail/947506)**[MP - ADVPL - Como compilar fontes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019132991-MP-ADVPL-Como-compilar-fontes)  
[RDMAKE e includes](https://suporte.totvs.com/portal/p/10098/download#detail/761443)

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
