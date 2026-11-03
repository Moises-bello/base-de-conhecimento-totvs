---
content_hash: b3da4f360f2fe86842ceb1092cd84591ce1c4978edab67d2c65594445f18af89
fetched_at: '2026-06-29T00:11:03.600321+00:00'
page_id: '624610986'
product: rm
source: tdn-rm
title: Portal de Imóveis - Montagem de Ambiente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=624610986
version: 11
---

Guia para montagem do ambiente de desenvolvimento#FF9000Checklist de Instalação

Checklist de Instalação

1. Resgatar os fontes do TFS.
2. Fazer instalação de todas [dependências de compilação](https://pvi-totvs.gitbook.io/pvi/monte-seu-ambiente-pvi#dependencias-para-compilacao).
3. Acessar o diretório dos fontes do Portal de Imóveis recuperados do TFS para sua máquina.
4. Executar o comando yarn
5. Incluir o arquivo de licença compartilhado em ./src/api
6. Acessar ./src/api e duplicar os arquivos config\_ambiente.php.new, config\_db.php.new, config\_php.php.new.
7. Dos arquivos duplicados no passo anterior, renomear às cópias removendo a extensão .new, por exemplo, "config\_db.php.new copia" para config\_db.php.
8. Rodar o comando de compilação "gulp watch" no diretório raiz.
9. Apontar o IIS para ler os fontes compilados para servir no endereço: <http://localhost:8000>
#FF9000Local dos Fontes no TFS

Para compilação do Portal de Imóveis é necessário primeiramente fazer cópia dos fontes no TFS. Para fins didáticos, usaremos como base apenas a versão "Atual" no TFS da TOTVS ($/RM/Atual/Release/FrameHTML/web\_src/app/Imb/Portal de Imóveis).

#FF9000Dependências para compilação

Todas dependências abaixo precisam ser instaladas uma única vez no sistema operacional.

* Ativar o IIS
* ​[Instalação extensão URL Rewrite](https://www.iis.net/downloads/microsoft/url-rewrite)​
* ​[Instalação extensão PHP Manager 1.5](https://www.iis.net/downloads/community/2018/05/php-manager-150-for-iis-10) ​
* ​[Node JS v10 ³](https://nodejs.org/pt-br/download/releases/)
* ​[Yarn](https://classic.yarnpkg.com/latest.msi)​
* ​[Bower](https://bower.io/#install-bower) (*npm install -g bower*)
* ​[Gulp](https://gulpjs.com/docs/en/getting-started/quick-start)  (*npm install --global gulp-cli*)
* ​[PHP (baixe o PHP customizado para o Portal de Imóveis) ¹](https://www.dropbox.com/sh/dn64vpafhtr84jl/AABWIsLNwrhxgvTMjMwsUHxIa?dl=1) ​
* ​[Composer](https://getcomposer.org/download/)​
* ​[Git ²](https://git-scm.com/downloads)​
* ​[Conversor PDF](https://www.dropbox.com/s/jr3i0g0huk24uz3/Protos-Conversor-PDF.exe?dl=1)​
* ​[Conversor Word](https://www.dropbox.com/s/fo3ip8ed51pb3iu/Protos-Conversor-Word.exe?dl=1)​
* ​[Microsoft ODBC Driver 17 for SQL Server](https://www.microsoft.com/pt-br/download/details.aspx?id=56567)​

1. Por uma questão de padronização do local de instalação do PHP, é sugerido extrair o download do PHP em C:\Protos\PHP. Caso faça opção por instalar em diretório diferente do indicado, será necessário editar o arquivo php.ini e alterar o endereço de extensões fixadas com diretório "C:\protos\php\ext\" para seu diretório de instalação.
2. Mesmo a TOTVS não usando Git para controle de versão Portal de Imóveis é necessário ter o Git para que gerenciador de dependências frontend do Portal de Imóveis possa baixar fontes do Git. Futuramente estaremos remover essa dependência, por enquanto será necessário ter o git.
3. Node precisar ser versão 10. Caso o desenvolvedor precise ter mais de uma versão do node instalada pode ser usado [nvm](https://github.com/coreybutler/nvm-windows/releases).
#FF9000Dependências do Portal

Depois de instalado todas dependências para compilação é necessário fazer instalação de dependencias do próprio Portal de Imóveis.

Dependências do Portal de Imóveis pode ser entendido como bibliotecas de terceiros como AngularJS, Bootstrap, APIs do Google Maps e etc.

Vamos partir do ponto que os fontes do Portal de Imóveis foram resgatados do TFS de $/RM/Atual/Release/FrameHTML/web\_src/app/Imb/Portal de Imóveis e mapeados para C:\RM\Atual\Release\FrameHTML\web\_src\app\Imb\Portal de Imóveis, então acesse diretório pelo *prompt* de comando e rode os comandos abaixo:

Midnight#FF9000Conceitos Importantes Pré Compilação

Em ambiente de desenvolvimento será usado apenas o comando usando o gerenciador de tarefas (gulp), esse comando irá gerar os fontes compilados em um subdiretório chamado **/build**, dentro deste subdiretório base do Portal de Imóveis. Esse comando também ficará verificando se houve alguma modificação nos fontes em **/src**,caso haja, os fontes serão compilados automaticamente e movidos para build, desse forma, você como desenvolvedor não precisa ficar rodando os comando de build o tempo todo nem fica clicando em botões de build.

#FF9000Arquivos de Configurações

Por padrão, o fonte já vem com alguns arquivo de configuração como exemplo e através destes arquivos de exemplo temos liberdade de ajustar configurações para se adequar às necessidade de cada instalação. Os arquivos de configurações estão localizados no subdiretório: ***${your-path}/src/api*** são:

* config\_ambiente.php.new
* config\_db.php.new
* config\_php.php.new

Para montagem manual dos ambientes, os arquivos listados acima precisam ser duplicados. Dos arquivos duplicados, ele precisam ser renomeados para seus respectivos nomes, porém sem a extensão .new. Por exemplo:

Você duplica (copia e colar) o arquivo **config\_ambiente.php.new,** no arquivo duplicado é que deve ser o arquivo renomeado para **config\_ambiente.php**

Repita esse mesmo processo para todos os outros arquivos.

Não renomeie diretamente os arquivos config\_ambiente.php.new, config\_db.php.new e config\_php.php.new, primeiro é necessário fazer uma cópia e renomer SOMENTE às cópias.

Todos os arquivos abordados aqui são são arquivos de configuração de ambientes, bancos de dados e parametrizações da linguagem PHP.

Veja um exemplo do arquivo de configuração de banco de dados (**/src/api/config\_db.php**):

Midnight [
'Portal de Imóveis' => [
'dsn' => 'sqlsrv:server=%s; database=%s',
'server' => 'seu-host',
'user' => 'sa',
'pass' => 'sua-senha',
'database' => 'sua-base-Portal de Imóveis',
'port' => '',
'charset' => 'utf8',
'collation' => 'SQL\_Latin1\_General\_CP1\_CI\_AS',
'logs' => false,
'debug' => false, // altere para true para salvar as consultas na pasta /log
'cache' => true,
],
],
'homologacao' => [
'Portal de Imóveis' => [
'dsn' => 'sqlsrv:server=%s; database=%s',
'server' => '',
'user' => '',
'pass' => '',
'database' => '',
'port' => '',
'charset' => '',
'collation' => '',
'logs' => false,
'debug' => false,
'cache' => true,
],
],
];]]>#FF9000Licença de uso compartilhada

Devido o controle de licenças, em desenvolvimento necessariamente precisar ser criado no domínio localhost:8000. O arquivo de licença é compartilhado entre todos participantes do time que queiram usar Portal de Imóveis. Para isso, precisa ser baixado por este [**link**](https://drive.google.com/file/d/12sn7tEy1okziyc9tfeZSH53tMYDkZ10T/view?usp=sharing) e colocado na sua instalação no diretório /src/api.

#FF9000Compilando

Para compilação, no diretório base do Portal de Imóveis rode o comando:

Midnight

Caso queira, o comando acima pode ser substituído por uma .bat, dessa forma, basta dar duplo em **build.watch.bat.** Ambas alternativas chegam ao mesmo resultado.

#FF9000Criando Site no IIS

O site precisa ser criado no IIS, para isso basta clicar com lado direito do mouse e adicionar novo site. Feito isso, precisa acessar o site criado, procurar pelo PHP Manager e registrar a versão do PHP instalada nos passos anteriores.

#FF9000Configurações Finais

Agora será necessário no IIS informar onde estão os fontes compilados do Portal de Imóveis, para isso acesse a home do site no IIS e siga os procedimentos da imagem.

#FF9000Alternativas ao IIS

Enquanto em ambiente de desenvolvimento, existe a possibilidade de não se preocupar com IIS e usar o servidor de testes embutido no PHP. Para isso, é necessário que o PHP esteja no PATH das variáveis de ambiente do sistema operacional.

Feito isso, basta que no diretório base dos fontes do Portal de Imóveis seja rodado o seguinte comando:

Midnight

Certifique que a porta 8000 não esteja sendo usada.

Caso o IIS esteja usando a porta 8000, você pode parar o site pelo IIS ou abrir o prompt de comando como administrador e executar o comando:

Midnight
