---
article_id: 360052612373
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 015d85868dafd9f6d7dd670f4b1fbec886bfa675c81429538af5c6016efe0e68
fetched_at: '2026-06-28T22:42:05.287847+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Preenchimento do campo 6- COD_REC no registro F600
type: support-article
updated_at: '2023-01-04T18:11:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052612373-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Preenchimento-do-campo-6-COD-REC-no-registro-F600
---

**Dúvida**Como preencher o campo COD\_REC no registro F600 ao gerar a EFD contribuições?  
  
**Ambiente**  
Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**Para carregar o código da receita no campo COD\_REC do registro F600 é necessário utilizar o Ponto de Entrada SPDF6004 .  
O ponto de entrada será executado para cada registro a ser considerado no bloco F600, permitindo que sejam definidas regras para determinar o código de receita para cada registro.  
Para definição das regras poderá ser utilizado o conteúdo do array aF600, que será passado por parâmetro para o ponto de entrada.  
Exemplo:

User function SPDF6004()

Local aF600 := ParamIxb[1]  
Local cArq := ""  
Local nRecSe5 := 0  
Local cCodRec := ""  
  
If Len(aF600) > 0  
    cArq := aF600[10]  
         If cArq == "SE5"  
               aAreaSE5 := SE5->(GetArea())  
               nRecSe5:= aF600[11]  
               DbSelectArea(cArq)  
               SE5->(dbGoto(nRecSe5))  
               If Alltrim(SE5->E5\_NATUREZ) == "NATF600" .And. Alltrim(SE5->E5\_CLIFOR)== "F600"  
                     cCodRec := "1234"  
                Else  
                     cCodRec := "9999"  
               EndIf  
               RestArea(aAreaSE5)  
         EndIf  
EndIf  
Return cCodRec

Documento técnico completo contendo orientações sobre a utilização do ponto de entrada:  
<https://tdn.totvs.com/display/public/PROT/4232725+DSERFINR-19192+DT+Ponto+de+Entrada+SPDF6004+no+bloco+F600>
