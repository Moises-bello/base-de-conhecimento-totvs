---
article_id: 360018331592
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 8b41f5d7864f19240ac43061190085905ce27571f86be6b59b4dbe2f4605e0c4
fetched_at: '2026-06-28T22:42:07.891393+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013
  Natureza da Operação C30_NATOPE inexistente
type: support-article
updated_at: '2022-08-18T17:43:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018331592-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T013-Natureza-da-Opera%C3%A7%C3%A3o-C30-NATOPE-inexistente
---

**Ocorrência**

Ao acessar o gerenciador de integração após integrar o layout T013 para o TAF, é apresentado o seguinte erro:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047653013/mceclip0.png)

Erro x - Linha: xx - O valor 'xxx' informado na coluna 14 para o campo Id. Natureza Operação **(C30\_NATOPE)** não existe na base de dados.  
  
**Ambiente**

TAF – A partir da versão 12.1.17  
  
**Causa**

Este incidente ocorre, pois a Natureza da operação (TES) não existe dentro do TAF ou quando o layout T009 não foi importado para o TAF na integração do T013.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o Extrator Fiscal;

2. Responda a pergunta: **"Deseja integrar:"**igual a **1-Somente Cadastros**;

3. Altere o período da extração para: Data de/Data até: 01/01/1979 até o dia atual. Dessa forma, o Extrator irá considerar os cadastros fora do período do documento fiscal, onde geralmente ocorre este erro.

3. Selecione o *Layout***T009 - Natureza de Operação**e confirme a extração;

4. Acesse o módulo **TOTVS Automação Fiscal** -> Miscelânea -> Integração -> Processamentos para processar os dados extraídos;

5. Confirme na tela do gerenciador de integração se houveram inconsistências na importação do *Layout*;

6. Acesse o gerenciador de integração e posicione o cursor no registro que houve inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que o registro que obteve a inconsistência seja integrado novamente ao TAF.
