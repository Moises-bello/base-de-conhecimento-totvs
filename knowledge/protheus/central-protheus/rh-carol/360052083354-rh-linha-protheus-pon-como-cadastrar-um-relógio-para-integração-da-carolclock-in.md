---
article_id: 360052083354
category: RH - Carol
content_hash: fa810e3a638b771948b4729216e7d5259869fdba6c5d8a58244bc381081c0009
fetched_at: '2026-06-28T22:44:56.632204+00:00'
product: protheus
section_id: 19035556880407
source: central-protheus
title: RH - Linha Protheus - PON -  Como cadastrar um relógio para integração da Carol/Clock
  In com o Ponto Eletrônico
type: support-article
updated_at: '2024-09-09T12:39:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052083354-RH-Linha-Protheus-PON-Como-cadastrar-um-rel%C3%B3gio-para-integra%C3%A7%C3%A3o-da-Carol-Clock-In-com-o-Ponto-Eletr%C3%B4nico
---

**Dúvida**Como cadastrar um relógio para integração da Carol/Clock In com o Ponto Eletrônico?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - A partir do release 12.1.27  
  
**Solução**Acesse a rotina de **Cadastro de Relógios** do Ponto Eletrônico em **Atualizações > Cadastro do Ponto > Relógios,** e inclua um cadastro como exemplificado abaixo:  
  
1 - **Controle** (P0\_CONTROL) = "P"  // Relógio de Ponto  
2 - **Tipo Arquivo** (P0\_TIPOARQ) = "R" // Integração com Carol ou TSA  
3 - **Nome do Arquivo** (P0\_ARQUIVO) = REP (será gatilhado **automaticamente** quando o Tipo do Arquivo for preenchido)  
4 - **Rep** (P0\_REP) = "" // Se o relógio for da Carol, este campo não deve ser preenchido  
5 - **Tipo do REP** (P0\_TPREP) = aqui deverá ser preenchido com a opção **1-1510** caso as marcações estejam atreladas ao **PIS** do funcionário ou **2-REP A** caso as marcações estejam atreladas ao **CPF** do funcionário.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18921475562263)  
  
**Saiba mais**[Integração Protheus x Carol Clock In](https://tdn.totvs.com/pages/releaseview.action?pageId=515294516)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
