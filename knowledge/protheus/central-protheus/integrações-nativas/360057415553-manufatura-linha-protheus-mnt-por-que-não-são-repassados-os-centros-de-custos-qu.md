---
article_id: 360057415553
category: Integrações Nativas
content_hash: b2baea1afcf800518a7cb4405f0fc1bb311cc80005ab30d2c8288e6d8b9da2fb
fetched_at: '2026-06-28T22:42:35.493098+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Por que não são repassados os Centros de
  Custos quando transferido Ativo Fixo pelo Manutenção de Ativos
type: support-article
updated_at: '2025-05-16T21:47:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057415553-Manufatura-Linha-Protheus-MNT-Por-que-n%C3%A3o-s%C3%A3o-repassados-os-Centros-de-Custos-quando-transferido-Ativo-Fixo-pelo-Manuten%C3%A7%C3%A3o-de-Ativos
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32166836307863)*Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Por que não são mais alterados os campo **Centros de Custos Despesa - N3\_CCUSTO**, **Centro de Custo Corr. Depr. - N3\_CCCORR**, **Centro de Custo Desp. Depr. - N3\_CCDESP**, **Centro de Custo Dep. Acumul. -N3\_CCCDEP**, **Centro de Custo Corr. Depr. - N3\_CCCDES** ao transferir um **Ativo Fixo** via **Manutenção de Ativos - SIGAMNT**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Todas as versões  
  
**Solução**Pelo módulo **Manutenção de Ativos**, ao transferir o **Centro de Custo** do bem integrado ao **Ativo Fixo**, quando o parâmetro **MV\_NGMNTAT - Integração Manutenção (MNT) com Ativo (ATF) Informar branco ou N - Não Integra; 1 = Alterações no ATF replicarão no MNT; 2 = MNT para ATF; 3 = MNT para ATF e ATF para MNT** igual a **3**, são alterados os campos **Centros de Custos Despesa - N3\_CCUSTO**, **Centro de Custo Corr. Depr. - N3\_CCCORR**, **Centro de Custo Desp. Depr. - N3\_CCDESP**, **Centro de Custo Dep. Acumul. -N3\_CCCDEP** e **Centro de Custo Corr. Depr. - N3\_CCCDES**, porém, ao alterar o **Centro de custo** de um **Ativo** pelo módulo **Ativo fixo** é alterado apenas o **Centro de Custo da Conta do Bem - N3\_CUSTBEM**.  
  
**Importante**  
O conceito da integração entre **Manutenção de Ativos** e **Ativo Fixo** é do módulo de **Ativo Fixo**. Após contato junto aos mesmos, foi entendido que a maneira correta é a de **transferência/alteração** de um **Centro de Custo - N3\_CUSTBEM** para apenas um **Centro de Custo - T9\_CCUSTO**.  
A partir do **Manutenção de Ativos**, esta troca de **Centro de custos** refletia na alteração dos demais campos e para os clientes que desejarem manter este comportamento será necessário que seja utilizado o **PE - Ponto de entrada** **ATF060END**. Para que seja executado exatamente da forma que o **Manutenção de Ativos** se comportava anteriormente a este ajuste, foi feito um exemplo que sendo compilado, manterá o ambiente da mesma forma que funcionava anteriormente.   
  
**Ponto de entrada ATF060END**

|  |
| --- |
| ``` #Include 'Protheus.ch'  User Function ATF060END()  	Local aArea  := GetArea() 	Local aParam := PARAMIXB //Objeto que vem como parâmetro.  	cCusto	:= aParam[1]:GetModel("GridFNS"):Getvalue("FNS_CCBEMD") 	cItem	:= aParam[1]:GetModel("GridFNR"):Getvalue("FNR_ITEORI") 	cCbase	:= aParam[1]:GetModel("GridFNR"):Getvalue("FNR_CBAORI")  	dbSelectArea("SN3") 	SN3->(DbSetOrder(11))//N3_FILIAL+N3_CBASE+N3_ITEM+N3_TIPO 	If(SN3->(MsSeek(xFilial("SN3") + cCbase + cItem ))) 		RecLock("SN3",.F.) 		//Centro de Custo 		SN3->N3_CCUSTO	:= cCusto 		SN3->N3_CCCORR	:= cCusto 		SN3->N3_CCDESP	:= cCusto 		SN3->N3_CCCDEP	:= cCusto 		SN3->N3_CCCDES	:= cCusto 		SN3->(MsUnlock()) 	EndIf  	RestArea(aArea)  Return ``` |

**Saiba mais**  
A documentação do **PE** **ATF060END** está disponível em [ATF060END - Gravação de dados adicionais após a transação da transferência de ativo](https://tdn.totvs.com/display/PROT/PE+ATF060END)
