---
content_hash: 906e064cc17ddc3f135e63e38d849f6767ae186808f9de9889525eed8a68665f
fetched_at: '2026-07-02T19:24:27.615731+00:00'
page_id: '658744519'
product: protheus
source: tdn-tec
title: a - Arquitetura de diretórios do projeto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=658744519
version: 3
---

Aconselhamos a utilização de um "versionador" de código, tal como o GIT.

Após criar um projeto novo em seu GIT remoto, faça o clone para criar seu diretório principal do projeto, na qual terão todos os arquivos fontes do seu projeto.

Caso não queria utilizar uma ferramenta de versionamento, apenas crie o diretório.

Exemplo:

```

```

Agora que temos nosso diretório principal do projeto, vamos começar a criar a estrutura na qual iremos trabalhar.

Vamos agora a criação de mais 2 (dois) diretórios, importante citar que serão subdiretórios a partir do principal do projeto, e eles serão base para distinguir dois tipos de fontes, são eles:

### Fontes Oficiais Projeto >> /src/

Os fontes abaixo desse diretório contém o desenvolvimento de funções e classes com as funcionalidades, regras, telas, api´s, etc.. que seu projeto necessita.

Esses fontes são os que estarão no RPO de produção de seu ambiente final.

Ficando então:

```

```

### Testes >> /test/

Os fontes abaixo desse diretório contém as implementações com os testes unitários, funcionais, integrados das funcionalidades desenvolvidas no diretório descrito acima.

Essas classes/funções não precisam ficar no RPO final de produção, na verdade, em boas práticas é bom que NÃO sejam expedidos ao RPO de produção, pois seu uso só é essencial ao ambiente e RPO que serão executados os testes.

Ficando então:

```

```

#### Módulos / Funcionalidades

Abaixo desses diretórios novos, todos os subdiretórios criados serão associados à funcionalidade a ser desenvolvida e todo diretório novo em /src/ precisa ter seu correspondente criado na estrutura em /test/.

Embora não seja uma exigência técnica que ambos diretórios tenham o mesmo nome, utilizamos esse padrão por 2 (dois) bons motivos:

* Boas práticas de desenvolvimento;
* Facilidade de manutenção

Com essa organização de diretórios, facilitamos o entendimento e manutenção das funcionalidades principais ao agrupar os fontes com as mesmas finalidades, como também, facilita a encontrar todos os fontes dos testes para essa funcionalidade.

Exemplo:  
Imagine que temos alguns fontes com manipulação de datas em nosso projeto, portanto, é importante agrupá-los em um mesmo local, nesse caso poderemos utilizar o nome /date/.

Logo, todos os testes desenvolvidos para cobrir todas as funcionalidades de data colocaremos também em /date/.

Como temos duas estruturas de diretórios, uma para a implementação da funcionalidade e outra para os testes, devemos então ter /date/ nos dois locais, ou seja, /src/ e /test/.

Em nosso exemplo acima, a estrutura final fica:
