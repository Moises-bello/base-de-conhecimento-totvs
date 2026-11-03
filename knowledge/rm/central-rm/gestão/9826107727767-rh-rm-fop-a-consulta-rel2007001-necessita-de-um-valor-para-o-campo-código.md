---
article_id: 9826107727767
category: Gestão
content_hash: 652c658938fb7991febe2413327457c7d82628bf55b8a5e7e1e1c1d28a7c537c
fetched_at: '2026-06-28T22:46:48.286206+00:00'
product: rm
section_id: 1500000861162
source: central-rm
title: RH - RM - FOP - A consulta "REL2.007.001" necessita de um valor para o campo
  código
type: support-article
updated_at: '2025-03-11T10:59:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9826107727767-RH-RM-FOP-A-consulta-REL2-007-001-necessita-de-um-valor-para-o-campo-c%C3%B3digo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:50 min****Ocorrência**Ao importar um relatório ocorre o seguinte erro: **A consulta "REL2.007.001\_#5" necessita de um valor para o campo código**

**![](https://totvssuporte.zendesk.com/attachments/token/5er1mm2U0u9kB8TcvSplD3dFV/?name=image.png)****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Este erro ocorre, pois esta marcado a flag Importar com Outro Código, no campo **Consulta SQL REL2.007.001.**  
  
**Solução**Para solucionar o problema siga as orientações abaixo.

Expanda as opções do relatório e clique em cada expressão da **Consulta SQL REL2.007.001**e verifique qual esta marcado a opção Importar com outro código, ou Não importar (Utilizar a Atual), e marque a opção Importar sentença e substituir se existir.

Conforme o print abaixo. Logo após informar em todas as expressões, clique em executar, o relatório será importado.

![](https://totvssuporte.zendesk.com/attachments/token/YoVejWaZU7W47nk5z3t1G7RpC/?name=image.png)
