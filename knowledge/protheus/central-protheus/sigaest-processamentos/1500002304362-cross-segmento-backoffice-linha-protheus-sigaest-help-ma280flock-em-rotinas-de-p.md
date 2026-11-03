---
article_id: 1500002304362
category: SIGAEST - PROCESSAMENTOS
content_hash: f1886e61f8efe8b3e8ac8f1b1a25a2ffae602b00c072cc4c4d09db03b572be04
fetched_at: '2026-06-28T22:39:04.861417+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  HELP MA280FLOCK em
  Rotinas de Processamentos
type: support-article
updated_at: '2023-04-11T17:16:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002304362-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-MA280FLOCK-em-Rotinas-de-Processamentos
---

**Ocorrência**Ao executar rotinas como: Refaz Saldos (MATA300), Refaz Acumulados (MATA215), Recálculo do Custo Médio (MATA330), Fechamento de Estoque (MATA280) gera-se o HELP **MA280FLOCK**.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**Este help é causado quando a rotina tenta travar uma tabela específica (que é mostrada no HELP) para que ela seja utilizada no processamento porém possui uma outra conexão utilizando a tabela, não permitindo assim prosseguir o processamento

**Solução**Para este problema temos soluções a depender da rotina.

**Para rotinas Recálculo do Custo Médio (MATA330) e Refaz Saldos (MATA300)**

Para estas rotinas, pode-se adotar a alternativa de desabilitar o parâmetro MV\_CUSTEXC, que permite ou não utilizar estas rotinas em modo exclusivo.

**Para demais rotinas de** **processamento**

Outras rotinas de processamento são executadas apenas de forma **exclusiva**, conforme exemplo abaixo da rotina Refaz Acumulados:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002074902/mceclip0.png)

Para estes casos, a solução é identificar envolvem os seguintes passos:

1° - Checar se há algum JOB habilitado;

2° - Checar se existe alguma conexão presa à alguma rotina ou tabela que o processamento faz checagem;

3° - Checar qual usuário poderia estar acessando à rotina/tabela;

4° - Reiniciar os serviços do Protheus e tentar executar novamente.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033442-SIGAEST-PROCESSAMENTOS)*
