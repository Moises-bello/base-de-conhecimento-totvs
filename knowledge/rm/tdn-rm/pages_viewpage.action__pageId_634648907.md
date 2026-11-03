---
content_hash: 783db725885fa11d1053a4486c3246a1f5265d882948fe8bebdde498170af45a
fetched_at: '2026-06-29T00:11:06.423927+00:00'
page_id: '634648907'
product: rm
source: tdn-rm
title: TOTVS Processos Fiscais (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=634648907
version: 20
---

|  |  |
| --- | --- |
| **Produto** | TOTVS Gestão Fiscal / TOTVS Gestão de Estoque, Compras e Faturamento |
| **Processo** | TOTVS Processos Fiscais (TPF) |

## **Conteúdo**

Conteúdo

## **01. Visão Geral**

Na integração do RM com o TOTVS Processos Fiscais (TPF) é utilizado o aplicativo Fiscal Sync que envia os arquivos XML para a plataforma Gestão Fiscal e consulta os documentos fiscais no Fisco para retornar ao RM.

Nesta integração o ERP RM envia os arquivos XML para a pasta de Saída (OUT) do Fiscal Sync, que processa e retorna o XML com a resposta na pasta de Entrada (IN).

Mais informações sobre o Fiscal Sync: <https://tdn.totvs.com/x/WYu4IQ>

## **02.****Pré Requisitos**

Para realizar o envio do arquivo XML é necessário que no Properties do Fiscal Sync esteja configurado com os diretórios de entrada, saída, processado e impressão ([Manual de Instalação - Fiscal Sync](https://tdn.totvs.com/pages/viewpage.action?pageId=570993088)):

         - Diretório de Entrada: Arquivos de retorno que a plataforma Gestão Fiscal recebeu do Fisco. Para o RM a pasta precisa ter o nome de IN.

         - Diretório de Saída:  Arquivos que o ERP envia para a plataforma Gestão Fiscal. Para o RM a pasta precisa ter o nome de OUT.

         - Diretório de Processado: Arquivos que a aplicação realiza a leitura do diretório de saída para enviar há plataforma de Gestão Fiscal e move para o diretório processado. 

         - Diretório de Impressão: Caso utilize o Servidor de Impressão Local (SIL), são os arquivos do fluxo 170 que são enviados para ser impresso no SIL. Se não utilizar o SIL apenas deixe o diretório em branco.

    Exemplo de configuração para o correto funcionamento da integração.

  É obrigatório que a pasta de Entrada possua o nome de IN e a pasta de saída possua o nome de OUT. E ambas precisam estar na mesma pasta de origem, conforme exemplo acima.

## **03. Documentos Disponíveis para Emissão**

Os documentos disponíveis para utilizar na integração atualmente são:

* NF-e
* NFC-e
* NFS-e (é necessário avaliar se o município esta disponível no TPF)

## **04. Parametrização RM**

01Parametrização por Coligada (Passo 1)

**Caminho:** BackOffice | Gestão de Estoque, Compras e Faturamento | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Importação/Envio de Arquivo XML.

Tipo Integração: TOTVS Processos Fiscais

Diretório Padrão para Importação dos Arquivos XML: Caminho das pastas parametrizadas na instalação do Fiscal Sync onde possuí a pasta IN e OUT dentro do diretório. É indicado a utilização de caminho de rede do servidor onde foi instalado o Fiscal Sync. Exemplo do caminho das pastas no passo 02 - Pré Requisitos.

2Parametrização por Filial (Passo 2)

**Caminho:**BackOffice | Gestão de Estoque, Compras e Faturamento | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | Importação/Envio de Arquivo XML.

Tipo de Documento Integração TOTVS Colaboração: Informar o tipo de documento utilizado. Os tipos de documentos disponíveis para serem utilizados nesta integração estão listados no passo 03 - Documentos Disponíveis.

Informações

Para a integração do RM com o TPF não é necessário informar os demais campos desta tela, somente o "Tipo de Documento Integração TOTVS Colaboração".

3Fracionamento (Passo 3)

**Caminho:**BackOffice | Gestão de Estoque, Compras e Faturamento | Ambiente | Segurança de Jobs Fracionáveis

Deverá ser feito um cadastro para cada um dos processos por perfil de usuário.

Processos e suas respectivas classes:

| Processo | Classe |
| --- | --- |
| Envio | FisNFSeEnvioData |
| Consulta | FisTotvsColabConsultaData |
| Importação | MovTOTVSColabImportacaoArquivosProc |

Esse cadastro é importante para garantir a execução performática das rotinas distribuindo a execução em vários processos, se o cadastro não for feito a execução é feita até que seja atingido o limite de cada processo, sendo necessário executar o processo várias vezes para processar todos os registros.

Limites de registros por execução para cada processo:

| Processo | Limite de Registros |
| --- | --- |
| Envio | 1000 |
| Consulta | 900 |
| Importação | 900 |

Para mais informações consulte a

## **05. Envio de Documentos**

0Nota Fiscal Eletrônica (NF-e)Informações

É necessário que o RM esteja parametrizado para o Envio de NFe.

Os processos de envio são realizados igual as demais integrações (TSS e TOTVS Colaboração).

Envio de NF-e

O processo pode ser executado pelo Gestão de Estoque, Compras e Faturamento menu Faturamento | SPED (Estadual) em "Processos | Enviar" ou pela tela de movimento, em "Processos | Enviar NF-e/NFC-e".

Documento do processo: 

Envio de Eventos

Os eventos são enviados pelo Gestão de Estoque, Compras e Faturamento menu Faturamento | SPED (Estadual) em Processos | Envio de Eventos.

Documento do processo: 

Inutilização de Numeração

A Inutilização de Numeração é enviada pelo Gestão de Estoque, Compras e Faturamento menu Faturamento | SPED (Estadual) em Processos | Inutilizar.

Documento do processo: 

Nota Fiscal Eletrônica de Serviços (NFS-e)Informações

É necessário que o RM esteja parametrizado para o Envio de NFS-e.

Os processos de envio são realizados igual às demais integrações (TSS e TOTVS Colaboração).

Envio de NFS-e

O processo de envio de notas pode ser executado pelo Gestão de Estoque, Compras e Faturamento menu Faturamento | Movimentação em "Processos | Enviar NFS-e".

Documento do processo:

Consulta de Notas

A consulta de notas pode ser feita importando o XML retornado do envio da nota em Integrações | Monitor de Arquivos | Processos | Importação de arquivos XML e, após importados os arquivos da nota, em Processos | Serviço de Consulta de Arquivos XML.  
Após esse processo, caso não houver nenhuma inconsistência na nota, seu status deve ficar como "Autorizada". Caso contrário, ficará como "Rejeitada" ou "Inconsistente".  
Para ver a causa da rejeição ou inconsistência, acesse a NFS-e | Anexos | Histórico da NFS-e.  
  
Mais informações sobre status da nota: [Status da NFS-e](https://tdn.totvs.com/display/public/LRM/Status+da+NFS-e)

Cancelamento de Notas

Para cancelar uma nota, ela deve ter sido enviada e consultada anteriormente. Acesse o cancelamento selecionando o movimento | Anexos | NFS-e (Notas Fiscais Eletrônicas Municipais) | Processos | Cancelar NFS-e.  
Após executar este processo, o status da nota mudará para "Cancelamento Pendente". Então siga os passos da consulta de notas novamente: vá em Integrações | Monitor de Arquivos | Processos | Importação de arquivos XML e, após importados os arquivos da nota, em Processos | Serviço de Consulta de Arquivos XML. Ao verificar o status da nota após esse processo, seu status será "Cancelado"

Documento do processo:

## **06. Retorno de Documentos (Consulta de Autorização)**

O retorno de documentos é realizado através do Gestão de Estoque, Compras e Faturamento em Integrações | Monitor de Arquivos. É possível realizar o agendamento dos Jobs para que os retornos ocorram automaticamente ou executá-los manualmente.

Existem dois Jobs a serem executados para que os arquivos .xml enviados pela TPF sejam importados.

0Importação de Arquivos XML

Esse processo é responsável por buscar os documentos .xml disponíveis na pasta de Entrada (IN) e distribuí-los por Coligada. Neste momento, nenhuma validação é feita. Após a execução desse processo, os documentos lidos são exibidos no ‘Monitor de Arquivos’ com o status ‘Pendente’, aguardando a ação do segundo processo. No Monitor de Arquivos será exibido apenas os documentos destinados à Coligada do usuário logado. Para executar esse processo, deve-se acessar “Processos | Importação de Arquivos XML”.

Serviço de Consulta de Arquivos XML

Esse processo é responsável por validar o arquivo .xml, de acordo com o tipo de documento em questão, através da chamada do serviço especifico para cada um deles. Serão verificados todos os documentos lidos pelo 1º Processo. Caso o documento esteja válido, o registro do arquivo é excluído do monitor, e atualiza o documento correspondente, indicando se ele foi autorizado ou rejeitado por exemplo.

Caso seja encontrado algum problema no arquivo importado, o status do registro é alterado para ‘Inconsistente’. Para verificar o erro, basta um duplo clique no registro para exibição do Log.

Quando o arquivo está Inconsistente, é necessário corrigir a causa do erro para tentar incluí-lo no sistema. Neste caso o seu status pode ser alterado manualmente para ‘Pendente’ através do processo “Alterar Status do Arquivo”.

Agendamento

Conforme citado, os dois Jobs podem ser executados imediatamente, ou agendados para funcionarem periodicamente. Para que não seja necessário uma constante intervenção manual do usuário, é indicado que o agendamento seja realizado.

Documento sobre agendamento de Job: [Link do documento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005088792-RM-Frame-Como-agendar-a-execu%C3%A7%C3%A3o-de-um-processo-)

Caso não esteja utilizando ambiente três camadas, é possível utilizar um servidor para simular o ambiente três camadas e executar os jobs. [Link do documento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006679772-RM-Frame-Configura%C3%A7%C3%A3o-para-simular-3-camadas)

## **07.****Rejeições e****Inconsistências**

Para verificar se o documento foi autorizado com sucesso ou se ocorreu alguma mensagem de rejeição ou inconsistência, é necessário verificar no registro original após a consulta do arquivo de retorno automático ou manual (Passo 06).

0Nota Fiscal Eletrônica (NF-e)

Para verificar se uma NF-e ou um evento de NF-e foi autorizado, rejeitado ou apresentou alguma inconsistência é necessário acessar o registro pelo Gestão de Estoque, Compras e Faturamento menu Faturamento | SPED (Estadual).

O registro da NF-e e/ou evento é alterado automaticamente após a consulta do arquivo conforme citado no passo 06 - Retorno de Documentos.

Caso tenha ocorrido rejeição ou inconsistência a mensagem pode ser verificada no Histórico da NF-e ou do evento, selecionando o registro e acessando Anexos | Histórico.

Inutilização

Para verificar se uma Inutilização foi autorizada ou rejeitada é necessário acessar o registro pelo Gestão de Estoque, Compras e Faturamento menu Cadastros | (Fiscais) Filial.

Deve-se selecionar a filial que foi enviado a inutilização e acessar Anexos | NF-e/NFC-e Inutilizadas.

Caso tenha ocorrido rejeição a mensagem pode ser verificada editando o registro de inutilização, no campo Mensagem de Retorno da SEFAZ.

## **08. Documentos de Entrada (Recebimento de xml)**

Documentos de Entrada:
