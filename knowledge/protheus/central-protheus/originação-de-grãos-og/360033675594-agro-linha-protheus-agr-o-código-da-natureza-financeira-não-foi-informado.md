---
article_id: 360033675594
category: Originação de Grãos (OG)
content_hash: e14192f71643a1af5874043fd761c7f8308c649e54cacf63ae43f037c6d18abc
fetched_at: '2026-06-28T22:45:41.079120+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - O código da natureza financeira não foi informado
type: support-article
updated_at: '2024-01-10T12:53:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033675594-Agro-Linha-Protheus-AGR-O-c%C3%B3digo-da-natureza-financeira-n%C3%A3o-foi-informado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:10 min**  
**Ocorrência**Na tentativa de efetuar a confirmação do romaneio **OGA250** - **Romaneio com Pesagem** e **OGA251** - **Romaneio sem Pesagem** ao gerar o documento de entrada é exibida a mensagem na tela: **A103NATURE** - **O código da natureza financeira não foi informado.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044140533/mceclip0.png)

**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
 **Causa**   
Esta mensagem é exibida porque a natureza que é gravada na nota de entrada não é a que foi informada no contrato, e sim a que foi informada no parâmetro **MV\_2DUPNAT** - **Campo ou dado a ser gravado na natureza do título de compras**.  
  
 **Solução**  
Para solucionar essa ocorrência é necessário inserir no parâmetro **MV\_2DUPNAT** a informação   
**SA2->A2\_NATUREZ**.

![FIG1224.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044150133/FIG1224.PNG)

É necessário que a natureza seja informada no cadastro do fornecedor.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044236793/mceclip0.png)

**Importante**A natureza informada no contrato é utilizada para a previsão financeira e não é passada para o título de compra.  
  
**Saiba mais**Para mais informações acerca do parâmetro**MV\_2DUPNAT** acesse a documentação:  
[Integração com o Módulo Financeiro](http://tdn.totvs.com/pages/releaseview.action?pageId=6085174)
