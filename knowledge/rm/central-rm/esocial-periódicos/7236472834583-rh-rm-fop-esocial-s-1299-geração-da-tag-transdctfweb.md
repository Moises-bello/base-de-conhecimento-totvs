---
article_id: 7236472834583
category: esocial - Periódicos
content_hash: 58631b5259e0013bf51401b3e4df51ac414fdb0931978a9be8a2dfa80a68cf0b
fetched_at: '2026-06-28T22:47:09.502852+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - S-1299: Geração da tag transDCTFWeb'
type: support-article
updated_at: '2024-06-20T11:32:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7236472834583-RH-RM-FOP-eSocial-S-1299-Gera%C3%A7%C3%A3o-da-tag-transDCTFWeb
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)  Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**Como gerar a *tag* **transDCTFWeb** (Transmissão imediata da DCTFWeb) no XML do S-1299?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Conforme o leiaute eSocial, a *tag* **transDCTFWeb** não deve ser gerada caso o período de apuração seja **menor** que 10-2021. Se o período de apuração for maior ou igual a 10-2021 **E** (classificação tributária informada no S-1000 for "04 - MEI" **OU** se o indicativo de tipo de guia estiver preenchido no S-1299), o preenchimento é obrigatório.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7238919773207/mceclip1.png)

Caso as condições acima sejam atendidas, basta acessar o menu **eSocial | Período de Apuração** e selecionar o parâmetro **Transmissão imediata da DCTFWeb** para que a *tag* seja gerada no XML doS-1299.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7239175134999/mceclip2.png)

**Saiba mais**  
Para mais informações, acesse:  
     - [Mapeamento dos eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409020102679)
