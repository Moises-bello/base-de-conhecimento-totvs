---
article_id: 360007130592
category: Gestão de Transportes (TMS)
content_hash: c08edbaa6e418e6d4f53effd80f743e94d38aaacadd64e10b0b86b1217dcbb7c
fetched_at: '2026-06-28T22:45:29.567868+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada MT940FIL Verifica Filial
type: support-article
updated_at: '2022-06-21T11:25:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007130592-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-MT940FIL-Verifica-Filial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:30 min  
  
Dúvida**Como implementar o ponto de entrada **MT940FIL** - **Verifica Filial**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**O ponto de entrada **MT940FIL** permite a verificação de filiais.  
  
**Programa** **Fonte**: MATA490.PRW  
  
**Sintaxe**: MT940FIL - Verifica Filial ( [ cAliasSF3)->F3\_NFISCAL ], [ cAliasSF3)->F3\_SERIE ], [ cAliasSF3)->F3\_CLIEFOR ], [ cAliasSF3)->F3\_LOJA ] ) --> nulo  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | cAliasSF3)->F3\_NFISCAL |  |  | Numérico |  |  | Armazena o Alias da Nota Fiscal. |  |  |  |  |  |  |  |  |  |  |
|  | cAliasSF3)->F3\_SERIE |  |  | Numérico |  |  | Armazena o Alias da Série. |  |  |  |  |  |  |  |  |  |  |
|  | cAliasSF3)->F3\_CLIEFOR |  |  | Numérico |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | cAliasSF3)->F3\_LOJA |  |  | Numérico |  |  | Armazena o Alias da Loja. |  |  |  |  |  |  |  |  |  |  |

**Retorno**:  
 **nulo**

(nulo)

**Observações**: Devido ao fato de alguns clientes processarem arquivos simultaneamente para todas as filias, a filial também estará na chave de chamada.
