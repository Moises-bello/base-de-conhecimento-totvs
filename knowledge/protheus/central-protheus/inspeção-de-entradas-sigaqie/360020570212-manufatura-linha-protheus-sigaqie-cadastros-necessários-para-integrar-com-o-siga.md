---
article_id: 360020570212
category: Inspeção de Entradas (SIGAQIE)
content_hash: dbcb77bf75ea35ab196f919f065e5eb0e481b33206f627e82ed6777094b0eee6
fetched_at: '2026-06-28T22:42:26.894893+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Cadastros necessários para integrar
  com o SIGAQIE
type: support-article
updated_at: '2025-03-20T19:26:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020570212-Manufatura-Linha-Protheus-SIGAQIE-Cadastros-necess%C3%A1rios-para-integrar-com-o-SIGAQIE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16745962469783) Tempo aproximado para leitura: **00:02:15 min****Dúvida**Quais são os cadastros necessários para integrar uma entrada com o módulo **SIGAQIE - Inspeção de Entradas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Solução**Para que um documento de entrada seja integrado com o módulo de **Inspeção de Entradas** é necessário realizar as parametrizações a seguir:  
  
1. Verificar como está preenchido o parâmetro **MV\_ARQPROD - O parâmetro configura se os dados de indicadores de produto serão considerados pela tabela SB1 ou se serão considerados pela tabela SBZ**.

1.1 Caso esteja preenchido como **SB1 - Descrição Genérica do Produto**, na rotina **MATA010 - Cadastro de Produto,** o campo **B1\_TIPOCQ** **- Tipo de C.Q.** existente na aba **CQ** deve ser informado como **Sigaquality**.  
1.2 Mas, se o parâmetro estiver preenchido como **SBZ - Indicadores de Produtos**, na rotina **MATA018**- **Indicador de Produto**, o campo **BZ\_TIPOCQ** **- Tipo de C.Q.** na aba **Cadastrar** deve ser informado como **Sigaquality**.

2. Na rotina **MATA061 - Produto x Fornecedor**, deverá informar o produto e o fornecedor em questão, preenchendo todos os campos obrigatórios e também os campos **Situação - A5\_SITU**, **Tempo Limite - A5\_TEMPLIM**, **Fab/Rev/Perm - A5\_FABREV**e **Tipo de Atualização - A5\_TIPATU**. Estes campos somente estarão disponíveis nesta rotina quando acessado a rotina pelo módulo **21 - Inspeção de Entradas.** Isto porque, estes campos são utilizados apenas por este módulo.  
  
3. Na rotina **QIEA010 - Especificação de produto**, incluir uma especificação para o produto em questão. A **Especificação de Produto** deve conter **Ensaio**.  
  
4. Incluir um documento de entrada para este produto por meio da rotina **MATA103 - Documento de entrada** ou **QIEA200 - Entradas.**Se a entrada for realizada pela rotina **QIEA200- Entradas** não gerará movimentação de estoque, e por consequência, a aba **Baixas do CQ** da rotina **QIEA215 - Resultados** não será exibida.  
  
**Observação**  
Também para a integração com o **SIGAQIE** é orientado verificar o parâmetro **MV\_QNFENOR - Define quais tipos de NF do tipo Normal serão enviadas para Inspeção, através da configuração de Poder de terceiros, TES - Tipo de Entrada e Saída, sendo: Normal, Remessa e Devolução**. No artigo [Manufatura - Linha Protheus - SIGAQIE - Notas fiscais do tipo Normal não aparecem para serem inspecionadas no SIGAQIE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30802386390679-Manufatura-Linha-Protheus-SIGAQIE-Notas-fiscais-do-tipo-Normal-n%C3%A3o-aparecem-para-serem-inspecionadas-no-SIGAQIE) consta o passo a passo desta validação.  
  
**Importante**Se após verificar os passos acima, ainda não for gerado um registro na rotina **QIEA215**, verifique na rotina **QIEA183 - Importação** qual o motivo pelo qual a entrada em questão não foi processada. Situação descrita no artigo: [Manufatura - Linha Protheus - SIGAQIE - Não gerou inspeção na tabela QEK](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411512345111-Manufatura-Linha-Protheus-SIGAQIE-N%C3%A3o-gerou-inspe%C3%A7%C3%A3o-na-tabela-QEK) .
