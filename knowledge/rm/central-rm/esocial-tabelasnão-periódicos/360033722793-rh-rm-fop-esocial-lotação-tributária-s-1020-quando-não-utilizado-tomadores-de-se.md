---
article_id: 360033722793
category: eSocial - Tabelas/Não Periódicos
content_hash: a6952e5461ef8eb4589696b4093452f9fb4e4baee16d430ee42b3cb954eb3c94
fetched_at: '2026-06-28T22:47:10.207061+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial  - Lotação tributária (S-1020) quando não utilizado
  tomadores de serviços
type: support-article
updated_at: '2024-10-21T11:58:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033722793-RH-RM-FOP-eSocial-Lota%C3%A7%C3%A3o-tribut%C3%A1ria-S-1020-quando-n%C3%A3o-utilizado-tomadores-de-servi%C3%A7os
---

**Dúvida**  
Como realizar a geração da lotação tributária (evento **S-1020**) para empresas que **não** utilizam tomadores de serviço?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Dúvida**  
Para empresas que não utilizam tomadores de serviços, a lotação tributária será somente uma visão do cadastro de seções centralizadoras de **CNPJ** e **FPAS**.

Desta forma, para gerar as lotações, siga os seguintes passos:  
1. Acesse **Configurações | Parametrizador|  eSocial | [Lotação Tributária](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452719470)**;  
1.1. Em caso de mais de um **FPAS** dentro da estrutura de uma seção centralizadora, selecione o parâmetro **Utiliza quebra de FPAS** informando o código de quebra. Exemplo: dentro da seção centralizadora **01**, existe um **FPAS** na seção **01.01** e outro na **01.02**; o código de quebra de **FPAS** neste caso são cinco interrogações (**?????**);  
2. Ao acessar **eSocial | Lotação Tributária**, o sistema irá apresentar automaticamente as lotações tributárias conforme exemplo a seguir;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042526254)

3. Após gerar as lotações, acesse **eSocial | Gerar Gatilhos Eventos Iniciais** para a geração da **Carga Inicial** do **S-1020.**  
  
**Importante**  
A partir da data de obrigatoriedade de eventos de tabela informada no parametrizador, qualquer alteração nas seções correspondentes às lotações tributárias irá gerar ou alterar gatilhos na fila de eventos do eSocial.  
  
**Saiba mais**  
Para mais informações acesse:  
   • [Lotação Tributária - Vídeo](http://tdn.totvs.com/pages/releaseview.action?pageId=305930212)  
   • [Folha de Pagamento - Lotação Tributária](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452719593)

   • [RH - RM - FOP - eSocial - Identificação da origem da Lotação Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015506452-RH-RM-FOP-eSocial-Identifica%C3%A7%C3%A3o-da-origem-da-Lota%C3%A7%C3%A3o-Tribut%C3%A1ria)
