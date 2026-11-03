---
article_id: 360026776892
category: Materiais - Compras (SIGACOM)
content_hash: 3818bed2d5934c6236b9fd9dea8ec1efa702b043eb8f3a5e4e580d29fbc5bfa8
fetched_at: '2026-06-28T22:41:10.467008+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Totvs Colaboração -
  Ponto de Entrada COMCOL2 para processar somente documentos do tipo Transferência
  entre Filiais
type: support-article
updated_at: '2022-05-16T20:59:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026776892-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Totvs-Colabora%C3%A7%C3%A3o-Ponto-de-Entrada-COMCOL2-para-processar-somente-documentos-do-tipo-Transfer%C3%AAncia-entre-Filiais
---

**Dúvida**

Totvs Colaboração - Ponto de Entrada **COMCOL2** para processar somente documentos do tipo Transferência entre Filiais  
  
**Ambiente**Protheus – compras – A partir da versão 11.80  
  
**Solução**

Ponto de Entrada: COMCOL2 - CUSTOMIZAÇÃO PARA PROCESSAR SOMENTE DOCUMENTOS DO TIPO TRANSFERÊNCIA ENTRE FILIAIS.

|  |  |
| --- | --- |
| Versões: |  |
| Compatível Países: | Todos |
| Sistemas Operacionais: | Todos |
| Compatível às Bases de Dados: | Todos |
| Nível de Acesso: | (Acesso Clientes) |
| Idiomas: | Todos |

Descrição:

```
Localização: Function COLNFeAut - Função responsável por validar as tabelas SE4/SF4 para geração automática dos documentos do TOTVS Colaboração. Em que Ponto: Na função COLNFeAut antes de entrar no laço para carregar os itens do documento importado, deve ser usado para verificar se somente serão processados os documentos do tipo transferência entre filiais, para permitir o processamento automático dos documentos importados somente quando for transferência entre filiais.
```

Programa Fonte:

```
COMXCOL.PRW
```

Parametros:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Nome | Tipo | Descrição | Default | Obrigatório | Referência |
|  | PARAMIXB[1] | Array of Records | Array contendo o cabeçalho do documento importado. |  |  |  |
|  | PARAMIXB[2] | Array of Records | Array contendo os itens do documento importado. |  |  |  |

Retorno:

```
Lógico
RETORNA SE O DOCUMENTO QUE ESTA SENDO PROCESSADO É DO TIPO TRANSFERÊNCIA ENTRE FILIAIS.
```

Programa Fonte:

```
COMXCOL.PRW
```

Exemplo:

```
User Function COMCOL2() 
Local aAreaSM0 := SM0->(GetArea())
Local aAreaSA2 := SA2->(GetArea())
Local aCabec   := PARAMIXB[1]  //Cabecalho dos principais campos da tabela SF1 (Cabecalho do documento de entrada)
Local aItens   := PARAMIXB[2]	//Itens dos principais campos da tabela SD1 (Itens do documento de entrada)
Local nPosFor  := aScan(aCabec,{|x| AllTrim(x[1]) == "F1_FORNECE"})
Local nPosLoj  := aScan(aCabec,{|x| AllTrim(x[1]) == "F1_LOJA"})
Local lRet	:= .F.

SA2->(DbSetOrder(1))
SA2->(dbSeek(xFilial("SA2")+aCabec[nPosFor,2]+aCabec[nPosLoj,2]))
If UsaFilTrf()
	lRet := (!Empty(SA2->A2_FILTRF))
Else
	SM0->(DbSetOrder(1))
	SM0->(MsSeek(cEmpAnt))
	Do While !SM0->(Eof()) .And. SM0->M0_CODIGO == cEmpAnt
		If (SM0->M0_CGC == AllTrim(SA2->A2_CGC))
			lRet := .T.
			Exit
		EndIf
		SM0->(DbSkip())
	EndDo
EndIf

RestArea(aAreaSM0)
RestArea(aAreaSA2)
Return lRet
```

***Saiba Mais:***

[COMCOL2 - CUSTOMIZAÇÃO PARA PROCESSAR SOMENTE DOCUMENTOS DO TIPO TRANSFERÊNCIA ENTRE FILIAIS.](https://tdn.totvs.com/pages/viewpage.action?pageId=51250475)
