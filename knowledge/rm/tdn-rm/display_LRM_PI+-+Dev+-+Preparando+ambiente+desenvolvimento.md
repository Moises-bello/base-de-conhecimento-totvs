---
content_hash: ad3f6d8f8084c092b7ac7d2b89ec092c03fdae9abe6ffbf1b3e420b6fe5cd011
fetched_at: '2026-06-29T00:11:21.263326+00:00'
page_id: '691443893'
product: rm
source: tdn-rm
title: PI - Dev - Preparando ambiente desenvolvimento
type: documentation
url: https://tdn.totvs.com/display/LRM/PI+-+Dev+-+Preparando+ambiente+desenvolvimento
version: 37
---

Este documento tem o objetivo de orientar como preparar e subir o Portal de Imóveis.

* ### **Para Debugar**

Executar todos os comandos no cmd como administrador.

IMPORTANTE

 Os Arquivos do PHP customizado, Word, Pdf e outros instaladores uteis ja se encontram no caminho:            
<https://drive.google.com/drive/u/0/folders/1DnFsCZd-WiHsgPv-RLP17kBpjX0qxhWV>

1 - Siga todos os passos descritos no link: .  
       
**Atenção:** a partir da versão 12.1.2402 o PVI teve o php atualizado para a versão 7.3.24 para atender ao oracle, então o build funciona somente quando este estiver sendo referenciado no iis.

Paginas Revitalizadas PI

Rodar o restore configurado para dar get nos arquivos do portal gestão de imoveis, onde se econtra os novos fontes de frontend em po-ui ou smartui que fazem parte da modernização do PI. crie na pasta bin do RM um diretorio com o nome "wwwroot" e no restore configure "Portais" para dar get nos fontes direto para o wwwroot da bin.

2 - A partir da versão 12.1.2205 a versão do Node utilizado é 14.15.5, para o controle de versão do Node é indicado a utilização do NVM for Windows.  
3 - Para debugar é indicado utilizar o VSCode. Abra o folder "C:\RM\Atual\Release\FrameHTML\**web\_src**\app\Imb\PVI".  
4 - Para controle de fontes pelo VSCode com vinculo ao TFS, instale a extension TFS com a logo laranjada. Em seguida, vá em File >> Preferences >> Settings, pesquise por "tfs" e no campo "Tfs: Location" informe o caminho do executavel do TFS instalado na máquina que será utilizada para alteração dos fontes.   
5 - As novas paginas (Componentes PO-UI ou SmartView) estão sendo criadas no repositorio do git "portalgestaoimoveis" e tem paginas que são chamada como iframe e paginas que são chamadas dentro de compilação que fica dentro de folder especifico dentro do proprio PVI compilado no pipeline.

Erro gulp watch

**Ao rodar o gulp watch para compilar os fontes do PI ocorre o erro abaixo.  
Erro:** LIBERTY LIBERTY LIBERTY  
com um loop infinito que pode até travar o cmd.  
Caso isso ocorrá podemos verificar se foi criado pelo yarn o download de codigo malicioso de loop infinito, isso poderá ser verificado em:  
citação do erro: <https://commons.wikimedia.org/wiki/File:Faker.js_zalgo_LIBERTY.svg>  
  
imagem do erro:

**SOLUÇÃO:**                    Apagar no caminho 'C:\RM\Atual\Release\FrameHTML\web\_src\app\Imb\pvi\node\_modules\colors\lib' no arquivo "index.js" o trecho de codigo  e salvar o arquivo.  
  
                  Dentro do folder "C:\RM\Atual\Release\FrameHTML\web\_src\app\Imb\pvi\node\_modules\colors\lib\custom" apagar o arquivo "american.js".

Yarn erro - bower

ao rodar o yarn erro para bower youtuber e outros. rodar o comando "yarn install" no cmd dentro do folder pvi com cmd em admin

Yarn erro - bower

Versão 14 do node para resolver, se não estiver com as dependências anteriores (yarn, bower) instaladas como global, favor instalar global.

*Seguir comandos de* dependências *de compilação em montagem de ambiente.*

Gulp erro - citação Laravel OCI

Atenção para erro de oracle circulado:

Verificar nas variáveis de ambiente se a pasta do oracle está sendo referenciada.  
para referenciar deverá criar em: 

Dentro do path citar a variável criada:

Dependencias Compilação - Variaveis Path

Verfificar se as variáveis das depencias de compilação foram adicionadas corretamente no path da maquina e do usuário.  
Variáveis do sistema:

Variáveis do usuario:

comman failed bower install

erro ocorrendo porque não está conseguindo sair do cmd para usar o gitbash mesmo com as variaveis de ambiente do git setada no windows,  
solução: tentar abrir no vscode o terminal git bash e rodar os comandos por ele  
ou  
tentar bower install novamente como admin do cmd

Erro git clone

erro ocorre por falta de permissão ao utilizar user e pass do git para login, atualize em "Painel de Controle\Contas de Usuário\Gerenciador de Credenciais" as credenciais do github com o login do seu usuário no git.

Login PI mestre

user: [mestre@totvs.com.br](mailto:mestre@totvs.com.br)  
pass: config\_ambiente.php - possui a senha master do PI - "p0rt@l"

Importante!

* Altere o arquivo 'main.js'  
  -  na função ngOnInit()  
  - atribua os valores diretamente as variaveis que estão sendo aguardadas serem entregues pela requisição:  
       - apiServerPortal = caminho do PVI até a porta (Ex.: <http://localhost:8000)>  
       - apiTokenPortal = token que pode ser encontrado via solicitação da API do RM (Ex.: <http://192.168.18.31:8051/api/connect/token>)  
       - idComissao = chave primaria da comissao que já se encontra cadastrada no banco de dados.

* Caso deseje poderá utilizar no browser do debug a url abaixo subistituindo as variáveis necessárias dos parametros da url.  
  - <http://localhost:4200/comissao-proposta?comissaoBackoffice=1&wsBasepvi=http:%2F%2Flocalhost:2209&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZW1haWwiOiJtZXN0cmVAdG90dnMuY29tLmJyIn0.zGSckaO_aA9QwML5MvZHOD0ncz2KPp4q0lxgMumXLf0>

Arquivo doc com alguns erros que devemos trazer para a pagina:  
<https://docs.google.com/document/d/1dNgWdx9tVkvzZUAom4bWBRoaei3NXhMi/edit>
