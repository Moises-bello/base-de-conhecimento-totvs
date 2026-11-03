---
article_id: 30802386390679
category: Inspeção de Entradas (SIGAQIE)
content_hash: 92385e2b315809c68d4e50bc26eca95c2a47377d102c1941ca9f42034e291bff
fetched_at: '2026-06-28T22:42:27.102492+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Notas fiscais do tipo Normal não aparecem
  para serem inspecionadas no SIGAQIE
type: support-article
updated_at: '2025-05-14T13:56:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30802386390679-Manufatura-Linha-Protheus-SIGAQIE-Notas-fiscais-do-tipo-Normal-n%C3%A3o-aparecem-para-serem-inspecionadas-no-SIGAQIE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30802386366487) Tempo aproximado para leitura: **00:03:30 min** **Dúvida**Por que notas fiscais do tipo **Normal** não aparecem para serem inspecionadas na rotina de **Resultados -** **QIEA215**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Solução**Para inspeção de notas de entrada do tipo Normal, deverá ser configurado o parâmetro **MV\_QNFENOR - Define quais tipos de NF do tipo Normal serão enviadas para Inspeção, através da configuração de Poder de terceiros,  TES - Tipo de Entrada e Saída, sendo: Normal, Remessa e Devolução.**  
  
**Exemplo**  
A **posição 1** responderá pelas **NFE** com **TES** de poder de terceiros, campo **F4\_PODER3** - **Poder Terc.** igual a **Não Controla**.  
A **posição 2** responderá pelas **NFE** com **TES** de poder de terceiros, campo **F4\_PODER3 - Poder Terc.** igual a **Remessa**.  
A **posição 3** responderá pelas **NFE** com **TES** de poder de terceiros, campo **F4\_PODER3** - **Poder Terc.** igual a **Devolução**.  
  
Se o parâmetro for configurado como **SNN - SIM, NÃO, NÃO**, indica que somente as **NFE - Nota Fiscal Eletrônica** do tipo **Normal** e com **Poder Terceiro - Não Controla** serão enviadas para a inspeção de entrada. Os demais tipos entrarão no armazém padrão.  
  
**Observação**  
A **TES - Tipo de Entrada e Saída** a ser utilizada é cadastrada na rotina **MATA080 - Tipos de Entradas e Saídas**. Nesta rotina também consta o campo **Poder Terceiro - F4\_PODER3** que será validado conforme o conteúdo do parâmetro **MV\_QNFENOR**.  
  
**Importante**  
No artigo [Manufatura - Linha Protheus - SIGAQIE - Cadastros necessários para integrar com o SIGAQIE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020570212-Manufatura-Linha-Protheus-SIGAQIE-Cadastros-necess%C3%A1rios-para-integrar-com-o-SIGAQIE) temos os demais **cadastros necessários** para integração como o **SIGAQIE - Inspeção de Entradas**.
