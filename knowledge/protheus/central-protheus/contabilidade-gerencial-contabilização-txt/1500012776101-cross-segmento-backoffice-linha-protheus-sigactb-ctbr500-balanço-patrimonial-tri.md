---
article_id: 1500012776101
category: Contabilidade Gerencial - Contabilização txt
content_hash: edf7cddf47f3bedbe1e2a24f210cd7e28e2df787862d4616fe10fe4219f7018f
fetched_at: '2026-06-28T22:40:55.470232+00:00'
product: protheus
section_id: 1500001537521
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBR500 - Balanço Patrimonial
  trimestral.
type: support-article
updated_at: '2024-09-26T20:10:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012776101-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR500-Balan%C3%A7o-Patrimonial-trimestral
---

**Dúvida**Como gerar o demonstrativo Balanço Patrimonial trimestral (CTBR500)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - TOTVS Contabilidade Gerencial - Todas as versões  
  
**Solução**

* Possuir o Calendário Contábil trimestral  (CTBA010).

* Realizar a apuração de resultado trimestralmente (CTBA211)

Particularidades do relatório:

* O relatório utiliza, obrigatoriamente, o recurso de "[Configurações de livro](https://tdn.totvs.com/pages/viewpage.action?pageId=338384314)".
* Permite apresentar os valores do semestre, caso respondido "Sim" para a pergunta "Demonstra Semestre?".

|  |
| --- |
| ***Importante:***  A personalização dos relatórios exigidos por lei, afeta a legalidade do documento. Por esta razão, por padrão do Sistema, a personalização destes documentos está bloqueada no ambiente Contabilidade Gerencial.  Observe a configuração do parâmetro [MV\_CTBPOFF](https://tdn.totvs.com/pages/viewpage.action?pageId=312160877). |

|  |
| --- |
| ***Importante******:***  Para imprimir este relatório considerando a visão gerencial com tipo de saldo variável, consulte o cadastro de [Visão Gerencial com tipo de saldo variável](https://tdn.totvs.com/pages/viewpage.action?pageId=341230810). |

---

**Procedimentos**

Para emitir o relatório Balanço Patrimonial:

1. Na janela de emissão do relatório "**Bal. Patrimonial**", clique em "**Parâmetros**".

O sistema apresenta a tela para configuração dos parâmetros referentes ao relatório.

2. Configure-os de acordo com orientação do help de campo.

|  |
| --- |
| ***Observação******:***  Para imprimir o nome da visão gerencial (definido na tabela CTS - Itens da Visão Gerencial), configure a pergunta "Título como nome da visão", com "SIM". |

3. Confira as configurações e confirme a impressão do relatório.

[MP-SIGACTB - Dre trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006850892-MP-SIGACTB-Dre-trimestral-?source=search)

4º Através do cadastro da visão gerencial (CTBA161) Verifique os campos abaixo

* Campo "Total geral" deve ser informado para entidade Sintética totalizador Ativo e Passivo , as demais sintéticas não precisão dessa configuração

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26654612711191)

* Quando Ativo "Coluna =1"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26654588492311)

* Quando passivo "Coluna =2"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26654588496663)

**Saiba Mais**

[CTBR500- Balanço Patrimonial](https://tdn.totvs.com/pages/viewpage.action?pageId=347445037)

[ECF Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006253692-MP-SIGACTB-ECF-Lucro-Presumido-N%C3%A3o-Gerou-P100-e-P150)

[ECD Arquivo trimestral, unificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025347591-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-TRIMESTRAL-UNIFICADA-)
