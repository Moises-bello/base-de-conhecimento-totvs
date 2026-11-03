---
article_id: 360043765813
category: Manutenção de Ativos (SIGAMNT)
content_hash: 6765890a695ef5f78d84076538cc8dd7725b2b112414dbffe18cbfa0ca1c9596
fetched_at: '2026-06-28T22:42:32.809195+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Bloqueio de funcionário para insumos previstos
type: support-article
updated_at: '2021-06-01T20:03:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043765813-Manufatura-Linha-Protheus-MNT-Bloqueio-de-funcion%C3%A1rio-para-insumos-previstos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)**Tempo aproximado para leitura: **00:03:30 min**  
**Dúvida**Como funciona o **Bloqueio de Funcionário** para **Insumos Previstos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**O processo de **Bloqueio de Funcionário**tem como finalidade possibilitar a **Reserva de mão de obra** para determinada **Atividade** em uma **Ordem de Serviço**, pode-se fazer uma analogia com o processo de empenho de produtos, realizado pelo módulo de **Estoque**. Desta forma, este bloqueio alerta que o mesmo funcionário seja escalado em outras ordens de serviço no período no qual foi feito a reserva.   
Os bloqueios de funcionário por previsão podem ser realizados tanto pela inclusão de um insumo do tipo mão de obra em um **Ordem de Serviço**, como de forma manual, ou seja, sem vinculo com qualquer **Ordem de Serviço**, diretamente pela rotina **Bloqueio de Funcionário - MNTA160**, centralizando todos os bloqueios na tabela **STK - Bloqueio de Funcionário**.  
Desta forma ao incluir um insumo previsto do tipo mão de obra em uma **Ordem de Serviço**, independente da rotina utilizada, o período de definido para utilização deste insumo fica registrado como bloqueado. No exemplo, por meio da rotina **Programação de O.S. - MNTA990**foi realizado a inclusão de um insumo previsto do tipo mão de obra, com duração de uma hora.

![](https://tdn.totvs.com/download/attachments/535860421/image2020-2-19_13-49-32.png?version=1&modificationDate=1582130972550&api=v2)

Após o processo de gravação da **Ordem de Serviço**, o insumo do tipo mão de obra gerou de forma automática o registro de **Bloqueio de Funcionário**. Este pode ser visualizado na rotina **Bloqueio de Funcionário - MNTA160**. O registro de bloqueio contém todas as informações referentes a sua origem, como **Ordem de Serviço**, plano de manutenção e tarefa.

![](https://tdn.totvs.com/download/attachments/535860421/image2020-2-19_13-55-23.png?version=1&modificationDate=1582131324050&api=v2)

Outra forma de realizar a inclusão deste bloqueio, é diretamente pela rotina **Bloqueio de Funcionário - MNTA160**, desta forma o registro fica sem qualquer vinculo a uma **Ordem de Serviço**, entretanto é considerada igualmente quando verificado a disponibilidade do funcionário na convocação de uma nova **Atividade**. Segue abaixo um exemplo de bloqueio realizado de forma manual:

![](https://tdn.totvs.com/download/attachments/535860421/image2020-2-19_14-7-13.png?version=1&modificationDate=1582132034210&api=v2)

Ao realizar a tentativa de incluir um novo insumo referente a um funcionário já bloqueado, o Sistema emite um alerta, onde é informado a existência da reserva do funcionário para outra tarefa no mesmo período. Conforme o exemplo, no qual se refere ao bloqueio realizado de forma manual no exemplo anterior.

![](https://tdn.totvs.com/download/attachments/535860421/image2020-2-19_14-27-38.png?version=1&modificationDate=1582133258587&api=v2)

A mensagem de alerta apresentada ao usuário possibilita duas escolhas, a escolha de seguir com este conflito de disponibilidades do funcionário ou a escolha de voltar e reprogramar o horário do insumo que está reportando no momento. Nos casos onde se é optado por manter o conflito, é gerado automaticamente um registro na tabela **STA - Problemas com Ordens Serviço**, o qual pode ser consultado posteriormente na rotina  **Consulta Ordem de Serviço - MNTC790,**conforme imagem abaixo:

![](https://tdn.totvs.com/download/attachments/535860421/image2020-2-19_14-45-32.png?version=1&modificationDate=1582134332503&api=v2)

Os registros de **Bloqueio de Funcionários** gerados pela processo de previsão de insumos do tipo mão de obra ou inclusão na rotina **Bloqueio de Funcionário - MNTA160**, além de serem considerados em validações na inclusão de insumos previstos, também são levados em consideração nas seguintes consultas e relatórios:

* **Consulta de Ordens de Serviço - MNTC755**
* **Consulta de nivelamento de Mão de Obra****- MNTC815**
* **Consulta de Disponibilidade x Realizados - MNTC905**
* **Programação O.S. - MNTA990 ( Utilizado nos folders de insumos )**

**Saiba mais**Caso tenha dúvidas sobre o reporte de horas para insumos do tipo mão de obra acesse o artigo[MP - MNT - Reporte de horas para insumos realizados do tipo mão de obra](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043259194)
