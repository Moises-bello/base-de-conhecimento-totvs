---
article_id: 360016576711
category: ADVPL - Ponto de Entrada
content_hash: 441b4026396fad9d47bd0b88935185e3854f32d2c85bafd209cfc634ffc41347
fetched_at: '2026-06-28T22:40:12.628083+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MT103SX1
type: support-article
updated_at: '2021-12-29T18:32:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016576711-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MT103SX1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Estou utilizando o Ponto de entrada MT103SX1 para manipular as respostas das perguntas do MTA103. No Ponto de entrada não pega contabilização On-Line ficar como SIM. Porem tem usuários que não muda ficando com NÃO.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**O ponto de entrada **MT103SX1** permite validar as perguntas e atribuir um novo valor, naquele momento que esta sendo executada a rotina, pois não esta sendo modificada na **SX1** (**na versão P12 as modificações do pergunte só pode ser feitas pelo configurado**), segue exemplo abaixo para melhor entendimento.

```
User Function MT103SX1()  
  
ALert("MT103SX1 " + cvaltochar(MV_PAR01)) //Apresenta o conteudo do MV_PAR01  
MV_PAR01=2   
ALert("MT103SX1 " + cvaltochar(MV_PAR01))//Apresenta o conteudo modificao do MV_PAR01  
  
Return
```
