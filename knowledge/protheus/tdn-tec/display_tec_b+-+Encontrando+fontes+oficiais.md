---
content_hash: ca29cfebf46e2b6d93623485ef5cf6c7fc60e105eb34205d834a97ab50e47f24
fetched_at: '2026-07-02T19:24:27.621532+00:00'
page_id: '658744523'
product: protheus
source: tdn-tec
title: b - Encontrando fontes oficiais
type: documentation
url: https://tdn.totvs.com/display/tec/b+-+Encontrando+fontes+oficiais
version: 3
---

Para algumas funcionalidades é importante que o **PROBAT** tenha conhecimento sobre quais são os fontes oficiais do seu projeto.

Hoje o **PROBAT** possui 2 modos de encontrar os fontes, sendo:

* Hierarquia de diretórios;
* Annotation.

### Hierarquia de diretórios

Caso você tenha seguido a recomendação anterior em (Arquitetura de diretórios do projeto) e todos os seus fontes oficiais estejam abaixo de /src/, recomendamos utilizar o modo [Hierarquia de diretórios], pois ele é o mais simples e eficaz, uma vez que ele irá encontrar todos os arquivos-fontes que existem fisicamente abaixo do diretório raiz.

Para isso, em seu INI informe:

```
Sendo:
```

* {SOURCE\_DISCOVERY\_MODE=0} Informa que o **PROBAT** fará as buscas dos arquivos por hierarquia de diretórios.
* {SOURCE\_PATH=C:/my\_project/src/} Diretório raiz onde possui todos os arquivos-fontes oficiais e subdiretórios do projeto.

### Annotation

Caso você tenha os fontes distribuídos de forma organizada diferente da descrita em [Hierarquia de diretórios] e o processo de refatorar a localização dos arquivos seja muito custoso, então o **PROBAT** possui um modo de encontrá-los através do uso de annotation.

Primeiro é preciso configurar o funcionamento para esse modo, sendo assim, informe conforme abaixo em sua INI:

```

```

Depois, em cada fonte oficial e em qualquer função ou classe presentes no fonte utilizar a annotation [DiscoverySrc].

Exemplo:

c#

```

```

Através da propriedade [folder] você irá informar qual o diretório na qual esse fonte está localizado.

Portanto através da reflection o **PROBAT** irá buscar todos os fontes que utilizam [DiscoverySrc] e assumirá como fontes oficiais do seu projeto.

Importante ressaltar que esse modo possui algumas limitações, vejamos:

* Só funcionará com fontes .tlpp, pois Annotation e Reflection é um recurso exclusivo do TLPP.
* Logo, fontes em ADVPL não serão encontrados por esse modo;
* É preciso refatorar todos os seus fontes oficiais para a inserção do @DiscoverySrc().
* Seu projeto precisa ser recompilado para que o recurso funcione.

### Tabela SQLite

Ao descobrir os arquivos fontes oficiais, o **PROBAT** irá gravar os dados na seguinte tabela do SQLite.

Nome Tabela: **PROBAT\_CONFIG\_SOURCES**

| Campo | Tipo Dado | Descrição |
| --- | --- | --- |
| CODE | N | Código do fonte oficial (uso interno) |
| FOLDER | C | Folder de localização do fonte |
| SOURCE | C | Nome do arquivo fonte |
| NAMESPACE | C | Namespace usada no fonte |
