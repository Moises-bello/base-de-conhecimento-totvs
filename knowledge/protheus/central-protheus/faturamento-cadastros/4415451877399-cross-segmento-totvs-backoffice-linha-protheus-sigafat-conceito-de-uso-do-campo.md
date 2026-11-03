---
article_id: 4415451877399
category: Faturamento - Cadastros
content_hash: 112246e1121b6d54a8909b45334e626fa1ffe226a00a5a435ba451dcee96a10f
fetched_at: '2026-06-28T22:38:35.267097+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Conceito de
  uso do campo E4_CCORREN
type: support-article
updated_at: '2021-12-09T20:27:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415451877399-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Conceito-de-uso-do-campo-E4-CCORREN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**  
Conceito de uso do campo **E4\_CCORREN.**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões.  
  
**Solução**

**Campo Con Corrente. >> E4\_CCORREN**

O help descreve essa frase **"Usa Conta corrente**".

Este é um campo de uso sistêmico,  indica se será utilizado a funcionalidade referente a conta corrente,.

Sua utilização funcionará agregada ao parâmetro **MV\_NATCCOR, onde s**eu conteúdo ( **MV\_NATCCOR** ) será validado na tabela de Naturezas (**SED**). Caso o campo **E4\_CCORREN** estiver como "**Sim**",  terá o valor desta natureza gravado no campo **E1\_NATUREZ,** caso estiver como **"Não",** a natureza gravada no campo **E1\_NATUREZ** será do parâmetro **MV\_NATFIN**.

Todavia, a indicação é apropriada para módulos que utilizam débito em TEF, como os módulos de **Automação Comercial** (SIGALOJA, FrontLoja, Venda Direta,PDV), que pode indicar débito em conta, para o módulo Faturamento, não tem uso, visto que o módulo não trabalha com cartão de débito ,  e a geração do  título sempre será NF.

Saiba mais sobre o uso do **E4\_CCORREN**:

**[SIGALOJA 0026 Como realizar a baixa de Títulos com associação a Conta Corrente?](https://tdn.totvs.com/x/sZLzEQ)**
