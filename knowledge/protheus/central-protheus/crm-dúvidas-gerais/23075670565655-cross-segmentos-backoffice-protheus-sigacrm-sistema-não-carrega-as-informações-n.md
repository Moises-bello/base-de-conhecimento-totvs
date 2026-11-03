---
article_id: 23075670565655
category: CRM - Dúvidas Gerais
content_hash: b524398bfb40841efcbcee5d3419bd25239f59f8f883172faa76d49b3a7e5785
fetched_at: '2026-06-28T22:40:27.734076+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Sistema não carrega as informações
  no campo Contato Ass AD1_CNTPRO
type: support-article
updated_at: '2024-04-26T13:47:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23075670565655-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Sistema-n%C3%A3o-carrega-as-informa%C3%A7%C3%B5es-no-campo-Contato-Ass-AD1-CNTPRO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23075670539927) Tempo aproximado para leitura: **00:03:00 min****Dúvida:**Através da rotina Oportunidade de Vendas FATA300, ao considerar a oportunidade como Ganha, em seguida acessar a aba de Aceite de Proposta, o sistema não carrega as informações no campo **Contato Ass. AD1\_CNTPRO**.  
  
**Ambiente:**Cross Segmentos - Backoffice Protheus - SIGACRM - Todas as versões

**Solução:**No fonte **FATV300A** existe uma função **(FT300VLSU5)** que valida se o contato da tabela **SU5** está relacionado à entidade para qual a Oportunidade foi aberta, ou seja, no campo **Contato Ass.** **AD1\_CNTPRO** o sistema só irá demonstrar os contatos associados à entidade **(Cliente, Prospect, etc.)** que está citado na Oportunidade.  
   
**Passo a passo:**

1 - Acesse a rotina Cadastro de Clientes (CRMA980);

2 - Sobre o registro deste cliente, clique em **'Outras Ações' -> 'Contatos';**

![CONTATO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23075717115799)

3 - Verifique se os contatos relacionados ao cliente não aparecem para assinatura;

4 - Relacione o contato ao Cliente para que o mesmo seja apresentado na lista de contatos para assinatura;

![CONTATO2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/23075717117207)

5 - Clique em confirmar para salvar os registros;

6 - Ao acessar a rotina de Oportunidade de Venda e gerar a proposta comercial, os contatos serão apresentados;

![contato3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/23075670545943)

**Veja também:**

**[Oportunidades (CRMA110 - SIGACRM)](https://tdn.totvs.com/pages/viewpage.action?pageId=346490322)**
