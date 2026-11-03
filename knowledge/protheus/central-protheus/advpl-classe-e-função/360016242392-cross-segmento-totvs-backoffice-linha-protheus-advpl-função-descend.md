---
article_id: 360016242392
category: ADVPL - Classe e Função
content_hash: cb0420c52da280929225d3007d03523531733b0254eda1d75f900b81e8fe47fc
fetched_at: '2026-06-28T22:40:20.726708+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Função Descend
type: support-article
updated_at: '2022-01-03T19:53:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016242392-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-Descend
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Cliente deseja realizar uma ordenação reversa utilizando a função [Descend()](http://tdn.totvs.com/display/framework/DESCEND%28%29+-+Descontinuada), mas não está sendo possível.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12.1.17

**Causa**A função Descend() só funciona na chave de índice quando os dados do ambiente são persistidos em .DBF.  
  
**Solução**

1. Crie um campo do tipo caractere;
2. Coloque no inicializador padrão a função Descend();
3. Execute o fonte em anexo para preencher o campo;
4. Crie dois índices: um para o campo personalizado e outro para índice para o campo padrão.

**Evidência**[DESCEND.7Z](https://totvssuporte.zendesk.com/attachments/token/nSfGSctsRzekW0VmVHFsXqkMr/?name=DESCEND.7z)
