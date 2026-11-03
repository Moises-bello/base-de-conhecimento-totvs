---
content_hash: 4f0c892747b4e49d3cd2e3492a1effb8066c105123aae1d57d0b0898f7a695b9
fetched_at: '2026-06-29T00:08:59.465358+00:00'
page_id: '362457676'
product: rm
source: tdn-rm
title: Dicas para um Código Mais Performático
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=362457676
version: 17
---

# Dicas para um Código Mais Performático

# Objetivo

Este documento tem por objetivo mostrar alguns itens para código mais performático que foram localizados no dia a dia do Analista.

# Dicas

falsedicasdica1Dica 1

Evitar chamadas "burras" ao server. Ao executar o ReadRecord é feita uma consulta que não vai retornar nada porque as chaves estão null e se existir campos complementares a lib vai executar uma consulta no banco que também não irá retornar nada.

c#

No caso acima é possível passar para o dataserver o contexto sem executar o ReadRecord, pois o método GetUsrFilter é um método do EduDataServer que estende de RMSDataServer.

c#(dataServerUserFilterTable))
userFilters = userFilters.Append(serverFilter != null ? serverFilter.GetUsrFilter(Context) : string.Empty);]]>c#dica2Dica 2

Evitar chamadas desnecessárias de ReadRecord, se deseja apenas trazer apenas alguns campos. Ao executar o ReadRecord é feita uma consulta que ir retornar um dataset completo com vários campos que nem serão utilizados, além de trazer os campos complementares do mesmo no dataset. Por exemplo, se há a necessidade de buscar os valores dos campos CODCURSO, CODHABILITACAO e CODGRADE não se dá a necessidade de executar um ReadRecord para tal fim.

c#("EduHabilitacaoFilialData");
DataSet ds = dtServer.ReadRecord(RMSSession.Context, new object[] { base.CodColigada, idHabFilial }, null);
if ((ds != null) && (ds.Tables.Count > 0) && (ds.Tables[0].Rows.Count > 0))
this.SetHabilitacaoFilial(
ds.Tables[0].Rows[0]["CODCURSO"].ToString(),
ds.Tables[0].Rows[0]["CODHABILITACAO"].ToString(),
ds.Tables[0].Rows[0]["CODGRADE"].ToString(),
idHabFilial);]]>

No caso acima ao invés de executar o um ReadRecord, executa-se um consulta simples trazendo apenas os campos pertinentes conforme abaixo.

c#c#dica3Dica 3

Sempre observar a ordem das chaves para fazer um join, ao colocar na ordem correta se torna mais performática a consulta. Abaixo temos um join com chaves fora da ordem no banco de dados.

sql

Abaixo temos o mesmo join com a ordem correta do banco.

sql

Ordem das chaves no banco.

dica4Dica 4

Sempre informar o tipo do campo no filtro da sua consulta. Abaixo temos um exemplo de filtro sem o tipo. A importância deste tipo é fazer com que a lib não procure que tipo (string, número, data e etc.) é aquele campo do filtro.

sql

Abaixo temos a tipagem de campos do filtro.

sql

Tipos disponíveis:

* \_D: DateTime;
* \_V: Float;
* \_N: Int;
* \_S: String;
* \_H: Short.
dica5Dica 5

Sempre utilizar o cache de parâmetro no lado **Client**, o carregamento da classe de parâmetros é muito custoso. Abaixo temos um exemplo que sempre ao chamar o EduParametros é feito o carregamento de toda a classe de parâmetros.

c#

Segue abaixo a utilização de cache de parâmetros.

c#dica6Dica 6

```
Evite utilizar os serviços abaixo para atualização de informações em lote, pois os mesmo geram muito IO no banco.
```

```
Dependendo do volume de dados isso se torna muito custoso, principalmente se estiver dentro de um laço de repetição.
```

c#
("SLANDESCPONTUAL", descontoPontual, campos, valoresPK, this.DBS, codUsuario, out registroExiste, out pk);
EduDatasetUtils.ExcluiRegistro
("SLANDESCPONTUAL", campos, valores, this.DBS, codUsuario);
EduDatasetUtils.InsereRegistro
("SLANDESCPONTUAL", descontoPontual, this.DBS, codUsuario);]]>

Uma solução seria conforme abaixo, carregar uma lista e executar um QueryUpdate com todos os dados.

c# MatriculaDisc = this.dbo.ReadFromTable(tbMatriculaDisc);
EduMatriculaDiscItem mat = MatriculaDisc.NewObject();
this.dbo.MoveValues(paramDisc, mat);
this.dbo.WriteToTable(MatriculaDisc);
this.DBS.QueryUpdate(tbMatriculaDisc, paramDisc.CodUsuario);]]>
