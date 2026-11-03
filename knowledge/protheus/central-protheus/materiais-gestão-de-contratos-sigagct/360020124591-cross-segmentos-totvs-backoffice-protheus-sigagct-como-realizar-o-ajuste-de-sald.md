---
article_id: 360020124591
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: ffbf316afa3164ac9d17a8eb8a168125661aabee26fb232d217e90c7fb62e7b2
fetched_at: '2026-06-28T22:37:20.025750+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar o Ajuste
  de Saldos em Contratos, Planilhas e Cronograma Financeiro ?
type: support-article
updated_at: '2026-01-23T14:00:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020124591-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-o-Ajuste-de-Saldos-em-Contratos-Planilhas-e-Cronograma-Financeiro
---

**Dúvida**

Como realizar o Ajuste ou Recálculo de Saldos em Contratos, Planilhas e Cronograma Financeiro ( CNTA320 )?

**Ambiente**

Protheus – Gestão de Contratos – A partir da versão 12.1.17

**Solução**

A rotina de Ajuste de Saldos, tem o objetivo de efetuar ajustes dos saldos do contrato, suas planilhas e cronograma financeiro caso estejam divergentes com as medições realizadas.

Pode ser utilizada caso existam problemas de saldos dos contratos para o seu recalculo conforme as movimentações existentes do contrato.

Para utilizar a rotina acesse a rotina Ajuste de Saldo (CNTA320) e informe os parâmetros informando:

- Contrato De?

- Contrato Até ?

Ao clicar em OK o sistema irá iniciar os processos para ajuste de saldos do contrato. Somente serão alterados os contratos que possuírem divergência entre as medições.

Primeiramente o sistema irá verificar as medições já realizadas para o contrato. Após esta análise o sistema irá verificar se o saldo do item está de acordo com as medições já realizadas, se sim, nenhuma alteração é realizada, caso contrário é efetuado o ajuste.

Além dos contratos vigentes, o sistema também considera os contratos em elaboração, recalculando seus totalizadores caso exista alguma inconsistência na base de dados.

Verificar o artigo abaixo com informações mais detalhadas sobre sua execução.

[GCT0130 - Ajustes de Saldos](https://tdn.totvs.com/pages/viewpage.action?pageId=968132056)

***Atenção!***

Por padrão a rotina processa apenas contratos com Medição Eventual igual a Não (**MV\_320SLD = 1**), para processar contratos com Medição Eventual = Sim e Fixos configure o parâmetro **MV\_320SLD = 2**.

Para criação do parâmetro, verificar documentação da issue referente no link abaixo:

[14208517 DMANMAT02-38264 DT Ajustes de Saldos de contratos eventuais](https://tdn.totvs.com/x/u19NKQ)

***Obs1:***

No ajuste ou recálculo dos saldos do contrato (CNTA320) serão considerados os valores no contrato de medições realizadas, para ajuste dos valores de cronograma, considerando também descontos, e ajustando os saldos de planilhas e contrato.

***Obs2:***

Na rotina de Ajuste de Saldos CNTA320, não possui funcionalidade para contratos Flexíveis do artigo abaixo, que não possuem itens na planilha do contrato:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a inclusão de um Contrato Flexível ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037640253-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-inclus%C3%A3o-de-um-Contrato-Flex%C3%ADvel)

***Saiba Mais:***

[GCT0130 - Ajustes de Saldos](https://tdn.totvs.com/pages/viewpage.action?pageId=968132056)

[14208517 DMANMAT02-38264 DT Ajustes de Saldos de contratos eventuais](https://tdn.totvs.com/x/u19NKQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
