---
article_id: 16106148240407
category: Materiais - Compras (SIGACOM)
content_hash: d2cfde739e71eecf138ab3d695c40f4571dff1b2f8b7ad8cae7ba5ff55e22d2c
fetched_at: '2026-06-28T22:41:20.071703+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA103 - Errorlog
  array out of bounds ( 0 of 248 ) on A103LINOK(MATA103.PRW) ao incluir Documento
  de entrada.
type: support-article
updated_at: '2023-07-18T12:33:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16106148240407-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA103-Errorlog-array-out-of-bounds-0-of-248-on-A103LINOK-MATA103-PRW-ao-incluir-Documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16106132557335) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao tentar incluir um documento de entrada o sistema gera o errorlog array out of bounds ( 0 of 248 ) on A103LINOK(MATA103.PRW) 27/06/2023 09:30:48 line : 5283.  
  
**Ambiente**Protheus – Compras – A partir da versão 12.1.33  
  
**Solução**

O errorlog ***array out of bounds ( 0 of 248 ) on A103LINOK(MATA103.PRW) 27/06/2023 09:30:48 line : 5283***indica que ocorreu um erro relacionado aos limites de um array, a função A103LINOK() está tentando acessar o elemento de um array além dos limites permitidos.

Isso significa que o campo não foi encontrado ou a informação está "inacessível". Dentre as principais razões para isso ocorrer, temos:

- Campo com "USADO" desmarcado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16106148217111)

- Nivel de campo acima 1 (Exemplo se tiver 9, isso significa que esse campo só pode ser utilizado pelo admistrador)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16106126085783)

- Na aba Módulos do configurador > Não está marcado "Todos Módulos"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16106132561559)

- Ou, existe alguma customização nesse campo feito pelo cliente, que torna-o nulo exemplo, um posicione customizado ou algo do tipo (nos campos de validação de usuário)

Faça essa análise com os seguintes campos abaixo conforme as instruções citadas acima:

D1\_CONTA  
D1\_CC  
D1\_ITEMCTA  
D1\_CLVL

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
