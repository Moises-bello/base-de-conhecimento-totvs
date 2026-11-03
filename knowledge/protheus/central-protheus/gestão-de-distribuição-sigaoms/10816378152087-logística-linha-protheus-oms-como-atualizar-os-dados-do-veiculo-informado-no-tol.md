---
article_id: 10816378152087
category: Gestão de Distribuição (SIGAOMS)
content_hash: f3b5ee4b1f18f14fcfdf120df58a246400e7bb3815e5e3f2a30c2adaee667487
fetched_at: '2026-06-28T22:45:49.607062+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: 'Logística - Linha Protheus - OMS - Como atualizar os dados do Veiculo informado
  no TOL/TRE no TOTVS OMS '
type: support-article
updated_at: '2022-12-08T18:28:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10816378152087-Log%C3%ADstica-Linha-Protheus-OMS-Como-atualizar-os-dados-do-Veiculo-informado-no-TOL-TRE-no-TOTVS-OMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:56 min** **Dúvida**Como atualizar os dados do Veiculo informado no **TOL/TRE** no **Protheus TOTVS OMS**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) -Todas as versões  
  
**Solução**O **TOL/TRE** envia as viagens geradas para o **TOTVS OMS**, para a formação das **cargas**, sendo que o envio é realizado pela chamada do **Web Service ReleaseTripPublishRequestService**. Segue exemplo do arquivo **XML**:

![xml_kcs.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/10817443065495)

Para isso, foi disponibilizada a rotina **OMSXCPL7-Monitor de Cargas**, que será responsável pelo gerenciamento das cargas em questão.  
  
Ao receber uma viagem do **TOL/TRE**,  para o preenchimento do **campo Placa Veic - DK0\_PLACA** será realizada uma busca pela **placa do veiculo** no **cadastro de veículos  - tabela DA3** no **TOTVS OMS**.

![VEICULO.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/10817460492183)

Se encontrado algum registro, o **veículo será associado a carga**. Para que isso ocorra é essencial que a **Placa** recebida do **TOL/TRE** seja idêntica a **Placa** cadastrada no **TOTVS OMS**.  
  
No **TOL/TRE** o veiculo é informado na opção de **Edição de Viagem**, conforme exemplo abaixo:

![edicao_viagem_tol.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/10817519955095)

**Saiba mais**Mais informações poderão ser acessadas no *link*:  
[Integração TOTVS OMS x TOTVS Otimização Logística - Planejamento](https://tdn.totvs.com/pages/releaseview.action?pageId=268801735)  
  
**Glossário**  
**TOL**- TOTVS Otimização Logística  
**TRE**- TOTVS Roteirização e Entrega **TOTVS OMS**- Order Management System
