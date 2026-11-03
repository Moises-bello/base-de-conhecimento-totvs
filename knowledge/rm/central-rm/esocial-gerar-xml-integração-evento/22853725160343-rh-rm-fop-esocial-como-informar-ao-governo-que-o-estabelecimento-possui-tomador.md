---
article_id: 22853725160343
category: eSocial - Gerar XML/ Integração Evento
content_hash: 81ff46205a1b8c9cadafac5749d364a6ebb6228abf4b772c1eb2c8e1b4e35610
fetched_at: '2026-06-28T22:47:12.048579+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Como informar ao governo que o estabelecimento possui
  tomador de serviços, para identificação no FGTS Digital
type: support-article
updated_at: '2026-06-01T13:45:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22853725160343-RH-RM-FOP-eSocial-Como-informar-ao-governo-que-o-estabelecimento-possui-tomador-de-servi%C3%A7os-para-identifica%C3%A7%C3%A3o-no-FGTS-Digital
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22853764523927) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**

Ao verificar a guia de FGTS Digital, é identificado que no Estabelecimento consta que não há Tomador, porém no RM Folha de Pagamentos consta o Tomador de Serviços cadastrado.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22853725136919)**

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
A identificação do tomador é enviada através da lotação tributária, evento S-1020.   
É necessário enviar o S-1020 com o CNPJ, CPF ou CNO do tomador de serviços, para que haja a identificação do mesmo no portal do governo e consequentemente no FGTS Digital. Para isto, o governo irá considerar o preenchimento nos seguintes tipos de lotação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23719116809239)

Para solucionar essa dúvida, realize os seguintes passos:

* **Para lotações que são identificadas como CNO**  
  1. Em **Administração de Pessoal | Identifique o funcionário desejado | Anexos | Históricos | Histórico de Rateio por Tomador e** verifique se consta vinculado o tomador de serviços desejado com o número do CEI vinculado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23719116840983)

2. Identifique no XML S-1200 deste funcionário, qual é a lotação que está sendo vinculada;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23719072299927)

3. Verifique se na lotação informada no XML S-1200, consta cadastrada com o tipo 02 e o CEI vinculado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23719072320023)

3.1. Caso esteja incorreto, realize a correção e envie o XML S-1020 da lotação, com competência igual ou anterior a competência que está sendo apurada;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23719162332567)

3.2 Após retifique o S-1200 ou S-2299.

* **Para lotações que são identificadas como CNPJ ou CPF**  
  1. Em **Administração de Pessoal | Identifique o funcionário desejado | Anexos | Históricos | Histórico de Rateio por Tomador** e verifique se consta vinculado o tomador de serviços desejado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22854081178775)

2. Identifique no XML S-1200 deste funcionário, qual é a lotação que está sendo vinculada;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22854081192471)

3. Verifique se na lotação informada no XML S-1200, consta cadastrada com algum dos tipos de lotação que são vinculadas o CNPJ ou CPF do tomador (03, 04, 05, 06, 07, 08 ou 09);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22854081208343)

3.1. Caso esteja incorreto o tipo de lotação, realize a correção e envie o XML S-1020 da lotação, com competência igual ou anterior a competência que está sendo apurada;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23719265168663)

3.2 Após retifique o S-1200 ou S-2299.
