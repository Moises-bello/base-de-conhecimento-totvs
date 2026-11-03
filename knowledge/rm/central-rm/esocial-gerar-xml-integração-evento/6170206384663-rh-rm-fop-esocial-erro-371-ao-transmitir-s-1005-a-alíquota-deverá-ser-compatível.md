---
article_id: 6170206384663
category: eSocial - Gerar XML/ Integração Evento
content_hash: 3cda52b7ecd70204bded186014cc6cb08b4341cf5500b1a5438d9bb3341b2d3c
fetched_at: '2026-06-28T22:47:12.123485+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 371 ao transmitir S-1005: A alíquota deverá
  ser compatível com o CNAE preponderante informado'
type: support-article
updated_at: '2024-06-26T17:47:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6170206384663-RH-RM-FOP-eSocial-Erro-371-ao-transmitir-S-1005-A-al%C3%ADquota-dever%C3%A1-ser-compat%C3%ADvel-com-o-CNAE-preponderante-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24447618712855) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao transmitir o evento S-1005 é apresentada a mensagem **Código de Ocorrência: 371 A alíquota devera ser compatível com o CNAE preponderante informado. Ação Sugerida: Verifique se a alíquota e o CNAE estão corretos.**

**![371.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/6193614551191)**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Esse incidente ocorre pois a alíquota RAT e o CNAE preponderante não se correspondem, sendo necessário a conferência se a alíquota RAT está cadastrada corretamente.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique no XML as *tags* **cnaePrep** e **aliqRat;**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6169677430679)

2. Acesse [**Tabela de CNAEs Preponderantes**](https://www.gov.br/esocial/pt-br/noticias/decreto-10-410-2020-altera-tabela-de-cnaes-preponderantes) do governo e verifique se a **alíquota RAT** corresponde ao **CNAE Preponderante.**  
3. No exemplo supracitado, a *tag* **cnaePrep** foi encaminhada como 4681805. Para este CNAE, a alíquota RAT informada pelo governo é 2. Será necessário alterar o cadastro da alíquota RAT no cadastro da seção em **Dados para INSS**, no campo **%Acid.Trabalho**:

![cnae.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/6196663490967)

4. Após regere o XML e integre com o governo.
