---
article_id: 360018849891
category: NFe - Nota Fiscal Eletrônica
content_hash: 21c810125b0282baea8924ab4239ed08b6e897fbfa3ce11f9cda026db491aa89
fetched_at: '2026-06-28T22:40:01.798415+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como instalar
  ( configurar / cadastrar ) o certificado digital modelo A3 '
type: support-article
updated_at: '2024-02-02T18:35:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018849891--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-instalar-configurar-cadastrar-o-certificado-digital-modelo-A3
---

**Dúvida**Como instalar ( configurar / cadastrar ) o certificado digital modelo A3?**Ambiente** **TSS -** a partir da versão**12.1.17 2.0** e **12.1.17 versão 3.0  
  
Solução****Procedimento de configuração de certificados modelo A3**  
  
Recomendamos fortemente a utilização do modelo A1, pois é mais simples de instalar e configurar, não existe concorrência de acesso ao Hardware, não existe incompatibilidades com Sistemas Operacionais, fácil substituição, funciona em máquinas virtuais e em ambientes em Nuvem e por ser um arquivo digital lógico é de acesso mais rápido e não opera a aplicação.

| **Vantagens modelo A1** | **Desvantagens modelo A3** |
| --- | --- |
| Sem concorrência de acesso ao hardware | Concorrência de acesso ao hardware |
| Sem incompatibilidades para os sistemas operacionais mais usados | Requer homologação do fabricante para os sistemas operacionais mais usados |
| Fácil substituição | Requer manuseio e porta de acesso disponível no servidor a ser instalado |
| Funciona em ambientes virtualizados | Não funciona em ambientes virtualizados |
| Arquivo lógico de acesso rápido maior desempenho de uso | Arquivo físico\lógico de acesso mais lento menor desempenho de uso |

**Tipos de documentos homologados para certificado modelo A3 no TSS:**

* NF-e
* CT-e
* E-Social
* REINF

Para utilização dos demais documentos será necessário um desenvolvimento participativo para maiores detalhes acionar o suporte TOTVS.

**Pré-requisitos de utilização modelo A3:**

A – Software (Gerenciador e drivers) do A3 deve estar instalado e configurado na máquina que irá executar o TSS.

B – Hardware (Token,SmartCard,etc…) do A3 deve estar instalado fisicamente na máquina que irá executar o TSS

C – Homologado apenas para sistema operacional Windows

D – Reunir as informações necessárias para configuração:

* Slot do certificado digital;
* Label do certificado digital ou ID em Hexadecimal;
* Senha do certificado digital, geralmente o PIN de acesso;
* Caminho e arquivo do modulo – biblioteca(.dll)

**Para ambientes em Cloud, ou servidores virtualizados, não é possível a utilização do certificado A3, dúvidas consulte nossa FAQ:**

