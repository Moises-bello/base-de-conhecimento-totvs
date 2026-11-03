---
article_id: 4407428210327
category: RH - Dissídio
content_hash: baeaab0eae4c379a8675cbf9ff758c2ee6544261b31a2501e86fbd2c1d04c13f
fetched_at: '2026-06-28T22:43:43.478096+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao gerar dissidio para a folha sistema apresenta
  mensagem: Não gerado - Já existe um registro com essa chave'
type: support-article
updated_at: '2025-08-20T12:43:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407428210327-RH-Linha-Protheus-GPE-Ao-gerar-dissidio-para-a-folha-sistema-apresenta-mensagem-N%C3%A3o-gerado-J%C3%A1-existe-um-registro-com-essa-chave
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34314203759383) Tempo aproximado para leitura: **00:01:00 min** **Ocorrência**Ao gerar o dissidio para a folha sistema apresenta a mensagem: Não gerado - Já existe um registro com essa chave.  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**  
A mensagem é apresentada pois o número de **documento** informado na geração do dissídio já consta em Valores Futuros do funcionário.  
  
**Solução**Informe um número de documento diferente do que consta na coluna Nr. Documento da rotina Valores Futuros dos funcionários que constam no log, pois mesmo que em Valores Futuros o registro já esteja como pago, não é possível inserir a mesma verba com o mesmo número de documento:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7557294721047)

**Saiba mais:**

**<https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio>**
