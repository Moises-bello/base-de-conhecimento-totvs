---
article_id: 35274075448855
category: Financeiro - Contas a Receber
content_hash: a6e7ed2f417394e4e6e3c076600cd3af341be673ad27b86439a44e1ed8183c42
fetched_at: '2026-06-28T22:38:12.620972+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA040 - Error.log
  de duplicidade em titulo NCC ao gerar uma nota de devolução
type: support-article
updated_at: '2025-09-29T16:35:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35274075448855-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Error-log-de-duplicidade-em-titulo-NCC-ao-gerar-uma-nota-de-devolu%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35274035791383) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
O que validar quando ocorre error.log de duplicidade em titulo NCC ao gerar uma nota de devolução?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**

Exemplo de mensagem no e**rror.log.**

**Cannot insert duplicate key row in object 'dbo.SE1000' with unique index 'SE1000\_UNQ'. The duplicate key value is (0101, 001, 000001 , 1 , NCC, 0).**

Este cenário ocorre devido a configuração incorreta do parâmetro **MV\_1DUP**comparado ao tamanho dos campos de parcelas do ambiente.

A condição para a correta geração das parcelas quando da entrada de nota fiscal de devolução é a necessidade do parâmetro **MV\_1DUP** estar configurado com o mesmo tamanho do campo parcela. Pois o **parâmetro** trabalha em conjunto com os campos **E1\_PARCELA** e **E2\_PARCELA** do financeiro.

**Exemplo: Se o tamanho do campo parcela for igual a 02 o MV\_1DUP deve estar cadastrado como “AA” ou “01”.**

Saiba mais:

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como deve ser configurado o parâmetro MV\_1DUP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33795001539351-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-deve-ser-configurado-o-par%C3%A2metro-MV-1DUP)
