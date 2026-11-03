---
article_id: 360007447511
category: Gestão de Transportes (TMS)
content_hash: bb6c22dd6adc4a0b752ff22b7c5ddc0c46fd9f26f3b91a1b211be58690f2f2a9
fetched_at: '2026-06-28T22:45:29.605136+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM040ALT Altera validações
  padrões do sistema
type: support-article
updated_at: '2022-01-18T17:41:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007447511-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM040ALT-Altera-valida%C3%A7%C3%B5es-padr%C3%B5es-do-sistema
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)*** Tempo aproximado para leitura: **00:01:12 min  
  
Dúvida**Como implementar o ponto de entrada **TM040ALT** **Altera validações padrões do sistema**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM040ALT** está localizado no **TMSA040** **Cotação de Frete**, permitindo efetuar validações ao selecionar na opção **Alterar** desconsiderando as validações padrões do sistema.  
  
**Programa Fonte**: TMSA040.PRW  
  
**Sintaxe**: TM040ALT - Altera Validações Padrões do Sistema ( [ cFilOri ], [ cNumCot ], [ cStatus ], [ lCopia ] ) --> lRet  
  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| cFilOri | Caracter | Filial de Origem |  |  |  |
| cNumCot | Array of Record | Número da Cotação |  |  |  |
| cStatus | Array of Record | Status da Cotação |  |  |  |
| lCopia | Array of Record | Indica se a opção selecionada se refere a copia da cotação |  |  |  |

**Retorno:**  
lRet  
         (logico)  
          Se F, efetuará as validações padrões do sistema.  
          Se T, não efetuará as validações padrões do sistema.  
  
**Exemplos:**  
User Function TM040ALT()  
Local cFilOri := ParamIXB[1]  
Local cNumCot:= ParamIXB[2]  
Local cStatus := ParamIXB[3]  
Local lCopia := ParamIXB[4]  
Aviso('P.E.: TM040ALT',' - '+cFilOri + "/" + cNumCot + "/" + cStatus ,{'OK'})  
Return .T.  
  
**Variáveis**:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
|  | Array of Record | Global | Não |  |
