---
content_hash: dc2a580f0bef0bd9194d6f5447df46289acad50d51aa5b7395f266c5b4d72e92
fetched_at: '2026-07-02T19:24:27.927335+00:00'
page_id: '697259079'
product: protheus
source: tdn-tec
title: Application Server - 19.3.2.1
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+19.3.2.1
version: 9
---

# Correções

Error.log ao acessar a Rotina de Cadastro de Clientes no SIGALOJA com Banco de Dados SQLite

Ocorrência: Uso da função TCGenQry2() para SQLITE com RDD TOPCONN (RPODB=SQLITE) finalizava a aplicação com erro "TCGenQry2 is not supported in SQLITE".

Solução: Funcionalidade da TCGenQry2 implementada também para SQLITE.

Chamado: DTAPPSRV-6069

Tela fica em branco ao efetuar o logoff utilizando a nova interface

Ocorrência: Ao utilizar o Protheus configurado com a nova interface de acesso baseada em PO UI e após solicitar o encerramento do ERP clicando no botão "Log Off...", uma tela totalmente em branco é exibida ao invés dos campos para a realização de um novo login.

Solução: Foi aplicado um ajuste para que o ciclo de vida do TWebChannel esteja atrelado ao da janela principal do sistema e não mais ao ciclo de vida da última janela criada. Para evitar consumo desnecessário de recursos, quando o objeto TWebChannel não for mais necessário, recomendamos que ele seja finalizado com TWebChannel:disconnect() e FreeObj().

Chamado: DTAPPSRV-6014

Ao executar o método TMailMessage:SaveAttach Could not create attachment file

Ocorrência: O método SaveAttach da classe TMailMessage só estava salvando os arquivos em disco após fechar a thread atual, gerando arquivos com tamanho 0 (zero) até o fechamento da thread.

Solução: Corrigido o fechamento dos arquivos realizado pelo método SaveAttach da classe TMailMessage.

Referente ao chamado: DTAPPSRV-5916

TMailMessage:Clear não limpa o último campo que foi definido

Ocorrência: O método Clear da TMailMessage não limpa o último campo definido no objeto.

Solução: Corrigido a limpeza feita pelo método Clear da TMailMessage.

.

Referente ao chamado: DTAPPSRV-5981

Access Violation na função tSslClient

Ocorrência: Ao tentar utilizar o método Send da classe ADVPL tSSLClient com a seção SSLConfigure ausente no appserver.ini, ocorre access violation no appserver.

Solução: Realizada uma correção no Application Server para proteger o uso do método Send.

Referente ao chamado: DTAPPSRV-6092

Função directory gerando access violation ao receber o atributo "V"

Ocorrência: Ao tentar utilizar a função directory passando como parâmetro o atributo "V" ocorria um access violation no APPServer.

Solução: foi realizada uma correção no APPServer para não ocorrer access violation nessa situação.

Referente ao chamado: DTAPPSRV-6208

Erro na função FwMsExcelXlsx em ambiente Linux

Ocorrência: Ao utilizar a função File2Printer para verificar a versão do executável da printer via AppServer Linux, o executável não é encontrado pela chamada do SO.

Solução: Isto acontecia pois o comando enviado para o SO não continha o prefixo de execução "./", corrigi a chamada dentro da File2Printer e o problema não acontece mais.

Referente ao chamado: DTAPPSRV-6082

# Melhorias

Suportar paths com espaço em branco para fontes e includes no preprocessador e AppServer Command Line

Ocorrência: A compilação e pre-compilação no Advpl via Command Line não trata adequadamente paths com espaços.

Solução: Implementado suporte a paths com espaço em branco para includes e arquivos na compilação via Command Line.

Referente ao chamado: DTAPPSRV-6051

Nova função para comparação da versão do TOTVS Application Server no formato NN.N.N.nnn como string.

Ocorrência: Necessidade de comparar o número da versão do TOTVS Application Server no formato NN.N.N.nnn como String, resolvendo problemas relacionados a comportamentos do tipo String ( por exemplo situações como "19.3.1.10" é MENOR que "19.3.1.9").

Solução: Criada a função **CmpBuildStr**,  para permitir a comparação entre duas strings no formato Build Version, considerando os valores numéricos.

Documentação:

Referente ao chamado: DTAPPSRV-6226
