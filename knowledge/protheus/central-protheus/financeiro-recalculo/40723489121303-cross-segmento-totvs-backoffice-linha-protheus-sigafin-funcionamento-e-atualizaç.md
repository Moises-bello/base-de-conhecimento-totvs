---
article_id: 40723489121303
category: Financeiro - Recalculo
content_hash: a9d1327bbd8f64fab31964ce4f54454b3f8134ad6494a2e4f8b6384541595780
fetched_at: '2026-06-28T22:37:27.649867+00:00'
product: protheus
section_id: 35058632967831
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Funcionamento
  e atualização do campo Maior Atraso (A1_MATR)
type: support-article
updated_at: '2026-05-25T18:05:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40723489121303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Funcionamento-e-atualiza%C3%A7%C3%A3o-do-campo-Maior-Atraso-A1-MATR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40723489113751)** Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Como funciona a atualização do campo Maior Atraso (A1\_MATR) no cadastro de clientes? Títulos em aberto, mesmo que vencidos e sem baixa, são considerados no cálculo do maior atraso? O campo A1\_MATR representa o maior atraso já registrado em todo o histórico do cliente ou apenas o maior atraso atualmente vigente?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as releases  
  
**Solução**

O campo A1\_MATR armazena o maior atraso histórico já registrado em todo o histórico do cliente, e não o atraso atualmente vigente. Pagamentos realizados em dia subsequentes não zeram e não diminuem o valor contido neste campo.

Se o maior atraso registrado de um cliente foi de 30 dias e as suas últimas 10 compras foram pagas rigorosamente em dia, o campo continuará exibindo o valor "30". O conteúdo deste campo somente será alterado caso ocorra um novo atraso que seja superior ao recorde anterior (exemplo: 32 dias), passando então a exibir este novo recorde histórico.

A atualização do campo ocorre sob as seguintes regras de negócio:

* **Títulos em aberto:** Enquanto o título vencido não recebe a baixa efetiva, o atraso é considerado pelo sistema como "em andamento".
* **Consolidação do atraso:** O sistema só consolida e atualiza o período de atraso como concluído no cadastro do cliente após a quitação (baixa) do título.
* **Inadimplência atual:** Como o título ainda está em aberto, o sistema ignora estes títulos inadimplentes para fins de histórico no campo A1\_MATR. O cálculo do maior atraso exige obrigatoriamente a existência de uma data de quitação efetiva.

**Saiba Mais:**

[Maior atraso do cliente Campos A1\_MATR e A1\_PAGATR](https://tdn.totvs.com/pages/releaseview.action?pageId=1070065746)
