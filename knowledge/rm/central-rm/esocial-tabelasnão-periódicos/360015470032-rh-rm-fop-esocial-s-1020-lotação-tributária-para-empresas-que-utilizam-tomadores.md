---
article_id: 360015470032
category: eSocial - Tabelas/Não Periódicos
content_hash: 3f017e2c60be67143d75b19860d85efc314ba6872cb4a2bc7ed7f2b68bf31710
fetched_at: '2026-06-28T22:47:10.509501+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - S-1020 - Lotação tributária para empresas que utilizam
  tomadores de serviços
type: support-article
updated_at: '2025-02-26T18:12:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015470032-RH-RM-FOP-eSocial-S-1020-Lota%C3%A7%C3%A3o-tribut%C3%A1ria-para-empresas-que-utilizam-tomadores-de-servi%C3%A7os
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22925996753047)** Tempo aproximado para leitura: **00:03:30 min****Dúvida**  
Como realizar a geração da lotação tributária (evento**S-1020**) para empresas que utilizam tomadores de serviço?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Para empresas que utilizam tomadores de serviços, as lotações tributárias serão geradas com base na estrutura de seção, quebra de FPAS e tomadores de serviços.

Desta forma, para gerar as lotações, siga os seguintes passos:

1. No TOTVS Folha de Pagamento acesse o menu **Configurações | Parametrizador|  eSocial | [Lotação Tributária](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452719470)**;  
1.1. Informe a **Máscara para Lotação Tributária** preenchendo os campos relacionados à **Quantidade de caracteres**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22926512038039)

1.2. Em caso de mais de um **FPAS** dentro da estrutura de uma seção centralizadora, selecione o parâmetro **Utiliza quebra de FPAS**informando o código de quebra. Exemplo: dentro da seção centralizadora **01**, existe um **FPAS** na seção **01.01** e outro na **01.02**; o código de quebra de **FPAS** neste caso são cinco interrogações (**?????**);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22926512046615)

2. Acesse o menu **eSocial | Lotação Tributária** e clique em **Processos | Gerar Lotação Tributária;**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043377353)**

2.1. Será apresentado um *wizard* para execução do processo. Informe o **Tipo de Lotação Default**, selecione a coligada e avance até concluir;  
2.2. O sistema irá gerar as lotações tributárias considerando;  
   • Seção centralizadora de CNPJ;  
   • Seção que atenda a quebra de FPAS;  
   • Tomadores de Serviços que atendam a regra de geração de Lotação Tributária;

   • Tomadores informados no rateio do funcionário.

   • Tomador de Serviço que estiver vinculado ao afastamento do funcionário.

   • Tomador Empresa Vinculado no Parametrizador| Folha Normal| Tomador de Serviço.

  Após execução do processo, as Lotações Tributárias serão visualizadas no cadastro de Lotação. No exemplo abaixo, foi gerada uma Lotação Tributária para cada centralizadora de CNPJ, além de uma Lotação Tributária para cada tomador que atenda condições de geração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22926501324951)

3. Após gerar as lotações, acesse **eSocial | Gerar Gatilhos Eventos Iniciais** para a geração da **Carga Inicial** do **S-1020.**

**Importante**A partir da data de obrigatoriedade de eventos de tabela informada no parametrizador, qualquer alteração nas seções correspondentes às lotações tributárias irá gerar ou alterar gatilhos na fila de eventos do eSocial.  
 **Saiba mais**Para mais informações acesse:  
   • [Lotação Tributária - Vídeo](http://tdn.totvs.com/pages/releaseview.action?pageId=305930212)  
   • [Folha de Pagamento - Lotação Tributária](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452719593)

   • [RH - RM - FOP - eSocial - Identificação da origem da Lotação Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015506452-RH-RM-FOP-eSocial-Identifica%C3%A7%C3%A3o-da-origem-da-Lota%C3%A7%C3%A3o-Tribut%C3%A1ria)
