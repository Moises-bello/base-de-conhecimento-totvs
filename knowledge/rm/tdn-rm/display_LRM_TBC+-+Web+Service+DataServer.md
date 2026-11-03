---
content_hash: 89c1df507ca70a52833f781aa667064402d5d3cf0fc4f851cb084f71406c4468
fetched_at: '2026-06-29T00:05:59.590965+00:00'
page_id: '191465821'
product: rm
source: tdn-rm
title: TBC - Web Service DataServer
type: documentation
url: https://tdn.totvs.com/display/LRM/TBC+-+Web+Service+DataServer
version: 51
---

## Introdução

---

O Web Service **wsDataServer** é o responsável pela manipulação dos dados do sistema

## Como funciona

---

   Estão expostos no **wsDataServer** alguns serviços, onde para consumi-los é necessário enviar através de uma requisição um envelope SOAP, passando os parâmetros de cada serviço.

Atenção

**Aviso importante!**

O wsDataServer foi concebido com uma inconsistência onde os separadores decimais dos campos retornado pelos métodos ReadRecord e ReadView não são compatíveis com os separadores esperados ao salvar registros utilizando o método SaveRecord. Isso acontece por que existe uma divergência de cultura (País/Região) entre os métodos.

Pelo fato de já existirem vários cliente utilizando o wsDataServer com este comportamento, optamos por não alterá-lo para não quebrar a compatibilidade. Então criamos formas de padronizar a cultura, consequentemente os separadores, utilizando parâmetros no arquivo de configuração do HOST.

Desta forma sugerimos que novas implementações com o wsDataServer utilize a opção "Invariant" como cultura, pois estamos trabalhando para que gradativamente tudo esteja padronizado, e esta opção será adotada.

Veja como configurar e saber mais sobre o assunto através do link abaixo:

[Separadores decimais nos Web Services do RM](http://tdn.totvs.com/display/LRM/Separadores+decimais+nos+Web+Services+do+RM)

## Serviços Disponíveis

---

GetSchema

Serviço responsável por retornar o esquema XSD do DataServer passado como parâmetro.

false1Request

Os parâmetros solicitado pelo GetSchema são:

DataServerName tipo **String**

Contexto tipo **String**

xmlRequest




GlbUsuarioData

COLIGADA=1
]]>ResponsexmlResponse









































































































































































































































]]]]>
]]>GetSchemaEmail

Serviço responsável por retornar o esquema XSD do DataServer passado como parâmetro.

false1Request

Os parâmetros solicitado pelo GetSchemaEmail são:

DataServerName tipo **String**

Contexto tipo **String**

EmailUsuarioContexto tipo ****String****

xmlRequest




GlbUsuarioData

COLIGADA=1

mestre@totvs.com.br
]]>ResponsexmlResponse









































































































































































































































]]]]>
]]>IsValidDataServer

Serviço responsável por retornar se o DataServer passado como parâmetro é válido.

false1Request

Os parâmetros solicitado pelo IsValidDataServer são:

DataServerName tipo **String**

xmlRequest




GlbUsuarioData
]]>ResponsexmlResponse


true
]]>ReadRecord

Serviço responsável por efetuar a leitura do DataServer e retornar um XML contendo registros de acordo com a chave primária e o contexto informado

false1Request

Os parâmetros solicitado pelo ReadRecord são:

DataServerName tipo **String**

PrimaryKey tipo **String**

Contexto tipo **String**

xmlRequest




GlbUsuarioData

mestre

CODSISTEMA=G
]]>ResponsexmlResponse










































































































































































































































mestre
Usuário Mestre
1
1997-01-01T00:00:00
oaEGFhDF
27621
1
Acesso02
2014-05-08T00:00:00
F
0
mestre@totvs.com.br
T
2015-07-03T14:48:08.447
matheus.sena
BH01

5ddcc1c2-94b4-4974-8ed3-99aeb3dee5cf
2015-07-03T14:48:08.473

1
G
mestre
1
13820
1
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53

6
G
mestre
1
16870
1
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53

7
G
mestre
1
-16926
1
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53

8
G
mestre
1
-22062
1
mestre
2015-03-20T15:39:08
mestre
2015-07-03T12:03:53

1
mestre
G
DBA
20
-4619
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

6
mestre
G
DBA
69
-17714
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

6
mestre
G
DP
70
18884
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

6
mestre
G
Perfil1
71
-14972
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

7
mestre
G
DBA
102
19415
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

7
mestre
G
DP
103
-26402
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

7
mestre
G
Perfil1
104
2505
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

8
mestre
G
DBA
0
-6925
mestre
2015-03-20T15:39:08
mestre
2015-07-03T12:03:53
1
]]]]>
]]>ReadRecordEmail

Serviço responsável por efetuar a leitura do DataServer e retornar um XML contendo registros de acordo com a chave primária, contexto e e-mail informado.

false1Request

Os parâmetros solicitado pelo ReadRecordEmail são:

DataServerName tipo **String**

PrimaryKey tipo **String**

Contexto tipo **String**

EmailUsuarioContexto tipo **String**

xmlRequest




GlbUsuarioData

mestre

CODSISTEMA=G

mestre@totvs.com.br
]]>ResponsexmlResponse










































































































































































































































mestre
Usuário Mestre
1
1997-01-01T00:00:00
oaEGFhDF
27621
1
Acesso02
2014-05-08T00:00:00
F
0
mestre@totvs.com.br
T
2015-07-03T14:48:08.447
matheus.sena
BH01

