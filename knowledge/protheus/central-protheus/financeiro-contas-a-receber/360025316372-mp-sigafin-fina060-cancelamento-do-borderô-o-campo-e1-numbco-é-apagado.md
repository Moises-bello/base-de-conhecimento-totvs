---
article_id: 360025316372
category: Financeiro - Contas a Receber
content_hash: 282d9942779d33cf9ab557d946edeea01b3db631d1b2346b8d29a154932d0e04
fetched_at: '2026-06-28T22:38:12.667967+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - FINA060 - Cancelamento do borderô o campo E1_NUMBCO é apagado
type: support-article
updated_at: '2025-11-11T18:27:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025316372-MP-SIGAFIN-FINA060-Cancelamento-do-border%C3%B4-o-campo-E1-NUMBCO-%C3%A9-apagado
---

**Dúvida**Ao cancelar um borderô é excluído o conteúdo do campo E1\_NUMBCO  
  
**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12.1.17  
  
**Solução**O campo **E1\_NUMBCO** grava o **nosso número** do boleto.  
Ao cancelar um borderô entende-se que o mesmo não será mais cobrado pelo banco e o campo E1\_NUMBCO é apagado, para ser criado um novo borderô e uma nova remessa ser realizada com aquele título.  
Porém, existem os pontos de entrada abaixo que podem atender sua necessidade, desde que não apague o campo no cancelamento do borderô.  
  
**FA60CAN1 -**Estorno de borderô do contas a receber  
O ponto de entrada **FA60CAN1** será executado antes da gravação do **SE1** no estorno do borderô do contas a receber.  
  
**FA60CAN2 -**Gravação de **SE1** no estorno do borderô  
O ponto de entrada será executado após gravar o **SE1** (restauração) no estorno do borderô. Este ponto pode ser usado para gravar dados como a caixa portadora origem no **SE1** no estorno, para isto a caixa portadora origem deveria ter sido guardada no **SEA** em campos de usuário (pode ser usado o ponto **Fa60BDE** para isto).

**Saiba mais**

**FA60CAN1**  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6071246>

**FA60CAN2**<http://tdn.totvs.com/pages/releaseview.action?pageId=6071247>
