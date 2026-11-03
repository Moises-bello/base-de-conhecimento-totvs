---
article_id: 360024700493
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: d50a18a7c168ba1e5232ed6498e2f35014e3c8e7c77fcfa3fae05e815bb95bb5
fetched_at: '2026-06-28T22:47:29.560690+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Como instalar e configurar o Meu RH
type: support-article
updated_at: '2025-09-12T19:15:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024700493-RH-RM-Meu-RH-Como-instalar-e-configurar-o-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05:17 min**

**Dúvida**Como instalar e configurar o *app* **Meu RH**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.17  
  
**Solução**Depois de instalar a Biblioteca RM, baixe o TOTVS RM Portal e siga os passos abaixo para instalar com sucesso o *app* **Meu RH.**  
  
**Requisitos:**Para acesso via aplicativo Meu RH:

* *Android* 5.0 ou superior.
* *iOS* 9.0 ou superior.

 A instalação poderá ser **Completa ou Personalizada.**

* **Completa:** O sistema irá instalar todos os portais: Meu RH , Novo portal do aluno e Novo portal do processo seletivo, onde ambos serão instalados automaticamente.

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360037782574/1.png)

* **Personalizada:** Será instalado o portal específico, isso é, o usuário irá selecionar qual Portal que deseja instalar, entre eles estão o Meu RH, Novo portal do aluno, Novo portal do processo seletivo e o Novo portal do Cliente - Incorporação Imobiliária.

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360037782614/2.png)

**Para ambas instalações, seguir o mesmo procedimento:**

**1.** Após a instalação, irá instalar a estrutura do *Corpore.NET* (Referente ao antigo portal) e a estrutura da *FrameHTML* (Referente a instalação dos novos portais). Essa pasta tem como finalidade guardar as instalações dos novos portais devido a alteração da tecnologia utilizada para o desenvolvimento.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002333981/mceclip1.png)

**Importante:**  
Validar de forma correta a porta e o nome do servidor caso não for utilizar *localhost.*

**2.**Configurar a URL do portal na *FrameHTML* em: **Totvs Folha de Pagamento | Ambiente | Parâmetros | Parâmetros Globais | *FrameHTML.***

**3.**No campo **Defina o endereço da *FrameHTML*** inserir o endereço: [http://LOCAL\_DE\_INSTALAÇÃO:PORTA](http://xn--local_de_instalao-nqb9eporta/)  
  
**4.** Siga as instruções de alterações para o arquivo **Web.config** conforme demonstrado na seção [Meu RH - Acesso web (via desktop)](http://tdn.totvs.com/pages/releaseview.action?pageId=287049983)**5.** Após a configuração, acessar o novo portal através do link [Http://LOCAL\_DE\_INSTALAÇÃO:PORTA/web/app/RH/PortalMeuRH](http://xn--local_de_instalao-nqb9eporta/)  
  
**6.** Para realizar o primeiro acesso, basta seguir os passos do documento [Como realizar o primeiro acesso ao Meu RH via Mobile?](http://tdn.totvs.com/pages/releaseview.action?pageId=465385586)

O Meu RH depende que o recurso de manipulação URL’s sem extensão definida esteja disponível no IIS (utilizado para funcionamento dos serviços REST). Contudo, identificamos que algumas versões do IIS não vem com suporte a tal recurso instalado por padrão, impossibilitando o funcionamento da aplicação.  
Caso tenha algum problema de funcionamento após sua instalação, a Microsoft lançou um *hotfix* de atualização do IIS para habilitar tal recurso. Link para download: [clique aqui](https://support.microsoft.com/en-us/help/980368/a-update-is-available-that-enables-certain-iis-7-0-or-iis-7-5-handlers).