5ddcc1c2-94b4-4974-8ed3-99aeb3dee5cf
2015-07-03T14:48:08.473

1
G
mestre
1
13820
1
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53

6
G
mestre
1
16870
1
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53

7
G
mestre
1
-16926
1
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53

8
G
mestre
1
-22062
1
mestre
2015-03-20T15:39:08
mestre
2015-07-03T12:03:53

1
mestre
G
DBA
20
-4619
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

6
mestre
G
DBA
69
-17714
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

6
mestre
G
DP
70
18884
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

6
mestre
G
Perfil1
71
-14972
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

7
mestre
G
DBA
102
19415
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

7
mestre
G
DP
103
-26402
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

7
mestre
G
Perfil1
104
2505
mestre
2011-04-14T15:55:17
mestre
2015-07-03T12:03:53
1

8
mestre
G
DBA
0
-6925
mestre
2015-03-20T15:39:08
mestre
2015-07-03T12:03:53
1
]]]]>
]]>ReadView

Serviço responsável por efetuar a leitura do DataServer e retornar um XML contendo registros de acordo com o **contexto** e o **filtro** informado.

false1Request

Os parâmetros solicitado pelo ReadView são:

DataServerName tipo **String**

Filtro tipo **String**

Contexto tipo **String**

xmlRequest




GlbUsuarioData

CODUSUARIO='mestre'

CODSISTEMA=G,CODUSUARIO=mestre,CODCOLIGADA=1
]]>ResponsexmlResponse




mestre
aa Mesaatre
Acesso02
1
1997-01-01T00:00:00
2015-07-03T16:52:51.293
mestre@totvs.com.br
]]]]>
]]>ReadViewEmail

Serviço responsável por efetuar a leitura do DataServer e retornar um XML contendo registros de acordo com o **contexto**,**filtro** e **e-mail** informado.

false1Request

Os parâmetros solicitado pelo ReadViewEmail são:

DataServerName tipo **String**

Filtro tipo **String**

Contexto tipo **String**

**EmailUsuario**

xmlRequest




GlbUsuarioData

CODUSUARIO='mestre'

CODSISTEMA=G,CODUSUARIO=mestre,CODCOLIGADA=1

mestre@totvs.com.br
]]>ResponsexmlResponse




mestre
Usuário Mestre
Acesso02
1
1997-01-01T00:00:00
2015-07-03T14:48:08.447
mestre@totvs.com.br
]]]]>
]]>SaveRecord

Serviço responsável por efetuar alterações de registros do DataServer de acordo com o **XML** informado.

falseATENÇÃO:

Se a Tag de algum campo for informada sem conteúdo, a informação será anulada ou preenchida em branco.

Mais informações para os 

Exclusão de registros Associados

Para se remover todos registros associados ao dado mestre do wsDataServer deve-se enviar uma tag vazia com o nome do registro. Não enviar nenhum registro associado não causará a exclusão destes registros.

(Ex.: No Data Server GlbUsuarioData o registro 'GUSUARIO' pode ter relação com várias 'GUSRPERFIL'. Para remover os dados de perfil 'GUSRPERFIL' associados deve-se enviar xml com os campos chave do registro <GUSUARIO> e o tag vazio<GUSRPERFIL/> j')

false1Request

Os parâmetros solicitado pelo SaveRecord são:

DataServerName tipo **String**

XML tipo **String**

Contexto tipo **String**

xmlRequest




GlbUsuarioData



mestre
Usuário Mestre
Acesso02
1
1997-01-01T00:00:00
2015-07-03T14:48:08.447
mestre@totvs.com.br
]]]]>

?
]]>ResponsexmlResponse


mestre
]]>SaveRecordEmail

```
Serviço responsável por efetuar alterações de registros do DataServer de acordo com o XML e Email informado. 
```

false1Request

Os parâmetros solicitado pelo SaveRecordEmail são:

DataServerName tipo **String**

XML tipo **String**

Contexto tipo **String**

EmailUsuarioContexto tipo **String**

xmlRequest




GlbUsuarioData



mestre
Usuário Mestre
Acesso02
1
1997-01-01T00:00:00
2015-07-03T14:48:08.447
mestre@totvs.com.br
]]]]>

?

mestre@totvs.com.br
]]>ResponsexmlResponse


mestre
]]>

totContext

## Formato dos parâmetros na Tag de contexto

Para o correto funcionamento da sua requisição, remova todos os espaços em branco do conteúdo da tag de Contexto.

O valor de cada parâmetro deve ser informado sem espaço ou caractere especial, como vírgula, aspas e etc.

powershellRDarkFormato esperadoCODCOLIGADA=1;CODUSUARIO=mestre;CODSISTEMA=F]]>

Exemplo de formato inválido

powershellFormato inválidoCODCOLIGADA = 1;CODUSUARIO="mestre";CODSISTEMA='F']]>

---

**Para utilização dos Web Services através do aplicativo "Totvs Web Service Test", clique [aqui](http://tdn.totvs.com/x/yBdFCg).**

Para maiores informações:

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

|  |  |
| --- | --- |
| **Produto** | Framework |
| **Versão** | 11.82.XX |
| **Processo** | Web Services |
| **Subprocesso** | Utilizando o Web Service wsDataServer |

|  |  |
| --- | --- |
| Status do Documento: | Finalizado |
| Data: | 30/06/2015 |
| Versão: | 11.82.XX |
| Versão Anterior: | 11.82.XX |
| Autores: |  |
