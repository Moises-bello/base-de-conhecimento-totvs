---
article_id: 16705515938711
category: ADVPL - Classe e Função
content_hash: efe1d9595752f80e2fa62355d2f349fc60bc49ccb695fbcabfbf6d5d307336e5
fetched_at: '2026-06-28T22:40:18.157568+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Uso de funções TLPP
  no AdvPL
type: support-article
updated_at: '2023-08-14T13:00:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16705515938711-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Uso-de-fun%C3%A7%C3%B5es-TLPP-no-AdvPL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16705545831319)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**É possível utilizar funções TLPP no AdvPL?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**As funções do TLPP podem ser utilizadas dentro do AdvPL desde que possuam um Namespace, o nome do *namespace* pode ser um nome simples ou um nome que contenha "." como separador por exemplo *"namespace.suafuncao()"*, desta forma ao chamar a função TLPP ela passa a reconhecer variáveis e funções com nomes maiores do que o permitido no AdvPL por conta do Namespace.

Desta maneira, ao a execução voltar para o programa em AdvPL evita ocasionar erros e também volta aos padrões AdvPL de tamanhos de variável e função.

**Exemplo**

Função TLPP

```
namespace exemplo  
  
function testeNamespace2  
conout("testeNamespace2")  
return
```

Chamada no AdvPL com namespace

```
user function exemplo1  
exemplo.testeNamespace2()  
return
```

**Saiba mais**[NameSpace](https://tdn.totvs.com/display/tec/Namespace)

[TLPP](https://tdn.totvs.com/display/tec/TLPP)
