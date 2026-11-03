---
article_id: 360037256314
category: Gestão de Frotas
content_hash: fc12fc8d39724c7e1d2af3e55e9b0548cb5f65c546738ff771468768c5d273a1
fetched_at: '2026-06-28T22:42:39.590602+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Rotina Status
type: support-article
updated_at: '2021-05-05T18:44:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037256314-Manufatura-Linha-Protheus-MNT-Rotina-Status
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:15 min**  
**Dúvida**Para que serve a rotina **Status  - MNTA710**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Solução**Essa rotina serve para cadastrar os **Status** para as categorias **Bem**, **Veículo integrado ao TMS**, **Pneu** e **Veículos sem integração**. Esses status serão atribuídos aos bens durante o processo de operação. Para que nos diversos pontos do Sistema seja possível a checagem e mudança de status para um bem da categoria **Pneu**, é necessário configurar um parâmetro específico e o código do status cadastrado. Abaixo, segue os status x parâmetro que devem estar associados ao bem:  
  
**Pneu em** **Estoque** - **MV\_NGSTEST**  
**Pneus em** **Transito** - **MV\_NGSTATR**  
**Aguardando Analise Técnica** - **MV\_NGSTAAT**  
**Removido de Serviço** - **MV\_NGSTARS**  
**Aguardando Reforma** - **MV\_NGSTAGR**  
**Aguardando Conserto** - **MV\_NGSTAGC**  
**Pneu Aplicado** - **MV\_NGSTAPL**  
**Estoque Novo** - **MV\_NGSTAEN**  
**Estoque Usado** - **MV\_NGSTAEU**  
**Estoque Reformado** - **MV\_NGSTAER**.  
  
**Importante**  
Por exemplo, se o código do **Status** para **pneu em estoque** for **001**, o parâmetro **MV\_NGSTEST** deverá ser igual a **001**.
