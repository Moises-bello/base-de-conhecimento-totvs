---
content_hash: 3d3e2ff50d7ae4b71c4e9475becdd62efa9aebd7c54175f7e19da236a78271ce
fetched_at: '2026-06-29T00:08:50.796014+00:00'
page_id: '334338597'
product: rm
source: tdn-rm
title: 05 - Personalizando cores
type: documentation
url: https://tdn.totvs.com/display/LRM/05+-+Personalizando+cores
version: 9
---

Informação

É possível personalizar as cores do TOTVS Educa Mobile através de uma ferramenta livre, descrita nessa seção.

Acesso o link [http://themeroller.jquerymobile.com](http://themeroller.jquerymobile.com/) e na primeira tela, caso seja necessário clique em "Get Rolling":

A seguir clique sobre a opção "Import", localizada no canto superior direito da tela para importar o arquivo de configurações padrão (.css) do TOTVS Educa Mobile e fazer as alterações que desejar:

Abra a pasta de instalação do TOTVS Educa Mobile, localize o diretório "Content/themes/totvs" e dentro desse diretório o arquivo "jquery.mobile.totvs.theme.css". Abra esse arquivo em um editor de textos de sua preferência, copie todo conteúdo e cole no espaço indicado "Import Theme" que foi aberto no item anterior e finalmente clique em "Import":

O estilo padrão será carregado e a personalização poderá ser realizada da forma que desejar. Para personalização dos tipos de fontes, podemos utilizar o menu disponível no lado esquerdo. Para a personalização das cores, podemos utilizar esse mesmo menu, ou arrastar as cores para as áreas correspondentes.

Informação

Para configuração das cores dos itens de menu do TOTVS Educa Mobile deve ser utilizada a propriedade "Linked list item" do tema listado na "coluna B" conforme imagens a seguir:

Após o término da personalização, é necessário fazer o download do arquivo. Para isso, clique no botão "Download" localizado na barra superior do site, preencha o campo "Theme Name" com o nome para o novo tema criado e em seguida clique em "Download Zip". Será gerado um arquivo com extensão ".zip" que você pode salvar no diretório que desejar.

Acesse a pasta de instalação do TOTVS Educa Mobile e localize o diretório "Content/themes", copie e cole a pasta "totvs" para que seja duplicada e então coloque um nome à sua escolha.

Dentro da pasta que acabou de ser criada, apague os arquivos com extensão ".css".

Localize o arquivo ".zip" que foi salvo anteriormente e que contem o novo tema criado, descompacte os arquivos ".css" e copie-os para a nova pasta criada no item anterior.

Edite o arquivo "Web.config.xml" que está dentro da pasta de instalação do TOTVS Educa Mobile, no diretório raiz e altere o valor da chave "Theme" para a nova pasta que foi criada. No caso dos exemplos que estão sendo utilizados nessa documentação, chamamos a pasta de "novo\_tema", portanto, a configuração ficará conforme a imagem a seguir:
