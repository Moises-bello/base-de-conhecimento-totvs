---
article_id: 360047143634
category: ADVPL - Classe e Função
content_hash: 3bf8a7be5a3bfa126b3e39419316ee7a42e8db1113688587f246719f70a3a612
fetched_at: '2026-06-28T22:40:15.725447+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Criando uma tela
  MVC só com GRID
type: support-article
updated_at: '2023-02-09T19:13:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047143634-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Criando-uma-tela-MVC-s%C3%B3-com-GRID
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como criar uma tela em MVC que tenha somente GRID?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**A nossa implementação de MVC obriga que todos os modelos possuam pelo menos uma estrutura de Field. Como podemos fazer um modelo que só tenha um Grid ?

Para isso é necessário criar um modelo que tenha uma estrutura Fields criada especificamente para cumprir a obrigatoriedade da implementação e que ficará escondida na visualização além do Grid que você deseja incluir.  
Abaixo como ficaria a tela e em anexo um exemplo de fazer isso, criando um Grid de Produtos ( SB1 ) sem cabeçalho.  
  
![MVC_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079293914/MVC_.png)

**Saiba mais**[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Classe MsNewGetDados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026101932)
