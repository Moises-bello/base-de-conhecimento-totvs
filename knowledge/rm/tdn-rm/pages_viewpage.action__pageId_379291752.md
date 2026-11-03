---
content_hash: 322f2ae9566006478790b88237ceab336d408b07fe195c8b14870bfcc1a2c60b
fetched_at: '2026-06-29T00:09:02.161037+00:00'
page_id: '379291752'
product: rm
source: tdn-rm
title: BD0020_BDE_Instalação_e_Configuração_SQL_SERVER
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379291752
version: 1
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Banco de Dados |
| **Versão RM** | : | Qualquer Versão |
| **Banco de Dados** | : | SQL Server |
| **Processo** | : | Instalação BDE |
| **Sub Processo** | : | Conexão de Dados |
| **Data da Publicação** | : | 05/03/2014 |

---

O BDE (Borland Database Engine) é um software que acompanha os aplicativos do **CORPORE RM** e é responsável pela comunicação entre estes aplicativos e o banco de dados.

As aplicações utilizam o **Alias "CORPORE RM"** no BDE para conectar a base de dados compartilhada

O BDE deve ser instalado antes de qualquer aplicativo do **CORPORE RM**. Se o BDE já estiver instalado, verifique se a versão que acompanha o aplicativo a ser instalado é a mais recente.

**1.** **Instalando o BDE:**

