---
article_id: 360025544331
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 6ddf4334f1a4b7858f1a4624cdde6da676f30b98a3b305d1b19389ad08cc1f4c
fetched_at: '2026-06-28T22:38:29.799468+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Erros relacionados a expressão
  Invalid Macro Source
type: support-article
updated_at: '2025-12-29T20:04:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025544331-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Erros-relacionados-a-express%C3%A3o-Invalid-Macro-Source
---

**Ocorrência**  
O que fazer quando o sistema gerar erro de **invalid macro source (SSYacc0105e: Error token failed, no valid token)?**  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - todas as versões.

**Causa**  
Esse tipo de erro, em geral, está relacionado às validações de usuário definidas na estrutura SX3, como nos campos X3\_RELACAO, X3\_PICTVAR, X3\_WHEN ou X3\_INIBRW, associados a determinado campo da tabela.

Outra possível causa é o cadastro de fórmulas ou filtros, especialmente nos casos em que a query esteja incompleta ou incorreta.

**Solução**  
Para corrigir o problema, siga uma das alternativas abaixo:

1. Se os campos **x3\_relação, x3\_pictvar, x3\_when ou x3\_inibrw,** da tabela informada no erro, se há alguma informação que não esteja entre aspas duplas, ou está com aspas duplas e simples ao mesmo tempo. Para corrigir, acerte a informação colocando entre aspas duplas .

Exemplo: **"1"** ;

2. Se alguma informação do tipo numérica sendo passada sem uso de aspas (" "), visto que o campos **x3\_relação, x3\_pictvar, x3\_when ou x3\_inibrw**são do tipo carácter. Para corrigir, acerte a informação colocando entre aspas duplas;

Exemplo: **"2";**

3. Se está sendo passado uma instrução ADVPL e não está fechando adequadamente parênteses, chaves e colchetes, para corrigir, acerte a expressão Advpl colocando os devidos  parênteses, chaves e colchetes que estão faltando.

**OBS 1:** Para descobrir o campo que apresenta o erro, basta procurar no errorlog, a tabela de estrutura SX3, que demonstrará o campo que foi lido e está com erro, exemplo:

d:\outsourcing\clientes\lvz2xd\protheus\_data\system\sx3010.dtc; Rdd:DBFCDX; Alias:SX3; Filter :; Recno:124520; Total Recs:124529; Order:2

Index (1) :\*\*SX30101 X3\_ARQUIVO+X3\_ORDEM

Field 1: D\_E\_L\_E\_T\_E\_D(C) :

Field 2: R\_E\_C\_N\_O(N) :124520

Field 3: X3\_ARQUIVO(C) :SA1

Field 4: X3\_ORDEM(C) :P6

**Field 5: X3\_CAMPO(C) :A1\_NR\_END**

Field 6: X3\_TIPO(C) :C

Field 18: X3\_RELACAO(C) :  
  
**Field 33: X3\_PICTVAR(C) :@!**

Field 34: X3\_WHEN(C) :

Field 35: X3\_INIBRW(C) : 

**OBS 2:** No caso do cadastro de fórmulas, procure no erro por querys incompletas que poderão também ser indicadas após a informação do erro no valid token:

* **invalid macro source (SSYacc0105e: Error token failed, no valid token)** :**IF(U\_NEO34A04(SF2->F2\_FILIAL,SF2->F2\_DOC,SF2->F2\_SERIE,SF2->F2\_CLIENTE,SF2->F2\_LOJA,SF2->F2\_TIPO) .AND.SUBSTR(SF2->F2\_EMISSAO,1,6)==SUBSTR(DTOS(DATE()),1,6).AND.!SF2->F2\_TIPO $ "D/B",SF2->F2\_VALISS ,****0** **on DETPROVA(MATXFUNA.PRX**) - Veja que nesta instrução falta o parênteses para fechar a query. Neste caso, basta finalizar a instrução com o parênteses.          ***Exemplo***: :IF((U\_NEO34A04(SF2->F2\_FILIAL,SF2->F2\_DOC,SF2->F2\_SERIE,SF2->F2\_CLIENTE,SF2->F2\_LOJA,SF2->F2\_TIPO) .AND.SUBSTR(SF2->F2\_EMISSAO,1,6)==SUBSTR(DTOS(DATE()),1,6).AND.!SF2->F2\_TIPO $ "D/B",SF2->F2\_VALISS ,0**)**

* **invalid macro source (SSYacc0105e: Error token failed, no valid token)** :**DbSetFilter({||(A1\_MSBLQL== "1" dToS(A1\_DTCAD) >= "20170201"** **.AND.** **)},'(A1\_MSBLQL== "1" dToS(A1\_DTCAD) >= "20170201" .AND. )')** on FWBRWTABLE:EXECUTEFILTER(FWBRWTABLE.PRW) - Veja que nesta instrução que não há término da query após o operador **.AND.**, neste caso, é preciso avaliar a query e corrigi-la , seja complementando a instrução após o operador .AND. ou finalizando a instrução, retirando o operador .AND. da query, por exemplo.

4. Caso o erro ocorra na abertura da rotina, avalie se há alguma fórmula criada dentro de filtros. Nessa situação, a recomendação é realizar a limpeza do profile do usuário por meio da rotina:

[Framework - Linha Protheus - Manutenção de Profile de Usuários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025097012-Framework-Linha-Protheus-Manuten%C3%A7%C3%A3o-de-Profile-de-Usu%C3%A1rios)
