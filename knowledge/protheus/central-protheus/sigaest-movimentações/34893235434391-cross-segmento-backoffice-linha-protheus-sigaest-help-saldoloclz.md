---
article_id: 34893235434391
category: SIGAEST - MOVIMENTAÇÕES
content_hash: d8f109342c6fe02bdc648513a9c845bc14bebe935667cbaf0ec3de78b3f8f436
fetched_at: '2026-06-28T22:38:55.597395+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP SALDOLOCLZ
type: support-article
updated_at: '2025-09-12T14:00:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34893235434391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-SALDOLOCLZ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34893275445399) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao tentar efetuar um movimento interno, ou baixa de CQ ocore o HELP SALDOLOCLZ

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34893275445911)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
Falta de saldo disponivel no endereço ou local em questão  
  
**Solução**

* Validar se o parametro **MV\_LOCALIZ** esteja ativo.
* Validar se por acaso usa controle de de WMS (**MV\_WMSNEW**) Se acaso voce possui integração com o WMS, e validou que os dados seguintes estejam corretos, sera necessario validar junto ao time Protheus WMS, pois o controle de endereço são em tabelas distintas do estoque.
* Conferir a existencia de saldo disponivel no endereço na tabela **SBF/SB2**  
  Conferir se o tamanho de campos das tabelas **SB2/SBF/SD3** referente aos campos **B2\_QATU/BF\_QUANT/D3\_QUANT** devem possuir exatamente o mesmo tamanho e picures na tabela **SX3**.
* Certificar se existe desbalanceamento de saldos, com uso do relatorio MATR282 : [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR282 - Parametrização para validar divergência de saldos SB2 x SB8 x SBF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-validar-diverg%C3%AAncia-de-saldos-SB2-x-SB8-x-SBF)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações de Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
