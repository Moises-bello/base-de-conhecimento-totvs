---
article_id: 360018358692
category: Financeiro - Baixas a Receber
content_hash: 38eb833102b0d13a4fca853e7fdd33b09fbc11d0c90822b664ccddf7d2f0e687
fetched_at: '2026-06-28T22:37:43.715298+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA070 - Baixa em Lote
type: support-article
updated_at: '2026-01-09T13:39:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018358692-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Baixa-em-Lote
---

**Dúvida**  
Como configurar e utilizar a Baixa por Lote na rotina Baixas a Receber Manual (**FINA070**)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – FINA070 - A partir da versão 12.1.17  
  
**Solução**  
Para a execução da **baixa por lote**, é necessário que o título esteja vinculado a uma **carteira diferente de zero**, ou seja, devidamente **transferido** ou incluído em **borderô**.

Alternativamente, os **códigos dos bancos** que serão utilizados no processo de baixa por lote devem estar previamente configurados no parâmetro **MV\_CARTEIR**, informados de forma sequencial e separados por **ponto e vírgula (;)**. No caso de utilização do parâmetro **MV\_CXFIN**, deverão ser cadastradas as **contas bancárias específicas** que participarão do processo.

### **Observações**

1. O banco ou a conta bancária cadastrada nos parâmetros **MV\_CARTEIR** ou **MV\_CXFIN** ficará impedida de realizar a **emissão de cheques** no módulo **Contas a Pagar**, uma vez que o sistema passa a tratá-la como um banco interno (caixa).
2. O processo de **baixa por lote a receber** não gera movimentação bancária individual por título. O sistema registra apenas um **movimento totalizador do lote**, refletido na **tabela de movimento bancário (SE5)** e suas respectivas **chaves estrangeiras (FKs)**.

### **Importante**

Os procedimentos descritos acima fazem parte do **padrão do sistema legado** e **não podem ser alterados**. Caso essas opções não atendam às necessidades do processo, recomenda-se a utilização da rotina **Baixas Automáticas (FINA110)**.  
  
**Saiba mais**  
[Diferença e tratamento: MV\_CARTEIR e MV\_CXFIN](http://tdn.totvs.com/pages/releaseview.action?pageId=172300136)
