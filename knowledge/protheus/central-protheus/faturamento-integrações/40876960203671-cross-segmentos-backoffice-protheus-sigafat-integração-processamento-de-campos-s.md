---
article_id: 40876960203671
category: Faturamento - Integrações
content_hash: f870aa708edf2a7e1ac7b911c1da5d0a40fe3d8ba339bf9ed391684337ff00b7
fetched_at: '2026-06-28T22:38:26.510272+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Integração - Processamento
  de campos sem tag e/ou customizados
type: support-article
updated_at: '2026-06-01T13:18:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40876960203671-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Integra%C3%A7%C3%A3o-Processamento-de-campos-sem-tag-e-ou-customizados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40876960180119) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como realizar a integração mensagem EAI, (CustomerVendor, Seller, Order e PriceListHeaderItem) para integrar os campos ao JSON, sem a necessidade de customizar o Protheus?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões;  
  
**Solução**  
Para o processamento de campos sem tag, sejam eles padrões ou customizados, foi implementada uma melhoria nas mensagens EAI (**CustomerVendor, Seller, Order e PriceListHeaderItem)**, permitindo que esses campos sejam integrados ao JSON sem a necessidade de customizações no Protheus.

Com essa implementação, os campos sem tag passam a ser tratados nativamente pela integração, simplificando o processo de manutenção e reduzindo a necessidade de desenvolvimentos específicos para atender esse cenário.

Para habilitar é necessário configurar o parâmetro **MV\_EAIFLDS**.

O parâmetro **MV\_EAIFLDS**(Tipo **Caracter**) contém 4 posições, considerando a seguinte estrutura:

![image-2025-3-28_8-28-35.png](https://tdn.totvs.com/download/attachments/928069091/image-2025-3-28_8-28-35.png?version=1&modificationDate=1743161315837&api=v2)

* **0** - Desabilita o envio dos campos sem tag e customizados.
* **1** - Habilita o envio dos campos sem tag e customizados.

#### **Processamento no Envio**

No processo de envio, os campos customizados e padrão que não possuírem as tags, mas apresentarem conteúdo preenchido, serão adicionados a uma seção denominada "**AddFields**" no**JSON**.

Essa seção conterá:

* O nome do campo ("**Field**").
* O respectivo conteúdo do campo ("**Content**").

#### **Processamento no Recebimento**

A leitura dos campos sem tag para o recebimento de mensagens EAI não requer a configuração do parâmetro **MV\_EAIFLDS**.

Durante o recebimento, os dados presentes na seção "**AddFields**" seguirão a mesma estrutura definida no envio, contendo os atributos "**Field**" e "**Content**". Esses campos serão adicionados ao array correspondente aos campos já tagueados, permitindo o processamento contínuo da mensagem.

Documentação completa com o exemplo de uso:

[Integração - Processamento de campos sem tag e/ou customizados](https://tdn.totvs.com/pages/releaseview.action?pageId=928069091)

[Integração de Adapters EAI](https://tdn.totvs.com/pages/releaseview.action?pageId=652401102)
