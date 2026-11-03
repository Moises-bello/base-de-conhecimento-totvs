---
article_id: 1500003955101
category: Inspeção de Entradas (SIGAQIE)
content_hash: b2fa64243a5253dfe2b0541fe762ec2d2f7324427b4eac7d7fcf41d029211699
fetched_at: '2026-06-28T22:42:26.909860+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Campo QEK_TAMAMO do QIEA215
type: support-article
updated_at: '2021-07-13T11:58:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003955101-Manufatura-Linha-Protheus-SIGAQIE-Campo-QEK-TAMAMO-do-QIEA215
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)* Tempo aproximado para leitura: **00:01:15 min**  
**Dúvida**Como é definido o tamanho da amostra no campo **QEK\_TAMAMO - Tam. Amostra** da rotina **QIEA215 - Cadastro de Resultados**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Solução**Se a unidade de medida do campo **QE6\_UNMED1 - Un. Medida 1** e de amostragem do campo **QE6\_UNAMO1 - Un. Amostr. 1** da rotina **QIEA010 - Especificações de Produtos** forem iguais, o campo **QEK\_TAMAMO** assume a quantidade do documento de entrada ou tamanho do lote. A quantidade do documento de entrada ou tamanho do lote é registrada no campo **QEK\_TAMLOT - Tam. Lote** do **QIEA215**.  
Porém, se as unidades de medida e amostragem forem diferentes, será verificado o conteúdo dos campos **QE6\_FATCO1 - Fat. Conv. 1** e **QE6\_TIPCO1 - Tipo Conv. 1** da rotina **QIEA010** para calcular o valor do campo **QEK\_TAMAMO**.  
Se no campo **QE6\_TIPCO1** estiver definido como **M-Multiplicador**, é multiplicado o conteúdo do campo **QE6\_FATCO1** pela quantidade do documento de entrada ou tamanho do lote, para resultar o valor do campo **QEK\_TAMAMO**. Mas, se no campo **QE6\_TIPCO1** estiver como **D-Divisor** é dividido a quantidade do documento de entrada ou tamanho do lote pelo conteúdo do campo **QE6\_FATCO1** para resultar na quantidade do campo **QEK\_TAMAMO**.
