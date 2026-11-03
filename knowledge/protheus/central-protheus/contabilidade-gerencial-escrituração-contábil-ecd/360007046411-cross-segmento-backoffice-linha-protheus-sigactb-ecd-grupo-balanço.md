---
article_id: 360007046411
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: dcba1d42514a9111a2f50119ca8f7a957c7189b398070c0bdbee3dabe3c06974
fetched_at: '2026-06-28T22:40:45.662633+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB-ECD - GRUPO BALANÇO '
type: support-article
updated_at: '2022-04-11T12:10:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007046411-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-GRUPO-BALAN%C3%87O
---

**Ocorrência**

Validando ECD tanto as contas do Ativo como as contas do Passivo, apresentam como grupo 1

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007285592/mceclip0.png)

Outro cenário, é a geração do CTBR500 as contas do Ativo e do Passivo saírem do mesmo lado do relatório

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007285652/mceclip1.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007285652/mceclip1.png)

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80]  
   
  
   
 **Solução**No modulo Contabilidade Gerencial - Atualizações / Entidades/ Visão Gerencial

Rotina CTBA161 - deve informa a coluna correspondente ao grupo e posição da conta

Exemplo: Conta 1.1.01.001

 Para que o sistema  gere  o passivo no  grupo **P (Passivo**), necessário informar a coluna 2  na visão gerencial 

Para mais detalhes :  [ECD : J100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-MP-SIGACTB-ECD-J100?source=search)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070752014/mceclip0.png)
