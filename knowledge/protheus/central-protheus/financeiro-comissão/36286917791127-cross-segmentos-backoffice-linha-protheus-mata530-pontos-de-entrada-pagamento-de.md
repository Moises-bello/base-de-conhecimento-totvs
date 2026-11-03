---
article_id: 36286917791127
category: Financeiro - Comissão
content_hash: bbebf3233d783832a0646eb792e967e37610effa23f9cb6068f387db005eee21
fetched_at: '2026-06-28T22:37:50.782630+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - MATA530 - Pontos de entrada Pagamento
  de comissão
type: support-article
updated_at: '2026-02-03T18:05:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36286917791127-Cross-Segmentos-Backoffice-Linha-Protheus-MATA530-Pontos-de-entrada-Pagamento-de-comiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36286917776151) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Quais são os pontos de entrada disponíveis na rotina **MATA530 – Atualização de Pagamento de Comissões**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
A seguir, apresenta-se a relação dos **pontos de entrada** disponíveis na rotina **Atualização de Pagamento de Comissões (MATA530)**:

* **MSE2530** – Executado antes da atualização do arquivo **SE2 (Contas a Pagar)** e antes da geração dos **lançamentos contábeis**.  
  Documentação: <https://tdn.totvs.com/x/PIVn>
* **M530AGL** – Responsável pela aplicação de **filtros nas condições selecionadas**.  
  Documentação: <https://tdn.totvs.com/x/AYZn>
* **M530TIT** – Permite a **manipulação dos dados do título** durante o processamento.  
  Documentação: <https://tdn.totvs.com/x/AoZn>
* **M530FIM** – Utilizado para a **atualização de datas** ao final do processo.  
  Documentação: <https://tdn.totvs.com/x/z4Vn>
* **M530DIRF** – Responsável pelo **preenchimento dos campos referentes à DIRF** no pagamento de comissões.  
  Documentação: <https://tdn.totvs.com/x/MgHnAg>
* **M530OK** – Realiza a **atualização final do pagamento de comissões**.  
  Documentação: <https://tdn.totvs.com/x/PIZn>

  **Saiba mais**

  [Financeiro - Comissão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/26655771327895-Financeiro-Comiss%C3%A3o)
