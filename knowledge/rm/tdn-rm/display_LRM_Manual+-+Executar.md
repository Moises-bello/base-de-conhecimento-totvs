---
content_hash: 8de89592d80623f9b671d70fddcca4141b91f6ee2c7452fd066db74911214e0b
fetched_at: '2026-06-29T00:08:47.197298+00:00'
page_id: '319787261'
product: rm
source: tdn-rm
title: Manual - Executar
type: documentation
url: https://tdn.totvs.com/display/LRM/Manual+-+Executar
version: 3
---

Utilize essa opção para executar um Layout usando o utilitário de linha de comando "TNF.Gen.Exec". Este utilitário deve ser executado utilizando o executor do .NET Core (dotnet exec TNF.Gen.Exec.dll). Utilize esta janela para verificar como devem ser passados os parâmetros de linha de comando para execução do Layout. Lembrando que este utilitário pode ser executado em várias plataformas além do Windows, como o sistemas Linux e MacOS.

*\* Esta opção não está disponível no Gerador RM, onde deve ser utilizado o processo de execução de Layouts do Gerador.*

![](/download/attachments/319787261/executar.png?version=1&modificationDate=1512921808000&api=v2)

1Layout

Exibe o nome do arquivo de Layout que será executado.

2Diretório de Destino

Informe o caminho onde os arquivos gerados na execução serão gravados. Caso o Layout contenha um diretório padrão definido, esta opção não precisa ser informada.

3Conexão

Selecione a conexão com o banco de dados que será utilizada para execução do Layout. Caso a conexão não seja informada, a conexão do Layout será utilizada para geração. Para mais informações consulte a [Configuração da Conexão](/pages/viewpage.action?pageId=319787266).

4Parâmetros do Layout

Informe os parâmetros de execução do Layout. Os parâmetros são definidos no Contexto de Parâmetros e todos os parâmetros obrigatórios devem ser informados para execução. Para mais informações consulte o [Contexto de Parâmetros da Geração](/pages/viewpage.action?pageId=319787298).

5Executar

Clique para exibir a linha de comando que será executada e executar.

6Fechar

Clique para fechar a janela de execução.

#### Exemplo

C:\Program Files\dotnet\dotnet.exe  exec "TNF.Gen.Exec.dll" "C:\Temp\TNF.CliFor.layout" "C:\Temp" -CT="TNF.Data.SqlDataAccess, TNF.Data" -CS="Data Source=.;Initial Catalog=RM12;User ID=rm;Password=rm" Coligada="1" CliFor="1"

|  |  |
| --- | --- |
| C:\Program Files\dotnet\dotnet.exe | Caminho do executável dotnet.exe que é instalado juntamento com o runtime do .NET Core. |
| exec "TNF.Gen.Exec.dll" | Informa que deve executar o utilitário de linha de comando "TNF.Gen.Exec.dll" disponível na pasta netcoreapp2 do diretório de instalação do gerador de saídas. |
| "C:\Temp\TNF.CliFor.layout" | Caminho do Layout do gerador de saídas que será executado. |
| "C:\Temp" | Caminho onde os arquivos gerados serão gravados. Caso o diretório padrão do Layout tenha sido informado esta opção poderá ficar vazia "". |
| -CT="TNF.Data.SqlDataAccess, TNF.Data" | Define o tipo de conexão com o banco de dados que será utilizada para execução do Layout. Este parâmetro é opcional. |
| -CS="Data Source=.;Initial Catalog=RM12;User ID=rm;Password=rm" | Define o string de conexão com o banco de dados que será utilizado para execução do Layout. Este parâmetro é opcional. |
| Coligada="1" CliFor="1" | Informe os parâmetros do Contexto de Parâmetros do Layout. Todos os parâmetros obrigatórios devem ser informados utilizado o formato NOME="VALOR". |

Informação

Para executar é necessária a instalação do runtime do .NET Core 2. Você pode baixa-lo diretamente da página da Microsoft de acordo com o sistema operacional em que ele será executado.

Para mais informações acesse: <https://www.microsoft.com/net/download/core#/runtime>.
