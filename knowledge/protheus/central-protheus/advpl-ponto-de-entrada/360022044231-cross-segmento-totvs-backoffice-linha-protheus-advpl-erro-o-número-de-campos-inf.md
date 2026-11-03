---
article_id: 360022044231
category: ADVPL - Ponto de Entrada
content_hash: 773378b3d40bdd7013153ec4fc1bdf7cdacd75ac85f069adb50eb1ca705950b0
fetched_at: '2026-06-28T22:40:11.687073+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro: O número
  de campos informado no registro difere do número de campos especificado no leiaute
  do arquivo'
type: support-article
updated_at: '2021-12-29T14:33:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022044231-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-O-n%C3%BAmero-de-campos-informado-no-registro-difere-do-n%C3%BAmero-de-campos-especificado-no-leiaute-do-arquivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Hoje utilizamos o ponto de entrada SPEDRTMS mas, ao gerar o SPED ICMS/IPI ele aponta um erro "O número de campos informado no registro difere do número de campos especificado no leiaute do arquivo." Resumindo estamos envia 23 ao invés de 25. Preciso saber se á alguma atualização deste ponto para envio do Sped.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**O ponto de entrada [SPEDRTMS](http://tdn.totvs.com/pages/viewpage.action?pageId=237377883) permite a confecção do bloco D, documentos fiscais II serviço (ICMS) para os Registros: **D100**, **D110**, **D120**, **D130**, **D140**, **D150**, **D160**, **D161**, **D162** e **D190**, de forma totalmente manual, para os clientes que não utilizam o módulo Gestão de Transportes. Desta forma, seguindo o exemplo documentado, o *array* de retorno de um registro, **D100** por exemplo, ira respeitar as posições e informações customizadas no ponto, se forem informados 25 posições no *array* de retorno, também será emitido no arquivo as 25 posições pra o registro de referência.  
Segue exemplo do ponto de entrada em questão, contendo os 25 campos conforme [Guia Prático EFD](http://sped.rfb.gov.br/estatico/E4/4A860113D8DEACA0CB7E609E7BDE7419EED43E/GUIA%20PR%C3%81TICO%20EFD%20ICMS%20IPI%20-%20v.%203.01.pdf):

```
#Include 'Protheus.ch'  
  
User Function SPEDRTMS()  
  
Local aLinha := {}   
Local aRet := {}   
Local nPos := ParamIXB[1]   
Local cReg := ParamIXB[2]   
Local cAlias := ParamIXB[3]   
Local aDoc := ParamIXB[4]   
   
SA1->(dbSelectArea("SA1"))   
SA1->(dbSetOrder(1))   
SA1->(dbSeek(XFILIAL("SA1")+aDoc[3] + aDoc[4] ))// O correto é 3 e 4  
  
If cReg == 'D140'  
   
 AAdd( aLinha , "D140" ) // 01 - REG   
 AAdd( aLinha , "SA1"+SA1->(A1_FILIAL+A1_COD+A1_LOJA) ) // 02 - COD_PART_CONSG   
 AAdd( aLinha , '9999999' ) // 03 - COD_MUN_ORIG   
 AAdd( aLinha , '9999999' ) // 04 - COD_MUN_DEST   
 AAdd( aLinha , "1" ) // 05 - IND_VEIC   
 AAdd( aLinha , "") // 06 - VEIC_ID   
 AAdd( aLinha , "0") // 07 - IND_NAV   
 AAdd( aLinha , "" ) // 08 - VIAGEM   
 AAdd( aLinha , LTrim(Transform(SF2->F2_VALMERC,"@E 99999999.99")) ) // 09 - VL_FRT_LIQ   
 AAdd( aLinha , "" ) // 10 - VL_DESP_PORT   
 AAdd( aLinha , "" ) // 11 - VL_DESP_CAR_DESC   
 AAdd( aLinha , "" ) // 12 - VL_OUT   
 AAdd( aLinha , LTrim(Transform(SF2->F2_VALBRUT,"@E 99999999.99")) ) // 13 - VL_FRT_BRT   
 AAdd( aLinha , 0 ) // 14 - VL_FRT_MM   
 AAdd( aRet , aLinha)  
  
ElseIf cReg == 'D100'  
   
 SA1->(dbSetOrder(1))   
 SA1->(dbSeek(XFILIAL("SA1")+aDoc[3] + aDoc[4] ))  
   
 aAdd(aLinha, "D100") //01 REG  
 aAdd(aLinha, "0") //02 IND_OPER  
 aAdd(aLinha, "0") //03 IND_EMIT  
 aAdd(aLinha, "SA1"+SA1->(A1_FILIAL+A1_COD+A1_LOJA)) //04 COD_PART  
 aAdd(aLinha, "57") //05 COD_MOD  
 aAdd(aLinha, "05") //06 COD_SIT - Inutilizado  
 aAdd(aLinha, aDoc[2]) //07 SER  
 aAdd(aLinha, "") //08 SUB  
 aAdd(aLinha, aDoc[1]) //09 NUM_DOC  
 aAdd(aLinha, aDoc[25]) //10 CHV_CTE  
 aAdd(aLinha, aDoc[5]) //11 DT_DOC  
 aAdd(aLinha, aDoc[5]) //12 DT_A_P  
 aAdd(aLinha, 0) //13 TP_CTe  
 aAdd(aLinha, "") //14 CHV_CTe_REF  
 aAdd(aLinha, aDoc[13]) //15 VL_DOC  
 aAdd(aLinha, 0) //16 VL_DESC  
 aAdd(aLinha, "2") //17 IND_FRT  
 aAdd(aLinha, aDoc[13]) //18 VL_SERV  
 aAdd(aLinha, aDoc[13]) //19 VL_BC_ICMS  
 aAdd(aLinha, aDoc[15]) //20 vL_ICMS  
 aAdd(aLinha, 0) //21 VL_NT  
 aAdd(aLinha, "") //22 COD_INF  
 aAdd(aLinha, "") //23 COD_CTA  
 aAdd(aLinha, "") //24 COD_MUN_ORIG  
 aAdd(aLinha, "") //25 COD_MUN_DEST  
 aAdd(aRet,aLinha)  
  
EndIf  
  
Return(aRet)
```
