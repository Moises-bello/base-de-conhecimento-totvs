---
content_hash: 5fe701e877df7d75bdc760f3611b8fe2de7e345eb2b65eb81e6cb822bae3c0c2
fetched_at: '2026-06-29T00:09:35.387261+00:00'
page_id: '425459336'
product: rm
source: tdn-rm
title: Biometria
type: documentation
url: https://tdn.totvs.com/display/LRM/Biometria
version: 6
---

A Biometria de usuários do TOTVS Gestão Bibliotecária funciona por meio da instalação de um pequeno scanner biométrico que, sob pressão do dedo do usuário, registra a impressão digital, possibilitando maior controle na identificação deste usuário.  
Para utilizar a biometria, você deverá cadastrar a impressão digital do usuário através do botão Cadastrar do campo Biometria do usuário que fica em **Cadastros > Usuário > Usuários > Dados Específicos**.

A Biometria poderá ser utilizada na tela de movimentações e de reservas para identificar o usuário.

Para utilizar as funções da biometria no TOTVS Gestão Bibliotecária é necessário utilizar um software terceiro que é responsável por fazer a comunicação com o dispositivo de leitura biométrica e também por fazer a leitura e comparação da biometria. O TOTVS Gestão Bibliotecária permite a utilização do software do fabricante **Griaule Biometrics e da NeuroTech (VeriFinger SDK 10.0)**.

# Griaule

A empresa **Griaule Biometrics** possui atualmente duas versões do software disponíveis para uso, porém somente uma ainda é comercializada, a versão **Griaule Fingerprint SDK 2009** (não é mais comercializada, porém ainda está disponível para o uso para quem possui a licença) e a versão **GBS Fingerprint SDK 2014** que é a versão atual de mercado da empresa.  
Caso o cliente deseje utilizar este recurso, ele deve entrar em contato com a empresa fabricante do SDK para adquirir as licenças de uso do software.  
Para informações sobre aquisição de licenças de uso: <https://griaule.com/>

