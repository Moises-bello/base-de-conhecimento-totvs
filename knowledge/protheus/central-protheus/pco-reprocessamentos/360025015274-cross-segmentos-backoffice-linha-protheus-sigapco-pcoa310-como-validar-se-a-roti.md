---
article_id: 360025015274
category: PCO - Reprocessamentos
content_hash: 18a6d32f9c3f95a30ba52a2790120212af375874dc0ebf5f92199b3c888e9f93
fetched_at: '2026-06-28T22:37:07.044329+00:00'
product: protheus
section_id: 1500001551022
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAPCO - PCOA310 Como validar
  se a rotina de reprocessamento de lançamentos esta sendo executada corretamente...
type: support-article
updated_at: '2023-01-09T19:30:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025015274-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAPCO-PCOA310-Como-validar-se-a-rotina-de-reprocessamento-de-lan%C3%A7amentos-esta-sendo-executada-corretamente
---

**Dúvida**Quando o reprocessamento de lançamento não reprocessar corretamente, o que analisar?   
  
**Ambiente**Protheus - PCO - A partir da versão 12.1.17.  
  
**Solução**Acessar a Rotina PCOA030,

* PCO -> Atualizações -> Lançamentos -> Por Processos.
* Posicione sobre o Processo que deseja Reprocessar e clique em Alterar.
* Informar sim nas opções, Cfg. On Line/ Perm. Reproc./ Exibe Lancto.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039366773/mceclip2.png)

Seguir a orientação do Link a baixo, para executar o reprocessamento (Com a flag, Visualizar Lançamentos Processados, selecionada).  
[MP - SIGAPCO - PCOA310 Como reprocessar lançamento.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019267711-MP-SIGAPCO-PCOA310-Como-reprocessar-lan%C3%A7amento-)  
  
Após a execução exibira a tela de configuração dos lançamentos.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038549474/mceclip3.png)

Para saber se a configuração esta correta e buscando as informações nas tabelas de origem, deve haver uma linha de Visualização dos Lançamentos (selecionada em Azul), para cada linha de configuração (selecionada em Vermelho).

Nessa tela, é possível confirmar os valores e editar o lançamento se necessário, após editar clicar nas setas (Verde) para atualizar.

Quando na configuração uma informação não estiver preenchendo, pode ser erro na sintaxe, tabela sem valor ou não estar posicionada a tabela nesse momento. É fácil verificar.

No canto superior esquerdo da tela, tem a opção Tabela, informe a tabela que deseja a informação, após carregar, localize o campo que deseja a informação, expanda o conteúdo clicando no + à esquerda do campo, que irá mostrar se o campo tem ou não informação.

A **tabela padrão** que o lançamento carrega as informações, é sempre a exibida no momento da subida da tela, para outras tabelas é necessário testar para verificação se irá atender a necessidade.

**Observação:**Ao fazer a verificação do lançamento, se identificar um campo pontual que o sistema não esta carregando informação, considerando ser campo da **tabela padrão**, entre em contato com o suporte da TOTVS informando o campo, a tabela e qual o processo que está reprocessando. (Antes certifique-se que tem informação na tabela, ao consultar a tabela no módulo de Origem das informações).
