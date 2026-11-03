---
article_id: 360051704414
category: ADVPL - Ponto de Entrada
content_hash: c401fe23f7b56ad1b87998bfa56ca43bc9712c2becc926df108a6b127e1002fb
fetched_at: '2026-06-28T22:40:11.852492+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MA330TRB:Recalculo não acata nova ordenação
type: support-article
updated_at: '2021-05-24T18:19:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051704414-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MA330TRB-Recalculo-n%C3%A3o-acata-nova-ordena%C3%A7%C3%A3o
---

**Dúvida**Por que a rotina MATA330 não acata a nova ordenação feita no PE MA330TRB para RE4/DE4?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão P12  
  
**Solução**O ponto de entrada **MA330TRB** permitir a modificação da ordenação das movimentações, não é qualquer tipo de mudança que pode ser realizada através desse processo. Para movimentações **RE4/DE4**, sempre deve ser respeitada a ordem entre esses movimentos, não sendo permitido que um movimento **DE4** seja posicionado antes do movimento **RE4** que o original.  
  
Mais detalhes podem ser obtidos nesta página do **TDN**:  
[**Como é feita a ordenação padrão das movimentações de transferência (RE4/DE4) e desmontagens (RE7/DE7)?**](https://tdn.totvs.com/pages/releaseview.action?pageId=285642207)

Destaque para o trecho abaixo:  
"**3) Uso do PE MA330TRB para puxar os movimentos RE4/DE4 e RE7/DE7 para uma sequência menor: lembrando que isto deve ser feito considerando o conjunto de movimentos, origem e destino(s). A de se observar que, com isto, a saída da origem pode cair em uma sequência de entrada no produto/local origem.**"

**Saiba Mais**[MA330TRB - Manipulação deste arquivo antes do processamento](https://tdn.totvs.com/pages/releaseview.action?pageId=6087642)
