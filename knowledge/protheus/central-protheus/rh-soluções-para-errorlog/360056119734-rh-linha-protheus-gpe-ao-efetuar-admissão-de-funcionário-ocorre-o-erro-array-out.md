---
article_id: 360056119734
category: RH - Soluções para error.log
content_hash: e1e74af98f423d9fc698c7330d36d8abec15f3b00bdc73229df9edf834d12690
fetched_at: '2026-06-28T22:44:08.735878+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao efetuar admissão de funcionário ocorre o erro:
  array out of bounds ( 0 of 9 ) on FINT2300NEW(GPEM026D.PRW)'
type: support-article
updated_at: '2025-08-22T18:01:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056119734-RH-Linha-Protheus-GPE-Ao-efetuar-admiss%C3%A3o-de-funcion%C3%A1rio-ocorre-o-erro-array-out-of-bounds-0-of-9-on-FINT2300NEW-GPEM026D-PRW
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34377470225815)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Ao efetuar admissão de um funcionário gera *error log*: ***array out of bounds* ( 0 of 9 ) *on* FINT2300NEW(GPEM026D.PRW).**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - à partir da versão 12.  
  
**Causa**Este erro ocorre devido à fontes desatualizados e campos não preenchidos corretamente.  
  
**Solução**Quando o número da **CNH** é preenchido, os outros campos passam a ser obrigatórios e a ausência de conteúdo num destes campos acaba gerando o erro log. Para correção, avalie se os campos listados abaixo estão devidamente preenchidos:  
  
   -> **Cnh Emissor**  
   -> **Cnh DtEmis**  
   -> **Cnh Dt Val**  
   -> **Cnh Categ**  
   -> **Cnh UF**Se os campos estiverem corretos e ainda persistir pode ser inconsistências no complemento cadastral do SIGATAF tabelas C1E e CR9 por favor avaliar as documentações abaixo:  
TAF - SIGATAF - Complemento cadastral (TAFA050) - Mudança da amarração de N:1 para 1:1  
[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042996074](https://www.google.com/url?q=https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042996074&sa=D&source=hangouts&ust=1598118724976000&usg=AFQjCNEBK9UBFmUeiedzEsIIpBK23Yd1Ig)     
  
TAF - SIGATAF - Complemento cadastral (TAFA050) - Amarração 1:1  
[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043508233](https://www.google.com/url?q=https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043508233&sa=D&source=hangouts&ust=1598118724976000&usg=AFQjCNH7z2iSK_nswg286GGzWrIsTUBoew)      
  
**Saiba mais:**[Pacote Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
