---
article_id: 30995007220119
category: Inspeção de Entradas (SIGAQIE)
content_hash: fa02c1a5779def2e79a0f887a717ce959db93c714dbcfed9bae25d396127be1a
fetched_at: '2026-06-28T22:42:27.106336+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - O número do Lote informado na Entrada
  já existe
type: support-article
updated_at: '2025-03-28T17:56:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30995007220119-Manufatura-Linha-Protheus-SIGAQIE-O-n%C3%BAmero-do-Lote-informado-na-Entrada-j%C3%A1-existe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30995007200791) Tempo aproximado para leitura: **00:00:45 min****Ocorrência**Na rotina **QIEA183 - Importação**, ao consultar a coluna **Inconsistência** consta a mensagem: **O número do Lote informado na Entrada já existe.**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Causa**Esta mensagem ocorre quando **já existe nota de entrada com mesmo número de lote cadastrada e integrada com o SIGAQIE - Inspeção de Entradas**.  
  
**Solução**Existe o parâmetro **MV\_QLOTUNI - Utiliza número de lote no cadastro de entregas**, que valida se o número de lote se repete. Estando o conteúdo do parâmetro **MV\_QLOTUNI** igual a **S - Sim,** e o número de lote se repetir, haverá mensagem informativa/impeditiva: **O número do Lote informado na Entrada já existe**.Para solucionar essa ocorrência, realize os seguintes passos:  
1. Altere o conteúdo do parâmetro **MV\_QLOTUNI** para **N - Não**;  
2. Após realizar o ajuste acima, acesse a rotina **QIEA183** novamente, selecione a nota fiscal, acesse o botão **Outras Ações** > **Importação** para que a nota fiscal em questão seja reprocessada.
