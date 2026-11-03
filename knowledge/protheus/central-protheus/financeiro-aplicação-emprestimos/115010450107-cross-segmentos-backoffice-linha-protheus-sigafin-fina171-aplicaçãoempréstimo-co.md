---
article_id: 115010450107
category: Financeiro - Aplicação / Emprestimos
content_hash: 7f0eacb00dc3515631c810fb03d178996aa67710afdba871eba928d3d7301e3a
fetched_at: '2026-06-28T22:37:59.472183+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA171 - Aplicação/Empréstimo
  - Como realizar despesas de empréstimo
type: support-article
updated_at: '2022-08-01T20:36:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010450107-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA171-Aplica%C3%A7%C3%A3o-Empr%C3%A9stimo-Como-realizar-despesas-de-empr%C3%A9stimo
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como realizar despesas de empréstimo. (**FINA171**)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA171 - Todas as versões  
  
**Solução**Quando é incluído um Empréstimo e colocado uma despesa, é gerado um título na **SE2** e uma movimentação **SE5.**  
  
Se o Empréstimo é cancelado/excluído por algum motivo, o título gerado no módulo contas a pagar referente as despesas não exclui o mesmo. Se faz necessário que faça a baixa deste título referente a despesa com o **MOTIVO DE BX = DEVOLUCAO**.

Assim o sistema irá efetuar um registro/movimentação na **SE5** com a carteira contrário que gerou na inclusão do Empréstimo populando o campo **E5\_RECPAG**.
