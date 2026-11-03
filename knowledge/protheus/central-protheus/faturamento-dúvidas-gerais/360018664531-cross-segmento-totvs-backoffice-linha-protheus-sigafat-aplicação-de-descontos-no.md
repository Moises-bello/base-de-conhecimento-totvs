---
article_id: 360018664531
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 83a38182565758e232094157b4fb811e53c25de125832e94ecb7ff665f9c0719
fetched_at: '2026-06-28T22:38:28.499003+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Aplicação de
  descontos no Faturamento (SIGAFAT)
type: support-article
updated_at: '2022-12-12T14:47:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018664531-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Aplica%C3%A7%C3%A3o-de-descontos-no-Faturamento-SIGAFAT
---

**Dúvida**

Como é aplicado o desconto do Faturamento?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Veja nosso vídeo How To sobre o processo: [How To | MP - SIGAFAT - Arredondamento dos descontos](https://youtu.be/LBp4RszLjLE)  
  
O desconto é aplicado da seguinte maneira:

O valor calculado está relacionado ao desconto proporcional por quantidade ou seja , o valor do desconto é dividido pela quantidade do produto conforme abaixo :

Valor total : 709,83

Desconto : 9,83

Quantidade : 49,50

9,83 / 49,50 = 0,19

Valor do desconto: 0,19

Recalculo efetuado

Valor original do produto : 14,34

Desconto: 0,19

14,34 – 0,19 = 14,15

Valor do produto já calculado com o desconto por item = 14,15

14,15 \* 49,50 ( quantidade ) = 700,42

709,83 – 700,42 = 9,41

Solução encontrada para o calculo

Ao calcular o valor do desconto, é encontrado o valor = 0,19858585858585858585858585858586

Aumentando o tamanho das casas decimais do campo “valor do desconto” para “5”, chegamos no valor : 14,34 – 0,19858 = 14,14142 \* 49,50 ( quantidade ) = 700,00029

Ao truncar o valor com duas casas decimais = 700,00

**Saiba mais:** [Arredondamento no desconto do Pedido de Venda / Orçamento de Venda](https://tdn.totvs.com/x/aNVZE)
