---
article_id: 115004669687
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 74e7fd6e4ac5c323b4e4fe139862078da46104fc606343901097c4c30622400f
fetched_at: '2026-06-28T22:38:29.990199+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Incorrect_syntax_near
type: support-article
updated_at: '2021-09-20T19:54:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004669687-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Incorrect-syntax-near
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**

Ao efetuar a contabilização, gera o erro:   
: Error : 102 (37000) (RC=-1) - [Microsoft][ODBC SQL Server Driver][SQL Server]**Incorrect syntax near "X"**  
  
**Causa**

O erro ocorre por que ao tentar executar uma query do lançamento padrão para a contabilização, o Banco de Dados está recebendo conteúdo de gravação com caractere especial **(' " # @ $ % ¨! & \*)**.

Exemplo:

Erro : 102 (37000) (RC=-1) - [Microsoft][ODBC SQL Server Driver][SQL Server]**Incorrect syntax near ''E"**. 

Veja a definição da Query do histórico aglutinado do lançamento padrão: 

**CT5\_HAGLUT(C)** :VENDAS NF."+SD2->D2\_SERIE+"/"+SD2->D2\_DOC+"-"+SUBSTR(SA1->A1\_NOME,1,15),1,40)      

Resultado recebido no arquivo de contra prova, tabela CTK :  **'VENDAS NF 001 000101 - 000008572-ABCIN ' E LTDA'**

O apostrofo entre a letra **N** e a letra **E** , é um caractere especial não aceito na montagem da query para o banco dados.

Neste caso, a  informação do nome do cliente no cadastro , por exemplo, possui um apostrofo ( ' ) na sua composição, isso interfere na codificação e gravação de banco de dados, onde ele entende que a query finalizou seu bloco de instruções quando encontra o apostrofo, o que vier após isso, fica caracterizado como erro de sintaxe.

**Ambiente**

Cross Segmentos- TOTVS Backoffice (Linha Protheus)-SIGAFAT- todas as versões  
  
**Solução**  
  
Para solucionar:  
1-Identifique o campo que está trazendo o caractere especial.

2-Retire o caractere especial da informação, assim não terá problemas para a gravação no Banco de Dados.

3- Em último caso, utilizar um execblock no lançamento padrão, para poder tratar caracteres especiais. Em caso de dúvidas sobre esse processo, contate nossa equipe de atendimento Advpl para melhor orientação.
