---
content_hash: b2d66df3a4f1abb4ff178223ed2699c5697f135ce8a5ab23760159fcab101494
fetched_at: '2026-06-29T00:11:43.471756+00:00'
page_id: '807213977'
product: rm
source: tdn-rm
title: Montagem de Ambiente
type: documentation
url: https://tdn.totvs.com/display/LRM/Montagem+de+Ambiente
version: 12
---

Guia para montagem do ambiente de desenvolvimento

**CheckList de Instalação**

1. Resgatar os fontes do TFS.

2. Fazer instalação de todas [dependências de compilação](https://pvi-totvs.gitbook.io/pvi/monte-seu-ambiente-pvi#dependencias-para-compilacao).

3. Acessar o diretório dos fontes do PVI recuperados do TFS para sua máquina.

4. Executar o comando yarn

5. Incluir o arquivo de licença compartilhado em ./src/api

6. Acessar ./src/api e duplicar os arquivos config\_ambiente.php.new, config\_db.php.new, config\_php.php.new.

7. Dos arquivos duplicados no passo anterior, renomear às cópias removendo a extensão .new, por exemplo, "config\_db.php.new copia" para config\_db.php.

8. Rodar o comando de compilação "gulp watch" no diretório raiz.

9. Apontar o IIS para ler os fontes compilados para servir no endereço: <http://localhost:8000>

**Local dos Fontes no TFS**

Para compilação do PVI é necessário primeiramente fazer cópia dos fontes no TFS. Para fins didáticos, usaremos como base apenas a versão "Atual" no TFS da TOTVS ($/RM/Atual/Release/FrameHTML/web\_src/app/Imb/PVI).

**Dependências para compilação**

Todas dependências abaixo precisam ser instaladas uma única vez no sistema operacional.

* Ativar o IIS (ativar ou desativar recursos do windows - habilitar todo o Serviço de Informação da Internet)
* [Instalação extensão URL Rewrite](https://www.iis.net/downloads/microsoft/url-rewrite) (disponivel no google drive)
* [Instalação extensão PHP Manager 1.5](https://www.iis.net/downloads/community/2018/05/php-manager-150-for-iis-10) (disponivel no google drive ou doc oficial do instalador --> )
* NVM (disponivel no google drive)
* Node JS v14 (nvm install 14) (PHP8 - pelo menos 14.21.3)
* [Bower](https://bower.io/#install-bower) (*npm install -g bower*)
* [Yarn](https://classic.yarnpkg.com/latest.msi) (disponivel no google drive)
* [Gulp](https://gulpjs.com/docs/en/getting-started/quick-start)  (*npm install --global gulp-cli*)
* [PHP (baixe o PHP customizado para o PVI) ¹](https://www.dropbox.com/sh/dn64vpafhtr84jl/AABWIsLNwrhxgvTMjMwsUHxIa?dl=1) - (verificar na pasta ext e no php.ini se está citando as dlls php\_oci.dll )
* [Composer](https://getcomposer.org/download/) (disponivel no google drive - Composer version 2.8.5 ou anterior)
* [Git ²](https://git-scm.com/downloads) (disponivel no google drive)
* [Conversor PDF](https://www.dropbox.com/s/ufm7p190hby8p8s/Protos-Conversor-PDF.zip?dl=1) (disponivel no google drive)
* [Conversor Word](https://www.dropbox.com/s/tycebpd7gc44uer/Protos-Conversor-Word.zip?dl=1) (disponivel no google drive)
* [Microsoft ODBC Driver 17 for SQL Server](https://www.microsoft.com/pt-br/download/details.aspx?id=56567)

1. Por uma questão de padronização do local de instalação do PHP, é sugerido extrair o download do PHP em C:\Protos\PHP. Caso faça opção por instalar em diretório diferente do indicado, será necessário editar o arquivo php.ini e alterar o endereço de extensões fixadas com diretório "C:\protos\php\ext\" para seu diretório de instalação.
2. Mesmo a TOTVS não usando Git para controle de versão PVI é necessário ter o Git para que gerenciador de dependências frontend do PVI possa baixar fontes do Git. Futuramente estaremos remover essa dependência, por enquanto será necessário ter o git.
3. Node precisar ser versão 10 (a partir da versão 2310 usamos node 14). Caso o desenvolvedor precise ter mais de uma versão do node instalada pode ser usado [nvm](https://github.com/coreybutler/nvm-windows/releases).

**Dependências do Portal**

Depois de instalado todas dependências para compilação é necessário fazer instalação de dependencias do próprio PVI.  
Dependências do PVI pode ser entendido como bibliotecas de terceiros como AngularJS, Bootstrap, APIs do Google Maps e etc.   
Vamos partir do ponto que os fontes do PVI foram resgatados do TFS de $/RM/Atual/Release/FrameHTML/web\_src/app/Imb/PVI e mapeados para C:\RM\Atual\Release\FrameHTML\web\_src\app\Imb\PVI, então acesse diretório pelo *prompt* de comando e rode os comandos abaixo:

*cd C:\RM\Atual\Release\FrameHTML\web\_src\app\Imb\PVI*

*yarn*

**Conceitos Importantes Pré Compilação**

Em ambiente de desenvolvimento será usado apenas o comando usando o gerenciador de tarefas (gulp), esse comando irá gerar os fontes compilados em um subdiretório chamado **/build**, dentro deste subdiretório base do PVI. Esse comando também ficará verificando se houve alguma modificação nos fontes em **/src**,caso haja, os fontes serão compilados automaticamente e movidos para build, desse forma, você como desenvolvedor não precisa ficar rodando os comando de build o tempo todo nem fica clicando em botões de build.

**Arquivos de Configurações**

Por padrão, o fonte já vem com alguns arquivo de configuração como exemplo e através destes arquivos de exemplo temos liberdade de ajustar configurações para se adequar às necessidade de cada instalação. Os arquivos de configurações estão localizados no subdiretório: ***${your-path}/src/api*** são:

* + config\_ambiente.php.new
  + config\_db.php.new
  + config\_php.php.new

Para montagem manual dos ambientes, os arquivos listados acima precisam ser duplicados. Dos arquivos duplicados, ele precisam ser renomeados para seus respectivos nomes, porém sem a extensão .new. Por exemplo:  
Você duplica (copia e colar) o arquivo **config\_ambiente.php.new,** no arquivo duplicado é que deve ser o arquivo renomeado para **config\_ambiente.php**  
Repita esse mesmo processo para todos os outros arquivos.

Não renomeie diretamente os arquivos config\_ambiente.php.new, config\_db.php.new e config\_php.php.new, primeiro é necessário fazer uma cópia e renomer SOMENTE às cópias.  
Todos os arquivos abordados aqui são são arquivos de configuração de ambientes, bancos de dados e parametrizações da linguagem PHP.   
Veja um exemplo do arquivo de configuração de banco de dados (**/src/api/config\_db.php**):

 [
'pvi' => [
'dsn' => 'sqlsrv:server=%s; database=%s',
'server' => 'seu-host',
'user' => 'sa',
'pass' => 'sua-senha',
'database' => 'sua-base-pvi',
'port' => '',
'charset' => 'utf8',
'collation' => 'SQL\_Latin1\_General\_CP1\_CI\_AS',
'logs' => false,
'debug' => false, // altere para true para salvar as consultas na pasta /log
'cache' => true,
],
],
'homologacao' => [
'pvi' => [
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
];]]>

**Licença de uso compartilhada**

Devido o controle de licenças, em desenvolvimento necessariamente precisar ser criado no domínio localhost:8000. O arquivo de licença é compartilhado entre todos participantes do time que queiram usar PVI. Para isso, precisa ser baixado por este [**link**](https://drive.google.com/file/d/12sn7tEy1okziyc9tfeZSH53tMYDkZ10T/view?usp=sharing) e colocado na sua instalação no diretório /src/api.

**Compilando**

Para compilação, no diretório base do PVI rode o comando:

gulp watch

Caso queira, o comando acima pode ser substituído por uma .bat, dessa forma, basta dar duplo em **build.watch.bat.** Ambas alternativas chegam ao mesmo resultado.

### **Criando Site no IIS**

O site precisa ser criado no IIS, para isso basta clicar com lado direito do mouse e adicionar novo site. Feito isso, precisa acessar o site criado, procurar pelo PHP Manager e registrar a versão do PHP instalada nos passos anteriores.  
  
Registrando PHP para site do PVI  
  
Escolhendo versão do PHP

**Configurações Finais**

Agora será necessário no IIS informar onde estão os fontes compilados do PVI, para isso acesse a home do site no IIS e siga os procedimentos da imagem.  
  
Selecionando os fontes no IIS

**Alternativas ao IIS**

Enquanto em ambiente de desenvolvimento, existe a possibilidade de não se preocupar com IIS e usar o servidor de testes embutido no PHP. Para isso, é necessário que o PHP esteja no PATH das variáveis de ambiente do sistema operacional.  
Feito isso, basta que no diretório base dos fontes do PVI seja rodado o seguinte comando:

php -S localhost:8000 -t build

Certifique que a porta 8000 não esteja sendo usada.  
Caso o IIS esteja usando a porta 8000, você pode parar o site pelo IIS ou abrir o prompt de comando como administrador e executar o comando:

iisreset /stop
