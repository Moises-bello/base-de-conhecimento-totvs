---
article_id: 360007504892
category: Gestão de Transportes (TMS)
content_hash: b24d096b18a9d3510ad0f27d170b026381cf8a0d9e937f51301713cd69a9a5a3
fetched_at: '2026-06-28T22:45:32.285938+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250XML Envio de Contrato
  com a REPOM
type: support-article
updated_at: '2023-10-10T11:57:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007504892-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250XML-Envio-de-Contrato-com-a-REPOM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18159409890455) Tempo aproximado para leitura: **00:00:50 min  
  
Dúvida**Como implementar o ponto de entrada **TM250XML**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM250XML** é responsável por receber e retornar ao Sistema o **XML** de envio de **Geração do Contrato** e **Cancelamento de Contrato** na integração com a REPOM.  
  
**Programa** **Fonte**: TMSREPOM.PRW  
  
Sintaxe: TM250XML - Envio de Contrato para a REPOM ( [ cXML ], [ ] ) --> cXML  
  
**Parâmetros**:

* Nome: cXML
* Tipo: Caracter
* Descrição: XML enviado a REPOM
* Default: Não possui default
* Obrigatório: Não

**Retorno**: cXML - Retorno do XML  
  
**Exemplo**:

```
#Include 'PROTHEUS.CH'  
  
User Function TM250XML()  
Local cXML := aClone(PARAMIXB[1])  
  
MsgAlert('Ponto de Entrada TM250XML')  
  
cXML := cXML + 'Ponto de Entrada TM250XML'  
  
Return(cXML)
```
