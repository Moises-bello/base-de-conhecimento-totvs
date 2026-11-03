---
article_id: 360007129492
category: Gestão de Transportes (TMS)
content_hash: 05d985578b4141b96e46e3400e592ab2b062390899b95229b4c74106c640edd2
fetched_at: '2026-06-28T22:45:29.550535+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada FISATEND
type: support-article
updated_at: '2022-06-21T11:23:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007129492-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-FISATEND
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura:**00:00:30 min  
  
Dúvida**Como implementar o ponto de entrada **FISATEND**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **FISATEND** permite realizar alterações no endereço da função **FISGETEND**.  
  
**Programa Fonte**: MATA950.PRW  
  
**Sintaxe**: FISATEND ( [ ] ) --> cRet  
  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
|  | Array of Record |  |  |  |  |

**Retorno**  
cRet  
        (caracter)  
        String com endereço alterado.

**Exemplos:**User Function FisAtEnd() Local cEndereco := ParamIXB[1]Local cRet := ''Local lCompEnd := .F.Local nPosEsp := 0cEndereco := AllTrim(cEndereco) If Type(Substr(cEndereco,1,1)) == 'N' cRet := 'RUA '+cEnderecoEndIfIf Rat(',',cEndereco) == 0 nPosEsp := Rat(' ',cEndereco) If Empty(nPosEsp) lCompEnd := .T. Else nPosEsp += 1 If Type(Substr(cEndereco,nPosEsp,1)) != 'N' lCompEnd := .T. EndIf EndIf If lCompEnd If Empty(cRet) cRet := cEndereco EndIf cRet += ' .' EndIfEndIf Return cRet  
  
**Variáveis**:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
|  | Array of Record |  |  |  |
