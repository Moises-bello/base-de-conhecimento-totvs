---
article_id: 360021137052
category: Inspeção de Processos (SIGAQIP)
content_hash: 356a81a6eae09108331ef016cb8e774d86f33b951b4fd518f9d0561d896fa972
fetched_at: '2026-06-28T22:42:25.674215+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Bloqueio da liberação do produto no
  CQ antes da liberação do laudo
type: support-article
updated_at: '2022-07-15T14:52:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021137052-Manufatura-Linha-Protheus-SIGAQIP-Bloqueio-da-libera%C3%A7%C3%A3o-do-produto-no-CQ-antes-da-libera%C3%A7%C3%A3o-do-laudo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:50 min  
  
Dúvida**Como impedir que o produto seja liberado do **CQ - Controle de Qualidade** pela rotina **MATA175 - Baixas do CQ** antes da liberação do laudo na rotina **QIPA215 - Cadastro de Resultados**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**Atualmente não existe nenhum bloqueio de estoque no módulo **SIGAQIP - Inspeção de Processos**. O produto é direcionado para a **Inspeção** pelo **SIGAQIP**, porém a baixa de **CQ** é realizada pelo módulo de Estoque. Mesmo que não exista laudo, a baixa de **CQ** poderá ser realizada.  
  
**Saiba mais**  
Caso desejar implementar uma validação no **MATA175**, poderá ser avaliado os pontos de entrada abaixo:  
[MT175FOK - Valida a linha do baixas do CQ](https://tdn.totvs.com/display/public/PROT/MT175FOK+-+Valida+a+linha+do+baixas+do+CQ)[MT175ATU - LiberaçãoRejeição de Material](https://tdn.totvs.com/pages/releaseview.action?pageId=6802946)
