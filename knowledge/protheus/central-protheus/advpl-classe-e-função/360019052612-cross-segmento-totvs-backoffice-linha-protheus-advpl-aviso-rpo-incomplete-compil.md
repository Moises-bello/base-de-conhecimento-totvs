---
article_id: 360019052612
category: ADVPL - Classe e Função
content_hash: 8a8bfee526dc3710e4d6a91e33185b27cac6a453a68dc16e5fadc3e0e7f7641d
fetched_at: '2026-06-28T22:40:14.480285+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Aviso: rpo incomplete
  compilation some programs will not work'
type: support-article
updated_at: '2022-01-03T21:41:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019052612-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Aviso-rpo-incomplete-compilation-some-programs-will-not-work
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**No console do *Application* *Server* é exibida a seguinte mensagem:

```
[WARNING] RPO incomplete compilation. Some programs will not work.
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**Essa mensagem é registrada no log de console do TOTVS | *Application Server*, quando realizada a carga do repositório para a memória, caso exista um ou mais fontes marcados com problema de compilação no Repositório.  
Tomemos como exemplo o cenário abaixo:  
Foi solicitado ao IDE/TDS a compilação de uma lista de fontes, como por exemplo uma compilação de um projeto inteiro ou uma pasta inteira de um projeto.

Durante a compilação, vários fontes são compilados com sucesso, porém no primeiro erro de compilação de um código, a compilação é interrompida.  
Todos os fontes compilados com sucesso são gravados no repositório, porém o ultimo fonte – que apresentou alguma ocorrência de erro durante a compilação – é removido do repositório, e marcado como incompleto.  
Este registro do repositório passa a ser mostrado no log de console, caso exista algum fonte no Repositório marcado como incompleto.  
  
**Solução**Para desmarcar um fonte incompleto, é necessário compilá-lo neste repositório.
