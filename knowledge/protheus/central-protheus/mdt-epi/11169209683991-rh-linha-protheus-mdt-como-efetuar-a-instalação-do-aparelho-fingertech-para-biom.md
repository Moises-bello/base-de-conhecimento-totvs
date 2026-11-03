---
article_id: 11169209683991
category: MDT - EPI
content_hash: dea54862aa203478100ef9ddcb8dc9237671577610435640fdb12bb1f67c4028
fetched_at: '2026-06-28T22:44:25.329649+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Como efetuar a instalação do aparelho FingerTech
  para Biometria no MDT
type: support-article
updated_at: '2025-08-06T12:48:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11169209683991-RH-Linha-Protheus-MDT-Como-efetuar-a-instala%C3%A7%C3%A3o-do-aparelho-FingerTech-para-Biometria-no-MDT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19303994484375) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como efetuar a instalação do aparelho FingerTech para biometria no MDT?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**A Biometria utilizada no módulo **SIGAMDT** homologou o aparelho **FINGERTECH** da **NITGEN** do modelo **Hamster DX**.   
Antes de iniciar o processo de cadastro biométrico, deve ser seguido o manual de instalação.  
  
**1** Baixar o driver se encontra no site do fabricante para download: [Hamster-DX-III-Windows-Driver-1.4.0.0](https://suporte.fingertech.com.br/leitores-biometricos/), selecionar a opção Baixar dentro de Drivers de Instalação   
![15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982738820887)  
 **1.1** Dentro da pasta baixada, execute o arquivo chamado **Instalador.bat** (talvez seja necessário utilizar a opção do click da direita chamada **Executar como Administrador**):   
  
![16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982738823191)  
 **![17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982784285335)  
  
1.2** O software iniciará a instalação, aguarde até apresentar a mensagem abaixo. Selecione a opção **Next**:  
  
![18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982784286231)  
  
**1.3** Para executar a captura da digital, selecionar os botões na sequência abaixo:

**Device Scan** - Nesse momento haverá uma busca do dispositivo   
**Init** - Começa a inicialização do dispositivo  
**Capture** - Colocar o dedo no aparelho para selecionar o botão de captura da digital  
  
![19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982738825495)  
 **1.4** Captura concluída, pode fechar o aplicativo.

![21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982784288919)  
 **1.5** Após realizar o teste, selecionar a opção **Finish**.

![22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982738831127)

**Instalar o SDK**  
**2**. O arquivo SDK se encontra no site do fabricante para download: [eNBioBSP SDK v5.2.0.6.](https://suporte.fingertech.com.br/devs-download-sdk/)

**2.1** Dentro da pasta baixada, selecionar a configuração do computador (32 bits ou 64 bits) e dentro dessa pasta, selecionar o arquivo chamado eNBioBSP\_v5.2.0.6.exe.  
  
![23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982738832023)  
  
![24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982738832535)  
 **2.2** Selecione a opção Next para prosseguir com a instalação:  
  
![25.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982784291735)  
 **2.3** Para aceitar os termos de uso, selecione a opção Yes:  
  
![26.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982784292503)  
 **2.4** Na pasta baixada, selecione o arquivo chamado **SERIAL.txt** e copie o conteúdo de dentro do arquivo:  
  
![27.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982784292759)  
  
**2.5** Utilize o Serial copiado para colar no campo **Serial Number**. Informe os demais campos e selecione a opção Next::  
  
![28.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982784293015)

**2.6** Selecione o local de instalação e selecione a opção Next até finalizar:

![29.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982784299159)  
  
![30.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982738838423)

![31.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982738838807)  
  
![32.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982784303639)  
  
![33.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982784308119)  
  
**DLLs**  
**3**. Não é mais necessário baixar.

**DLL**

As DLLs são geradas automaticamente com a instalação do SDK atualizado

**Instalação do Serviço para a Comunicação com o Protheus**  
**4**. Instalar o Serviço para a Comunicação com o Protheus. o mesmo se encontra no site do fabricante para download. Necessário copiar o link <https://bit.ly/2FVCejw> do executável **FingertechWeb\_Installer** e colar no Navegador.

**4.1** Dentro da pasta baixada, selecionar o arquivo chamado **FingertechWEB**.

**4.2** Selecionar a opção Próximo até finalizar:  
  
![34.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982738842647)  
  
![35.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33982738843671)  
  
**5°** Após todas essas configurações, antes de iniciar o processo de cadastro da Biometria, deverá iniciar o aplicativo **FingerTechWeb** (procure por esse nome na lupa do Windows) será demonstrado o ícone  ![](https://tdn.totvs.com/download/thumbnails/712475862/image2022-9-27_10-39-47.png?version=1&modificationDate=1664285988773&api=v2) veja se aparece iniciado:  
  
![](https://totvssuporte.zendesk.com/attachments/token/C5G9UzARzcF3pcMXM68zoO5Ef/?name=image.png)  
  
Ao efetuar a instalação será criado uma pasta na raiz (normalmente criada em C:\FingertechWeb) onde, dentro dela consta o arquivo **Configuracao.ini**. Por default, o sistema cria a configuração na porta 9000, abra o arquivo **Configuracao.ini**. e veja se é apresentado assim:  
  
![](https://totvssuporte.zendesk.com/attachments/token/p6QuEhu2pz6A8YWGrA34lWiF4/?name=image.png)  
  
How To | SIGAMDT - Configuração Biometria - Instalação - Linha Protheus  
  
  
  
  
  
  
**Saiba Mais**[MDT0113 Configurar o Uso da Biometria no SIGAMDT](https://tdn.totvs.com/display/PROT/MDT0113+Configurar+o+Uso+da+Biometria+no+SIGAMDT)[Como configurar o uso da Biometria no SIGAMDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11169895277207)  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
