---
article_id: 19026224618135
category: Gestão de Distribuição (SIGAOMS)
content_hash: bd62afca89be5a13ad52f67b626b7358274bd502b578806d4a5c8441c5f599a1
fetched_at: '2026-06-28T22:45:49.750227+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como tratar a mensagem PickUpWinStartIsAfterEnd
  no envio do Pedido de Vendas para TOL/TRE
type: support-article
updated_at: '2024-01-04T17:39:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19026224618135-Log%C3%ADstica-Linha-Protheus-OMS-Como-tratar-a-mensagem-PickUpWinStartIsAfterEnd-no-envio-do-Pedido-de-Vendas-para-TOL-TRE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19026229558423) Tempo aproximado para leitura: **00:02:18 min** **Dúvida**Como tratar a mensagem **PickUpWinStartIsAfterEnd** no envio do **Pedido de Vendas** para **TOL/TRE?****Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Ao enviar **Pedido de Vendas** pela rotina **OMSXCPL6** para **TOL/TRE,** o Sistema valida o preenchimento de **Datas** que irão compor as seguintes *tag's* no **XML do Pedido de Vendas**, são elas:

* **DeliveryEnd**: Data de Entrega  
  Essa *tag* é alimentada com a data informada no campo **Data de Entrega - C5\_FECENT** no **cabeçalho** do Pedido de Venda ou no campo **Data da** **Entrega - C6\_ENTREG**, localizado no **item** do Pedido de Venda.
* **ErpCreationDt**: Data de Emissão   
  Essa *tag* é alimentada com a data informada no campo **Data da Emissao - C5\_EMISSAO**, localizado no **cabeçalho** do Pedido de Venda.   
  Temos o parâmetro **MV\_CPLDTPD**, para definir qual Data deverá ser considerada. O parâmetro poderá ser configurado com as seguintes opções:  
  **1 = Data Atual**  
  **2 = Data de Emissão do Pedido**
* **PickupStart**: Inicio da Operação/Coleta  
  Essa *tag* é alimentada com a data informada no campo **Data Inicio de Embarque -** **C6\_DATAEMB**, localizado no **item** do Pedido de Venda, caso esteja em branco, irá gravar a data atual do Sistema. A hora é fixa igual a 00:01:00.

Segue exemplo, onde a **Data de Entrega é menor que  a Data de Emissão**. Nesse exemplo ocorre rejeição pelo **TOL/TRE**:

**MV\_CPLDTPD** = 2 Data de Emissão do Pedido    
**Data Atual do Sistema**: 20/12/2023  
**Data da Emissao - C5\_EMISSAO**:20/12/2023  
**Data de Entrega - C5\_FECENT**:19/12/2023  
**Data da Entrega - C6\_ENTREG**:21/12/2023  
**Data Inicio de Embarque - C6\_DATAEMB**:20/12/2023  
  
**Envio de Pedidos - OMSXCPL6**, apresenta a rejeição **PickUpWinStartIsAfterEnd**:

![erro.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/20005201819031)

Como o **XML** de integração foi gerado:

![xml.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/20005218008471)

Após corrigir a **Data de Entrega para 22/12/2023**, o Pedido de Venda foi integrado:

**![integrado.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/20005201842583)**

Como o **XML** de integração foi gerado:

**![xml ok.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/20005218021143)**

**Saiba mais**Mais informações poderão ser acessadas no *link* abaixo:  
[Logística - Linha Protheus - OMS - Envio de Pedidos do TOTVS OMS para TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011610682-Log%C3%ADstica-Linha-Protheus-OMS-Envio-de-Pedidos-do-TOTVS-OMS-para-TOL-TRE)  
  
**Glossário****TOL** - TOTVS Otimização Logística  
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
