---
article_id: 12246928502167
category: Materiais - Compras (SIGACOM)
content_hash: 3f799ec692e641f8748efedc2c119502178a0474966de89092f00a6849dc2d43
fetched_at: '2026-06-28T22:41:11.704221+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Por que as informações
  referentes ao Frete no Pedido de Compras não aparecem na Prenota ou no Documento
  de Entrada ?
type: support-article
updated_at: '2023-02-07T19:34:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12246928502167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Por-que-as-informa%C3%A7%C3%B5es-referentes-ao-Frete-no-Pedido-de-Compras-n%C3%A3o-aparecem-na-Prenota-ou-no-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que as informações referentes ao Frete no Pedido de Compras não aparecem na Prenota ou no Documento de Entrada ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**Para que as informações referentes ao Frete, inclusas no Pedido de Compras, sejam importadas para as rotinas de Prenota / Documento de Entrada, é preciso habilitar o parâmetro MV\_VALFRET.

.F. = Não desabilita validação do sistema (campo F1\_FRETE fica bloqueado quando o Pedido for vinculado a Prenota / Nota de Entrada).  
.T. = Desabilita validação e permite alterar o conteúdo do campo TIPO FRETE (F1\_TPFRETE). 

Caso seja necessário criar o parâmetro, seguir o passo a passo:

1 - No Configurador (SIGACFG) acesse Ambientes / Cadastros / Parâmetros.

![fig1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12246728770711)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
