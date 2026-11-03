---
article_id: 360026397711
category: Inspeção de Entradas (SIGAQIE)
content_hash: 16220495c6d469e7fb16f1a96ef8630a40119acf59fd42ddea1831ecc8b6b3e6
fetched_at: '2026-06-28T22:42:27.109966+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - O produto não possui revisão disponível
type: support-article
updated_at: '2021-06-23T12:24:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026397711-Manufatura-Linha-Protheus-SIGAQIE-O-produto-n%C3%A3o-possui-revis%C3%A3o-dispon%C3%ADvel
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:10 min****Ocorrência**Na rotina **QIEA183 - Importação**, ao consultar a coluna **Inconsistência** consta a mensagem: **O produto não possui revisão disponível.**  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
 **Causa**Esta mensagem ocorre quando a **Data de Início de Vigência da Especificação do Produto** na rotina **QIEA010** **- Especificação do Produto** é superior à data de entrada da nota fiscal ou quando **não existe** especificação de produto cadastrada para o produto em questão.   
  
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse a rotina **QIEA010** e verifique se existe uma **Especificação** para o produto em questão. Caso não existir, cadastre a especificação.
2. Caso já existir especificação para o produto na rotina **QIEA183**, verifique a **Data de Vigência**. Esta data precisa ser inferior à data de entrada da nota fiscal em questão.
3. Após realizar os ajustes acima, acesse a rotina **QIEA183** novamente, selecione a nota fiscal, acesse o botão **Outras Ações** > **Importação** para que a nota fiscal em questão seja reprocessada após o ajuste do cadastro da especificação.
