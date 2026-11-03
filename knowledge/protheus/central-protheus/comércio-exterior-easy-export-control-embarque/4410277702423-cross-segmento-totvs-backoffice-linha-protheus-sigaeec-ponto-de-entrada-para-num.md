---
article_id: 4410277702423
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 136d6e2c0d0b3ad071cf72539ef5a3a73be45bfedd410cf4ec49a003389d7e9d
fetched_at: '2026-06-28T22:36:39.225441+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Ponto de entrada
  para numeração da Invoice '
type: support-article
updated_at: '2021-10-18T21:13:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410277702423-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Ponto-de-entrada-para-numera%C3%A7%C3%A3o-da-Invoice
---

**Dúvida**Estou precisando de um ponto de entrada quando o usuário clicar no botão faturamento   
tenha uma opção de poder manipular o numero da invoice, qual seria o mesmo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Pode ser utilizado o ponto de entrada **GRV\_CPOS\_CUSTOM** na rotina EECAE100.

| Nome | Tipo | Descrição |
| --- | --- | --- |
| **GRV\_CPOS\_CUSTOM** | Caracter | Permite o tratamento de campos customizado no momento da gravação do embarque. |

Segue abaixo um exemplo do ponto de entrada:

```
User Function EECAE100()  
  
Local cParam := Iif(ValType(ParamIXB) == 'A', ParamIXB[1], ParamIXB)  
  
If cParam == 'GRV_CPOS_CUSTOM'  
  
MsgInfo("Passou no ponto")  
EEC->EEC_NRINVO := "TESTE"  
  
Endif  
  
  
Return
```

**Saiba mais****[PE EECAE100 Embarque](https://tdn.totvs.com/display/public/PROT/DT+PE+EECAE100+Embarque)**
