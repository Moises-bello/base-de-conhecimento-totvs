---
article_id: 24993118874135
category: Financeiro
content_hash: 098929e84d143be50f7274bb5e79627216d035ee1ebd4b1f7d5f32738a7edd38
fetched_at: '2026-06-28T22:38:03.028688+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA450 - Ao tentar
  compensar o titulo ocorre o Help: RECNO - Não existe registro no arquivo em pauta'
type: support-article
updated_at: '2024-11-04T14:20:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24993118874135-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA450-Ao-tentar-compensar-o-titulo-ocorre-o-Help-RECNO-N%C3%A3o-existe-registro-no-arquivo-em-pauta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24993118851479) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao tentar compensar o titulo na compensação entre carteira ocorre o Help: RECNO - Não existe registro no arquivo em pauta   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24993118854679)  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Uma das causa é o titulo estar na carteira de cobrança E1\_SITUACA=2  
  
**Solução 1**Na rotina **FINA450** pressione a tecla "**F12**" para acessar os parâmetros da rotina e altere o parâmetro "**Comp.Titulos Transf**" = **Sim**, com isso será possível compensar o titulo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24993118856599)

**Solução 2**

Se estiver compensando o tipo:PA/RA/NCC/NDF utilizar a opção "Compensar Títulos de Crédito"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27539545456919)

**Solução 3**

Verificar se os títulos estão liberados para pagamento.

[SIGAFIN - FINA580 - Como utilizar a rotina liberação para baixa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016596851-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA580-Como-utilizar-a-rotina-libera%C3%A7%C3%A3o-para-baixa)

**Saiba mais:**[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA450 - Como funciona a Compensação entre Carteiras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7813623585431-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA450-Como-funciona-a-Compensa%C3%A7%C3%A3o-entre-Carteiras)
