---
article_id: 360028613772
category: CRM - Dúvidas Gerais
content_hash: 0721700a3a8c4bf7b9f78fd8d9431ec2355dba923e072b7e4c5c16d523bd8c3e
fetched_at: '2026-06-28T22:40:27.497767+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Posição do Cliente - Seleção
  das Filiais para o Histórico de Cobrança
type: support-article
updated_at: '2024-04-25T12:16:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028613772-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Posi%C3%A7%C3%A3o-do-Cliente-Sele%C3%A7%C3%A3o-das-Filiais-para-o-Hist%C3%B3rico-de-Cobran%C3%A7a
---

**Dúvida**

As informações apresentadas no **Histórico de Cobrança** refletem apenas à Filial Ativa em uso (logada), não apresentando assim, as informações das demais filiais selecionadas pelo usuário.

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12

**Solução**

Após a aplicação do patch de atualização :  [**https://suporte.totvs.com/portal/p/10098/download?e=752637**,](https://suporte.totvs.com/portal/p/10098/download?e=752637)deste requisito, e da configuração do parâmetro **MV\_HCOBMFL** em seu ambiente, a apresentação da tela da **Consulta do****Histórico de Cobrança** possuirá dois possíveis comportamentos.

Com o parâmetro **MV\_HCOBMFL** configurado como **.F.** (*Default*), o comportamento da **Consulta do****Histórico de Cobrança** apresentará apenas os Atendimentos de Cobrança do cliente na filial logada, ignorando assim os **Atendimentos de Cobrança** das demais filiais selecionadas na tela de **Seleção de Filiais** da **Posição de Clientes**.

Com o parâmetro **MV\_HCOBMFL** configurado como **.T.**, o comportamento da **Consulta do****Histórico de Cobrança** apresentará os Atendimentos de Cobrança do cliente em todas as filiais selecionadas na tela de **Seleção de Filiais** da **Posição de Clientes**.

Detalhes em :**<http://tdn.totvs.com/pages/releaseview.action?pageId=489771455>**
