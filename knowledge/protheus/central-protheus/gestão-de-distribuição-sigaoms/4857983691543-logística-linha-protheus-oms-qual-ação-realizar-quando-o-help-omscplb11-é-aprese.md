---
article_id: 4857983691543
category: Gestão de Distribuição (SIGAOMS)
content_hash: c092a22f5370c2e4bd0ade1a1c0aa7d6eb184b5bdc86c24416f5581fee5d4561
fetched_at: '2026-06-28T22:45:50.110114+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Qual ação realizar quando o help OMSCPLB11
  é apresentado no Estorno de Documento
type: support-article
updated_at: '2022-12-26T11:11:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4857983691543-Log%C3%ADstica-Linha-Protheus-OMS-Qual-a%C3%A7%C3%A3o-realizar-quando-o-help-OMSCPLB11-%C3%A9-apresentado-no-Estorno-de-Documento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**No módulo **TOTVS OMS - Order Management System**, ao realizar o estorno de uma quantidade que não será mais faturada, é apresentado o *help* **OMSCPLB11-O pedido XYZ possui quantidade comprometida com o Cockpit Logístico. Desfaça a integração antes de estornar a liberação do pedido**.  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Causa**Esse incidente ocorre, pois é necessário **Cancelar** a **Integração** no **TOL - TOTVS Otimização Logística** para o **Pedido de Venda** vinculado ao **Documento** que deseja **Estornar** na rotina **Preparação dos Documentos de Saída - MATA460A.****Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse a rotina **Exclusão Documento de Saída - MATA521A**, selecione o documento que será excluído. Verifique o preenchimento do **Parâmetro F12**, pergunte **Retornar Ped. Venda?**
2. Acesse a rotina **Envio de Pedidos - OMSXCPL6**, selecione o **Pedido de Venda** que deverá ser  Cancelada  a Integração no **TOL**. Para realizar o Cancelamento a  rotina possui  os botões de **Desatualizar Pedido Posicionado - F4** ou **Outras ações/Desatualizar Pedido Posicionado - F2**. Mais informações poderão ser acessadas no *link:* [Logística - Linha Protheus - OMS - Cancelamento de Pedidos de Venda integrados ao](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012128902-Log%C3%ADstica-Linha-Protheus-OMS-Cancelamento-de-Pedidos-de-Venda-integrados-ao-TOL) [TOL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012128902-Log%C3%ADstica-Linha-Protheus-OMS-Cancelamento-de-Pedidos-de-Venda-integrados-ao-TOL)
3. Acesse a rotina **Preparação Documento Saída - MATA460A**, selecione o documento excluído, em **Outras ações/Estornar Doc's Saída**
4. Acesse a rotina **Pedido de Venda - MATA410**, selecione o **Pedido de Venda** referente o documento excluído, em **Outras ações/Excluir/Resíduo**. O **Pedido de Venda** será atualizado com o *status* igual a **Encerrado**.

Abaixo segue exemplo de utilização demonstrados com *print's* das rotinas citadas:  
  
Consulta da **Viagem**, onde esta Viagem contém **2 Pedidos de Venda**:

![TOL1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/6802328619671/TOL1.JPG)

Para essa **Viagem**, com 2 Pedidos de Vendas, **foram geradas 2 documentos**:

![TOL2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/6802408324119/TOL2.JPG)

Na rotina **Exclusão Documento de Saída - MATA521A**, selecione o documento que será excluído:

![TOL3.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/6802449650327/TOL3.JPG)

Na rotina **Envio de Pedidos - OMSXCPL6**, selecione o **Pedido de Venda** que deverá ser  Cancelada  a Integração no **TOL:**

**![TOL4.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/6802474960535/TOL4.JPG)**

Na rotina **Preparação Documento Saída - MATA460A**, selecione o documento excluído, em **Outras ações/Estornar Doc's Saída:**

**![TOL5.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/6802517478423/TOL5.jpg)**

Na rotina **Pedido de Venda - MATA410**, selecione o **Pedido de Venda** referente o documento excluído, em **Outras ações/Excluir/Resíduo:**

**![TOL6.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/6802592294167/TOL6.jpg)**

O **Pedido de Venda** será atualizado com o *status* igual a **Encerrado:**

**![TOL7.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/6802584698007/TOL7.JPG)**

**Consulta da Viagem** no **TOL**, o **Pedido de Venda** que teve a sua **integração Cancelada no TOL** pela rotina **Envio de Pedidos - OMSXCPL6** , deixou de existir na **Viagem 54211**:

**![TOL8.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/6802769048599/TOL8.JPG)**

**Saiba mais**  
Mais informações poderão ser acessadas nos *link's*:   
[Logística - Linha Protheus - OMS - Envio de Pedidos do TOTVS OMS x TOL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011610682-MP-OMS-Envio-de-Pedidos-do-TOTVS-OMS-para-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)