**Griaule Fingerprint SDK 2009:**   
O Griaule Fingerprint SDK 2009 é preferencialmente utilizado com o Windows no modo 32 bits (x86), caso o Windows utilizado esteja em modo 64 bits (x64) e o RM esteja sendo executado também em 64 bits (x64) é necessário efetuar um ajuste para que o RM seja executado em 32 bits (x86) e consiga comunicar corretamente com o SDK e o leitor biométrico, clique [aqui](http://tdn.totvs.com/x/PQ4wDg) para as orientações.   
Este software permite a utilização da biometria com leitores de diversos fabricantes, porém existem os homologados pela TOTVS para utilização, ambos funcionam em versões do Windows 32 bits (x86) e 64 bits (x64):

* Digital Persona U.are.U 4000
* Digital Persona U.are.U 4500

   
Os seguintes passos devem ser realizados para instalação do software de biometria:   
- Executar o instalador do **Griaule Fingerprint SDK 2009**.  
   
**Em versões inferiores ao Sistema operacional Windows 7:**  
Retire da pasta **C:\CorporeRM\RM.Net** as seguintes dlls, caso elas existam:

* libusb0.dll
* Interop.SSLCOMLib.dll
* Neurotec.Biometrics.Gui.VFView.dll
* Neurotec.Biometrics.VFNetWrapper.dll
* FingerPrinterDll.dll
* ScanMan.dll
* ssl.dll
* sslCom.dll
* sslFile.dll
* sslUareU.dll
* VFinger.dll

**Sistema operacional Windows 7**  
- Registre a GrFingerX.dll, para isto utilize o atalho Windows + R para abrir o Executar, na caixa de texto digite o comando regsvr32.exe C:\RM\RM.NET\GrFingerX.dll e em seguida clique no botão OK.   
**Observação**  
Caso apareça a mensagem "Dll sslCom.dll não registrada" você deverá clicar no botão Iniciar (do windows) e escolher o menu Executar. Na caixa de texto da janela Executar, digite o comando regsvr32.exe C:\RM\RM.NET\sslCom.dll e em seguida clique no botão OK para que a dll sslCom.dll seja registrada.  
**GBS Fingerprint SDK 2014:**   
Está versão do SDK está disponível em 32 bits (x86) e 64 bits (x64), é necessário somente instalar a versão compatível com o sistema operacional e com a execução do RM.exe, se estiverem sendo executados em 64 bits (x64) é necessário que o SDK 64 bits (x64) esteja instalado.   
Após a instalação é necessário copiar algumas dll's (arquivos) do SDK para a pasta onde está sendo executado o RM.exe. As dll's vão estar na pasta "bin" de instalação do SDK da Griaule.

* GBSFingerprint.dll
* GBSFingerprint.NET.dll
* GBSFingerprintCapPluginDPOneTouch.dll
* GBSFingerprintCapPluginFutronic.dll
* opencv\_core249.dll
* opencv\_ml249.dll
* pthreadVC2.dll
* RS\_SDK\_64.dll

Após a cópia destes arquivos o RM irá ter acesso ao SDK da Griaule e consiguirá efetuar leituras biométricas.   
**Leitores homologados**   
Para informações sobre leitores biométricos homologados entre em contato diretamente com a Griaule, pois o RM.exe não faz a comunicação com o dispositivo, mas sim o SDK, ele é responsável pela comunicação direta com o dispositivo.   
Observação: para evitar possíveis conflitos é recomendável ter apensar uma versão do SDK instalado.

# NeuroTech

A empresa NeuroTech possui apenas uma versão, a VeriFinger SDK 10.0, caso o cliente deseje utilizar este recurso, ele deve entrar em contato com a empresa fabricante do SDK para adquirir as licenças de uso do software. 

Para Informações sobre a aquisição de licenças de uso: <https://www.neurotechnology.com/verifinger.html>

### VeriFinger SDK 10.0 (e superiores)

Esta versão do SDK está disponível em 32 bits (x86) e 64 bits (x64), é necessário somente instalar a versão compatível com o sistema operacional e com a execução do RM.exe.

Após a instalação é necessário copiar algumas pastas e dll's (arquivos) do SDK para a pasta onde está sendo executado o RM.exe. As dll's vão estar na pasta "bin" de instalação do SDK da VeriFinger, lembrando que se o RM.exe estiver sendo executado em 32 bits os arquivos estarão na pasta **Win32\_x86** e caso seja 64 bits na pasta **Win64\_x64**.

As pastas e arquivos que devem ser copiados são:

Para a pasta de execução do RM.exe (RM.net)

* Pastas:
  + **Activation**
  + **FScanners**
* Arquivos:
  + Todas as dll's

Para a pasta anterior a execução do RM.exe (RM.net)

* Pastas:
  + **Data**
    - Somente o arquivo **Fingers.ndf**
  + **Licenses**
    - Com todos os arquivos que existirem na pasta

#### Utilização da versão trial (versão 11 e superiores)

A partir da versão 11 do SDK, é possível utilizar a versão trial (licença válida para testes por 30 dias).

Com a licença Trial ativada pela NeuroTech é necessário que na pasta Licenses, exista o arquivo "TrialFlag.txt" com a tag "True" no seu conteúdo. Caso não utilize a versão Trial, o arquivo deve conter a tag "False".

**Observação**: a tag "True" no arquivo TrialFlag não define a licença do SDK como Trial, ela é somente um complemento a licença utilizada pelo gerenciador de licenças do SDK, ou seja, mesmo contendo o valor "True" no arquivo, o SDK considera a validade da licença.

Informações

A utilização do SDK na versão Trial está disponível no RM a partir das versões 12.1.32.290, 12.1.33.255, 12.1.34.154 e 12.1.2205.101.

#### Leitores homologados:

Para informações sobre leitores biométricos homologados entre em contato diretamente com a NeuroTech, pois o RM.exe não faz a comunicação com o dispositivo, mas sim o SDK, ele é responsável pela comunicação direta com o dispositivo.   
Observação: para evitar possíveis conflitos é recomendável ter apensar uma versão do SDK instalado.
