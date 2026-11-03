---
content_hash: 857fd3560477075bff7de2a603401ab57e979e423454191eb5ff13908856415d
fetched_at: '2026-06-29T00:06:16.230618+00:00'
page_id: '212893889'
product: rm
source: tdn-rm
title: SAU0057_Resultados_de_Exames_na_Internet
type: documentation
url: https://tdn.totvs.com/display/LRM/SAU0057_Resultados_de_Exames_na_Internet
version: 5
---

# Resultados de Exames na Web

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Hospitalar |
| **Versões:** | A partir da 11.82 |
| **Ocorrência:** | disponibilizar os resultados de exames na internet por meio de consulta ao número do pedido e de uma senha. |
| **Passo a passo:** | Configuração de Parâmetros necessária:  Em **Opções/Parâmetros/Parâmetros Gerais, página Unidade Diagnóstico II, grupo Resultados de exames online.** Configure os parâmetros a seguir:   "Disponibiliza resultados online?", este parâmetro indica se os resultados de exames serão disponibilizados na internet.  "Diretório dos arquivos de resultados online", este parâmetro indica em qual pasta do servidor, os resultados serão armazenados. Informe um caminho de rede para que o sistema grave num único local.    Em **Opções/Parâmetros/Parâmetros Gerais, página Unidade Diagnóstico.** Configure os parâmetros a seguir:  "Relatório de impressão do Resultado de exame Laboratorial", este parâmetro indica qual relatório do novo gerador será utilizado para impressão dos resultados de exames laboratoriais.  "Relatório de impressão do Resultado de exame de imagem", este parâmetro indica qual relatório do novo gerador será utilizado para impressão dos resultados de exames de imagem.    Processo de Utilização:   1. Acesse os **Parâmetros gerais**, página **Unidade Diagnóstico II** e preencha os parâmetros em destaque. 2. Na página **Unidade Diagnóstico**, preencha os relatórios que serão utilizados. 3. Faça o pedido de exames normalmente, marcando o checkbox **Resultados online.** Com esta opção marcada, uma senha é gerada. 4. Ao liberar o exame, um arquivo pdf com o resultado do exame é salvo na pasta indicada no parâmetro. 5. Acesse o endereço para a consulta do resultado. 6. Clique no ícone destacado para salvar o resultado do exame.       Instalação do TOTVS Business Connect:  Para utilizar a funcionalidade de resultados online, será necessário instalar o TOTVS Business Connect. É ele que irá prover os serviços utilizados.  O diretório default é C:\Totvs\CorporeRM\WS\_TBC  Após a instalação, é necessário fazer algumas configurações:   * Adicionar o arquivo **wsResultadosOnline.asmx** na pasta base do TOTVS Business Connect * Copiar as dlls abaixo que ficam na pasta **C:\Totvs\CorporeRM\RM.Net** para a pasta **bin** do TOTVS Business Connect (C:\Totvs\CorporeRM\WS\_TBC\bin)  * RM.Sau.Interfaces.Intf.dll * RM.Sau.Mobile.Intf.dll * RM.Sau.Mobile.Services.dll * RM.Sau.Parametros.Intf.dll * RM.Sau.RegistroAtendimento.Intf.dll * RM.Sau.UnidadeDiagnostico.Intf.dll * RM.Sau.Utils.Intf.dll * RM.Sau.WebService.dll  * Conferir o arquivo web.config (C:\Totvs\CorporeRM\WS\_TBC). A chave DBAlias deve ser o mesmo utilizada pela aplicação. É com este alias que ele irá conectar no banco.     Outro detalhe é que no arquivo web.config que está na pasta WS\_TBC, deve-se remover as linhas:  <authorization>  <deny users="?"/>  </authorization>    Publicação do site Resultados online:   * Descompacte o zip dentro da pasta Totvs.  * Acesse o IIS e selecione e clique na opção Default Web site. Com o botão direito, selecione a opção Adicionar Aplicativo.  * Informe o campo Alias com o nome que aparecerá no browser. * Informe o caminho da pasta ResultadosOnline que contém os arquivos do site.      * No arquivo web.config, altere os campos destacados.   + A coligada da base utilizada e um usuário e senha válidos no sistema. Utilizado apenas para executar os serviços.   + A chave wsResultadoOnline deve conter o endereço em que o TOTVS Business Connect foi instalado.   + A chavev pathTmpFile, contem o endereço no servidor em que os resultados dos exames serão baixados. Este endereço deve ser diferente os endereço informado nos parâmetro gerais.      * Para acessar o painel acesso o navegado e digite <http://localhost/nomeInformadoNoAlias>. |

divs
