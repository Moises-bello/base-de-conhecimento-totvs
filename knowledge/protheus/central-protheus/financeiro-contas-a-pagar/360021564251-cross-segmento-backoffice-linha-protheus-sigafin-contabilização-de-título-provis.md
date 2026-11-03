---
article_id: 360021564251
category: Financeiro - Contas a Pagar
content_hash: f0f2ddd1885c5c9145bb61ec2be8e09eae8724a0851be2b20b414b3a74829b1b
fetched_at: '2026-06-28T22:38:07.260302+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Contabilização de título
  Provisório - PR
type: support-article
updated_at: '2026-05-21T20:05:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021564251-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Contabiliza%C3%A7%C3%A3o-de-t%C3%ADtulo-Provis%C3%B3rio-PR
---

**Dúvida**  
Como é feita a contabilização de provisionamentos no Contas a Pagar?  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Financeiro – FINA050– A partir da versão 11.80  
  
O conceito de provisionamento no Contas a Pagar é atribuído aos títulos do tipo PR (Provisório). Nesse cenário, posteriormente será necessária a substituição deste título por um tipo efetivo (BOL, DP, NF, entre outros), por meio da opção **Outras Ações > Substituir,** para que sejam contabilizadas a inclusão e a substituição.

Para a contabilização da inclusão do título provisório, é utilizado o lançamento padrão **510**, o mesmo utilizado para inclusão de títulos de Contas a Pagar em geral.

No momento da substituição do título provisório por um título efetivo, como, por exemplo, do tipo NF, a contabilização deste processo pode ser realizada por meio do lançamento padrão **533**, utilizando como regra a tabela **SE2** como valor base (`SE2->E2_VALOR`).

Durante o processo:

* O título de provisionamento será baixado;
* O título substituto será apresentado em tela para definição do tipo e confirmação;
* Após a confirmação, o lançamento padrão **510** será novamente considerado para a inclusão do novo título e**,** em seguida, o lançamento **533.**

**Exemplo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40649267781655)

**Importante:**  
Caso a opção seja excluir automaticamente o título provisório após a substituição, poderá ser utilizado o Ponto de Entrada **F50DELPR**. Nessa situação, a contabilização do processo também ocorrerá através do lançamento padrão **533**.
