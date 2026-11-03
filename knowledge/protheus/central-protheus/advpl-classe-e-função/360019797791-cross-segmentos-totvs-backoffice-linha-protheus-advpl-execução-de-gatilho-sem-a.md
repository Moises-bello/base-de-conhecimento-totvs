---
article_id: 360019797791
category: ADVPL - Classe e Função
content_hash: aadfd5d864866f569251a81d17bdefabd25553b27ed832fd82bba399c0f37263
fetched_at: '2026-06-28T22:40:19.296660+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Execução de Gatilho
  sem a necessidade de enter no campo
type: support-article
updated_at: '2024-01-18T13:52:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019797791-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Execu%C3%A7%C3%A3o-de-Gatilho-sem-a-necessidade-de-enter-no-campo
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**É possível acionar um gatilho, sem a necessidade de pressionar <ENTER> no campo?

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Os gatilhos são disparados por padrão ao você incluir uma informação e dar enter no campo, porém caso surja a necessidade de sua execução fora deste contexto, se faz necessário a utilização da função **RunTrigger**.

```
/****utilizando no aCols ******/  
If ExistTrigger('C6_PRODUTO') // verifica se existe trigger para este campo  
  RunTrigger(2,n,nil,,'C6_PRODUTO')  
Endif  
  
/****utilizando na Enchoice ******/  
If ExistTrigger('C5_CLIENTE')  
  RunTrigger(1,nil,nil,,'C5_CLIENTE')  
Endif
```

**Saiba Mais**[Runtrigger](http://tdn.totvs.com/pages/releaseview.action?pageId=6815032)  
[Gatilhos](http://tdn.totvs.com/display/framework/SX7+-+Gatilhos+de+Campos)
