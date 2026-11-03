---
article_id: 5825993939607
category: BI - Business- Intelligence - Workflow
content_hash: a61afe1840179b4207dc90ae3bab4dc07202404cefe5894074563be77929ff2a
fetched_at: '2026-06-28T22:37:03.049242+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Falha na criação da
  tabela SXM
type: support-article
updated_at: '2022-06-15T18:21:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5825993939607-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Falha-na-cria%C3%A7%C3%A3o-da-tabela-SXM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como realizar a criação da SXM após gerar o erro?

```
SXM010: TOP Error -19 - [ERROR] (from tDBServer::ROP_CREATEFILE - table SXM010) Invalid operation with active transaction.  
( From tDBServer::ROP_CREATEFILE )
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - BI - Todas versões  
  
**Solução**Para realizar a criação da SXM em ambiente com o dicionário em Banco, favor seguir os passos abaixo:

* Inicie os serviços(*appserver, dbaccess, smartclient*) como administrador;
* Verifique se há uma caixa de e-mail Workflow configurada no módulo Configurador (Ambientes -> Workflow -> Contas de e-mail) e se a mesma está selecionada na página de Parâmetros do Workflow;
* Feita as validações acima, execute a função padrão *WFTEST* via Smartclient conforme telas abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5825526234647/mceclip0.png)![WFTEST2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5825559810967/WFTEST2.PNG)

* Após preencher e executar a função de teste, será enviado um e-mail de teste simples contendo um link onde ao clicar e responder o mesmo o Timeout será registrado e a SXM recriada em banco.

**Saiba mais**[Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Como configurar para uso o Workflow via Configurador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4446748107159)
