---
article_id: 360007316471
category: Gestão de Transportes (TMS)
content_hash: c2e71d4145852ddaa25186646e0ceeb51c77a289d268790ca31e19d5800fee40
fetched_at: '2026-06-28T22:45:31.085712+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM200EXC Procedimentos
  após exclusão de Campos
type: support-article
updated_at: '2022-08-23T14:53:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007316471-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM200EXC-Procedimentos-ap%C3%B3s-exclus%C3%A3o-de-Campos
---

***![blobid0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8367860528663/blobid0.png)Tempo aproximado para leitura: 00:00:20 min*****Dúvida**Como implementar o ponto de entrada **TM200EXC** Procedimentos após exclusão de Campos?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM200EXC** está localizado no fonte **TMSA200** - Cálculo do Frete, e executa procedimentos após deletar alguns campos: **Filial do Documento**, **Número do Documento**, **Série do Documento** e **Número do Documento de primeiro percurso,** na nota fiscal do cliente. Procedimento este executado devido ao estorno do cálculo do frete.  
  
  
**Programa** **Fonte**: TMSA200.PRW  
  
**Sintaxe**: TM200EXC - Procedimentos após exclusão de Campos ( [ Nulo ] ) --> Nil  
  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| Nulo | Array of Record |  |  |  |  |

**Retorno**:  
  
**Nil**

(nulo)* Não tem retorno.

**Exemplos**:  
  
User Function TM200EXC()

MsgAlert('Passei por mais uma nota')

Return Nil
