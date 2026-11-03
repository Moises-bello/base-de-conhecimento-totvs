---
article_id: 23923132076695
category: Gestão organizacional
content_hash: edf6693606994adabe1d39df1cd6b0576cffca43f268f1a69cb8e7e8155ce80e
fetched_at: '2026-06-28T22:47:22.252990+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - S-2500: Data de desligamento de preenchimento obrigatório'
type: support-article
updated_at: '2024-06-10T18:23:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23923132076695-RH-RM-RHU-S-2500-Data-de-desligamento-de-preenchimento-obrigat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23923132047767) Tempo aproximado para leitura: **00:01:09 min** **Dúvida**Ao incluir um contrato de trabalho no cadastro do Processo Trabalhista para um funcionário que não possui informação no evento S-2190, S-2200 ou S-2300, o RM esta exigindo que a data de desligamento seja preenchida. O que fazer quando o reclamante ainda não foi desligado da empresa?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155** e superiores.  
  
**Solução**De acordo com o leiaute do eSocial, quando o reclamante foi admitido em data anterior ao eSocial e você envia as informações de admissão através do evento S-2500, o campo referente a data de desligamento deverá ser preenchido obrigatoriamente:![](https://totvssuporte.zendesk.com/attachments/token/I86dIhl7VQkPY1i3dLQmzULqW/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/na04RFaFOaVexUdSLS9VWJBut/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/sBaCqJtnEp9Ecp2ol1jJFFbUc/?name=image.png)

Se em seu cenário atual o reclamante ainda esta ativo na empresa, ou seja, ainda é seu funcionário, a orientação do eSocial é que neste caso seja enviado um evento admissional (S-2200 ou S-2300) informando o número do processo trabalhista.

Posteriormente, deverá realizar o envio do evento S-2500 preenchendo o campo 'Possui informações de vínculo no evento S-2190, S-2200 ou S-2300 no declarante' como 'SIM' e desta forma não precisará preencher o campo referente a data de desligamento.  
  
Segue trecho do MOS contendo tal informação, seguido do link para acesso:  
  
![Exibindo image.png](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEVQqO81roHsL%2FfhrGJU4eJCTIuVdT%2BPD3%2FWvka2775Y%2BXdrah5MBG8WXgzauWlInyyahP4wJrfOYsFnn3RLoGmuJF2iI4A7tRm8i9SWWlb%2FrpAUpfcacm0JBb39wzWgkyqjYeU9e0XhEEz%2BJBMWvKzl%2BcnnXca5cVhsO8eyoa%2FrWsyWryPQlike08rYJeB0czJ8b7%2BTLUQHQQ%2F%2FKRSNuGxFZJAeLPQrp7su3zXkoLFUf2atZ9ggEMIYEJdx%2B%2FwERkLqC3bRyCR1b6eMoF9I6T1kC3nHU%2B9AGkAU1okyhkEl%2BcL%2F3Mouy5GEPM1w1Z6V6Ms39FJ0OXExrdIQHWCV9GiSNooYtonI001ha4dWFrpl21gGUDRoYXF9e7N7KjCCdd%2FgFvO6m8UoyYf%2FC9GzL8824z%2FLHXql9pFMa1JHP2QmKFgi7dMctFacnJNgO%2Fu2jtzn7I8xDZq%2BWVCK%2BCciuEpZv4O%2BmYA4m9jLIzcFbhphnd7%2BoGSqSBbU%2BdIrqo7Pu%2FJqv4An%2FECkmrMV6vRRBs%2FyPrFoXqruy2sELOjHN6fIZgF3cXHpV0ygjd1SFk%2FcjQ%3D%3D&sz=w1919-h959)  
  
[MANUAL DE ORIENTAÇÃO DO eSOCIAL](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-07-2023.pdf/)  
  
**Saiba Mais**  
Para maiores informações sobre o cadastro do evento S-2500, acesse:  
[RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)
