---
article_id: 360021143092
category: RH - Soluções para error.log
content_hash: 8d6ac01c7796f458c0e6abdd74f569fed5091682924339816055d207cad797e6
fetched_at: '2026-06-28T22:44:08.936576+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Error log no fechamento do roteiro array out of
  bounds ( XX of XX ) on FGRAVATRANS(GPEM120.PRX) '
type: support-article
updated_at: '2022-11-09T14:50:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021143092-RH-Linha-Protheus-GPE-Error-log-no-fechamento-do-roteiro-array-out-of-bounds-XX-of-XX-on-FGRAVATRANS-GPEM120-PRX
---

**Dúvida**Na execução do **Fechamento do Roteiro** de **adiantamento** ou da **folha**, **ADI** ou **FOL**, através da rotina **GPEM120**, gera *error log:* ***array out of bounds* ( XX of XX ) *on* FGRAVATRANS(GPEM120.PRX)**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre devido a falta de campos entre as tabelas **SRC** e **RGB**  
  
**Solução**Verificar se houve inclusão de campos de usuários em ambas as tabelas **SRC** e **RGB**. Ao criar campo padrão de usuário, via Configurador na tabela RGB, é necessário que os mesmos campos sejam criados também na tabela SRC. Essas tabelas necessitam andar em conjunto para correto funcionamento da rotina. Conforme exemplo abaixo:  
![2018-12-28_13_52_00-TOTVS_Educacional__Microsiga__02.9.0099.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360017971031/2018-12-28_13_52_00-TOTVS_Educacional__Microsiga__02.9.0099.png)

**Saiba Mais**[Pacote Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Soluções para Error log](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115003853987-RH-Solu%C3%A7%C3%B5es-para-error-log)
