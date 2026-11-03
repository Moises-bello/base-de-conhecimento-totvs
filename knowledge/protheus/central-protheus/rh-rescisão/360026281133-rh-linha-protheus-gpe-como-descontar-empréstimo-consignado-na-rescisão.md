---
article_id: 360026281133
category: RH - Rescisão
content_hash: 89b08179370202c6d30edb416e9234dcc33aad5cf608e74233a9d8b7791b307c
fetched_at: '2026-06-28T22:43:48.647636+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como descontar empréstimo consignado na rescisão
type: support-article
updated_at: '2026-02-24T14:47:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026281133-RH-Linha-Protheus-GPE-Como-descontar-empr%C3%A9stimo-consignado-na-rescis%C3%A3o
---

**Dúvida**  
Como descontar empréstimo consignado na rescisão e onde parametrizar o percentual de desconto?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - GPE - Gestão de Pessoal - A partir da Versão 12  
  
**Solução**  
Abaixo o que verificar para que o empréstimo consignado seja descontado na rescisão:  
  
1. Valide o cadastro da verba de desconto de empréstimo consignado na rotina de **Verbas** pelo caminho  **>Atualizações >Definições de cálculos >Verbas**, ela deve estar com o campo **Emp. Cons.** com SIM:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041554293)

2. Verifique o lançamento na rotina **Valores Futuros** pelo caminho **Atualizações >Lançamentos >Valores Futuros**, a coluna **Emp. Cons.** também deve estar com SIM:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38604886071063)

3. Verifique se o lançamento na rotina Valores Futuros pelo caminho  **Atualizações >Lançamentos >Valores Futuros**, se o campo **Situação** está como **ATIVO**  
  
![]()![](https://centraldeatendimento.totvs.com/hc/article_attachments/38604866927255)

4. O mnemônico **P\_PERCONS** deve estar preenchido com o percentual a ser descontado na rescisão, para isso, valide na rotina **Mnemônicos** pelo caminho **>Atualização >Definição de cálculos >Mnemônicos**:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040725074)
