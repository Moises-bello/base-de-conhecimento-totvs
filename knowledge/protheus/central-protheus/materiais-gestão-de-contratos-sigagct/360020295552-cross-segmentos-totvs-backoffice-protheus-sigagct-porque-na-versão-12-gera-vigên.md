---
article_id: 360020295552
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 5ebb6a28f5291c4987ecad8fad950d5f6438f836302effb56195e79d11dabc43
fetched_at: '2026-06-28T22:37:20.123999+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Porque na Versão 12
  gera Vigência do Contrato com um dia a mais no campo de Data Final Contrato ?
type: support-article
updated_at: '2022-05-19T20:52:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020295552-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Porque-na-Vers%C3%A3o-12-gera-Vig%C3%AAncia-do-Contrato-com-um-dia-a-mais-no-campo-de-Data-Final-Contrato
---

**Dúvida**Porque na Versão 12 gera Vigência do Contrato com um dia a mais no campo de Data Final Contrato ?  
  
**Ambiente**Protheus - Gestão de Contratos -  a partir da versão 12  
  
**Solução**

O cálculo da data final do contrato de acordo com o período de vigência para a versão 11 possuía uma diferença de 1 dia entre as datas de inicio e termino do contrato. Para ajustar essa diferença sem mudar as regras existentes no sistema para todos os clientes foi disponibilizado o novo parâmetro MV\_GCTDTAN. Veja abaixo suas configurações:

**O parâmetro MV\_GCTDTAN (default .F.)**

Conteúdo igual a .F. = Quando o conteúdo for igual a .F. (False - Falso) deixa a data final do contrato com um dia a menos que data inicial.

Conteúdo igual a .T. = Quando o conteúdo for igual a .T. (True - Verdadeiro) realiza o calculo da data final do contrato com um dia a mais que sua data inicial.

***Saiba Mais:***

*[GCT0108](https://tdn.totvs.com/display/PROT/GCT0108+-+Data+Final+Contrato) [- Data Final Contrato](https://tdn.totvs.com/display/PROT/GCT0108+-+Data+Final+Contrato)*

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
