---
article_id: 16595925125527
category: Escrita Fiscal - Configurador de Tributos
content_hash: a604db717b22a98e672d11cb16e8c74462413ecf22f65f60386e220b4fec6bae
fetched_at: '2026-06-28T22:39:17.413712+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como configurar
  o fundo FDI do estado PI?
type: support-article
updated_at: '2024-11-18T12:00:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16595925125527-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-configurar-o-fundo-FDI-do-estado-PI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16595886403991) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Como configurar o fundo FDI do estado PI?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Incluir na rotina FISA170 o FUNDO FDI

FISA170

![](https://totvssuporte.zendesk.com/attachments/token/cQvhWkHaMRHup1u5tUA616Wea/?name=image.png)

Perfil do Produto

![](https://totvssuporte.zendesk.com/attachments/token/4bEfpsraKKcSKNRTjPzV9oGce/?name=image.png)

O produto deve estar cadastrado no SB1

Perfil Operação  = 000050

![](https://totvssuporte.zendesk.com/attachments/token/MVKpF1ItoD4DpH27SmIsNoAE4/?name=image.png)

CFOP 5501 / 5502

Perfil de Participante

![](https://totvssuporte.zendesk.com/attachments/token/D1xoTiMakmGlisrN2kKhIIijY/?name=image.png)

Perfil origem / destino

Saídas internas = 00007

![](https://totvssuporte.zendesk.com/attachments/token/V8qL65t380de2C8pBOPMb9upk/?name=image.png)

Regra da base de calculo

000042 - FDI

![](https://totvssuporte.zendesk.com/attachments/token/TBn3ZVo5Aasja3jbCkm414Ryf/?name=image.png)

Nesse exemplo usei o valor da mercadoria se precisar que seja o valor contábil somente escolher essa opção.

Regra da Alíquota

![](https://totvssuporte.zendesk.com/attachments/token/doKLwKruW8VHIHujSg17GoJWj/?name=image.png)

Regra de escrituração

![](https://totvssuporte.zendesk.com/attachments/token/OX18zx3R9Jvl8nqLmunAs0Juc/?name=image.png)

Regra da escrituração documento

![](https://totvssuporte.zendesk.com/attachments/token/ZeAzYwIaIF8iKcNdW6igh2VFH/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/gvskazqU8KXfGY0oGHA2wFfl8/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/0dFI25iJRGp7Z2dkmVoUqzqFS/?name=image.png)

TES

Pode configurar os impostos que precisar.

O CFOP precisa ser o amarrado na regra

![](https://totvssuporte.zendesk.com/attachments/token/zmqxohrEjUu5KaoWIdoaVJCMw/?name=image.png)

Cod apura. conforme DECRETO DECRETO Nº 22.013, 22.013, DE 24 DE ABRIL DE 2023, amarrado no TES

Reflexo

![](https://totvssuporte.zendesk.com/attachments/token/23t51e9Hxwhd30zX0jPRTVnyg/?name=image.png)

Pedido de Saídas

MV\_ESTADO = PI

Cliente = PI

![](https://totvssuporte.zendesk.com/attachments/token/g4mYziafuSe0ADERs8wTIFlE3/?name=image.png)

Lançamento da apuração

![](https://totvssuporte.zendesk.com/attachments/token/sbYXNFmkWceZWQGOmrvNNhVyO/?name=image.png)

Apuração do ICMS

![](https://totvssuporte.zendesk.com/attachments/token/e8Nb5zCXzve3zVkEfhthOjxW2/?name=image.png)

A GNRE será gerada no final da apuração do ICMS
