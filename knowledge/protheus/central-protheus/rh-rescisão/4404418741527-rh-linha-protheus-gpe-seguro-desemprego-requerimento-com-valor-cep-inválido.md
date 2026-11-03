---
article_id: 4404418741527
category: RH - Rescisão
content_hash: d8b98ca70702256fcd3b56d0855b23dbf5defb64c5a34cff3520fc52a6fa4cd4
fetched_at: '2026-06-28T22:43:51.053107+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE -  Seguro Desemprego : Requerimento com valor CEP
  inválido'
type: support-article
updated_at: '2025-06-16T18:55:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404418741527-RH-Linha-Protheus-GPE-Seguro-Desemprego-Requerimento-com-valor-CEP-inv%C3%A1lido
---

**Ocorrência**Erro ao enviar arquivo de Seguro Desemprego : Requerimento com valor CEP inválido.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Causa**CEP cadastrado não existe.   
  
**Solução**Após a geração do arquivo do Seguro Desemprego, o validador no site do Empregador Web só verifica se o arquivo possui o layout correto e apresenta resultado de provado para envio.   
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404423259287/mceclip1.png)

Ao tentar enviar o arquivo via Empregador Web, é apresentada a mensagem que o CEP é inválido, pois nesta transmissão ele verifica a existência do CEP informado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404418619799/mceclip0.png)

Acesse o cadastro de funcionário e verifique o CEP cadastrado:   
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404419268247/mceclip4.png)

A validação do CEP pode ocorrer através do link abaixo:   
<https://buscacepinter.correios.com.br/app/endereco/index.php>
