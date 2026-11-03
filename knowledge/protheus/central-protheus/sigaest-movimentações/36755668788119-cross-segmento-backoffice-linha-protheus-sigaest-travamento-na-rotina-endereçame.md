---
article_id: 36755668788119
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 801775d3c79a7fa1f25c14e1effcbbf50083c18edbf9127d516ef7e641af959f
fetched_at: '2026-06-28T22:38:58.398619+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Travamento na rotina
  Endereçamento(MATA265).
type: support-article
updated_at: '2025-12-03T17:55:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36755668788119-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Travamento-na-rotina-Endere%C3%A7amento-MATA265
---

O artigo orienta a coleta de informações para analisar travamentos na rotina de endereçamento de produtos MATA265 no TOTVS Protheus, incluindo uso do LOGPROFILER, configuração de TraceStack no appserver.ini, envio da ID da Central de Diagnóstico e geração do DBTrace do processo para diagnóstico detalhado.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36755668774039) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como tratar casos de travamento na rotina de endereçamento de produtos MATA265?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Para melhor avaliarmos a performance, peço gentilmente as seguintes informações complementares:

Execute a rotina demostrando o seu passo  a passo e gere os seguintes procedimento:

* O LOGPROFILER (<https://tdn.totvs.com/display/public/framework/LogProfiler+-+Como+executar>)
* Coloque as tags da TraceStack para o Logprofiler vir com as pilhas das chamadas de erros que ocorrerem nesse processamento. Exemplo de configuração que fará no   appserver.ini: <https://tdn.totvs.com/display/tec/TraceStack>
* Nos enviar a ID da sua Central de Diagnóstico atualizada conforme a documentação: [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como enviar dados pela Central de Diagnóstico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)
* O DBTrace do processo, desde o momento de acessar a rotina até o cenário apresentado. Informações para nos encaminhar o DBTrace: [Logística - Linha Protheus - OMS - Como gerar Totvs Replay, DBTrace e Inspetor de Objetos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6493773904535-Log%C3%ADstica-Linha-Protheus-OMS-Como-gerar-Totvs-Replay-DBTrace-e-Inspetor-de-Objetos)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
