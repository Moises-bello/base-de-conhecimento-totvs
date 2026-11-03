---
article_id: 6113330053911
category: RH - Contabilização
content_hash: 0a15493c03021e6ba07c1aa2b6129752d81241af9774ab092ef5f67ff2ca1385
fetched_at: '2026-06-28T22:43:45.864428+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como utilizar o ponto de entrada GP110ACT
type: support-article
updated_at: '2025-07-28T20:06:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6113330053911-RH-Linha-Protheus-GPE-Como-utilizar-o-ponto-de-entrada-GP110ACT
---

Ponto de entrada para alterar valores do arquivo SRZ (Resumo da Folha) antes de processar a contabilização

Fonte: GPEM110.PRX

**02. EXEMPLO DE UTILIZAÇÃO**

#Include "Protheus.ch"  
/\*  
No exemplo, a contabilização das filiais 01, 02, 03, 04 e 05 é centralizada na filial 01  
\*/  
User Function GP110ACT()  
  
Local aRet    := { "01", "01"}  
  
//Retira a chave única da tabela SRZ, devido necessidade de atualização da SRZ  
If SX2->( dbSeek("SRZ") )  
    SX2->( Reclock("SX2", .F.) )  
    SX2->X2\_UNICO := ""  
    SX2->( MsUnlock() )  
EndIf  
  
//Efetua alteração da filial da tabela SRZ, conforme código enviado para a função SRZFilReplace()  
SRZFilReplace( "01" , /\*bCondReplace\*/ )  
  
Return( aRet )

**03. VARIÁVEIS DE RETORNO**

**Outras Ações / Ações relacionadas**

| Nome | Tipo | Descrição |
| --- | --- | --- |
| aRet | array | [ 1 ] = Código da filial onde a contabilização será efetuada |
|  |  | [ 2 ] = Código da filial onde a contabilização será centralizada |

**04. NA PRÁTICA**  
Exemplo montado (disponível também anexo):  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6440997212183)

Funcionamento do PE 410ARQ:  
![GP110ACT.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/6441271449111)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de Pagamento do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-)
