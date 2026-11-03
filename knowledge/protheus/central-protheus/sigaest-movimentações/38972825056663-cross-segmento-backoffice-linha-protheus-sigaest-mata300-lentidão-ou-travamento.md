---
article_id: 38972825056663
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 4360221b4b2d717a44ddc85aa6867554ef4b3a613c1a240b01e6adbc669917ea
fetched_at: '2026-06-28T22:38:57.093771+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA300 - Lentidão
  ou Travamento no Processamento do Refaz Saldos
type: support-article
updated_at: '2026-03-25T18:45:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38972825056663-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA300-Lentid%C3%A3o-ou-Travamento-no-Processamento-do-Refaz-Saldos
---

A rotina Refaz Saldos (MATA300) no Protheus pode apresentar lentidão devido a diversos fatores, como fontes de estoque desatualizadas, configurações do parâmetro MV\_A300THR ou customizações ativas. Recomenda-se atualizar fontes, revisar parâmetros, desativar customizações, enviar dados via Central de Diagnóstico e utilizar DBTrace e LogProfiler para análise detalhada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38972809140631) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Ao processar a rotina Refaz Saldos (MATA300) ocorre lentidão e/ou travamento na execução. **O que fazer para melhorar a performance ou impedir que a mesma conclua o processamento?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
  
**Solução**  
O processamento do **Refaz Saldos (MATA300)** pode ser impactado por diversos fatores que afetam o tempo de execução. É importante considerar que a rotina recalcula os saldos de estoque com base nos movimentos do sistema, e sua execução pode ser feita em modo compartilhado ou exclusivo, controlado pelo parâmetro **MV\_CUSTEXC**.

Para identificar o motivo do aumento no tempo de processamento, recomenda-se:

**Verificar se houve algum fato relevante no sistema entre as execuções.**

1. Avaliar se as fontes do estoque estão desatualizadas, conforme o último pacote de expedição contínua do Estoque e Custos [Acumulado BackOffice conforme sua versão](https://tdn.totvs.com/x/2hgdHw). Observação: Aplicar após backups e validar primeiro em ambiente teste.
2. Verificar como está  o conteúdo do parâmetro [**MV\_A300THR**](https://tdn.totvs.com/x/WxA1Hg)no seu ambiente.
3. Desativar as customizações conforme esse boletim [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como desabilitar customizações no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018286552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-desabilitar-customiza%C3%A7%C3%B5es-no-Protheus)
4. Encaminhe os dados de ambiente via Central de Diagnósticos. Veja neste artigo como enviar através do atalho SHIFT + F6: [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como enviar dados pela Central de Diagnóstico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)
5. O DBTrace durante processamento da rotina MATA300 e o LogProfiler da rotina: [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como gerar o LogProfiler e Dbtrace?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019902592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-gerar-o-LogProfiler-e-Dbtrace)
6. Encaminhe a CV8 em formato SQLITE, filtrada pela rotina MATA300 no campo CV8\_PROC

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
