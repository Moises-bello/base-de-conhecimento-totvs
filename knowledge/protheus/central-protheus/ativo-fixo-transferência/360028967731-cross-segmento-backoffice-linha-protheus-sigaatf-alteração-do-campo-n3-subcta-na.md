---
article_id: 360028967731
category: Ativo Fixo - Transferência
content_hash: e91a5552bc7b6d3f403022369efc480a0ffa679714abd3db4842f0484d70f479
fetched_at: '2026-06-28T22:41:52.130164+00:00'
product: protheus
section_id: 1500001536061
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ALTERAÇÃO DO CAMPO N3_SUBCTA
  NA TRANSFERÊNCIA
type: support-article
updated_at: '2021-11-17T19:50:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028967731-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ALTERA%C3%87%C3%83O-DO-CAMPO-N3-SUBCTA-NA-TRANSFER%C3%8ANCIA
---

**Ocorrência**Na transferência contábil infomando outro item de despesa, o item atual do campo N3\_SUBCTA não é substituído  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo - Todas as versões  
  
  
**Causa**Verificar como esta o parâmetro **MV\_ATFSCDP**   
  
**Solução**

os parâmetros MV\_ATFSCDP e MV\_ATFCVDP tem o objetivo de estabelecer um vínculo entre dois campos relativos a Entidades Contábeis e que possuem a mesma função dentro do módulo Ativo Fixo:

•N3\_SUBCTA - N3\_SUBCDEP: ambos se referem ao Item de Despesa de Depreciação.

•N3\_CLVL - N3\_CLVLDEP: ambos se referem à Classe de Despesa de Depreciação.

O parâmetro MV\_ATFSCDP define o conteúdo dos campos N3\_SUBCTA e N3\_SUBCDEP e pode ser configurado com:• T = o conteúdo será o mesmo para ambos,   
ou F = o conteúdo será diferente.

O parâmetro MV\_ATFCVDP define o conteúdo dos campos N3\_CLVL e N3\_CLVLDEP e pode ser configurado com:• T = o conteúdo será o mesmo para ambos,  
ou F = o conteúdo será diferente.

Importante:O Sistema já possui tratamento semelhante para o Centro de Custo, por meio do parâmetro MV\_ATFCCDP,  
que define o conteúdo dos campos N3\_CCUSTO e N3\_CCDESP. (T = conteúdo será o mesmo para ambos ou F = conteúdo será diferente).

**Saiba Mais:**<http://tdn.totvs.com.br/pages/releaseview.action?pageId=454832787>
