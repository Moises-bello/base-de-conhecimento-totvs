---
content_hash: f33ac7354167dd76695be0a7e576e97874f046cc8ad6696896b8a20920594273
fetched_at: '2026-06-29T00:09:09.215233+00:00'
page_id: '393353174'
product: rm
source: tdn-rm
title: Data de alteração para eventos que possuem histórico (Eventos 2206 e 2306)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393353174
version: 7
---

Sempre que o usuário realizar uma alteração no cadastro de funcionário será verificado se os campos abaixo foram alterados e deverá criar um gatilho considerando as datas de mudança informadas na alteração (histórico).

Será criado um gatilho para cada uma das datas diferentes, agrupando por data de alteração:

* Salário
* Horário
* Função
* Transferência entre Seções
* Cargo de confiança

Caso esteja alterado um campo diferente dos mencionados acima, ou seja, que não tem histórico, a data do gatilho deverá ser a data do sistema operacional.

 A informação está após a execução de script de atualização da base de dados.

**ATENÇÃO:** O script a ser executado se encontra em <https://suporte.totvs.com/portal/p/10098/download#detail/706173>

 Ao salvar, caso a alteração seja anterior a competência atual, será apresentado uma mensagem de confirmação informado que todas as alterações posteriores devem ser retificadas.

**Exemplo:**

Cadastro             Data da Mudança

Horário                10/05/2018

Salario                  01/05/2018

Função                 20/05/2018

Caso tenha uma nova alteração de função com data anterior a 20/05/2018 será verificada a menor das alterações de todos os eventos S-2206 existentes na fila de eventos maior ou igual a data escolhida e será apresentado uma mensagem orientando para a retificação da informação caso necessário.

**Geração do XML**

Na geração dos XMLs S-2206 ou S-2306, para os campos abaixo, a informação será a maior do histórico de mudança.

O resultado deverá ser o registro do histórico com maior data desde que seja menor ou igual a data do gatilho.

* Salário
* Horário
* Função
* Transferência entre Seções
* Cargo de confiança

Gerar um gatilho para cada data preenchida na tela.

**Exemplo:**

01/09 = alteração do salário

10/09 = alteração do horário

**Gerado para a alteração salarial o XML com salário alterado e o horário do histórico em 01/09**

**Gerado para a alteração de horário o XML com salário alterado e o horário também alterado**

Ao realizar uma alteração no cadastro do funcionário e salvar o sistema gerará um gatilho para cada alteração realizada, sendo que a data da alteração será a data da mudança do campo:

**Exemplo:**

Informações do cadastro do funcionário

**Nome: Edmundo**

**Função: 00002**

PFHSTFUNCAO 01/09: 0001

PFHSTFUNCAO 14/09: 0002

**Seção: 03.01**

 PFHSTSECAO 01/09 = 03.01

**Horário: 0002**

PFHSTHORARIO 01/09 = 0001

 PFHSTHORARIO 10/09 = 0002

**Salário: R$ 8.555,09**

PFHSTSAL 01/09 = R$ 8.555,09

**Informações do XML S-2206**

DATA MUDANÇA            FUNÇÃO                     SEÇÃO                  HORÁRIO           SALARIO

01/09                                    0001                           03.01                     0001                      8.555,09

10/09                                    0001                           03.01                     0002                      8.555,09

14/09                                    0002                           03.01                     0002                      8.555,09

**XML DA DATA DE ALTERAÇÃO 01/09**

**XML DA DATA DE ALTERAÇÃO 10/09**

**XML DA DATA DE ALTERAÇÃO 14/09**
