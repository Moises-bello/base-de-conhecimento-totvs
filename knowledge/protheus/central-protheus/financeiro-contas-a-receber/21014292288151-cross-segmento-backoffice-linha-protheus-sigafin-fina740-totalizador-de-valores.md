---
article_id: 21014292288151
category: Financeiro - Contas a Receber
content_hash: 8a49f985dcf603cb74c4c6ed49cf45a69237e9a90138ab6fe7d3a8c47bb47c96
fetched_at: '2026-06-28T22:38:12.516633+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA740 - Totalizador
  de valores no contas a receber
type: support-article
updated_at: '2026-03-27T13:24:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21014292288151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA740-Totalizador-de-valores-no-contas-a-receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21014292264983) Tempo aproximado para leitura: **00:05:00min**  
  
**Dúvida**  
Como criar totalizador de valores no contas a Receber?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Na rotina **Funções contas a Receber** ou **Contas a receber** quando clicado na engrenagem, no canto superior direito  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21014292267543)

1. Acesse a **Colunas** e selecione: **Totalizador de Valores**.
2. Localize a coluna: **Vlr. Título**.
3. **Preencha os seguintes campos:**
   * **Título:** Insira uma descrição apropriada (exemplo: **Soma Vlr dos Títulos**).
   * **Tipo:** Selecione **1 - Totalizar**.**Máscara:** Insira **@E 9,999,999,999,999.99**.

![Gravar_2025_02_13_09_44_02_187.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29958512668439)

   
Após salvar o processo, será necessário clicar na coluna **Vlr. Título** no **Browse**, onde o totalizador foi criado. O sistema, então, exibirá o total dos valores dos títulos apresentados na tela.

**Observação:**

Comportamento do Totalizador com Filtros no Browse: Por características de performance do componente de browse, a totalização dos valores nas colunas não ocorre de forma automática após a aplicação de filtros dinâmicos. Caso os valores totais não sejam atualizados imediatamente ao filtrar os títulos, é estritamente necessário acionar o botão "Recalcular Total", localizado no canto inferior direito da interface. Esta ação força o sistema a reprocessar a soma, considerando exclusivamente o novo escopo de registros exibidos em tela.
