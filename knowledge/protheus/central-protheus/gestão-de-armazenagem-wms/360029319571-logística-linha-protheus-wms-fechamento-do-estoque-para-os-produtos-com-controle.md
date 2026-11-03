---
article_id: 360029319571
category: Gestão de Armazenagem (WMS)
content_hash: 687094e33a6d371995b6f7c56e297829a2c6700a84d09d18be6af98f8c76c358
fetched_at: '2026-06-28T22:45:48.033859+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Fechamento do estoque para os produtos com
  controle WMS
type: support-article
updated_at: '2021-07-20T19:28:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029319571-Log%C3%ADstica-Linha-Protheus-WMS-Fechamento-do-estoque-para-os-produtos-com-controle-WMS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)***Tempo aproximado para leitura:**00:01:06 min****Dúvida**Como funciona o fechamento do estoque para os produtos com controle **WMS** *-* **Warehouse Management System**?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) – A partir da versão 12  
  
**Solução**O fechamento do **WMS** é realizado juntamente com a virada de saldos do estoque, a qual é processada por meio da rotina **MATA280 - Virada dos Saldos**.   
  
Durante o procedimento, se o parâmetro **MV\_WMSNEW - Utiliza novo conceito WMS (Movimentações e Estoque por Endereço)** estiver ativo, a tabela de saldos iniciais por endereço gerada é a **D15 - Saldos Iniciais Endereco WMS**.  
  
O processamento da virada de saldos pode ser efetuado via *procedure* ou função **ADVPL**, sendo que ambas se baseiam nas movimentações do kardex, **D13 - Movto Estoque Por Endereço WMS**, para compor o saldo do produto no endereço do período informado.  
  
**Saiba mais**  
O procedimento para realizar o fechamento do estoque para os produtos com controle **WMS** está descrito em: [Funcionamento do Fechamento do Estoque Para os Produtos Com Controle WMS](http://tdn.totvs.com/display/PROT/Funcionamento+do+Fechamento+do+Estoque+Para+os+Produtos+Com+Controle+WMS)
