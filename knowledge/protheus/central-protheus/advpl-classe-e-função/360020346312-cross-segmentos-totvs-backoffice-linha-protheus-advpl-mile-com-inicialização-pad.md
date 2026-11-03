---
article_id: 360020346312
category: ADVPL - Classe e Função
content_hash: a0f19d441d7722f8c0c22b51e0d105e5a4ba8076a9342f153bb898d34efb0d10
fetched_at: '2026-06-28T22:40:20.514453+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Mile com inicialização
  padrão
type: support-article
updated_at: '2022-04-18T11:35:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020346312-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Mile-com-inicializa%C3%A7%C3%A3o-padr%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**É possível utilizar um inicializador padrão em um campo no momento da importação de um layout do MILE (*Model Integrator Layout Engine*)?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
 **Solução**Será necessário informar a regra de inicialização do campo que será incluso na área de Execução do MILE (campo XZ4\_EXEC):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016506672/mceclip1.png)  
  
Está regra deve atribuir o valor ao campo desejado:

```
C5_NUM := GetSXENum("SC5", "C5_NUM")
```

E a origem do dado (XZ4\_SOURCE) deve ser respeitada, assim sendo, uma vez que eu informei que o campo C5\_NUM terá como origem de dados a posição 2, deve ser inserido um valor nesta posição:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016558351/mceclip3.png)  
  
**Saiba mais**  
[MILE - Model Integrator Layout Engine](http://tdn.totvs.com/display/framework/MILE+-+Model+Integrator+Layout+Engine)
