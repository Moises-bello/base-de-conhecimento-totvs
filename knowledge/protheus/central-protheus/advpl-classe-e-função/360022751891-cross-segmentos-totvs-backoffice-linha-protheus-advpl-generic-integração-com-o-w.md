---
article_id: 360022751891
category: ADVPL - Classe e Função
content_hash: 4eff4c167e774b9adace7f295320bc98d83562556475ddb49c457c63cc55ebf6
fetched_at: '2026-06-28T22:40:19.520474+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Generic integração
  com o word e copias de arquivos
type: support-article
updated_at: '2024-01-03T18:03:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022751891-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Generic-integra%C3%A7%C3%A3o-com-o-word-e-copias-de-arquivos
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**A documentação do TDN não esta legível sobre as funções de integração Office: [GENERIC - INTEGRACAO COM O WORD E COPIAS DE ARQUIV](http://tdn.totvs.com/display/public/mp/GENERIC+-+INTEGRACAO+COM+O+WORD+E+COPIAS+DE+ARQUIV)  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Solução**Segue conteúdo formatado:   
O Word só abre/cria Documentos em um local físico, isto e, tem que ter acesso ao diretório/drive, não pode ser via Server do *Protheus*, do Client o *Word* não abre diretamente no Server a não ser que esteja mapeado e o Client esteja com acesso de gravação.  
Para que o Client possa visualizar/atualizar algum documento devera ser copiado do Server para o Client os arquivos necessários para a realização das tarefas e de acordo com a necessidade/objetivo poderá ser retornado para Server através das funções CPYS2T() E CPYT2S(). Em alguns casos onde sera feita apenas a leitura poderá ser utilizado o *WordViewer* mencionado em outro item do Banco de Conhecimento.  
É aconselhável que as versões do Office instaladas nas maquinas *Client* e *Server* serem iguais para evitar problemas futuros, como por exemplo, a criação de um documento no Officer2000 e a leitura feita por um *Client* que tenha o Officer 97. Outro ponto importante e que a instalação do Windows e Office devera ser feita do zero (formatar HD), não instalar versões de upgrade, experiencia obtida em vários clientes.  
Exemplo de copia do Server para o Client:  
  
**CPYS2T**("\DOCS\EXEMPLO.DOC","C:\WINDOWS\TEMP",.T.)  
1o. Parâmetro e o nome do arquivo a ser copiado para o Client  
2o. Parâmetro e o diretório do Client e/ou local físico onde sera copiado o arquivo.  
3o. Parâmetro se deseja compactar o arquivo (recomendável).  
  
**CPYT2S**("C:\WINDOWS\TEMP","\DOCS\EXEMPLO.DOC",.T.)  
Exemplo de copia do Client para o Server:  
1o. Parâmetro e o nome do arquivo a ser copiado para o Server  
2o. Parâmetro e o diretório do Server  
3o. Parâmetro se deseja compactar o arquivo (recomendável).  
  
**Observação:** Os Arquivos que poderão ser copiados deverão estar necessariamente embaixo do *RootPath*, isto e, o diretório DOCS do exemplo acima devera ser subdiretório do diretório colocado no *RootPath*, apenas um exemplo existe outras maneiras de direcionar o diretório.   
  
Funções do Word:  
oWord:=OLE\_CreateLink("TMSOLEWORD97")  
-Função que abre o Link com o Word tendo como parâmetro a versão (Office 95 ou Office 97)  
  
OLE\_SetProperty(oWord, OLEWDVISIBLE, .T. )  
OLE\_SetProperty(oWord, OLEWDPRINTBACK,.T. )  
-Função que faz o Word aparecer na Área de Transferência do Windows, sendo que para habilitar/desabilitar e só colocar .T. ou .F.  
  
OLE\_SetProperty(oWord,OLEWDLEFT ,000)  
OLE\_SetProperty(oWord,OLEWDTOP ,090)  
OLE\_SetProperty(oWord,OLEWDWIDTH ,480)  
OLE\_SetProperty(oWord,OLEWDHEIGHT,250)  
-Funções que configuram o tamanho da janela do Word  
  
OLE\_OPENFILE(oWord,"C:\WINDOWS\TEMP\EXEMPLO.DOC",lReadOnly,"SENHAXXX","SENHAWWW")  
-Função de abertura do Documento com os parâmetros lReadOnly (Somente Leitura), com SENHAXXX (senha de abertura do Documento) e com SENHAWWW (senha de gravação).  
  
OLE\_NewFile(oWord,"C:\WINDOWS\TEMP\EXEMPLO.DOT")  
-Função para criar um Documento com Modelo(DOT) especificado no parâmetro.  
  
OLE\_SaveAsFile(oWord,"C:\WINDOWS\TEMP\EXEMPLO1.DOC","SENHAXXX","SENHAWWW",.F.)  
-Função que salva o Documento com o nome especificado, com senha e no formato Word.  
  
OLE\_SaveFile(oWord)  
-Função salva o Documento corrente.  
  
OLE\_SetDocumentVar(oWord,"Adv\_NomeFilial", "Microsiga Software S/A")  
-Função que atualiza as variáveis do Word, conforme exemplo ira atualizar a variável "AdvNomeFilial" com o conteúdo "Microsiga Software S/A". O RdMake GPEWORD poderá servir de exemplo para atualização de variáveis.  
  
OLE\_Updatefields(oWord)  
-Função que atualiza os campos da memoria para o Documento, utilizada logo apos a função OLE\_SetDocumentVar().  
  
OLE\_PrintFile(oWord,"ALL",nPagInicial,nPagFinal,nCopias)  
-Função que imprime o Documento corrente podendo ser especificado o numero de copias, podendo também imprimir com um intervalo especificado nos parâmetros "nPagInicial" ate "nPagFinal" retirando o parâmetro "ALL".  
  
OLE\_CloseFile(oWord)  
-Função que fecha o Documento sem fechar o Link com o Word, utilizado para manipulação de dois ou mais arquivos (recomendado fechar todos os arquivos antes de fechar o Link com Word)  
  
OLE\_CloseLink(oWord)  
-Função que fecha o Link com o Word.
