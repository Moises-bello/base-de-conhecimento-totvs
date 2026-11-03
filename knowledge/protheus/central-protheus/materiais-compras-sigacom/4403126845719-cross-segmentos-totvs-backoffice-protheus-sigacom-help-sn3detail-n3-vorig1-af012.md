---
article_id: 4403126845719
category: Materiais - Compras (SIGACOM)
content_hash: 873723239f2eff32dbf275afac4b90104adbce26afdc6a37a03ae6b22c903268
fetched_at: '2026-06-28T22:41:18.970158+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - HELP SN3DETAIL N3_VORIG1
  AF012TPNEG no Documento de Entrada - MATA103
type: support-article
updated_at: '2023-11-23T20:25:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403126845719-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-SN3DETAIL-N3-VORIG1-AF012TPNEG-no-Documento-de-Entrada-MATA103
---

**Ocorrência**Help SN3DETAIL N3\_VORIG1 AF012TPNEG sendo apresentado ao tentar fazer a classificação de um documento de entrada com ativo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403130322967)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Todas as versões  
  
**Causa**O Help é apresentado quando se está fazendo a entrada de um documento com valor negativo na rotina do MATA103 e não há configuração de parâmetro para aceitar valores negativos no Ativo Fixo.  
  
**Solução**O parâmetro MV\_N3TPNEG deve ser alimentado com os conteúdos do campo N3\_TIPO possíveis de aceitar entrada com valor negativa no Ativo Fixo:

Ex: 05 ( Tipo que no ativo fixo permite uma reavaliação negativa ). 

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403126652311)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403126656279)

Sendo assim possível fazer a classificação do documento de entrada.

***Saiba Mais :***

[MP-SIGAATF - O QUE TRATA O CAMPO N3\_TIPO?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035878114)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
