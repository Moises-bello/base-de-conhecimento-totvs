---
content_hash: 15aaacb064a86d615c93c8bbc687f29a4b8878af7c32130b62b7c2e7c993237d
fetched_at: '2026-06-29T00:10:57.245831+00:00'
page_id: '59900121'
product: rm
source: tdn-rm
title: Instalação e ativação do License Server no RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=59900121
version: 6
---

**1. O LicenseServer**

O servidor de licenças TOTVS é o responsável pela liberação de senhas e controle aos acessos simultâneos (semaforização). A configuração deste servidor como um servidor de licenças (LicenseServer) exige a instalação do dispositivo de licenças Hardlock, na porta paralela ou USB.

**Desenvolvimento/Procedimento**

**Importante:** O Hardlock foi descontinuado, deve-se utilizar o License Server Virtual.  
  
**Saiba mais:**  
Para mais detalhes sobre a instalação do License Server Virtual acesse o link abaixo:  
[TOTVS License Server Virtual](https://tdn.totvs.com/display/framework/TOTVS+License+Server+Virtual)  
  
Caso o ambiente não esteja dentro da portabilidade para instalação do License Server Virtual, poderá utilizar o arquivo de emergência. Para tanto, poderá entrar em contato com o CST - Senhas para solicitar o arquivo emergencial enquanto realiza a migração para o LSV ou gerar o arquivo de emergência no Portal do Cliente. Detalhes no link abaixo:  
[Procedimento para utilizar arquivo de emergência](https://tdn.totvs.com/pages/releaseview.action?pageId=271408244)

**1.1.****Instalador**

O instalador do LicenseServer é enviado juntamente com o seu Hardlock.

**Obs.:** - Antes da instalação do Hardlock, você deverá solicitar os arquivos de licença (**vide tópico 3**).

- Conecte o Hardlock na máquina onde o LicenseServer será configurado.

- Por ter sido descontinuado, o instalador do License Server Hard Lock não está disponível para download.

- Verifique se a plataforma onde será realizada a instalação do LicenseServer está homologada através do link .

**Instalação p****ara Windows:**

Para executar o instalador, localize os arquivos de instalação na pasta INSTALADORES do CD. Ao executar o Setup será apresentada a tela abaixo, onde deverá ser escolhida a linguagem para instalação da ferramenta.

Depois, será montado o ambiente de instalação...

Será apresentada a tela de boas vindas no assistente e instalação será iniciada com a apresentação do Termo de Licença de Uso do software.

Para continuar com a instalação, você deve aceitar somente se concordar com os termos ali expressos e em caso de quebra de acordo estará passível às sanções legais previstas em lei de Copyright.

**1.2.****Contrato de Licença**

Depois a tela “Local de destino” será exibida, para seleção do caminho da instalação do TOTVS LicenseServer. Se você quiser instalar o servidor de licenças em outro caminho, pode selecionar este caminho clicando no botão “Procurar”. O endereço de instalação padrão é:**“C:\TOTVSLicense\BIN”.**

**1.3.****Local de Destino**

A partir deste ponto, você está configurando o LicenseServer de acordo com suas necessidades. Haverá um padrão se você deseja uma configuração básica, apesar de não ser recomendado devido à grande variação de ambientes possíveis.

**1.4.****Tela “Configuração LicenseServer”**

Se você habilitar o LicenseServer, serão apresentadas as telas para a montagem do arquivo de configuração do LicenseServer.

**1.5.****Porta para configuração do listener**

Como o serviço do LicenseServer é um listener, precisamos informar uma porta para a comunicação com os servidores. A porta default é “5555” ou outra qualquer que esteja disponível entre “1024” e “65535”.

**1.6.****Habilitar ou não habilitar a Numeração Automática**

Temos a possibilidade de habilitar a Numeração Automática para que seja controlada pelo LicenseServer. Vale ressaltar que a indicação da TOTVS é para que utilizemos a numeração automática pelo LicenseServer caso isto esteja disponível na linha de produto. Consulte o manual da linha de produto para mais informações.

**Para usuário Datasul, Logix ou RM:**

Deve-se optar por **NÃO** habilitar, pois o controle de numeração destas soluções é feito por meio de uma ferramenta diferente.

**1.7.****Tela “Instalação do Hardlock”**

Nesta tela poderemos escolher se será ou não instalado o driver do Hardlock de forma automática pelo instalador. Caso escolha não instalar, os drivers homologados para os modelos de Hardlock serão copiados para a pasta “DRIVERS” dentro do path de instalação do

LicenseServer para que assim a instalação possa ser efetuada manualmente após o término do assistente de instalação. O path padrão para a pasta de driver é “C:\TOTVSLicense\Drivers”.

Se for escolhida a opção para instalação automática, será apresentada a tela para seleção do modelo de Hardlock que será utilizado no TOTVS LicenseServer.

Encerrados os passos de seleção das opções de instalação, o assistente exibirá o path para instalação e cópia dos arquivos.

**1.8.****Permissão de execução**

Após a instalação do LicenseServer, devem-se conceder permissões para execução do serviço nas **Propriedades do Meu Computador** **Avançado**...

 

... **pasta Prevenção de Execução de dados**, e incluir o Serviço TOTVSappServer.exe, que se encontra dentro do diretório **C:\TOTVSLicense\BIN**.

 

**1.9.****Verificações**

· Verificar nos serviços do Windows (**Iniciar Ferramentas Administrativas Serviços**) se o TOTVS LicenseServer está configurado para iniciar automaticamente e se está iniciado.

· Conferir se o número que consta nos arquivos de licença TOTVSlic\_2100010692.key e applylic\_2100010692.key são iguais ao do Hardlock

· Renomear os arquivos de licença antes de colocá-los no diretório: C:\TOTVSLicense\BIN

TOTVSlic\_2100010692.key è TOTVSlic.key

applylic\_2100010692.key è applylic.key

*Acessar o aplicativo TOTVS Monitor para verificar se os arquivos de licença estão sendo lidos corretamente.*

**Instalação para Linux**

Para iniciar a instalação copie o instalador do TOTVS LicenseServer em uma pasta local.

Devido à variação das línguas utilizadas para instalação, foram criados 3 arquivos de instaladores, onde:

- Install\_eng: help de instalação utilizando o inglês com língua base;

- Install\_spa: help de instalação utilizando o espanhol com língua base;

- Install\_ptb: help de instalação utilizando o português Brasil com língua base.

Existe ainda a variação de sistemas operacionais 32 (x86) ou 64 (x64) bits por este motivo foram criados dois pacotes de instalação baseado no GCC do kernel do Sistema Operacional onde:

- Para sistemas operacionais x86 que utilizam o GCC 3, utilizar o arquivo *totvslicenseserver‐10.1‐1.i386.rpm*;

- Para sistemas operacionais x86\_x64, baseados no GCC 4, utilizar o arquivo*totvslicenseserver‐10.1‐1.x86\_64.rpm*.

**Para exemplificar:**

Utilizando RedHat 3.2 onde a instalação deve ser em espanhol, usaremos o help de instalação “install\_spa” em conjunto com o pacote totvs‐licenseserver‐10.1‐1.i386.rpm.

O path de instalação dos arquivos do TOTVS LicenseServer será sempre o */totvslicense*, onde os diretórios:

**BIN**: contém o executável e o arquivo de configuração.

**LEIAME**: com a regra para utilização do software.

**DRIVERS**: que contém o driver do Hardlock modelo HASP que deverá ser instalado manualmente após o encerramento da instalação padrão.

Caso você opte por instalar os arquivos em outro path, deverá efetuar a cópia dos arquivos manualmente.

Abaixo seguem as telas do help onde o usuário deverá responder a algumas perguntas pertinentes à configuração do TOTVS LicenseServer.

**1.1.****Instaladores**

Para iniciar a instalação, vá até a pasta onde foram baixados os arquivos e rode o instalador na linguagem desejada. Abaixo está sendo instalado em português.

A partir deste ponto, você estará configurando o LicenseServer de acordo com suas necessidades, onde sempre teremos um default para os usuários que desejam uma configuração básica, apesar de não ser recomendado devido à grande variação de ambientes possíveis.

**1.2.****Configuração do LicenseServer**

Após a tela de boas‐vindas (abaixo), serão efetuadas as perguntas para criação do arquivo de configuração do serviço. Para prosseguir, pressione <<ENTER>>.

**1.3.****Configuração do Listener**

Como o serviço do LicenseServer é um listener, precisamos informar uma porta para a comunicação com os servidores. A porta default é “5555” ou outra qualquer que esteja disponível no range entre “1024” e “65535”. Para o exemplo abaixo, foi escolhida a porta “5858” para ser a porta de comunicação com o LicenseServer.

Para qualquer pergunta, o símbolo asterisco determina qual é a opção default de instalação e para se alterar a opção, basta pressionar o número da opção desejada e pressionar <<ENTER>>.

**1.4.****Habilitação do serviço do LicenseServer**

Logo em seguida, será perguntado se o serviço do TOTVS License será habilitado ou não. Selecione a opção SIM.

**1.5.****Habilitação da Numeração Automática**

Temos a possibilidade de habilitar a Numeração Automática para que seja controlada pelo LicenseServer. Vale ressaltar que a indicação da TOTVS é para que utilizemos a numeração automática pelo LicenseServer caso isto esteja disponível na linha de produto. Consulte o manual da linha de produto para mais informações.

**Para usuário Datasul, Logix ou RM:**

Deve-se optar por **NÃO** habilitar, pois o controle de numeração destas soluções é feito por meio de uma ferramenta diferente.

Encerrados os passos de seleção das opções de instalação, o pacote de instalação será instalado automaticamente e passará as últimas informações para o usuário.

**2.****Configuração do RM com o LicenseServer**

**2.1.****Configuração no RM**

Para realizar a configuração do aplicativo de acordo com as informações do servidor de licenças:

* Depois do Login com o **usuário Administrador do RM**, clique em SIM na tela abaixo:

* Preencha o IP da máquina onde o Hardlock está instalado e a Porta (5555 por padrão)

Se você quiser, pode alterar as configurações em Parâmetros Globais (**Opções Parâmetros Globais Pasta LicenseServer**).

**3.****Instruções para solicitações pertinentes de senhas**

As instruções a seguir são válidas exclusivamente para solicitações referentes a senha de acesso aos produtos TOTVS. As solicitações devem ser realizadas exclusivamente através do Portal [www.totvs.com/suporte](http://www.totvs.com/suporte),

**3.1.****Siga o passo-a-passo:**

1. Acessar [www.totvs.com/suporte](http://www.totvs.com/suporte) e efetuar o login:

2. Acessar a opção RM:

3. Clicar em “CST”

4. Selecionar o assunto “SENHAS” e ocorrência “LIBERAÇÃO DE SENHAS”

5. Preencher as informações solicitadas na descrição do chamado e clicar em “Enviar Chamado” conforme imagem anterior. O número do chamado será apresentado após a conclusão da abertura.

**3.2.****Possíveis ocorrências durante a instalação do TOTVS LicenseServer**

**Windows**

***BIND ERROR #10048****no Prompt do TOTVS LicenseServer: deve-se verificar se os Serviços “TOTVS LicenseServer” estão sendo executando juntamente com o Server do LicenseServer (Prompt do DOS) ao mesmo tempo.*

***ERRO #10000****ao realizar teste na configuração do LicenseServer no aplicativo: Verificar se os arquivos de licença foram renomeados e se estão no diretório correto (C:\TOTVSLicense\BIN)*

***ERR0002:****ERR0002: Não foi possível estabelecer conexão com TOTVS Application Server. ao acessar o TOTVS Monitor: Verificar se os arquivos de licença foram solicitados e se estão no diretório correto (C:\TOTVSLicense\BIN)*

**Linux**

Devido às regras de segurança de alguns sistemas operacionais, algumas das funcionalidades do instalador podem não funcionar corretamente. Neste caso o usuário deverá efetuar os processos manualmente.

Abaixo algumas das ocorrências mais comuns.

• Assistente não instalar o software: usuário utilizado na instalação não ter os direitos de Administrador sobre o hardware.

Logar como o “root” da máquina e efetuar uma nova instalação.

• Não copiou os arquivos para o path: caso isto ocorra, verifique se o pacote fora instalado, remova-o e rode o assistente novamente.

• O serviço do license não “enxerga” o Hardlock: esta situação pode ocorrer por dois motivos mais comuns:

1. O Sistema Operacional não permite “acesso” à porta onde está instalado o Hardlock: neste caso deve-se pedir ao administrador para efetuar a liberação.
2. Driver do Hardlock não está instalado: neste casso será necessário efetuar a instalação manualmente, onde para o Hardlock modelo “HASP” o driver está disponível no path de instalação e para o Hardlock “Safenet Proteq”, deverá ser acessado o site do fabricante para efetuar o download pertinente ao seu sistema operacional.

• Server do TOTVS License apresenta erro de BIND ao subir os serviços: a porta do serviço ou do License podem estar sendo utilizadas por outro aplicativo. Neste caso será necessário alterar as portas no arquivo de configuração¹. Quanto às portas:

- Sessão [TCP]: o parâmetro “port” se refere à porta do serviço do TOTVS License. Este não é o serviço listener do License Server. A porta² padrão de instalação é “2234”

- Sessão [LICENSESERVER]: o parâmetro “port” é a porta onde o listener do LicenseServer está conectado aguardando a solicitação por parte dos aplicativos. A porta padrão do listener do LicenseServer é “5555”.

1 /totvslicense/bin/totvsappserver.ini e deve-se utilizar o vi para editar o arquivo.

2 As portas do serviço poderão ser alteradas para qualquer porta disponível no range entre “1024” e “65535”.

**4.****Dúvidas frequentes**

**01)****Será entregue uma cópia do Hardlock para servir de backup? Em caso de problemas na peça, eu fico sem os acessos?**

Não, não existe cópia do Hardlock. Em caso de problemas você pode ligar ao **CST TOTVS**, e será fornecida uma senha de emergência. Esta senha terá validade de **24 horas** e possibilitará o acesso ao aplicativo ate que o problema com o Hardlock seja solucionado.

Para aplicar a senha de emergência você precisará acessar a aplicação, caso o Licence server não seja encontrado, uma janela para preenchimento dos seus parâmentros será aberta. No canto direito desta janela existe o botão "Entrar senha de emergência", clique neste botão e insira a senha no campo que será apresentado.

**02)****Qual o prazo para substituição do Hardlock ocorrendo:**

**a.****Perda ou roubo?**

No caso de perda, você deve acionar o EAR para solicitar um novo Hardlock.

**b.****Aquisição de licenças adicionais / Movimentação de licenças entre módulos (licenças light)?**

No caso de licenças adicionais não há necessidade de substituição do Hardlock. A mudança se da nos arquivos TOTVSlic.key e Applick.Key que serão enviados por email pela TOTVS.

**03)****Como faço para ter licenciamento em meu ambiente de Homologação (testes)?**

As licenças para o ambiente de teste serão concorrentes com as licenças de produção, ou seja, a base de teste será apontada para o mesmo Hardlock que a base de produção. Com isso o cliente terá que administrar o uso das licenças disponíveis.

**04)****Qual o valor de substituição do Hardlock?**

A cobrança do Hardlock depende da negociação com o EAR. Se for gratuito, o próprio EAR pode abrir um chamado no CST solicitando um novo envio. Se houver custo, o EAR fará uma proposta para faturamento.

**05)****A TOTVS terá uma política de atualização do Hardlock?**

O Hardlock não vence. O que vence são os arquivos **TOTVSlic.key** e **Applick.Key**. Estes arquivos serão substituídos quando expirarem e são eles que contêm as licenças adquiridas.
