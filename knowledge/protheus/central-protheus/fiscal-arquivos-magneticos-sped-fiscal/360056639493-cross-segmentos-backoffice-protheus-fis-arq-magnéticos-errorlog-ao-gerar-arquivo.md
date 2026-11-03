---
article_id: 360056639493
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 6f7f1c6b8216b26c00dc0c90ecf61b4c2cdae3190bc84a12604e0d1c1f51b87a
fetched_at: '2026-06-28T22:42:00.937782+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - ERROR.LOG AO
  GERAR ARQUIVO DA NOVA GIA-SP
type: support-article
updated_at: '2024-06-19T17:26:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056639493-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-ERROR-LOG-AO-GERAR-ARQUIVO-DA-NOVA-GIA-SP
---

**Dúvida**

Error.log ao gerar arquivo da Nova GIA-SP:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094887153)

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Este erro ocorre quando o campo "C2T\_AJUCOM" na base do cliente, por algum motivo foi criado como **text** ou **image** e o correto é VARCHAR.  
  
Verificar se o campo na SX3 está como M e tamanho 999 ?  
  
Caso esteja, realizar um backup da tabela "C2T", e DROPAR a mesma, em seguida acessar o TAF para que a tabela "C2T" seja recriada corretamente.

Para recriara tabela C2T :

**Modulo 84 - SIGATAF** > ATUALIZAÇÕES-> Encerramento de Período -> Apuração Sub/ICMS
