---
article_id: 41304734753687
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 4a048d0989b20c4f560c0bfe8d0bddb24978361c0e187741c182664141eb532c
fetched_at: '2026-06-28T22:38:57.441342+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Transferência de produtos
  com numero de série.
type: support-article
updated_at: '2026-06-17T20:25:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41304734753687-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Transfer%C3%AAncia-de-produtos-com-numero-de-s%C3%A9rie
---

Ao transferir produtos com número de série sem informar o endereço destino, o produto não é incluído na agenda de endereçamentos no TOTVS Backoffice. Isso ocorre porque, para produtos com número de série, é necessário informar o endereço destino para evitar alterações no número serial. Contudo, a rotina permite a ausência do endereço para casos específicos onde o endereçamento não é desejado.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41304708265495) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao efetuar uma Transferência de produtos com número de série e não for informado o endereço destino, o produto não gera saldo a endereçar.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
Esse incidente ocorre quando é realizada a inclusão de uma Transferência Múltipla sem informar o endereço destino quando o produto possui controle de endereço número de série.    
  
**Solução**  
Somente para produtos com número de série, conceitualmente, durante a transferência deve ser informado o endereço destino, pois o produto não será colocado na agenda de endereçamentos (SDA - saldo a endereçar). Pois, se fosse colocado, permitiria um novo endereçamento e também a mudança do número serial.

A rotina não obriga informar um endereço destino devido a existirem negócios em que não se deseja ter endereçamento. No entanto, a recomendação para usuários que irão transferir materiais com numero de série, é informar o endereço e série destinos.

**Saiba Mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)  
[*PEST06517 - MATA261 - Transferencia de produtos com numero de série.*](https://tdn.totvs.com/pages/releaseview.action?pageId=1075954529)
