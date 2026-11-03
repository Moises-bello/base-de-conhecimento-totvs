---
article_id: 360052670173
category: RH - Rescisão
content_hash: e289879cd0e93d2eb18dcd67e9a280fe6ce0a6ec77ef69530a051807157d2a84
fetched_at: '2026-06-28T22:43:54.459650+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Sistema apresenta erro HELP: GPM600HAND'
type: support-article
updated_at: '2026-05-18T18:41:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052670173-RH-Linha-Protheus-GPE-Sistema-apresenta-erro-HELP-GPM600HAND
---

**Dúvida**Sistema apresenta erro HELP: GPM600HAND.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**A mensagem apresentada GPM600HAND significa:  
"Este usuário não tem direitos de gravação no diretório especificado no parâmetro do nome do arquivo."

No exemplo abaixo o erro ocorre em geração de arquivo seguro desemprego (rotina GPEM090). Atualizando o arquivo de destino e nome arquivo, o erro é solucionado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084091153/mceclip0.png)
