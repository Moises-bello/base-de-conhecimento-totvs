---
article_id: 11468755236759
category: SIGAEST - PROCESSAMENTOS
content_hash: 3ac88f45ec12fa15081273e70518bd2c5bd39081a7367308822849c3fdf04faf
fetched_at: '2026-06-28T22:39:04.944076+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA215 - Refaz Empenhos
  via Schedule não processa
type: support-article
updated_at: '2025-03-12T12:41:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11468755236759-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA215-Refaz-Empenhos-via-Schedule-n%C3%A3o-processa
---

**Ocorrência:**

O que fazer quando ao executar a rotina Refaz Acumulados(MATA215) via Schedule, é informado que o processo foi iniciado e após poucos segundos finalizado no Schedule, porém não houve execução aparente?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11482718253207)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução:**

Como a rotina demanda acesso exclusivo para ser executada, com usuários *logado* ou o configurador aberto ela não realizará nenhum processamento, e se analisar a tabela de Log de Processamento (CV8), apenas apresentará a mensagem "Processamento iniciado".

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11483156349207)

Com o configurador aberto ele torna o ambiente compartilhado porque abre diversas tabelas, impossibilitando a execução da rotina.

Após fechar o configurador a execução do Schedule é processada normalmente, e ao analisar a tabela de Log de Processamento são informadas novas mensagens:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11489004544919)

Validar também se as tag's abaixo estão configuradas no appserver do ambiente:

**[OnStart]**

jobs=FWSCHDMANAG,FWSCHDQUEUE

RefreshRate=120

**[FWSCHDMANAG]**

Main=FWSCHDMANAG

Environment=(NOME DO AMBIENTE)

**[FWSCHDQUEUE]**

Main=FWSCHDQUEUE

Environment=(NOME DO AMBIENTE)

Para uma visão mais detalhada do funcionamento do Schedule Protheus, consulte as documentações  nos link's abaixo:

Appserver: [Clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=233735618)

Configurador: [Clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=271167961)

**Saiba mais:**

*[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - MATA215 - Refaz Empenhos via Execauto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003543821)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Execução de Schedule Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048543893)*

*[Clique aqui e veja mais artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)*
