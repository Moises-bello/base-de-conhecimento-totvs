---
article_id: 38948008372759
category: Financeiro - Novo Gestor Financeiro
content_hash: 0bd64b0f62b8cff0f39a775f64da63d11f772caf6a52804de66178734e3d9b3c
fetched_at: '2026-06-28T22:37:41.521487+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA717 - Execução job travada
  em uma filial
type: support-article
updated_at: '2026-03-12T11:37:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38948008372759-Cross-Segmento-Backoffice-Linha-Protheus-FINA717-Execu%C3%A7%C3%A3o-job-travada-em-uma-filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38948008366487) Tempo aproximado para leitura: **00:09 min**  
  
**Ocorrência**  
Ao executar a rotina **FINA717** via schedule, o sistema entra em um loop realizando diversas tentativas de posicionamento em um registro da tabela **SEA**, ocasionando travamento no processamento. Como consequência, novos jobs deixam de ser executados e a transmissão dos dados precisa ser realizada manualmente.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Esse comportamento pode ocorrer devido às permissões de acesso associadas ao usuário utilizado para execução do job, mesmo quando a configuração está corretamente configurada.

Para que a rotina **FINA717** consiga realizar corretamente a leitura e o processamento das informações entre as diferentes filiais, é necessário que o job seja configurado por grupo de empresas e selecionando apenas uma filial do grupo, além disso é necessário que o usuário responsável pela execução possua habilitadas no sistema as permissões abaixo no controle de acesso por grupo:

* **196 – Filtro - Visualiza outras filiais**
* **197 – Filtro - Visualiza outras Unidades de Negócio**
* **198 – Filtro - Visualiza outras Empresas**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38948008367895)

Quando essas permissões não estão habilitadas, o sistema restringe a visualização e o acesso aos dados de outras filiais. Como consequência, durante a execução do job o processamento pode apresentar comportamentos como tentativas repetidas de posicionamento em registros da tabela **SEA**, ocasionando loop no processamento e impedindo a execução correta da rotina.

Dessa forma, orienta-se validar as permissões do usuário configurado para execução do schedule, garantindo que os acessos mencionados estejam devidamente habilitados. Após o ajuste, o processamento da rotina tende a ocorrer normalmente, considerando todas as estruturas necessárias para a transmissão das informações.

**Saiba Mais:**

[**Configuração dos Jobs (Comunicação bancaria online)**](https://tdn.totvs.com/pages/releaseview.action?pageId=667370586)
