---
article_id: 22274208294551
category: Inspeção de Entradas (SIGAQIE)
content_hash: b1806022feb75d3af7e8411c12261606ba2c816ec9c3809ba4455ed597a187ad
fetched_at: '2026-06-28T22:42:27.093783+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Nota de Industrialização
type: support-article
updated_at: '2024-03-25T11:11:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22274208294551-Manufatura-Linha-Protheus-SIGAQIE-Nota-de-Industrializa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22274199880599) Tempo aproximado para leitura: **00:01:05 min** **Dúvida**Por que **notas de industrialização** não aparecem para serem inspecionadas na rotina de **Resultados - QIEA215**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Solução**Quando é incluída uma **nota de industrialização** na rotina **MATA103 - Documentos de Entrada** o campo **Tipo - D1\_TIPO** deve possuir o conteúdo igual à **N - Normal**. Neste caso, será verificado qual a **TES - Tipo de Entrada** que foi utilizada neste documento para então verificar na rotina **MATA080 - Tipos de Entradas e Saídas** qual o conteúdo do campo **Poder Terceiro - F4\_PODER3**. Para a **nota de industrialização** o campo **Poder Terceiro** deve ser igual à **D - Devolução.**  
Também sendo a nota do tipo **N -Normal** e **Poder Terceiro** igual a **D - Devolução** é verificado a terceira posição do parâmetro **MV\_QNFENOR - Define quais tipos de nota fiscal de Normais serão enviadas para inspeção através da configuração de poder de terceiros da TES - Tipo de Entrada e Saída, sendo: Normal, Remessa e Devolução** que para integrar precisa ser igual a **S - Sim**.  
  
**Exemplo**  
A **posição 1** responderá pelas **NFE** de devolução com **TES** de poder de terceiros, campo **F4\_PODER3** - **Poder Terc.** igual a **Não Controla**.  
A **posição 2** responderá pelas **NFE** de devolução com **TES** de poder de terceiros, campo **F4\_PODER3** igual a **Remessa**.  
A **posição 3** responderá pelas **NFE** de devolução com **TES** de poder de terceiros, campo **F4\_PODER3** igual a **Devolução**.  
  
Se o parâmetro for configurado como **NNS - NÃO, NÃO, SIM**, indica que somente as **NFE - Nota Fiscal Eletrônica Normal** com **Poder de Terceiro** de **Devolução** serão enviadas para a inspeção de entrada. Os demais tipos entrarão no armazém padrão.  
Atualmente não existe um controle específico para que apenas alguns produtos, ao serem devolvidos, não sejam encaminhados ao **CQ - Controle de Qualidade**.
