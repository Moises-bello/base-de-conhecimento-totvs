---
content_hash: 435694b2a02a8a08534e6f7efb0484cb0356cab2ccf243768fe64ac0865aeaaa
fetched_at: '2026-06-29T00:08:46.596550+00:00'
page_id: '317305881'
product: rm
source: tdn-rm
title: Consulta ao acervo - WebService
type: documentation
url: https://tdn.totvs.com/display/LRM/Consulta+ao+acervo+-+WebService
version: 8
---

### Visão geral

O objetivo deste dataserver é possibilitar a consulta ao acervo através de webservice, será retornado exatamente a mesma consulta ao acervo utilizada na pesquisa geral do TOTVS Gestão Bibliotecária.

Através do dataserver "**BibConsultaAcervoDataWS**" é possível por meio dos métodos **ReadView** e **ReadRecord** realizar uma busca que retorne vários resultados e detalhar um resultado específico, assim como na tela de consulta ao acervo disponibilizada pelo TOTVS Gestão Bibliotecária.

### Método ReadView

Este método realiza a busca geral ao acervo, deve ser informando o campo e o termo que será pesquisado. O sistema irá realizar uma busca e se encontrar publicações irá retornar um dataset (XML) com quatro tabelas, a primeira com os detalhes da publicação ou das publicações encontradas, a segunda com as unidades bibliotecárias que as publicações encontradas possuem exemplares, a terceira e quarta respectivamente com os autores e assuntos vinculados as publicações.

As tabelas Unidades, Assuntos e Autores são relacionadas com a tabela Publicação, os relacionamentos de ambas as tabelas é dado pelas colunas **CODIGOITEMPESQUISA, CODCOLIGADA** e **CODPUBLIC.**

### Método ReadRecord

Este método é responsável por carregar os detalhes  de uma única publicação, além de carregar os mesmos dados que já são retornados pelo **ReadView** deuma determinada publicação, serão retornados também todos os exemplares disponíveis para a publicação, bem como, os dados de sumário, marc21, volumes, áreas e subáreas de conhecimento.

Os exemplares retornados para uma determinada publicação poderão ter artigos e fascículos, estes dados estão vinculados com a tabela de exemplares, e este vínculo poderá ser utilizado pelas colunas **CODCOLIGADA**, **CODPUBLIC** e **CODEXEMPLAR.**

Os demais dados são únicos por publicação e sendo assim não precisam de vínculos diretos com a publicação pois já são vinculados a ela.

### Campos permitidos para a pesquisa

Para a pesquisa (**ReadView**) devem ser informados dois campos (detalhados no próximo item), um deles é qual campo será utilizado para a busca, ou seja, qual campo o sistema irá utilizar para pesquisar o termo de uma publicação.

Abaixo segue a lista de campos que são permitidos, se for informado um campo que não existe nesta lista o sistema não retornará resultados.

|  |  |
| --- | --- |
| **Nome do campo** | **Campo para busca** |
| Artigo | Artigo |
| Assunto | Assunto |
| Autor | Autor |
| Categoria | Categoria |
| Classificação | Classificacao |
| Código Auxiliar | CodAuxiliar |
| Coleção | Colecao |
| Data de registro | DataReg |
| Edição | Edicao |
| Editora | Editora |
| Função do autor | FuncaoAutor |
| Geral | Geral |
| Grupo de Publicação | GrupoPublic |
| Informações | Informacoes |
| ISBN (Livro) | ISBN |
| ISSN (Periódico) | ISSN |
| Local da publicação | LocalPublic |
| Localização | Localizacao |
| Mês | Mes |
| Notações | Notacoes |
| Número do Tombo | NumTombo |
| Palavra Chave | PalavraChave |
| Série | Serie |
| Subclassificação | SubClassific |
| Subtítulo | Subtitulo |
| Sumário | Sumario |
| Título equivalente | TituloEquivalente |
| Título Original | TituloOriginal |
| Título Principal | TituloPrincipal |
| Título Uniforme | TituloUniforme |

**Utilização do WebService**

**Pesquisa ao acervo**

Para realizar uma buscar por um determinado termo deve ser utilizado a operação de ReadView, esta operação deve ter como filtro o campo que será pesquisado e o termo da pesquisa, separados por **";" (ponto e vírgula)** .

Exemplo: realizar busca pelo **título principal** que contenha o nome **Teste Pesquisa**, assim o filtro do método **ReadView** deve ser "**TituloPrincipal;Teste Pesquisa**".

ObservaçãoSe o filtro não estiver no formato correto, com um campo para pesquisa que exista na lista acima e um termo a ser pesquisado o sistema não retorná registros. 

### Exemplo do retorno da chamada da pesquisa

**Detalhar um exemplar da pesquisa**

É possível detalhar uma publicação utilizando o método **ReadRecord**após realizar a operação de **ReadView**, assim como na atual tela de pesquisa do *TOTVS Gestão Bibliotecária*, o sistema retorna uma lista de publicações (ReadView) e permite selecionar uma publicação para o detalhamento (ReadRecord).

O método **ReadRecord** para este dataserver **BibConsultaAcervoDataWS** obriga o preenchimento de seis (6) campos que existem na operação de pesquisa (ReadView) para compor a chave primária do registro, são eles:

* CODCOLIGADA (Código da coligada)
* CODPUBLIC (Código da publicação)
* CODVOLUME (Código do volume)
* EDICAO (Edição)
* ANO (Ano)
* NPAGINAS (Número de páginas)

Observações

Somente os campos código da coligada e da publicação sempre retornarão valores, os demais podem ser nulos, assim deve ser passado o valor -1 no respectivo campo da chave.

#### Exemplo de utilização:

Com base no retorno do **ReadView** deverá ser feita a chamada do método **ReadRecord,** este método terá como filtro os campos:

* **CODCOLIGADA;CODPUBLIC;CODVOLUME;EDICAO;ANO;NPAGINAS**

O código da coligada (CODCOLIGADA) e da publicação (CODPUBLIC) são obrigatórios na chave primária do método (PrimaryKey), os demais podem ser nulos, mas caso de fato sejam nulos, deve ser passado o valor **"-1'** pois sempre devem existir valores na composição**.**

No exemplo abaixo é possível identificar que para a publicação em questão foi utilizado os seguintes itens para a chave primária:

* CODCOLIGADA = 1
* CODPUBLIC = 2990
* CODVOLUME = -1 (retornado nulo pelo ReadView)
* EDICAO = -1 (retornado nulo pelo ReadView)
* ANO = 2017
* NPAGINAS = -1 (retornado nulo pelo ReadView)

**Retorno do webservice à chamada do ReadRecord**

Conforme descrito, no ReadRecord é carregado o detalhamento da publicação, assim o retorno contará com todas as tabelas retornadas pelo ReadView e também as específicas do ReadRecord que são as de exemplares (exemplares, fascículos e artigos), áreas de conhecimento e sumário. 

Os dados da ficha catalográfica não são carregados pelo ReadRecord pois estes dados são montados em tempo de execução diretamente na tela.
