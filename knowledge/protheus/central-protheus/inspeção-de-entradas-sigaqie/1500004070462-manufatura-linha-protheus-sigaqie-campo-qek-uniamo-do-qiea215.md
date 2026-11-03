---
article_id: 1500004070462
category: Inspeção de Entradas (SIGAQIE)
content_hash: 89133c5bc097ea8cc2617cf897357be954b4b9510345b0c8f8c7bcd1d1ba203b
fetched_at: '2026-06-28T22:42:26.913194+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Campo QEK_UNIAMO do QIEA215
type: support-article
updated_at: '2021-07-13T11:59:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004070462-Manufatura-Linha-Protheus-SIGAQIE-Campo-QEK-UNIAMO-do-QIEA215
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)* Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**Qual a unidade de medida considerada para o campo **QEK\_UNIAMO - Un. Amostra** da rotina **QIEA215 - Cadastro de Resultados**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Solução**Se a unidade de medida do campo **QE6\_UNMED1 - Un. Medida 1** e de amostragem do campo **QE6\_UNAMO1 - Un. Amostr. 1** da rotina **QIEA010 - Especificações de Produtos** forem iguais, o campo **QEK\_UNIAMO** assume a unidade de medida definida no campo **QE6\_UNMED1**.  
Porém, se as unidades de medida e amostragem forem diferentes, o campo **QEK\_UNIAMO** assumirá a unidade de amostragem definida no campo **QE6\_UNAMO1**.
