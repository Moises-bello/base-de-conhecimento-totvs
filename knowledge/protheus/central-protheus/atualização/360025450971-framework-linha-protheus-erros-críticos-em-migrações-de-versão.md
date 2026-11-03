---
article_id: 360025450971
category: Atualização
content_hash: 968e4ff1dad49fb78a883c98fc0476a9575fc254a3afe2cd5cc5f29e3ff85a1c
fetched_at: '2026-06-28T22:42:21.323211+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus - Erros críticos em migrações de versão
type: support-article
updated_at: '2026-06-05T01:57:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025450971-Framework-Linha-Protheus-Erros-cr%C3%ADticos-em-migra%C3%A7%C3%B5es-de-vers%C3%A3o
---

**Dúvida**Quais são os erros críticos mais comuns em migrações de versão?  
   
 **Ambiente**Protheus - AppServer - Todas as versões  
   
**Solução**Durante migrações de versão e de release, podem ocorrer erros críticos, que impedem a continuação da migração até que sejam corrigidos. Abaixo listamos os erros críticos mais comuns e suas correções:  
  
**O campo <campo> da chave de indice <alias> ordem # registro <# registro>, nao existe no SX3 da empresa <empresa>**  
1. Abra via APSDU o arquivo SIX da empres  
2. Identifique a chave de indice que está gerando o erro  
3. Exclua o índice referente a tabela com erro  
  
**O gatilho <campo> seqüência 000 está duplicado**  
1. Abra via APSDU o arquivo SX7 da empresa.  
2. Indexe o arquivo pelo campo X7\_CAMPO.  
3. Localize o gatilho e exclua o registro duplicado.  
  
**A chave de índice <alias> ordem 0 registro <recno> esta duplicado**  
1. Abra via APSDU o arquivo SIX da empresa.  
2. Indexe o arquivo pelo campo INDICE.  
3. Verifique se o conteúdo da chave de índice do erro não existe em índices de ordem inferior da tabela.  
4. Exclua o índice duplicado.  
  
**O arquivo <alias> esta duplicado no SX2**  
1. Abra via APSDU o arquivo SX2 da empresa.  
2. Indexe o arquivo pelo campo X2\_CHAVE.  
3. Localize o arquivo e exclua o registro duplicado.  
  
**O tamanho das casas decimais do CAMPO <campo> TABELA <tabela> é diferente do dicionário de dados**  
1. Abra via APSDU a TABELA, se estiver vazia basta simplesmente dropar a TABELA do Banco de dados.  
2. Caso tenha conteúdo, abra a estrutura da tabela e verifique o tamanho do decimal do campo com erro.  
3. Abra o SX3 da empresa, localize o campo e compare o tamanho do X3\_DECIMAL com o tamanho do decimal da TABELA.  
4. Corrija a estrutura no SX3.  
  
**O tamanho do CAMPO <campo> TABELA <tabela> é diferente do dicionário**  
1. Abra via APSDU a TABELA, se a TABELA estiver vazia basta simplesmente dropar do Banco de dados.  
2. Caso o arquivo tenha conteúdo, abra a estrutura da tabela e verifique o tamanho do campo com erro.  
3. Abra o SX3 da empresa, localize o campo e compare o X3\_TAMANHO com o tamanho do campo na TABELA.  
4. Corrija a estrutura no SX3.  
  
**O campo <campo> esta duplicado no SX3**  
1. Abra o SX3 da empresa.  
2. Indexe o arquivo pelo campo X3\_CAMPO.  
3. Localize o campo duplicado.  
4. Exclua o registro.  
  
**O tamanho no SX3 do campo <campo> é diferente do SXG**  
**O tamanho no SX3 do campo <campo> é inferior do limite do SXG**  
1. Abra o SX3 da empresa.  
2. Indexe o arquivo pelo campo X3\_CAMPO.  
3. Localize o campo com erro, verifique o conteúdo dos campos X3\_TAMNHO e X3\_GRPSXG.  
4. Faça um filtro na tabela somente com os campos que tenha o X3\_GRPSXG igual ao campo com erro.  
5. Compare o X3\_TAMANHO de todos os campos.  
6. Abra o SXG da empresa e verifique o conteúdo do campo SIZE do grupo informado no X3\_GRPSXG.  
7. Corrige o tamanho do campo no SX3 e na tabela.  
  
**O tamanho da pergunta 00 do grupo <grupo> é diferente do SXG**  
**O tamanho da pergunta 00 do grupo <grupo> é superior ao limite do SXG**  
1. Abra o SX1 da empresa.  
2. Indexe o arquivo pelo campo X1\_GRUPO.  
3. Localize a pergunta com erro, verifique o conteúdo dos campos X1\_TAMNHO e X1\_GRPSXG.  
4. Faça um filtro na tabela somente com as perguntas que tenha o X1\_GRPSXG igual à pergunta com erro.  
5. Compare o X1\_TAMANHO de todas as perguntas.  
6. Abra o SXG da empresa e verifique o conteúdo do campo SIZE do grupo informado no X1\_GRPSXG.  
7. Corrige o tamanho do campo no SX1.  
  
**O campo de usuário <campo> existe na versão padrão e será substituído pelo campo da versão**  
**Type:= c; Size:= 11; Decimal:= 0**  
**Type:= c; Size:= 11; Decimal:= 0**  
1. Abra o SX3 da empresa.  
2. Localize o campo.  
3. Altere o conteúdo do campo X3\_PROPRI para S.
