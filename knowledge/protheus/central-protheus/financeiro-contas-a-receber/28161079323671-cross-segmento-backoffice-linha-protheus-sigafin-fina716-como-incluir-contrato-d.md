---
article_id: 28161079323671
category: Financeiro - Contas a Receber
content_hash: 95b8774ade820674793c1c711754b254dc1e0c56e72b0b931ffe4c6884e29104
fetched_at: '2026-06-28T22:38:12.865883+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA716 - Como incluir
  contrato de financiamento em dólar
type: support-article
updated_at: '2024-12-02T11:37:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28161079323671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Como-incluir-contrato-de-financiamento-em-d%C3%B3lar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28161108964375) Tempo aproximado para leitura: **00:08:00 min****Dúvida**Como incluir contrato de financiamento em dólar?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA716 - Todas as versões  
  
**Solução**

Para realizar o processo de inclusão, utilizamos a rotina FINA716, destinada à gestão de empréstimos.

Como exemplo, vamos validar um contrato incluído em 17/03/2021. Nesse caso, é importante destacar que, por se tratar de um contrato em dólar, é necessário que a moeda esteja devidamente cadastrada no sistema para o período correspondente.

No exemplo, na data de 17/03/2021, a taxa de câmbio aplicada era de 5,6296. Certifique-se de que o cadastro da moeda e o valor do câmbio estejam corretos para evitar inconsistências no registro do contrato.

Cadastro moeda '**Rotina** **MATA090'**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28161079307927)**

Inclusão do empréstimo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28161108967063)

Segue um exemplo de projeção das parcelas. Neste contrato, não há informações detalhadas sobre os valores de cada parcela. Assim, anexamos uma captura de tela dos valores produzidos pelo Protheus.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28161108968599)

Caso os valores apresentados não estejam conforme as expectativas, é recomendável validar junto ao banco uma planilha contendo o cálculo detalhado de cada parcela. Isso se torna particularmente relevante se existir uma taxa específica aplicada, onde o Templates pode ser usado para fazer os cálculos conforme as informações do banco.

Obs. O vencimento terá que alterar manual.

**Saiba mais**

[Aplicações e empréstimos - FINA716 - Financeiro P12](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680254799)

[Cadastro de templates - FINA716](https://tdn.totvs.com.br/display/public/PROT/Cadastro+de+templates+-+FINA716)
