---
article_id: 360021114952
category: Inspeção de Entradas (SIGAQIE)
content_hash: 6efaf729081c45107f75f810a575d1608a89395bb1845be8ab31c66fec38f071
fetched_at: '2026-06-28T22:42:27.098140+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Notas fiscais de devolução não aparecem
  para serem inspecionadas no SIGAQIE
type: support-article
updated_at: '2025-03-20T19:07:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114952-Manufatura-Linha-Protheus-SIGAQIE-Notas-fiscais-de-devolu%C3%A7%C3%A3o-n%C3%A3o-aparecem-para-serem-inspecionadas-no-SIGAQIE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22273811724567)**Tempo aproximado para leitura: **00:01:40 min  
  
Dúvida**Por que notas fiscais do tipo **Devolução** não aparecem para serem inspecionadas na rotina de **Resultados -** **QIEA215**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Solução**Para inspeção de notas de entrada do tipo **Devolução**, deverá ser configurado o parâmetro **MV\_QNFEDEV - Define quais tipos de nota fiscal de devolução serão enviadas para inspeção através da configuração de poder de terceiros da TES - Tipo de Entrada e Saída, sendo : Normal, Remessa e Devolução**.  
  
**Exemplo**  
A **posição 1** responderá pelas **NFE** de devolução com **TES** de poder de terceiros, campo **F4\_PODER3** - **Poder Terc.** igual a **Não Controla**.  
A **posição 2** responderá pelas **NFE** de devolução com **TES** de poder de terceiros, campo **F4\_PODER3** igual a **Remessa**.  
A **posição 3** responderá pelas **NFE** de devolução com **TES** de poder de terceiros, campo **F4\_PODER3** igual a **Devolução**.  
  
Se o parâmetro for configurado como **SNN - SIM, NÃO, NÃO**, indica que somente as **NFE - Nota Fiscal Eletrônica** de devolução do tipo **Não Controla** serão enviadas para a inspeção de entrada. Os demais tipos entrarão no armazém padrão.  
Atualmente não existe um controle específico para que apenas alguns produtos, ao serem devolvidos, não sejam encaminhados ao **CQ - Controle de Qualidade**.  
  
**Observação**  
A **TES - Tipo de Entrada e Saída** a ser utilizada é cadastrada na rotina **MATA080 - Tipos de Entradas e Saídas**. Nesta rotina também consta o campo **Poder Terceiro - F4\_PODER3** que será validado conforme o conteúdo do parâmetro **MV\_QNFEDEV**.  
  
**Importante**  
Para notas do tipo **Beneficiamento,** é aplicada a mesma regra acima, a partir do parâmetro **MV\_QNFEBEN** que define quais tipos de **Nota Fiscal de Beneficiamento** serão enviadas para inspeção, através da configuração de poder de terceiros, **TES Entrada**, sendo: **Normal**, **Remessa** e **Devolução**.
