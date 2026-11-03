---
article_id: 360028307112
category: esocial - Periódicos
content_hash: 0b1067fc58b5e9b96785087f1e7ba3eb04f997b60699bf86d8d7e59da9bc04b9
fetched_at: '2026-06-28T22:47:09.187880+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Como desonerar uma empresa no eSocial
type: support-article
updated_at: '2026-05-27T21:09:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028307112-RH-RM-FOP-eSocial-Como-desonerar-uma-empresa-no-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22598872357783)**Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como informar a desoneração da folha de pagamento da empresa no eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da release 12.1.21  
  
**Solução**

Conforme *Layout* do eSocial, a desoneração da folha só é possível para empresas cuja classificação tributária for igual a [02,03,99].

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029692652)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029682551)

Para validação destas informações, acesse **eSocial | Informações do Empregador** e confirma os campos **Classificação Tributária** e **Indicativo de Desoneração da Folha**. No evento S-1000, esta informação é preenchida na tag **<indDesFolha>**.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029696812)

​​Após as validações supracitadas, caso sua empresa esteja apta a encaminhar a desoneração da folha de pagamento, realize o passo a seguir:

**1**. No menu **eSocial | Período de Apuração**, crie/edite o período de apuração desejado e preencha os campos relacionados às **Informações Substituição Patronal**.

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22598872380311)

**2.** Acesse **eSocial | Gerar XML (Periódicos)** e faça a geração do S-1280 para integração e transmissão ao RET.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22598872395031)

​  
**Importante**  
O evento S-1280 deverá ser enviado antes de realizar o fechamento dos eventos periódicos com o envio do evento S-1299. Caso o período esteja fechado sem o envio do S-1280, será necessário reabrir o período através do evento S-1298, enviar o S-1280 e retificar os eventos S-1200 para validar corretamente a desoneração.

**Saiba mais**  
Para mais informações, acesse:  
- [S-1280](http://tdn.totvs.com/pages/releaseview.action?pageId=364909345)  
- [Desoneração de CNO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028548251)  
- [Desoneração da Folha de Pagamento - Nota de esclarecimento RFB - TOTVS](https://www.totvs.com/blog/fiscal-clientes/desoneracao-da-folha-de-pagamento-nota-de-esclarecimento-rfb/?utm_source=whatsapp&utm_medium=-&utm_campaign=rh&utm_term=gsp&utm_content=-)
