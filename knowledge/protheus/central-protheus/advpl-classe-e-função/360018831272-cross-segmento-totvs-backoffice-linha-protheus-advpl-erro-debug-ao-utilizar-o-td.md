---
article_id: 360018831272
category: ADVPL - Classe e Função
content_hash: 0351c11820813e083108cb425e9a169b45fbd4f42c3624cbbc290a03f0846ed3
fetched_at: '2026-06-28T22:40:15.804243+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro debug ao utilizar
  o TDS
type: support-article
updated_at: '2022-01-03T21:56:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018831272-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-debug-ao-utilizar-o-TDS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao Debugar apresenta o erro, fechando a tela.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Erro pode ocorrer devido as configurações de depuração  
  
**Solução**Verifique as configurações do include de projeto e configurações de debug.

* Na opção Debug-> Depurar Configurações

![image2017-9-13 11:23:32.png](http://tdn.totvs.com/download/attachments/286751993/image2017-9-13%2011%3A23%3A32.png?version=1&modificationDate=1505312939000&api=v2)

* Verifique no campo parâmetros se contem a expressão "-M", está errado pois essa opção é da Função para o remote é só selecionar a opção Múltiplas sessões

![image2017-9-13 11:21:15.png](http://tdn.totvs.com/download/attachments/286751993/image2017-9-13%2011%3A21%3A15.png?version=1&modificationDate=1505312939000&api=v2)

![](http://tdn.totvs.com/download/attachments/286751993/image2017-9-13%2011%3A28%3A24.png?version=1&modificationDate=1505312939000&api=v2)

Observação: Pode travar também ao acionar parâmetros
