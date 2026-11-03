---
article_id: 1500012361522
category: Financeiro - Contas a Receber
content_hash: 82a79d5dd5f155da853615e8f03728679554e8a9a7e1c8683a145b2d8a4b12b7
fetched_at: '2026-06-28T22:38:12.649834+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA330 - HELP:NOTITSEL
type: support-article
updated_at: '2026-06-03T19:07:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012361522-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA330-HELP-NOTITSEL
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23008203597719)**Tempo aproximado para leitura: **00:10:00 min**

**Ocorrência**  
Ao realizar a compensação na rotina FINA330, apresenta o mensagem de HELP: **NOTITSEL**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA330 - Todas as versões  
  
**Causa**  
Quando é compensado uma NF com um RA/NCC e é apresentado o HELP: NOTITSEL  
  
**Solução**  
Temos alguns processos que ao serem executados na rotina de Compensação o sistema retornará o help NOTITSEL.

Neste artigo será mencionado alguns cenários para que sejam validados, buscando agilizar a solução do tema.

1 - Note se no estorno  é o mesmo cliente e loja, caso não seja vai até o parâmetro (F12) da rotina **Fina330** e configure para não considerar o cliente ou a loja ou os 2.  
  
![img 1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37345392963095)​  
  
2 - Outro erro é quando o **E5\_DOCUMEN** esteja vazio, ou o sistema tenha gravado errado o processo

![img 2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37345392966295)

​  
  
3 - Cliente lança uma **NF** e uma **RA/NCC** , na hora de compensar/estornar, da erro **NOTITSEL**, com uma **RA/NCC**.  
Verificar os campos “Parcela” das tabelas **SE1** e **SE5** se estão com o mesmo tamanho no dicionário e banco de dados. Assim como o conteúdo do parâmetro **MV\_1DUP** se está coerente ao tamanho destes campos.

Valide se os campos abaixo possuem os mesmos tamanhos na **SE1** e **SE5**, além disso valide a quantidade de "caracteres" que tem nos campos abaixo dos registro com problema. Por exemplo.  
Tamanho e conteúdos dos Campos:

**E1\_FILIAL = E5\_FILIAL**  
**E1\_PREFIXO = E5\_PREFIXO**  
**E1\_NUM = E5\_NUMERO**  
**E1\_PARCELA = E5\_PARCELA**  
**E1\_TIPO = E5\_TIPO**                                                                                                                                        

**Exemplo**  
Quantidade de "caracteres":  
Veja que o registro possui o campo **E1\_NUM** com '5555     ', ou seja nesse registro o campo **E1\_NUM** possui quantidade de "caracteres" 9 contando o 5555 e os espaços em branco.

**Importante**  
O campo **E5\_DOCUMEN** contém uma chave, onde a mesma deve respeitar os espaços dos campos.  
  
![img3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37345381902615)​  
  
4 - Valide se o campo **MV\_1DUP** está de acordo com a documentação abaixo.  
[Cross Segmento - Backoffice Linha Protheus - FINA050 - Desdobramento acima de 35 parcelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021873891-MP-SIGAFIN-Desdobramento-acima-de-35-parcelas)  
  
5 - Observe se no estorno a data da contabilização está diferente, exemplo contabilizou dia 26/12/2020 e e estornou dia 23/12/2020 nessa situação é apresentado o help.

6 - Se o título compensado está em outra filial, utilize e opção de Filiais para buscar os registros por filial 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11820768815511)

7 - Se o parâmetro [**MV\_RARTIMP**](https://tdn.totvs.com/display/public/PROT/MV_RARTIMP)estiver configurado para reter os **impostos no RA**, ao realizar uma compensação entre um **RA** com impostos e uma **NF** sem impostos é apresentado o help.

Quando é usado [MV\_RARTIMP](https://tdn.totvs.com/display/public/PROT/MV_RARTIMP) = 1, os impostos do tipo RA terão que ter os mesmo impostos do tipo NF para que não apresente o HELP NOTITSEL  
Sugiro que use os mesmos códigos de natureza e cliente tanto na NF como no RA.

8 - Caso algum dos registros estejam com o E5\_SEQ ou FK1\_SEQ de forma NÃO incremental  repetindo a mesma sequência, ao estornar poderá apresentar

"HELP NOTITSEL Não foi localizado nenhum titulo para a compensação"

Exemplo:

NF compensando parcial com NCC

a) NF compensou parcial com a NCC, será criado 2 linhas nas tabelas SE5 e FK1, com o conteúdo E5\_SEQ=**01**, FK1\_SEQ=**01**

b) NF compensou parcial novamente com a NCC, será criado 2 linhas nas tabelas SE5 e FK1, com o conteúdo E5\_SEQ=**02**, FK1\_SEQ=**02**

c) NF compensou parcial novamente com a NCC, será criado 2 linhas nas tabelas SE5 e FK1, com o conteúdo E5\_SEQ=**03**, FK1\_SEQ=**03**

Caso houver um problema de base onde a próxima compensação parcial **d)** grave conteúdo E5\_SEQ=**01**, FK1\_SEQ=**01**, ao estornar essa baixa irá apresentar

"HELP NOTITSEL Não foi localizado nenhum titulo para a compensação" já que teremos duas compensações com o mesmo numero de sequência de baixas.

Para incrementar a sequência de baixa, o sistema obtém o conteúdo do campo FK7\_IDDOC da NCC e pesquisa se tem o mesmo conteúdo no campo FK1\_IDDOC, caso não encontre será gravado a sequência E5\_SEQ=**01**, FK1\_SEQ=**01.**

**Saiba Mais**

[Compensação - Geração dos impostos do título RA - MV\_RARTIMP](https://tdn.totvs.com/display/public/PROT/MV_RARTIMP)

[Compensação contas a receber- FINA330 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=505768648)
