---
article_id: 4409779262487
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 04398b629b3b6f8eea3ad32e185cb2be497c4cadda0942846be8828b87255243
fetched_at: '2026-06-28T22:40:47.675939+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - ECF como gerar
  o registro Y570
type: support-article
updated_at: '2025-04-25T11:38:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409779262487-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-como-gerar-o-registro-Y570
---

**Dúvida**ECF como gerar o registro Y570  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - Todas as versões  
  
**Solução**

As informações geradas no registro Y570, são extraídas do módulo financeiro no contas a receber (SE1).

São levados as baixas geradas na (SE1) do tipo IR- e CS-

Nas tabelas de integrações (TAFST1 e TAFST2) os dados da **SE1** gera o bloco **T108.**

No TAF esses registros vão para a tabela **CEX** e podem ser verificados na rotina **TAFA350.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409995587223)

[Geração dos Blocos X e Y](https://tdn.totvs.com/pages/releaseview.action?pageId=243650896)

**Geração:**

Escrituração contábil + ECF (CTBS001)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409778948503)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409770767383)

SE1:

![](https://totvssuporte.zendesk.com/attachments/token/baqS1dAhDigzG5bnoNP9QpeaL/?name=inline1975296673.png)

**[Registro Y570 - Demonstrativo do Imposto de Renda e CSLL Retidos na Fonte](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECFEscritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoY-Informa%C3%A7%C3%B5esGerais)**

* Tabelas - CEX (Demonst. IR e CSLL Ret. Fonte) / CW9 (Códigos Retenção Rec. Federal)
* Registro do Layout TOTVS - T108
* Rotina - TAFA350 (Demonst. IR e CSLL Ret. Fonte)

![](https://totvssuporte.zendesk.com/attachments/token/nhIMP5yisAtRyNICQQ9IkJFqv/?name=inline-1224673780.png)

**Saiba mais**

[Geração bloco X e Y](https://tdn.totvs.com/pages/releaseview.action?pageId=243650896)

[Parâmetros ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406505730327-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Wizard-rotina)

[Pacote de atualização ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004873211-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pacote-de-atualiza%C3%A7%C3%A3o-e-como-realizar-a-atualiza%C3%A7%C3%A3o-da-ECF-2021-leiaute-7)

[Leiaute de integração TAF](https://tdn.totvs.com/pages/viewpage.action?pageId=187534666)
