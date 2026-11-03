---
article_id: 4411710504855
category: Financeiro
content_hash: 9b746b2c0b3d7933c68655003feb58c3c3a3cc22609b70a73b9795a73316b94f
fetched_at: '2026-06-28T22:38:01.093578+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Erros críticos e mais
  comuns ao rodar UPDDISTR
type: support-article
updated_at: '2021-10-29T12:15:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411710504855-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Erros-cr%C3%ADticos-e-mais-comuns-ao-rodar-UPDDISTR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Quais são erros críticos mais comuns em migrações ao rodar **UPDDISTR**  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – A partir da versão 12.1.23  
  
**Solução**Abaixo, os erros críticos e mais comuns ao rodar UPDDISTR

**O campo <campo> da chave de índice <alias> ordem # registro <# registro>, não existe no SX3 da empresa <empresa>**

- Abra via **APSDU** o arquivo **SIX** da empresa  
- Identifique a chave de **índice** que está gerando o erro  
- Exclua o **índice** referente a **tabela** com erro

**O gatilho <campo> sequência 000 está duplicado**

1. Abra via **APSDU** o arquivo **SX7** da empresa.  
2. Indexe o arquivo pelo campo **X7\_CAMPO**.  
3. Localize o gatilho e exclua o registro duplicado.

**A chave de índice <alias> ordem 0 registro <recno> esta duplicado**

1. Abra via **APSDU** o arquivo **SIX** da empresa.  
2. Indexe o arquivo pelo campo **INDICE**.  
3. Verifique se o conteúdo da chave de índice do erro não existe em índices de ordem inferior da tabela.  
4. Exclua o índice duplicado.

**O arquivo <alias> esta duplicado no SX2**

1. Abra via **APSDU** o arquivo **SX2** da empresa.  
2. Indexe o arquivo pelo campo **X2\_CHAVE**.  
3. Localize o arquivo e exclua o registro duplicado.

**O tamanho das casas decimais do campo <campo> arquivo \dadosadv\<arquivo>.dbf é diferente do dicionário de dados**

1. Abra via **APSDU** o arquivo existente no diretório **DADOSADV**, se o arquivo estiver vazio, basta simplesmente excluir o arquivo.  
2. Caso o arquivo tenha conteúdo, abra a estrutura da tabela e verifique o tamanho do decimal do campo com erro.  
3. Abra o **SX3** da empresa, localize o campo e compare o tamanho do **X3\_DECIMAL** com o tamanho do decimal do arquivo.  
4. Corrige a estrutura no **SX3** ou no arquivo.

**O tamanho do campo <campo> arquivo \dadosadv\<arquivo>.dbf é diferente do dicionário**

1. Abra via **APSDU** o arquivo existente no diretório **DATA\Banco de Dados**, se o arquivo estiver vazio, basta simplesmente excluir o arquivo.  
2. Caso o arquivo tenha conteúdo, abra a estrutura da tabela e verifique o tamanho do campo com erro.  
3. Abra o **SX3** da empresa, localize o campo e compare o **X3\_TAMANHO** com o tamanho do campo no arquivo.  
4. Corrija a estrutura no **SX3** ou no arquivo.

**O campo <campo> não existe no arquivo \dadosadv\<arquivo.dbf**

1. Abra o **SX3** da empresa.  
2. indexe o arquivo pelo campo **X3\_CAMPO**.  
3. Localize o campo no **SX3** e verifique sua estrutura.  
4. Abra o arquivo no diretório **DADOSADV**, verifique em sua estrutura se o campo existe.  
5. Crie o campo no arquivo.

**A estrutura do arquivo <arquivo> não existe o existe no SX3**

1. Abra o **SX3** da empresa.  
2. Indexe o arquivo pelo campo **X3\_ARQUIVO**.  
3. Localize o arquivo com erro.  
4. Para solução do problema, pode excluir o arquivo no **SX2** ou incluir os campos referentes ao arquivo no **SX3**.

**O campo <campo> esta duplicado no SX3**

1. Abra o **SX3** da empresa.  
2. Indexe o arquivo pelo campo **X3\_CAMPO**.  
3. Localize o campo duplicado.  
4. Exclua o registro.

**O tamanho no SX3 do campo <campo> é diferente do SXG**  
**O tamanho no SX3 do campo <campo> é inferior do limite do SXG**

1. Abra o **SX3** da empresa.  
2. Indexe o arquivo pelo campo **X3\_CAMPO**.  
3. Localize o campo com erro, verifique o conteúdo dos campos **X3\_TAMNHO** e **X3\_GRPSXG**.  
4. Faça um filtro na tabela somente com os campos que tenha o**X3\_GRPSXG** igual ao campo com erro.  
5. Compare o**X3\_TAMANHO** de todos os campos.  
6. Abra o **SXG** da empresa e verifique o conteúdo do campo SIZE do grupo informado no **X3\_GRPSXG**.  
7. Corrige o tamanho do campo no **SX3** e na tabela.

**O tamanho da pergunta 00 do grupo <grupo> é diferente do SXG**  
**O tamanho da pergunta 00 do grupo <grupo> é superior ao limite do SXG**

1. Abra o **SX1** da empresa.  
2. Indexe o arquivo pelo campo **X1\_GRUPO**.  
3. Localize a pergunta com erro, verifique o conteúdo dos campos **X1\_TAMNHO** e **X1\_GRPSXG**.  
4. Faça um filtro na tabela somente com as perguntas que tenha o **X1\_GRPSXG** igual à pergunta com erro.  
5. Compare o **X1\_TAMANHO** de todas as perguntas.  
6. Abra o **SXG** da empresa e verifique o conteúdo do campo SIZE do grupo informado no **X1\_GRPSXG**.  
7. Corrige o tamanho do campo no **SX1**.

**O campo de usuário <campo> existe na versão padrão e será substituído pelo campo da versão**  
Type:= c; Size:= 11; Decimal:= 0  
Type:= c; Size:= 11; Decimal:= 0

1. Abra o **SX3** da empresa.  
2. Localize o campo.  
3. Altere o conteúdo do campo **X3\_PROPRI** para **S**.

**Saiba mais**

<https://tdn.totvs.com/pages/viewpage.action?pageId=181965468>