[TSS0041 - É possível configurar certificado A3, em ambiente Cloud em Servidores Virtuais](http://tdn.totvs.com/pages/viewpage.action?pageId=329023719)

**Atenção**

A instalação bem como a configuração do gerenciador do certificado no sistema operacional não é de responsabilidade da TOTVS, sendo necessário o prévio teste e validação de sua funcionalidade. Sugerimos que esta instalação e configuração seja realizada por um profissional com o conhecimento exigido pelo fabricante do Hardware.

![(warning)](http://tdn.totvs.com/s/en_GB/7201/3d89a43db3618502ceb73a83aa0af888aa0a285a/_/images/icons/emoticons/warning.png) Os passos a seguir são orientações e dicas para se obter os dados necessários que serão exigidos ao se configurar um Hardware A3 nos produtos TOTVS.

**1 - Identificar em seu A3, os dados exigidos no item D:**

Sabendo que cada fornecedor de certificado A3 tem seu próprio gerenciador de certificado, podem existir diferenças de como conseguir estes dados.

Abaixo listamos algumas dicas e procedimentos para ajudar a encontrar essa informação:

* **Slot do certificado digital:**

SLOT é uma divisão que existe dentro do A3, normalmente o fabricante insere o certificado dentro do **SLOT 0**. Dentro do gerenciador do certificado é possível obter este dado.

**Exemplo Pronova:**

![](http://tdn.totvs.com/download/attachments/329031101/pronova.jpg?version=1&modificationDate=1515414145000&api=v2&effects=drop-shadow)

**Exemplo Aladin(SafeNet)**:

![](http://tdn.totvs.com/download/attachments/329031101/Aladin.jpg?version=1&modificationDate=1515414055000&api=v2&effects=drop-shadow)

* **Label do certificado digital ou ID em Hexadecimal**

Lavel ou ID Hex é a identificação do certificado digital armazenado dentro do hardware, é o nome que as aplicações procuram o certificado dentro do A3.

**Exemplo Pronova:**

**![](http://tdn.totvs.com/download/attachments/329031101/Log-Pronova.jpg?version=1&modificationDate=1515414249000&api=v2&effects=drop-shadow)**

**Exemplo Aladin(SafeNet):**

![](http://tdn.totvs.com/download/attachments/329031101/log-Aladin.jpg?version=1&modificationDate=1515414334000&api=v2&effects=drop-shadow)

Dica, existem o programa gratuito chamado **OpenSC**, com o comando abaixo é possível listar todos os objetos (certificados) dentro do hardware.

C:\OpenSC\tools>pkcs11-tool.exe --module c:\windows\system32\etpkcs11.dll -l -O

**Observação:**O caminho bem como a **DLL** de uso será de acordo com o fornecedor do certificado.

* **Senha do certificado digital, geralmente o PIN de acesso.**

Senha ou Pin de acesso, é o código informado pelo fornecedor do A3, para acessar as chaves privadas do certificado armazenado.

Geralmente no gerenciador do certificado é solicitado este PIN de acesso.

* **Informar o caminho e arquivo do modulo – biblioteca(.dll)**

Informar o caminho absoluto da **Dynamic-link library** (biblioteca de vínculo dinâmico) ou **DLL** para o fabricante a ser configurado, o caminho do repositório de DLL(s) é indicado pelo fabricante no momento da instalação do driver oficial.

Geralmente este arquivo está dentro da System32 ou SysWOW64, isso pode variar com o Sistema Operacional e versão do Driver do aplicativo instalado.

Uma dica para encontrar este arquivo é acessando o certificado pelo navegador FireFox, nele existe um módulo de acesso ao gerenciador físico e é possível verificar qual a DLL que ele utiliza.

Quando o certificado é importado no navegador Firefox é possível visualizar a DLL e o caminho usado pelo drive do fornecedor para gerenciamento do certificado, essa opção está disponível na opção ***“Dispositivos de Segurança”***

![](http://tdn.totvs.com/download/attachments/329031101/Firefox1.jpg?version=1&modificationDate=1515413688000&api=v2&effects=border-simple,shadow-kn)

**Exemplo Pronova:**

![](http://tdn.totvs.com/download/attachments/329031101/Firefox2.jpg?version=1&modificationDate=1515413826000&api=v2&effects=border-simple,shadow-kn)

**Exemplo Pronova:**

*C:\Windows\System32\asepkcs.dll*

**Exemplo Alladin:**

*C:\Windows\System32\etpkcs11.dll*

**2 – Habilitando logs adicionais no TSS, para verificação de mensagens informativas de comunicação como A3**

Basta acrescentar as tags abaixo no appserver.ini na sessão SSLConfigure para acompanhar as mensagens de comunicação

**Verbose=1  
Bugs=1**

![](http://tdn.totvs.com/download/attachments/329031101/image2018-1-8_10-30-3.png?version=1&modificationDate=1515414604000&api=v2&effects=drop-shadow)

**Exemplo de mensagens:**

![](http://tdn.totvs.com/download/attachments/329031101/Mensagens.jpg?version=1&modificationDate=1515414902000&api=v2&effects=drop-shadow)

**3 – Configuração na aplicação TOTVS dos dados obtidos no item 1**

Nas telas das aplicações da TOTVS deve existir a possibilidade de configurar os dados obtidos:

**Exemplo TAF**

![](http://tdn.totvs.com/download/attachments/329031101/TAF1.jpg?version=1&modificationDate=1515426527000&api=v2)

![](http://tdn.totvs.com/download/attachments/329031101/TAF2.jpg.png?version=1&modificationDate=1515426646000&api=v2)

![](http://tdn.totvs.com/download/attachments/329031101/TAF3.jpg?version=1&modificationDate=1515426607000&api=v2)

![](http://tdn.totvs.com/download/attachments/329031101/TAFZZ.jpg?version=1&modificationDate=1515426739000&api=v2)

![](http://tdn.totvs.com/download/attachments/329031101/TAF5.jpg?version=1&modificationDate=1515427256000&api=v2)

![](http://tdn.totvs.com/download/attachments/329031101/TAF6.jpg?version=1&modificationDate=1515427275000&api=v2)

**Exemplo ERP Protheus NF-e**

Os passos a seguir são para configuração do certificado modelo A3 são referentes ao ERP Protheus 12, o **wizard configure** auxilia a configuração do certificado.

![](http://tdn.totvs.com/download/attachments/329031101/1.jpg?version=1&modificationDate=1515414940000&api=v2)

Ao selecionar a opção de Wiz.Config. a tela de boas-vindas irá guia-lo até a configuração do certificado e demais propriedades utilizadas na rotina de emissão de nota eletrônica.

![](http://tdn.totvs.com/download/attachments/329031101/2.jpg?version=1&modificationDate=1515414965000&api=v2)

O próximo passo é informar onde encontrasse o serviço web-service do TSS este endereço é composto por um endereço de host e uma porta de conexão.

![](http://tdn.totvs.com/download/attachments/329031101/3.jpg?version=1&modificationDate=1515414977000&api=v2)

Selecione o tipo de certificado a ser utilizado na configuração do certificado para o modelo A3 em questão selecione a opção **HSM.**

![](http://tdn.totvs.com/download/attachments/329031101/4.jpg?version=2&modificationDate=1515426665000&api=v2)

A previa seleção do campo HSM implica na indicação das demais informações de configuração no cerificado.

* Slot do certificado digital
* Label do certificado digital
* Informe a senha do certificado digital
* Informar o caminho e arquivo do modulo do HSM

![](http://tdn.totvs.com/download/attachments/329031101/5.jpg?version=1&modificationDate=1515414997000&api=v2)

**4-Lista de certificados homologados junto com acompanhamento dos clientes:**

Atualmente a aplicação TSS utiliza para acesso ao Hardware o padrão **modulo/slot/label ou ID hex**.

Este é o padrão de mercado dos fabricantes de A3, desta forma mesmo que seu modelo não esteja na lista, existe grande possibilidade de compatibilidade.

**Abaixo seguem as marcas e modelos de certificados tipo A3 aceitos:**

| HSMs | Marca | Observação | Status |
| --- | --- | --- | --- |
| LUNA SA | Safenet | (warning)  Utilizado em aplicações Windows podendo funcionar em demais S.O.s | SUPPORTED |
| LUNA SP | Safenet | (warning)  Utilizado em aplicações Windows podendo funcionar em demais S.O.s | SUPPORTED |
| LUNA PCI | Safenet | (warning)  Utilizado em aplicações Windows podendo funcionar em demais S.O.s | SUPPORTED |
| LUNA PCM | Safenet | (warning)  Utilizado em aplicações Windows podendo funcionar em demais S.O.s | SUPPORTED |
| PROTECTSERVER Externo | Safenet | (warning)  Utilizado em aplicações Windows podendo funcionar em demais S.O.s | SUPPORTED |
| PROTECTSERVER Gold | Safenet | (warning)  Utilizado em aplicações Windows podendo funcionar em demais S.O.s | SUPPORTED |
| ProtectHost EFT | Safenet | (warning)  Utilizado em aplicações Windows podendo funcionar em demais S.O.s | SUPPORTED |

**Observação:**

Para o pleno funcionamento da NF-e é necessário que o certificado digital no HSM seja importado com as seguintes diretivas:

CKA\_PRIVATE

CKA\_VERIFY

CKA\_SIGN

| **Token** | Marca | Observação | Status |
| --- | --- | --- | --- |
| EPASS2000 | Pronova | (warning)  A versão *"SC"*SmartCard pode funcionar  com as configurações do e-Token | SUPPORTED |
| Aladdin eToken PRO (Java) | Aladin | (warning)  A versão *"SC"*SmartCard pode funcionar  com as configurações do e-Token | **SUPPORTED** |

**Observação:**

Caso o padrão utilizado pelo certificado não seja compatível com o procedimento descrito, é necessário acionamento ao suporte para orientação e possível homologação do fabricante em questão.

|  |  |
| --- | --- |
| **Observações:** | Para o sucesso da instalação e configuração sempre verificar a correta instalação do hardware bem como a utilização de drive(s) homologado(s) para o S.O. utilizado. |
