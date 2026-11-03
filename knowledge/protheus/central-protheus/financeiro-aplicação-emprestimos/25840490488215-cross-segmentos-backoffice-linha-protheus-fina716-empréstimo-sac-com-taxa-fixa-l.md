---
article_id: 25840490488215
category: Financeiro - Aplicação / Emprestimos
content_hash: 46c5485f9ff38a67e244268efd8ff325930af0ea16b0bf74926aef05f5817950
fetched_at: '2026-06-28T22:37:59.358508+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA716 Empréstimo SAC com taxa
  fixa ligado ao índice CDI pós fixado
type: support-article
updated_at: '2025-01-24T20:26:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25840490488215-Cross-Segmentos-Backoffice-Linha-Protheus-FINA716-Empr%C3%A9stimo-SAC-com-taxa-fixa-ligado-ao-%C3%ADndice-CDI-p%C3%B3s-fixado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25840441786903) Tempo aproximado para leitura: **00:010:00 min****Dúvida**Como incluir um emprestimo com taxa CDI pos fixado e taxa fixa   
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
**1.** Realizar os cadastros dos templates:  
**Template 1:** CDI com o percentual 80%  
**Template 2:** Taxa Fixa com o percentual 20%  **![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842745876759)  
  
2.** Nesse exemplo vamos incluir um empréstimo com os valores:

Data da inclusão: 03/06/2024  
Vlr. Operação: 1.000.000,00  
Gera parcela: Sim   
 **![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842745878551)**

Prazo: 2  
Primeiro Vencimento: 28/06/2024  
Dia fixo para vencimento: 31

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842745881367)  
  
3.** Na projeção de valor das parcelas os juros estão com base na taxa fixa referente ao **Template 2:** Taxa Fixa com os percentuais 20%    
**Obs.** Nesse momento não é calculado os juros com base no CDI, a correção do CDI será realizada no momento do pagamento das parcelas  
 **![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842761458327)**

**4.** Vamos realizar o pagamento da primeira parcela na data 28/06/2024, conforme o print

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842761461399)**

No pagamento da parcela que será informado a correção do **template 1** CDI  
Então com base no contrato de 1.000.000,00 entre a data inicial 03/06/2024 a data final 28/06/2024 com 80% do CDI a correção é o valor de **5.985,95**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842761463831)**

Apenas para comparação exemplo com o simulador do banco central com a taxa do CDI comparando com o cálculo do Protheus

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842761466647)**

**5.** Pagamento da outra parcela do contrato na data 31/07/2024 **![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842761468695)**Calculo realizado pelo Protheus da correção CDI no valor de **3.625,35**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842745899799)**Comparação no simulador com o valor corrigido na data final **3.625,35**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842745902487)**

**Saiba mais**

[Aplicações e empréstimos - FINA716 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=680254799)

[Cadastro de templates - FINA716](https://tdn.totvs.com/display/public/PROT/Cadastro+de+templates+-+FINA716)
