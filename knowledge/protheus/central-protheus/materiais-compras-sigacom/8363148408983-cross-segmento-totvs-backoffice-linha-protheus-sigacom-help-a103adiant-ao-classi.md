---
article_id: 8363148408983
category: Materiais - Compras (SIGACOM)
content_hash: 2dabc284f6f56c23a15ac5656ac84b80b118355d2027239fc0f322b0aca48c49
fetched_at: '2026-06-28T22:41:11.647342+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Help A103ADIANT
  ao Classificar um Documento de Entrada
type: support-article
updated_at: '2023-07-21T13:26:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8363148408983-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Help-A103ADIANT-ao-Classificar-um-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15992801442839) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao classificar um Documento de Entrada é apresentado o Help A103ADIANT

![imagem2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8362811299223)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12

**Causa**

O sistema tem uma validação onde a  Data de emissão do Pedido de Compras não Pode ser maior que a Data Base que logou no sistema.

 SC7->C7\_EMISSAO > dDataBase

**Solução**Para que seja possível classificar o Documento de Entrada, é preciso que a Data Base do Sistema seja maior que a Data de Emissão do Pedido.

Exemplo Data Base do sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16191730216599)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16191703519767)

Obs:A Data de Emissão da Nota da nota fiscal Não é validada nesse help, o sistema valida apenas a Data que Logou no sistema.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
