---
content_hash: 6543fd50bcb477e55023b7bb682faf99a6416ba8a2834ed61fb38f4370c9d847
fetched_at: '2026-06-29T00:12:03.308200+00:00'
page_id: '906825138'
product: rm
source: tdn-rm
title: Processo Sped Multicoligada
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+Sped+Multicoligada
version: 8
---

# **01.****Visão Geral**

O SPED Multicoligada tem como objetivo a digitalização simultânea dos livros contábeis de uma ou mais coligadas.

# **02.****Execução do Processo**

**2.1. Seleção de Escriturações**

Através da tela de cadastro, o usuário poderá selecionar uma ou mais escriturações contábeis das coligadas às quais tem acesso. A quantidade de seleção determinará o número de arquivos gerados, sendo um para cada escrituração informada.

**2.2. Abertura do Processo**

Após a seleção das escriturações, o usuário inicia o processo de SPED Multicoligada, que apresentará uma visão com os dados das opções escolhidas, incluindo:

* Status;
* Código Coligada;
* Código Escrituração;
* Número Ordem;
* Forma da Escrituração;
* Descrição;
* Data Inicial;
* Data Final;

Nesta visão o usuário devera verificar os tipos de escrituração e informar caso necessário os arquivos adicionais esperados, ao selecionar uma escrituração, o campo Status indicara se a mesma precisa importar arquivo(s), uma grid abaixo apresentara, separadamente quais tipos de arquivos são esperados e possibilitara a importação do mesmo.

Status

O campo Status apresentara 3 tipos.

**- Sucesso**: Todos os arquivos adicionais necessários foram informados.

* Indica que esta tudo correto e sua escrituração esta preparada para executar.

**- Facultativo**: Caso existam documentos J800 para essa escrituração, inclua-os no grid à direita.

* Indica que no caso do J800, enquanto houver arquivos para enviar é possível envia-los. Nesse caso não há limite de envio.

**- Obrigatório**:  É obrigatório informar o arquivo **J801 ou Razão Auxiliar** para essa escrituração, inclua-os no grid à direita.

* Indica que sua escrituração não pode ser executada, a mesma não tem todos os arquivos necessários e não esta completa para executar.

Para anexar arquivos à escrituração, selecione a linha correspondente, clique em 'Incluir' no grid à direita e, na tela exibida, escolha o tipo de arquivo permitido para anexaçã

Clique aqui para exibir a inserção de arquivos complementares

# **03.****Download dos arquivos**

Após a execução das escriturações selecionadas será exibida uma visão com os dados das escriturações e o arquivo gerado para cada uma delas. A visão exibirá as seguintes informações:

* Código Coligada;
* Código Escrituração;
* Data Inicial;
* Data Final;
* Nome do Arquivo, que foi gerado;
* Tamanho do Arquivo, que foi gerado;
* Botão de Download;

Vale destacar que estarão disponíveis duas opções de download:

1. Um botão que permitirá o download de todos os arquivos listados na visão de escriturações contábeis.
2. Um botão em cada linha da visão, contendo as escriturações contábeis selecionadas, que permitirá o download exclusivo do arquivo correspondente a cada escrituração.
