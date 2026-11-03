---
content_hash: c9d42aa08d40ddd51c627546f2a5144189036ea2fcdd8863e7b948fd7bc40fe4
fetched_at: '2026-06-28T21:35:23.637695+00:00'
page_id: '257623442'
product: fluig
source: tdn-fluig
title: Servidor de indexação único
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=257623442
version: 45
---

Atenção

Esta página foi revisada para considerar as novas configurações de *server* do Fluig para a atualização 1.6.

# Índice

4true.\*ndicenone

Importante!

Antes de prosseguir com as instruções descritas nessa página, realize os passos contidos na documentação .

# Introdução

---

As instruções a seguir completarão a instalação de um Servidor de indexação em um único servidor dedicado, continuando as instruções iniciadas em .

# Configurando o Fluig para usar o Servidor de indexação

---

No servidor onde está instalado o Fluig, acesse o diretório [Instalação fluig]/repository/wcmdir/config e edite o arquivo [configuration.properties](http://tdn.totvs.com/pages/viewpage.action?pageId=257623022). Caso o arquivo configuration.properties não exista, crie um novo arquivo com este nome.

Se o Indexer possuir acesso ao [repositório](http://tdn.totvs.com/pages/viewpage.action?pageId=233766796) do Fluig, adicione/edite a seguinte linha, informando o endereço do servidor de indexação onde o Fluig Indexer foi instalado:

1true:8983/solr]]>

Isto fará com que os dados do Indexer sejam salvos no [repositório](http://tdn.totvs.com/pages/viewpage.action?pageId=233766796).

Ou se o Indexer **não** possuir acesso ao [repositório](http://tdn.totvs.com/pages/viewpage.action?pageId=233766796) do Fluig, adicione/edite as seguintes linhas:

xml1true/solr
totvs/solrURL=http://:8983/solr
totvs/solrRemote=true
totvs/solrCloud=false]]>

Isto fará com que o Fluig envie os documentos para extração e indexação neste servidor. Lembramos apenas que sem acesso ao repositório, este processo é mais lento do que o acesso direto via repositório. Os dados do Indexer serão salvos no servidor do Indexer.

Observação

Caso o parâmetro *solrRemote* seja alterado após a criação de empresa, os dados do Indexer continuarão sendo salvos conforme sua configuração inicial, sendo a alteração válida apenas para novas empresas. A reinicialização do servidor de aplicação pode ser necessária.

# Executando o serviço Fluig Indexer

---

* Basta executar o arquivo [Instalação do fluig Indexer]/solr/startStandalone.sh ou [Instalação do fluig Indexer]/solr/startStandalone.bat que o processo será inicializado.

* Para interromper o serviço de indexação, execute o arquivo [Instalação do fluig Indexer]/solr/stopStandalone.sh ou [Instalação do fluig Indexer]/solr/stopStandalone.bat.

Observação

É importante que o Fluig Indexer seja iniciado antes do Fluig, caso contrário este irá considerar que não há serviço de Indexação disponível.

# Registrando o Fluig Indexer como serviço no Windows/Linux

---

Para registrar o Fluig Indexer como serviço, utilize os  padrão do sistema operacional em questão.
