---
content_hash: 4427d32257e530d2a8ed97ed4df0cbcf8f5436d9c6547585afda614192a08f72
fetched_at: '2026-06-29T00:05:50.988852+00:00'
page_id: '104661173'
product: rm
source: tdn-rm
title: Sub - Relatório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=104661173
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Reports                        **Versão:**11.82 |
| **Processo** | **:** | Relatório |
| **Subprocesso** | **:** | Sub- Relatório |
| **Data da publicação** | **:** | 25/11/2013 |

**Introdução**

Ao selecionar esta opção serão apresentadas as tabelas disponíveis em “Lista de Campos”. Esta opção constrói uma associação mestre detalhe entre duas tabelas.

Um exemplo pratico seria

Coligadas -> Filiais

Seção -> Funcionário

Cliente -> Lançamento

Turma -> Aluno

Podemos optar por duas opções

A primeira “Sem ligamento”

Nesta opção o Report ira inserir um subdetalhe para o detalhe1 sem ligamento, ou seja sem relacionamento com algum tipo de tabela ou SQL.

Neste caso o usuário pode optar por inserir posteriormente uma tabela, uma SQL, etc.

A segunda “tabela disponível” (em nosso exemplo Filiais). Nesta opção serão apresentadas as tabelas que foram adicionadas anteriormente ao relatório.

Em nosso exemplo será apresentada a tabela de “Filiais”, neste caso o report já fará um relacionamento direto entre as tabelas de coligadas(máster) e filiais(child), inserindo um subdetalhe com a tabela selecionada.

**Exemplo Prático**

Como exemplo vamos fazer um relatório de envelope de pagamento para demonstrar a utilização do recurso **SUB RELATÓRIO** .

Assim é criado um relatório (ENVELOPE) com a tabela Ficha Financeira (PFFINANC), como tabela máster do detalhe1. No cabeçalho do detalhe1 foi incluído o Campo Nome da tabela de Funcionários (PFUNC) onde é configurada uma quebra por Chapa.

Adicionamos um filtro de Mês e ano de competência

Ao gerar o relatório temos o Resultado abaixo:

Para utilizar o Recurso Sub Relatório, temos que criar dois relatórios para retornar os valores de proventos e descontos do funcionário.

Assim criamos dois relatórios um para retornar apenas proventos e outro para retornar apenas descontos:

Segue abaixo as imagens mostrando a estrutura destes dois relatórios criados. Vale ressaltar que a diferença entre os dois é apenas o filtro no relatório utilizando o campo Provento/desconto (PROVDESCBASE) da tabela PEVENTO.

Assim:

Criado apenas um Detalhe1 com a tabela Master FICHA FINANCEIRA com os campos:

Configuramos o tamanho e margem do relatório nas propriedades **RptReport** como mostrado abaixo:

Com essas configurações a estrutura ficará desta forma:

Após a criação dos relatórios vamos incluir o recurso SUB RELATÓRIO no relatório Principal.

Conforme exemplo:

Após incluir o Sub Relatório, Agora basta vincular o relatório de Proventos nas propriedades do Sub Relatório e definir o relacionamento:

Parametrizando o relacionamento.

 

Relatório Gerado com os proventos do Funcionário:

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
