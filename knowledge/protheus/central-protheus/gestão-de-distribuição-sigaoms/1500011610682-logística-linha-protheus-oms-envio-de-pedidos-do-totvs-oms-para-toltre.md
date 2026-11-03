---
article_id: 1500011610682
category: Gestão de Distribuição (SIGAOMS)
content_hash: e1e7a6c644f21e6eb048a72bc3cde655b655c634852aee87b916201ad53c5af7
fetched_at: '2026-06-28T22:45:49.804293+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Envio de Pedidos do TOTVS OMS para TOL/TRE
type: support-article
updated_at: '2024-06-04T19:15:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011610682-Log%C3%ADstica-Linha-Protheus-OMS-Envio-de-Pedidos-do-TOTVS-OMS-para-TOL-TRE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23949938263575)**Tempo aproximado para leitura: **00:04:48 min**  
**Dúvida**Como realizar o **Envio de Pedidos - OMSXCPL6** do **TOTVS OMS**  para **TOL/TRE**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Ao cadastrar um **Pedido de venda - MATA410**, quando a integração estiver ativa, os dados são enviados ao **TOL/TRE**, utilizando a rotina **Envio de Pedidos de Venda - OMSXCPL6,** localizada em **Atualizações/Cockpit****Logístico** por meio do método **OrderAcquisitionService.**

**![omsxcpl6.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019264622)**

Após os pedidos de vendas integrados ao **TOL/TRE****,** serão criados **pedidos de transporte** e poderão ser visualizados em: **Programação - Analise**, deve-se filtrar os dados da **Cesta Geral**.  
  
No **TOTVS OMS**, as principais funcionalidades da rotina **Envio de Pedido de Venda - OMSXCPL6**, são:

* Envio de pedidos Completos ou Parciais
* Cancelamentos de Pedidos Completos ou Parciais
* Envio de Pedidos via *Schedule*

A rotina **Envio de Pedidos de Venda - OMSXCPL6**, permite selecionar uma lista com os pedidos de venda para envio ao **TOL/TRE**, sendo que estes pedidos são filtrados conforme as seguintes premissas:

* O pedido deve montar carga, preencher o campo **Carga - C5\_TPCARGA** igual a **1-Utiliza**.
* O pedido não deve estar faturado, o campo **Nota Fiscal - C9\_NFISCAL**, deverá estar **em branco**.
* Não deve possuir **carga** gerada pelo **TOTVS OMS**.
* O pedido deve respeitar o range de dados dos filtros da rotina.
* Para não permitir o envio de pedidos sem liberação, o parâmetro **MV\_CPLPELB** deverá estar **igual a 2.** Os pedidos não devem possuir bloqueios de **estoque**, campo **Bloqueio Estoque - C9\_BLEST** e **crédito** campo **Bloqueio Credito - C9\_BLCRED**.
* Para permitir o envio de pedido sem liberação, o parâmetro **MV\_CPLPELB** deverá estar **igual a 1.** Será permitido o envio de toda a quantidade do pedido campo **Quantidade Vendida - C6\_QTDVEN**, mesmo que existam bloqueios.
* Pedidos que ainda não foram completamente enviados, campo **Status da Integração - C6\_INTROT** igual a **1-Não integrado** ou **4-Integrado Parcialmente**.

Após os pedidos serem filtrados, a rotina **Envio de Pedido de Venda - OMSXCPL6**  ainda permite alterar as quantidades para a integração pelo botão **Alterar Quantidade da Integração - F10**, sendo que, por seu intermédio é possível informar quais quantidades do pedido serão integradas, onde cada integração do pedido gera uma **sequência de integração diferente**.  
  
**Filtros da rotina de envio:  
Filial de / até**   
**Pedido de / até**   
**Emissão de / até**   
**Data liberação de / até**   
**Cliente de / até**  
**Loja de / até**   
**Data de entrega de / até**   
**Tipo de pedido de venda** - Com base no campo **Tipo Pedido - C5\_TIPO**   
**Estado de entrega de / até** - Com base no estado do fornecedor - campo **Estado - A2\_EST** e cliente - campo **Estado - A1\_EST**   
**Município de entrega de / até** - Com base no município do fornecedor - campo **Código do Município - A2\_COD\_MUN** e cliente - campo **Código do Município - A1\_COD\_MUN**   
**Status integração** - Com base no campo **Status da Integração - C6\_INTROT**   
**Tipo de frete** - Com base no campo **Frete - C5\_TPFRETE**  
**Pedido totalmente liberado** - Se marcado como **sim** apresenta somente pedidos totalmente liberados e sem bloqueios.  
  
As **tabelas e campos** envolvidos no processo de **envio de pedidos** são:  
  
**DK3 - Sequência de Integração CPL - Pedidos  
DK3\_FILIAL** - Filial do Sistema   
**DK3\_ITEMPE** - Item do Pedido de Venda   
**DK3\_PEDIDO** - Pedido de Venda   
**DK3\_PRODUT** - Código do Produto   
**DK3\_QTDINT** - Quantidade Integração   
**DK3\_SEQUEN** - Sequência de Integração   
**DK3\_STATUS** - Status da Integração, sendo 1-Integrado; 2-Cancelado; 3-Cancelado Parcial  
**DK3\_VIAGID** - Identificador Viagem **TOL/TRE**  
 **SC6 - Itens dos Pedidos de venda  
C6\_INTROT** - Status da Integração, sendo 1-Não Integrado; 2-Integrado;3-Falha de Integração;   
4-Integrado Parcial  
**C6\_DATCPL** - Data da Integração  
**C6\_HORCPL** - Hora da Integração  
  
**Saiba mais**Mais informações poderão ser acessadas nos *link's*:   
[Envio de Pedidos de Venda - OMSXCPL6](https://tdn.totvs.com/pages/viewpage.action?pageId=549492947)[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Como habilitar geração de arquivo de LOGs na integração do TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060684834-MP-OMS-Como-habilitar-gera%C3%A7%C3%A3o-de-arquivo-de-LOG-na-integra%C3%A7%C3%A3o-do-SIGAOMS-x-Cockpit-Log%C3%ADstico-Neolog)  
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na Integração TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003568682-MP-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-Integra%C3%A7%C3%A3o-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
