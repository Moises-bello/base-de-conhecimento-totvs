---
article_id: 360058825654
category: RH - Soluções para error.log
content_hash: aecdb2edcb153da12f130ea826ecdcfdeed9255f11bc635e25f8bf79fb64732c
fetched_at: '2026-06-28T22:44:09.991683+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - MDT - Erro ao tentar alterar o campo TN0_CODFAS: invalid
  macro source (SSLex0105e: Invalid token, Line 1, Offset 43, ?):({ || Posicione("TLZ",1,xFilial("TLZ")+TLM?TLM_SUBFAS,"TLZ_DESCRI")
  }) on FWLOOKUP:BUILDCOLUMN(FWLOOKUP.PRW) '
type: support-article
updated_at: '2021-07-01T19:42:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058825654-RH-Linha-Protheus-MDT-Erro-ao-tentar-alterar-o-campo-TN0-CODFAS-invalid-macro-source-SSLex0105e-Invalid-token-Line-1-Offset-43-Posicione-TLZ-1-xFilial-TLZ-TLM-TLM-SUBFAS-TLZ-DESCRI-on-FWLOOKUP-BUILDCOLUMN-FWLOOKUP-PRW
---

**Ocorrência**Ao realizar um **Cadastro de Riscos**, na rotina **MDTA180**, ao tentar alterar o campo "**Fase da Obra**" (**TN0\_CODFAS**) é gerado o *error log*: *"****invalid macro source* (SSLex0105e: *Invalid token, Line* 1, *Offset* 43, ?):({ || *Posicione*("TLZ",1,xFilial("TLZ")+TLM?TLM\_SUBFAS,"TLZ\_DESCRI") }) on FWLOOKUP:BUILDCOLUMN(FWLOOKUP.PRW)**"  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre devido a consulta padrão do campo estar incorreta  
  
**Solução**Realize o ajuste conforme passo-a-passo abaixo:  
**No configurador****1.** Em **Base de Dados / Dicionário / Base de Dados,** selecionar a opção **Consultas Padrão**.  
**2.** Através da Lupa de Pesquisa, buscar pela consulta **TLP001**.  
**3.** Selecionar a opção **Editar;****4.** Clicar em **Avançar:** ![](https://tdn.totvs.com/download/attachments/577181358/image2020-12-8_16-14-56.png?version=1&modificationDate=1607458030667&api=v2)  
  
**5.** Clicar em **Avançar:**![](https://tdn.totvs.com/download/attachments/577181358/image2020-12-8_16-14-46.png?version=1&modificationDate=1607458030693&api=v2)  
  
**6.** No quadro **Colunas**, selecionar o campo **Desc. Fas**e e clicar na opção **Editar Coluna** para alterar o conteúdo:  
![](https://tdn.totvs.com/download/attachments/577181358/image2020-12-8_16-16-3.png?version=1&modificationDate=1607458030637&api=v2)  
  
**7.**Alterar o conteúdo abaixo e Confirmar:  
De: Substr(Posicione("TLZ",1,xFilial("TLZ")+TLM->TLM\_FASE,"TLZ\_DESCRI"),1,20)    
Para: **Posicione("TLZ",1,xFilial("TLZ")+TLM->TLM\_FASE,"TLZ\_DESCRI")**![](https://tdn.totvs.com/download/attachments/577181358/image2020-12-8_16-19-7.png?version=1&modificationDate=1607458030600&api=v2)  
  
**8.** Ainda no quadro Colunas, selecionar o campo Desc. **Sub-Fase** e clicar na opção **Editar Coluna** para   
alterar o conteúdo:  
![](https://tdn.totvs.com/download/attachments/577181358/image2020-12-8_16-54-28.png?version=1&modificationDate=1607458030573&api=v2)  
  
**9.**Alterar o conteúdo abaixo e Confirmar:  
De: Substr(Posicione("TLZ",1,xFilial("TLZ")+TLM->TLM\_SUBFAS,"TLZ\_DESCRI"),1,20)  
Para: **Posicione("TLZ",1,xFilial("TLZ")+TLM->TLM\_SUBFAS,"TLZ\_DESCRI")**![](https://tdn.totvs.com/download/thumbnails/577181358/image2020-12-8_17-3-24.png?version=1&modificationDate=1607458030543&api=v2)  
  
**10.**Selecionar a opção **Avançar**![](https://tdn.totvs.com/download/attachments/577181358/image2020-12-8_17-3-49.png?version=1&modificationDate=1607458030513&api=v2)  
  
**11.**Selecionar a opção **Finalizar:**![](https://tdn.totvs.com/download/attachments/577181358/image2020-12-8_17-4-15.png?version=1&modificationDate=1607458030457&api=v2)  
  
**12.**Repetir o procedimento acima para a consulta **TLP002** com o campo **Desc. Sub-Fase:**De: Substr(Posicione("TLZ",1,xFilial("TLZ")+TLM->TLM\_SUBFAS,"TLZ\_DESCRI"),1,20)  
Para: **Posicione("TLZ",1,xFilial("TLZ")+TLM->TLM\_SUBFAS,"TLZ\_DESCRI")  
  
Saiba mais**Acumulado MDT: <https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/mdt>  
Pacote Acumulado do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>
