---
article_id: 12781738661271
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 59d8802dbde082a02c8ed923fc5a283d7a9486ffe28583a629b344987914db34
fetched_at: '2026-06-28T22:42:02.637561+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Bloco H entregue
  no mês 01 gerando erro no PVA no mês 02
type: support-article
updated_at: '2023-03-01T19:05:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12781738661271-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Bloco-H-entregue-no-m%C3%AAs-01-gerando-erro-no-PVA-no-m%C3%AAs-02
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Por qual motivo ocorre o erro de validação abaixo na entrega do **Sped Fiscal** referente ao mês de Fevereiro, sendo que o **Bloco H** já foi entregue em janeiro?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12781607268247)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Quando o **bloco H** já foi entregue em **janeiro** e ao validar o **Sped Fiscal** referente à competência de **fevereiro** é apresentado o erro de validação em questão, primeiramente, é preciso verificar se o campo **02 - IND\_MOV** do registro **H001 - Abertura do Bloco H** está sendo gerado como 1 no arquivo txt  
  
![](https://totvssuporte.zendesk.com/attachments/token/1hZB5hD3XsfgHo3fgt0XRn1Q8/?name=inline1046264317.png)​  
  
Caso já esteja, alguns clientes já abriram chamado quanto a este tema e ocorre que quando o **Bloco H** é entregue em  janeiro, ao validar fevereiro o validador critica essa informação, porque se trata de um bloco que deve ser entregue, **obrigatoriamente** até fevereiro, e no caso, o **PVA** não entende que já foi entregue no mês anterior.  
  
Nesse caso, orientamos que entre em contato diretamente com a **SEFAZ** do estado, visto que, o arquivo está sendo gerado corretamente.