* Baixe o instalador do BDE no [Portal de Downloads](https://suporte.totvs.com/download):

* O programa de instalação iniciará, automaticamente, a cópia dos arquivos do BDE para o disco rígido da estação de trabalho, no caminho <Drive>:\Program Files\Borland\Common Files\BDE (ou <Drive>:\Arquivos de Programa\Borland\Arquivos Comuns\BDE, para versão do Windows em português).
* No final da Instalação, clique no botão [FINISH] para concluir. Esta instalação criará o ícone do BDE (BDE Administrator) no grupo de programas RM Sistemas.

**2.** **Configurando o BDE**

Depois de instalado o BDE, é preciso configurá-lo para que o mesmo possa prover o acesso ao banco de dados desejado. Sendo assim, execute o programa **BDE Administrator**, no grupo de programas Iniciar | Programas | RM Sistemas ou dentro do Painel de Controles.

**Observação**: A versão mais recente do Instalador do BDE, distribuída pela TOTVS, possui as respectivas configurações para o Windows Vista.

**3.** **Criando um novo DataBase Alias**:

No menu **Object**, selecione a opção **New**;

No diálogo **New Database Alias**, selecione o banco (**Oracle**) para o qual será criado o Database Alias;

Informe os parâmetros de configuração do novo Database Alias. Estas configurações podem ser diferentes para cada cliente. O ideal é começar com uma configuração um pouco mais moderada e aumentar gradativamente caso se faça necessário. Deixar os valores no limite superior dos mesmos pode evitar alguns erros, porém em contrapartida pode prejudicar o desempenho.

Agora informaremos um nome para nosso alias. Por padrão, bases que serão utilizadas por sistemas do CorporeRM devem ser iniciados com o nome “CorporeRM”. Depois de nomeado, passaremos a configurar o alias criado:

* Altere o campo *“Server Name”* para o nome da maquina onde se encontra o banco de dados restaurado;

* Altere o campo “D*atabase Name”* para o nome do banco de dados em questão criado no SGDB do SQL Server já restaurado;

* Preencha o campo “User Name” com o nome de um usuário com acesso para este banco de dados. (Por padrão usamos o nome “rm” ou “sysdba”).

Após estes preenchimentos, vamos testar a conexão com o banco: Primeiramente, salve estas alterações pelo ícone localizado na parte superior do BDE Administrator:

Clicando em OK em seguida:

Após os procedimentos acima serem efetuados, clique duas vezes sobre o alias criado, o BDE solicitará uma senha para executar tal conexão, por padrões, para o usuário “rm” deve-se usar a senha “rm” e para o usuário “sysdba” deve-se usar a senha “masterkey”.

Não esqueça que você terá que ter rodado os scripts de usuário para que a conexão funcione perfeitamente:

Caso a conexão seja bem sucedida, após digitar a senha e clicar em “OK” o sistema apresentará o alias com um quadrado verde conforme imagem abaixo:

Deve-se verificar os parâmetros abaixo para uma boa performance do sistema e prevenir alguns erros:

**Na guia Database, ainda no alias CorporeRM:**

Type – selecionando o banco de dados (MSSQL)

"BLOB" (Binary Large OBject), recipiente para campos de origem diversas, podendo ser até mesmo objetos definidos pelo próprio usuário. Num BLOB pode-se guardar imagem, som, textos longos, textos longos formatados. Este parâmetro pode comprometer a performance do sistema, por isso sugerimos que seja aumentado gradativamente.

O Blob Size – Limita o tamanho que a área temporária utilizada na memória (buffer) pode chegar. Setando este parâmetro para 64, significa que sua aplicação pode chegar a um blob de 64 K. >32 e <1000. Sugerido inicialmente: 64

O Blob Cache – Determina a quantidade de Blobs que poderá armazenar na estação. Setando este parâmetro para 128, significa que a aplicação poderá trabalhar com o máximo de 128 blobs armazenados, caso ultrapasse, o sistema irá emitir a seguinte mensagem: "Invalid Blob handle in record buffer", neste caso é só aumentar. >64 e < 65536. Sugerido inicialmente: 128

Caso os valores destes parâmetros sejam alterados, os valores dos parâmetros na tela *Drivers/Native/MSSQL* deverão ser alterados também com os mesmos valores.

**Na guia Configuration:**

*Drivers/Native/MSSQL*

* Time out – O máximo do tempo que a estação aguarda para o resultado de retorno do servidor. Valor em segundos. Aumente este valor gradativamente pois o mesmo pode degradar a performance. *Sugerido inicialmente: 7200*
* Connect Time out – O tempo que a estação vai aguardar uma resposta de conexão com o servidor. Valor em segundos. *Sugerido* *inicialmente: 120*
* Max Dbprocesses: Quantidade máxima de processos concorrentes no SQL - *Sugerido inicialmente: 90*

***System/Init***

* Langdriver – Driver da linguagem do sistema apropriado para a versão do Windows do seu país: 'ascii' ANSI
* Memsize – Máximo de memória que o BDE poderá utilizar. Mínimo 16 MB, máximo 205 MB. Sugerimos que coloque o valor da memória da estação, desde que seja menor que 205.
* Maxfilehandles – Máximo de arquivos concorrentes que o BDE poderá suportar, o valor alto dará impacto a uma boa performance no sistema, porém utilizará mais recurso do sistema operacional. Dever ser usado somente valor inteiro de 5 a 4096.
* MaxBufSize – Indica os recursos alocados para o buffer, e bufsize indica os recursos necessários para armazenar o buffer. Dever ser usado somente valor inteiro de 5 a 4096.

O print abaixo demonstra um exemplo de configuração. Estas configurações podem ser diferentes para cada cliente. O ideal é começar com uma configuração um pouco mais moderada e aumentar gradativamente caso se faça necessário. Deixar os valores no limite superior dos mesmos pode evitar alguns erros, porém em contrapartida pode prejudicar o desempenho.

Após realizar qualquer alteração na aba Configuration, salve-a clicando na seta conforme print abaixo:

Após isto, será preciso reiniciar o BDE.

As configurações do BDE podem afetar diretamente as rotinas ainda em Delphi, rotinas migradas não terão relação com estes procedimentos e no modelo três camadas estarão sendo processados nos servidores de aplicação e JOB.

Para Mais Informações

**COMUNIDADE **[R@Tecnologia](http://fluig.totvs.com/portal/p/10097/subject/rtecnologia-community)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs: [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados);
