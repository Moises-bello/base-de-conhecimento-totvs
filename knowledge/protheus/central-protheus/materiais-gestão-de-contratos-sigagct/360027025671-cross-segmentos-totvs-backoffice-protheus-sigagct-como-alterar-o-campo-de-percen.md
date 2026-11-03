---
article_id: 360027025671
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 9cf6d30ac5f5be81d98eca271a8e97c346dd61633a9a97a5f6036d2d2b380e4c
fetched_at: '2026-06-28T22:37:19.768818+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como alterar o campo
  de percentual mínimo de caução (CN9_MINCAU) em contratos com a situação vigente
  ?
type: support-article
updated_at: '2022-05-19T20:42:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027025671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-alterar-o-campo-de-percentual-m%C3%ADnimo-de-cau%C3%A7%C3%A3o-CN9-MINCAU-em-contratos-com-a-situa%C3%A7%C3%A3o-vigente
---

**Dúvida**Como alterar o campo de percentual mínimo de caução (CN9\_MINCAU) em contratos com a situação vigente ? ( Revisão de Caução )  
  
**Ambiente**Microsiga Protheus – Gestão de Contratos – A partir da versão 12  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Habilite o parâmetro **MV\_CNRVCAU** com conteúdo .T. para que possa habilitar a revisão de caução.  
2.Cadastre o tipo da revisão de caução em cadastros>tipos>revisão rotina CNTA010. Na inclusão do cadastro selecione o Tipo E - Caução.  
3. Na rotina Manutenção CNTA300 selecione o contrato , acesse Outras Ações>Revisões>Caução observe que o campo %Caução (**CN9\_MINCAU**) foi habilitado para edição.

**Observação:** Esse Tipo de Revisão é apenas para Caução Manual.

***Saiba Mais:***

[GCT0090- Revisão de Caução](https://tdn.totvs.com/pages/releaseview.action?pageId=285661505)

[MP - SIGAGCT - Quais são os tipos de Revisão disponíveis, para revisar contratos no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034587334)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
