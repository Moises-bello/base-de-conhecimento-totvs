---
article_id: 360043259194
category: Manutenção de Ativos (SIGAMNT)
content_hash: 33460f51384e9b6b42ca286ea0d005c244b2a91804284052fb5cdad2384dcd58
fetched_at: '2026-06-28T22:42:34.391273+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Reporte de horas para insumos realizados
  do tipo mão de obra
type: support-article
updated_at: '2021-09-21T20:58:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043259194-Manufatura-Linha-Protheus-MNT-Reporte-de-horas-para-insumos-realizados-do-tipo-m%C3%A3o-de-obra
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)**Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como funciona o **Reporte de Horas** para insumos realizados do tipo mão de obra?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - A partir da versão 12  
  
**Solução**O processo de **Reporte de Horas** para mão de obra tem como finalidade possibilitar o lançamento de um consumo daquela mão de obra para determinada atividade, seja ela **produtiva** ou **improdutiva**. Sendo que este reporte em nenhum momento tem relação com o processo de **previsão** e **bloqueio de funcionários**. Porém de forma semelhante ao bloqueio, o reporte de horas apresenta alertas ao tentar aplicar um insumo referente a um funcionário que já tenha um reporte vinculado. Este processo pode ser realizado somente diretamente pela rotina **Reporte de Horas da Mão de Obra - MNTA992**, centralizando todos estes lançamento na tabela **TTL - Reporte de Horas da MDO**.  
Desta forma ao incluir um **Reporte de Mão de Obra** o período informado fica registrado como já atuado. Note que no exemplo, por meio da rotina de reporte foi realizado a inclusão de um registro com duração de 30 minutos.

![image2020-2-19_15-55-32.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059410433/image2020-2-19_15-55-32.png)

Na tentativa de incluir um novo insumo referente a um funcionário já reportado, o Sistema emite uma alerta, no qual é informado a existência de um reporte do funcionário para o mesmo período. Conforme exemplo a seguir, no qual se refere ao reporte realizado no exemplo anterior. Sendo este alerta impeditivo para continuidade do processo, assim se torna obrigatória a necessidade de reprogramar este insumo.

![image2020-2-19_15-58-7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058506194/image2020-2-19_15-58-7.png)

Os registros de reporte gerados pela rotina **Reporte de Horas da Mão de Obra - MNTA992**, além de serem considerados em validações na inclusão de insumos realizados, também são levados em consideração na seguinte consulta e relatório:

* **Consulta Gerencial de Mão de Obra - MNTC400**
* **Consulta de Disponibilidade de Funcionários - MNTC415**

**Saiba mais**Caso tenha dúvidas sobre o bloqueio de funcionário acesse o *link*: [Bloqueio de funcionário para insumos previstos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043765813)
