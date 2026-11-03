---
article_id: 360020163551
category: GPE - eSocial - Carga Inicial
content_hash: 9569d9ccd6e4f23f7844d0b1df4fd6d9eef18d8680fc7b7e2df21f05eca02b8f
fetched_at: '2026-06-28T22:45:03.075670+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus -  GPE - eSocial - S-1010 - Em qual tabela fica gravado
  o código e a descrição dos campos RV_INCIRF, RV_INCFGTS, RV_INCSIND e RV_INCCP do
  eSocial
type: support-article
updated_at: '2025-03-03T20:17:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020163551-RH-Linha-Protheus-GPE-eSocial-S-1010-Em-qual-tabela-fica-gravado-o-c%C3%B3digo-e-a-descri%C3%A7%C3%A3o-dos-campos-RV-INCIRF-RV-INCFGTS-RV-INCSIND-e-RV-INCCP-do-eSocial
---

**Dúvida**Em qual tabela fica gravado o código e a descrição dos campos RV\_INCIRF, RV\_INCFGTS, RV\_INCSIND e RV\_INCCP do **eSocial**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**O código e a descrição dos campos estão gravados direto no código fonte da rotina cadastro de verbas (**GPEA040**) de acordo com a descrição que existe no leiaute do **eSocial** evento **S-1010**, por esse motivo não existe tabela no sistema onde é possível essas informações.  
  
Para ver o código e a descrição dos campos é necessário consultar o leiaute do eSocial no evento S-1010.  
Link: [Portal eSocial - Documentação](https://www.gov.br/esocial/pt-br/documentacao-tecnica)

* RV\_INCCP = tag codIncCP
* RV\_INCIRF = tag codIncIRRF
* RV\_INCFGTS = tag codIncFGTS
* RV\_INCSIND = tag codIncSIND

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
