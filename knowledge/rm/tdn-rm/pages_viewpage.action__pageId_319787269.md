---
content_hash: da22f8b8079382f079e551785671dc13383c4d7f293c6737f0258158f4b5719b
fetched_at: '2026-06-29T00:08:47.222341+00:00'
page_id: '319787269'
product: rm
source: tdn-rm
title: Manual - Configuração do Arquivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=319787269
version: 4
---

As configurações do arquivo definem as propriedades específicas de cada arquivo que será gerado. Um Layout deve conter pelo menos um arquivo para ser gerado. Entre as suas configurações destaca-se o tipo de arquivo, tipo de codificação e outras propriedades.

1Nome

Informe o nome identificador do arquivo. O nome do arquivo deve ser único para o Layout e é utilizado para definição do nome do arquivo gerado, concatenando a ela a data e hora da geração mais a extensão do arquivo.

2Descrição

Informe um texto descritivo para o arquivo. Este texto será utilizado para geração do arquivo de documentação do Layout.

3Tipo do Arquivo

Selecione o tipo de arquivo que será gerado. Os tipos disponíveis são:

##### Arquivo Texto

Esta é a opção padrão do tipo de arquivo, será utilizado para a maioria dos arquivos gerados.

##### Arquivo Texto (TAF)

Esta opção está disponível somente para o RM e é utilizado internamente para gerar arquivos no padrão do TAF (TOTVS Apuração Fiscal).

4Codificação do Arquivo

Selecione o tipo de codificação de texto que será utilizada para geração do arquivo. Existem vários tipos de codificação disponíveis entre as mais utilizadas estão o padrão ASCII, UTF-8 e Windows-1252.

Para mais informações consulte: <https://pt.wikipedia.org/wiki/Arquivo_de_texto>

5Propriedades

Informe aqui as propriedades específicas para geração do arquivo. As propriedades disponíveis estão detalhadas abaixo.

|  |  |
| --- | --- |
| Extensão do arquivo | Informa qual é a extensão padrão para o tipo de arquivo selecionado. |
| Gerar nome de arquivo dinâmicamente | Indica se o nome do arquivo gerado deve ser definido dinâmicamente, utilize esta opção para alterar o nome do arquivo a ser gerado de acordo com uma expressão do gerador. Ao alterar esta opção para True, uma aba nome do arquivo será exibida para que seja configurada a expressão do nome do arquivo. Para mais informações consulte [Nome do Arquivo](http://tdn.totvs.com/display/LRM/Manual+-+Nome+do+Arquivo). |
| Incluir linha em branco no fim do arquivo | Indica se o gerador deverá incluir automáticamente um linha em branco no final do arquivo. Alguns arquivos de intercambio precisam dessa linha em branco para que o arquivo seja considerado válido. |
| Nome | Informa o nome do tipo de arquivo somente para informação. |
| Separador de campos | Informe qual caractere deverá ser utilizado como separador de campos do arquivo, ao informar este caractere, o gerador irá inclui-lo automáticamente para separar os valores de cada campo do registro. |
| Separador final de linha | Informe qual caractere deverá ser utilizado como separador de final de linha do arquivo. Alguns arquivos de intercambio necessitam deste caractere no final da linha para que o registro seja válido. |
| Separador inicial de linha | Informe qual caractere deverá ser utilizado como separador de inicial de linha do arquivo. Alguns arquivos de intercambio necessitam deste caractere no início da linha para que o registro seja válido. Geralmente os arquivos que tem um separador inicial tem também um separador final de linha igual. |
| Sobrescrever o arquivo no diretório padrão | Indica se o gerador deve sobrescrever o arquivo de de mesmo nome gerado no diretório padrão. |
| Suprimir linhas em branco | Indica se o gerador deve incluir no arquivo gerado as linhas cujos campos não contenham nenhuma informação válida. |
| Utilizar a data atual para compor o nome do arquivo | Indica se o gerador deverá concatenar a data e hora atual no nome do arquivo gerado. Esta opção é ignorada quando o nome do arquivo é gerado dinâmicamente por uma expressão. |
