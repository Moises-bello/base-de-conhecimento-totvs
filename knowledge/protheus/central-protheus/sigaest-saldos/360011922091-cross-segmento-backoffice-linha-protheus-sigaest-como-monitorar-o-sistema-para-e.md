---
article_id: 360011922091
category: SIGAEST - SALDOS
content_hash: 960d019de33d21c2951b28bb4fe239f3a31ba32e1b49a33dced5479f7dd0129c
fetched_at: '2026-06-28T22:39:14.775505+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como monitorar o Sistema
  para evitar desbalanceamento de Tabelas utilizando o MV_LOGMOV?
type: support-article
updated_at: '2026-05-29T16:00:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011922091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-monitorar-o-Sistema-para-evitar-desbalanceamento-de-Tabelas-utilizando-o-MV-LOGMOV
---

O parâmetro MV\_LOGMOV, quando ativado com "Sim", gera arquivos de log na pasta System para monitorar e identificar divergências entre as tabelas de lote, endereço e saldo físico (SB8, SBF, SB2). Esses logs contêm informações detalhadas sobre as ocorrências, auxiliando na identificação da origem dos problemas. É essencial garantir que o ambiente esteja livre de divergências antes de ativar o parâmetro.

**Dúvida**  
Como monitorar o Sistema para evitar desbalanceamento de Tabelas de Rastro (SB8), Endereço (SBF) e Saldo Físico (SB2)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O parâmetro MV\_LOGMOV tem como função rastrear as divergências nas movimentações de lote e/ou endereço.

Quando o parâmetro está com o conteúdo igual a “Sim”, o mesmo gera um arquivo na pasta System com a inicial “***CM??????.LOG***”, quando:

*- Houver diferença de Lote entre as tabelas SD5, SDA e SDB*

*- Houver diferença entre o Sub-Lote movimentado e o gravado nos arquivos SD5, SDA e SDB*

*- Houver diferença de Saldo entre SB2, SB8 e SBF.*

***Veja a imagem de exemplo abaixo gerada na pasta system.*** Ordenar a pasta por Data de modificação e acompanhar os novos logs gerados.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4463251642903)

O arquivo conterá informações importantes para se descobrir a origem do problema que gerou a divergência (data e hora da ocorrência, lista de chamada das linhas de programa, nome do usuário e lista de ocorrências para o produto movimentado).

***Veja um exemplo na imagem abaixo:***

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4463253263127)

**Importante:** **Para o correto funcionamento, antes da ativação do parâmetro é necessário que o ambiente esteja livre de divergências.**

**Saiba Mais:**  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
