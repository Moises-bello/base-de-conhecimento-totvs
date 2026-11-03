---
content_hash: b8bea53baa1231312ae7453760fcbb98f3e53aa0f1af65e89adcfaaf0f106425
fetched_at: '2026-06-29T00:09:02.477603+00:00'
page_id: '379313947'
product: rm
source: tdn-rm
title: 'Guia de atualização do ambiente substituindo o RPO:'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379313947
version: 11
---

Os procedimentos abaixo devem ser realizados para atualização do pacote do eSocial expedido no dia 12/09/2018, para os produtos TAF e TSS.

Obtendo os arquivos de atualização via Portal do Cliente TOTVS (clique para expandir)

# Atualização de Produto

Acessar a página de Downloads e Atualizações, e **selecionar a linha de produto e-SOCIAL**:

Link: <https://suporte.totvs.com/portal/p/10098/download>

1. Selecionar a opção correspondente ao DATASUL / RM, e baixar o pacote do release desejado.

Observação: Aos clientes da linha RM, faça o download do arquivo: 18-09-12-ATUALIZACAO\_TAF\_ESOCIAL\_REINF\_RM\_DATASUL\_PORTUGUES.ZIP.

2. Existem três opções de idioma, escolha a que deseja utilizar, abaixo temos o exemplo da versão em Português:

Estes arquivos abaixo contém toda a atualização necessária de TAF e TSS para entrega do eSocial, a diferença deles é o idioma, trata-se de um conjunto único de atualização. Conteúdo:

- Descompactar o pacote selecionado e utilizar no passo a passo de atualização

ATENÇÃO!

Avaliar se o Filtro está para apresentar "**Todos Pacotes Disponíveis**", e utilizar o ultimo pacote de atualização disponível.

Passo a passo de atualização (clique para expandir)Atualização do TAF (clique para expandir)

Pare o serviço do TAF-WS nos serviços do Windows.

Caso o serviço não seja parado automaticamente, apresentando a mensagem abaixo, realize o seguinte procedimento antes de prosseguir:

Procedimento para parar o serviço através do DOS:

Acesse o “Gerenciador de tarefas do Windows” > aba “Serviços” e localize o código PID do mesmo.

No prompt de comando do DOS (cmd) digite: taskkill /pid XXXX /f

Onde XXXX é o PID do serviço) e tecle “Enter”. Neste momento o serviço será interrompido.

Realizado o procedimento de parada do serviço, voltamos para a atualização do sistema.

Atualização do repositório de objetos (clique para expandir)

Substituir o arquivo tttp120.rpo na pasta \apo\ do diretório de instalação do sistema

Importante!

Faça um backup do arquivo antes de substituí-lo!

Atualização do dicionário de dados e do menu (clique para expandir)

a) Copiar os arquivos sdfbra.txt e sx2.unq para a pasta \systemload\ do diretório de instalação do sistema.

b) Copiar o arquivo sigataf.xnu para a pasta \system\ do diretório de instalação do sistema.

c) Executar o compatibilizar de dicionário de dados (UPDDISTR)

Será solicitado a seleção dos Grupos de Empresa que devem ser atualizados:

• Nas telas iniciais serão exibidas as informações de ambiente e o propósito do compatibilizador, selecione o botão “Avançar”:

• Após o processamento do compatibilizador o dicionário do TAF estará atualizado:

• Para verificar se houve alguma inconsistência durante a atualização do dicionário de dados, clique em "Consulta LOG":

• Então clique em "Filtrar" e selecione o campo "Tipo do evento" como "Critical Error".

• Caso o filtro retorne algum evento de "Critical Error", significa que foram encontrados problema na base de dados e nenhuma atualização foi efetivada no ambiente. Neste caso o UPDDISTR não tem autonomia para corrigir e os ajustes devem ser realizados pelo Administrador do Sistema.

 • Para maiores detalhes de utilização da ferramenta UPDDISTR acesse [Atualizador de dicionário e base de dados - UPDDISTR](http://tdn.totvs.com/pages/viewpage.action?pageId=181965468).

Nova execução

Neste momento, ao concluir a execução desta atualização, deve ser avaliado a necessidade de nova execução do UPDTAF, conforme informado no início do tópico I**I****I****. Atualizar o Dicionário de Dados ( UPDTAF )**

**Segunda etapa de atualização de dicionário de dados**

• Após finalizar a execução dos pacotes atualizados pelo UPDDISTR, deve-se executar novamente o UPDTAF para realizar demais ajustes de ambiente:

• Quando a varredura do sistema identificar que não há necessidade de execução do UPDDISTR, será apresentada uma lista de ajustes que devem ser realizados no ambiente, conforme demonstrado abaixo:

• Selecione as atualizações, por release, que devem ser realizadas.

Status

A coluna 'Status' informa quais atualizações ainda são necessárias. Caso todas estejam com o Status "Executado", este procedimento pode ser ignorado.

• Após realizar a seleção, clique em 'Processar' e aguarde o término da execução.

• No final do processamento serão apresentadas os ajustes realizados no ambiente, conforme demonstrado abaixo:

Atualização do TSS (clique para expandir)

Atualização do repositório de objetos

Substituir o arquivo tttp120.rpo na pasta \apo\ no diretório de instalação do TSS

Arquivo do pacote

Arquivo do sistema à ser substituído.

Importante!

Faça um backup do arquivo antes de substituí-lo!

Atualização dos arquivos de schema:

Atualização dos arquivos de URL:  /
