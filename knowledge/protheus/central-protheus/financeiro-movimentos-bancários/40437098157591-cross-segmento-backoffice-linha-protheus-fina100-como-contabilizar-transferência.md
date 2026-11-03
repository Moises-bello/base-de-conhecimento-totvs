---
article_id: 40437098157591
category: Financeiro - Movimentos Bancários
content_hash: 1e65a30e8bd4d42302d7b4f19ed0e863aae9f451d8a5c894b8a8424033b53bd2
fetched_at: '2026-06-28T22:37:31.817014+00:00'
product: protheus
section_id: 35057601824535
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus -FINA100 - Como contabilizar transferência
  bancária
type: support-article
updated_at: '2026-05-13T12:47:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40437098157591-Cross-Segmento-Backoffice-Linha-Protheus-FINA100-Como-contabilizar-transfer%C3%AAncia-banc%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40437066273943) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Como realizar a contabilização de transferência bancária?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as versões.  
  
**Solução**  
Existem dois lançamentos padrão para que o sistema realize a contabilização das transferências bancárias:

* 560: Movimento Bancário - Transferência Saída Banco Origem.
* 561: Movimento Bancário - Transferência de Entrada para Banco Destino.

Estes lançamentos são configurados como partida simples e gerados simultaneamente por apenas uma transação. Como um lançamento é a contrapartida contábil do outro, torna-se obrigatória a seleção da Carteira TODAS no processo de contabilização off-line para garantir a consistência contábil.

**Importante**

Na tela de inclusão das transferências bancárias **(FINA100)**, caso o campo Data Crédito seja alterado, apenas o lançamento de destino terá o campo **Data Disponibilidade (E5\_DTDISPO)** atualizado. O movimento de origem altera o saldo bancário imediatamente. Para garantir a integridade dos saldos no balanço contábil, as transferências serão contabilizadas sempre pelo campo **Data Baixa (E5\_DATA),** independentemente da configuração dos parâmetros :  "**Contabiliza baixa ?** " [**Data Baixa** (**E5\_DATA**), **Data Digitação** (**E5\_DTDIGIT**) ou **Data  Disponibilidade** (**E5\_DTDISPO**)]

**Passos**

1. O lançamento padrão **560**irá realizar a contabilização do movimento de Saída (origem da transferência):

|  |  |
| --- | --- |
| Cod Lanc Pad (CT5\_LANPAD) | 560 |
| Sequencial (CT5\_SEQUEN) | 001 |
| Descrição (CT5\_DESC) | Movimento Bancário - Transferência Saída Banco Origem |
| Cta Débito (CT5\_DEBITO) |  |
| Cta Crédito (CT5\_CREDIT) | IIF(ALLTRIM(FUNNAME())=="FINA100",POSICIONE("SA6",1,XFILIAL("SA6")+STRTRAN(STRLCTPAD,"/",""),"A6\_CONTA"),SA6->A6\_CONTA) |
| Vlr Moeda 1 (CT5\_VLR01) | SE5->E5\_VALOR |
| Histórico (CT5\_HIST) | '560:001 Transf Banc Saída: ' + STRLCTPAD **(1)**  '560:001 Transf Banc Saída: ' + SA6→(A6\_COD+"/"+A6\_AGENCIA+"/"+A6\_NUMCON) **(2)** |
| Origem Lcto (CT5\_ORIGEM) | '560:001 Transf Banc Saída: ' + STRLCTPAD **(1)**  '560:001 Transf Banc Saída: ' + SA6→(A6\_COD+"/"+A6\_AGENCIA+"/"+A6\_NUMCON) **(2)** |
| **(1) ONLINE = STRLCTPAD -**Variável PRIVATE que contém o valor Banco/Agencia/Conta do banco **Origem** **(2) OFFLINE =**A rotina CTBAFIN utiliza o arquivo SA6 para indicar o Banco de origem. | |

2. O lançamento padrão **561**irá realizar a contabilização do movimento de Entrada (destino da transferência):

|  |  |
| --- | --- |
| Cod Lanc Pad (CT5\_LANPAD) | 561 |
| Sequencial (CT5\_SEQUEN) | 001 |
| Descrição (CT5\_DESC) | Movimento Bancário - Transferência Entra Banco Destino |
| Cta Débito (CT5\_DEBITO) | IIF(ALLTRIM(FUNNAME())=="FINA100",POSICIONE("SA6",1,XFILIAL("SA6")+STRTRAN(STRLCTPAD,"/",""),"A6\_CONTA"),SA6->A6\_CONTA) |
| Cta Crédito (CT5\_CREDIT) |  |
| Vlr Moeda 1 (CT5\_VLR01) | SE5->E5\_VALOR |
| Histórico (CT5\_HIST) | '561:001 Transf Banc Entrada: ' + STRLCTPAD **(1)**  '561:001 Transf Banc Entrada: ' + SA6→(A6\_COD+"/"+A6\_AGENCIA+"/"+A6\_NUMCON) **(2)** |
| Origem Lcto (CT5\_ORIGEM) | '561:001 Transf Banc Entrada: ' + STRLCTPAD**(1)**  '561:001 Transf Banc Entrada: ' + SA6→(A6\_COD+"/"+A6\_AGENCIA+"/"+A6\_NUMCON) **(2)** |
| **(1) ONLINE = STRLCTPAD -**Variável PRIVATE que contém o valor Banco/Agencia/Conta do banco **Destino** **(2) OFFLINE =**A rotina CTBAFIN utiliza o arquivo SA6 para indicar o Banco destino. | |

**Saiba mais**

[560/561 Contabilização da transferência bancária](https://tdn.totvs.com/pages/releaseview.action?pageId=569477911)
