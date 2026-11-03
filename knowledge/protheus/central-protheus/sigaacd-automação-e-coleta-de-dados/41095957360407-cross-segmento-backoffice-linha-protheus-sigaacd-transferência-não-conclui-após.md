---
article_id: 41095957360407
category: SIGAACD - Automação e Coleta de Dados
content_hash: 508108a5248f6b2f0d53f335ae474a591bc072f87e07c64d3842f462e7155fbe
fetched_at: '2026-06-28T22:39:13.840739+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Transferência não
  conclui após atualização para a versão 3.1.14 do App Meu Coletor de Dados
type: support-article
updated_at: '2026-06-09T19:40:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41095957360407-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Transfer%C3%AAncia-n%C3%A3o-conclui-ap%C3%B3s-atualiza%C3%A7%C3%A3o-para-a-vers%C3%A3o-3-1-14-do-App-Meu-Coletor-de-Dados
---

Ao atualizar o app "Meu Coletor de Dados" para a versão 3.1.14, as transferências não concluem devido à ausência da função "validDelivery" no fonte ACDM010 até 30/01/2026. A solução é atualizar o pacote acumulado do BackOffice, disponível no link indicado, que inclui a função "validDelivery" com data de 24/04/2026.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41095985117975) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao atualizar o app "Meu Coletor de Dados" para a versão 3.1.14, as transferências não concluem.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Causa**  
Esse incidente ocorre por não existir a função "**validDelivery"**, que não se encontra no fonte ACDM010 até a data de 30/01/2026.   
  
**Solução**  
Para conseguir concluir a entrega da transferência, é necessária atualização do pacote acumulado do BackOffice. Para baixar o pacote, basta [**clicar aqui.**](https://tdn.totvs.com/pages/releaseview.action?pageId=522000602)

A partir da aplicação do pacote do link acima, o fonte ACDM010 ficará com a data de 24/04/2026 com a inclusão da função "**validDelivery"**.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
