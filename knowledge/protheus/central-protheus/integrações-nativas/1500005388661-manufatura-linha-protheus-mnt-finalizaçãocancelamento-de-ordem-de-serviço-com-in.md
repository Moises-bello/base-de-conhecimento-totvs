---
article_id: 1500005388661
category: Integrações Nativas
content_hash: a4c97383fc0b31cfe8f2e564948f236aed14ca9ff587d2617aa5d09137395979
fetched_at: '2026-06-28T22:42:35.410131+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Finalização/Cancelamento de ordem de serviço
  com insumos vinculados a uma solicitação de armazém
type: support-article
updated_at: '2022-04-14T17:08:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005388661-Manufatura-Linha-Protheus-MNT-Finaliza%C3%A7%C3%A3o-Cancelamento-de-ordem-de-servi%C3%A7o-com-insumos-vinculados-a-uma-solicita%C3%A7%C3%A3o-de-armaz%C3%A9m
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)** Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Como é o comportamento do processo de finalização e cancelamento de **O.S** - **Ordens de Serviço** que possuem um ou mais insumos atrelados a **S.A - Solicitação de Armazém**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Versão 12  
  
**Solução**Seguem os comportamentos de cancelamento e finalização de uma **O.S** com insumos vinculados a uma **S.A.**:  
**Cancelamento**Para o cancelamento da **O.S** é necessário que a **S.A** não possua uma pré-requisição. Caso possua, o Sistema apresenta um alerta, e será necessário realizar a exclusão da mesma e posteriormente prosseguir com o cancelamento da **O.S**. Ao confirmar o cancelamento todos os insumos previstos serão excluídos juntamente com as **S.A's** associadas.  
 **Finalização**No processo de finalização da **O.S** não será verificado se os insumos previstos que contenham **S.A**, já tiveram a pré-requisição gerada. Assim a finalização pode ser confirmada sem qualquer impedimento. Contudo as **S.A** não baixadas são mantidas após a finalização da **O.S**, assim possibilitando que a mesma gere uma pré-requisição e efetue a aplicação na ordem de serviço mesmo após sua finalização.   
  
**Saiba mais**Para informações complementares, verifique o *link* [Reporte de insumos aplicados por meio do módulo Estoque/Custos - SIGAEST](https://tdn.totvs.com/pages/viewpage.action?pageId=560639677)
