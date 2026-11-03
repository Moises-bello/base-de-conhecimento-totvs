---
article_id: 360018478811
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 429c3b812fa54b4d453d9f546f4da72c643a71029b143db2ff0bcfd191bc63d1
fetched_at: '2026-06-28T22:42:07.858527+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013
  - C30_CODITE não existe na base de dados
type: support-article
updated_at: '2022-11-14T14:26:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018478811-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T013-C30-CODITE-n%C3%A3o-existe-na-base-de-dados
---

**Ocorrência**

Ao acessar o gerenciador de integração após integrar o layout T013 para o TAF, é apresentado o seguinte erro:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047651193/mceclip1.png)

Erro x - Linha: xx - O valor 'xxx' informado na coluna 3 para o campo Id. Item (**C30\_CODITE** ) não existe na base de dados.  
  
**Ambiente**

TAF –  A partir da versão 12.1.17  
  
**Causa**

Este incidente ocorre, pois o produto não existe dentro do TAF ou quando o layout T007 não foi importado para o TAF na integração do T013.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o Extrator Fiscal e certifique-se que o seu extrator seja do mês 07 ou acima;

2. Responda a pergunta: **"Deseja integrar:"**igual a **1-Somente Cadastros**;

3. Altere o período da extração para: Data de/Data até: 01/01/1979 até o dia atual. Dessa forma, o Extrator irá considerar os cadastros fora do periodo do documento fiscal, onde geralmente ocorre este erro.

3. Selecione o *Layout***T007- Identificação do Item**e confirme a extração;

4. Acesse o módulo **TOTVS Automação Fiscal** -> Miscelânea -> Integração -> Processamentos para processar os dados extraídos;

5. Confirme na tela do gerenciador de integração se houveram inconsistências na importação do *Layout*;

6. Acesse o gerenciador de integração e posicione o cursor no registro que houve inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que o registro que obteve a inconsistência seja integrado novamente ao TAF.
