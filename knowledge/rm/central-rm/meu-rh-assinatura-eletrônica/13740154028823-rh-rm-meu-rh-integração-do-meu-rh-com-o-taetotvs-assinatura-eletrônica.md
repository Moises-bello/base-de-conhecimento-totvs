---
article_id: 13740154028823
category: Meu RH - Assinatura Eletrônica
content_hash: 467802b0f1ed822c7a82763f9c8fd3989d8e4bd82c0ce214629eaffc9e0289e1
fetched_at: '2026-06-28T22:47:28.768737+00:00'
product: rm
section_id: 19399655101335
source: central-rm
title: RH - RM - Meu RH - Integração do Meu RH com o TAE(Totvs Assinatura Eletrônica)
type: support-article
updated_at: '2026-03-03T19:50:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13740154028823-RH-RM-Meu-RH-Integra%C3%A7%C3%A3o-do-Meu-RH-com-o-TAE-Totvs-Assinatura-Eletr%C3%B4nica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19040509488791) Tempo aproximado para leitura: **00:07:54 min**  
  
**Dúvida**  
Como configurar a integração do Meu RH com o TAE (Totvs Assinatura Eletrônica).  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.2302.164

**Solução**  
Com o avanço da tecnologia, a digitalização de documentos tornou-se uma tendência irreversível. As empresas já não podem prescindir da agilidade proporcionada pelos sistemas digitais, e isso inclui a geração e a armazenagem de todo tipo de documentos.

O TOTVS Assinatura Eletrônica é uma plataforma centralizada para gestão e execução de assinaturas eletrônicas, e oferece total segurança e validade jurídica aos documentos.

[Saiba mais sobre o TAE clicando aqui.](https://produtos.totvs.com/ficha-tecnica/tudo-sobre-o-totvs-assinatura-eletronica/)

**Permissões:**  
**Sistema: Folha de Pagamento / 19 - Portal RH (Portal) /  19.05  -  TOTVS Assinatura Eletrônica**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13739264720919)**  
  
**Parametrização:**  
1 - Acesse sistema **RM/ aba ambiente / parâmetros / parâmetros globais / item 30 " Integração com Totvs assinatura eletrônica".**

![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-16_16-9-34.png?version=1&modificationDate=1673896174937&api=v2)

**URL de Autenticação** .: [https://totvssign.totvs.app/identityintegration](https://totvssign.staging.totvs.app/identityintegration)

**URL da API de integração** .: [https://totvssign.totvs.app](https://totvssign.staging.totvs.app/)

**URL de login via formulário web** .: [https://totvssign.totvs.app/webapptotvssign/#/auth/login?external=true](https://totvssign.staging.totvs.app/webapptotvssign/#/auth/login?external=true)

**Usuário de Serviço** : [x](mailto:marcelo.vieira@totvs.com.br)xxx

**Senha do usuário de serviço** : xxxx

![](https://tdn.totvs.com/download/attachments/733186927/image2023-3-27_17-25-46.png?version=1&modificationDate=1679948782960&api=v2)

Modulo **Folha de Pagamento / aba configurações / parametrizador / RM Portal / Totvs assinatura eletrônica.**  
  
Nesta Etapa cadastre o usuário que será responsável pela publicação e envio do documento no TAE(Totvs assinatura eletrônica).

Usuário Publicador xxxxx@xxxxx.com

Senha Usuário Publicador xxxxxxxxxxxxxx

![](https://tdn.totvs.com/download/attachments/733186927/image2023-3-3_10-3-28.png?version=1&modificationDate=1677848609207&api=v2)

**Importante:** O usuário inserido no grupo de quiosque do modulo folha de pagamento tem obrigatoriamente que estar cadastrado como um usuário publicador no TAE (Totvs assinatura eletrônica).

Para mais informações[Fluxo Administrador TAE(Totvs assinatura eletrônica).](https://tdn.totvs.com/display/public/TAE/Manual+Operacional#deck_gestao--440824956)  
  
No cadastro do funcionário deve estar vinculado o e-mail. O usuário publicador do TAE ira direcionar o documento para ser assinado para o e-mail do funcionário.

![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-16_16-14-26.png?version=1&modificationDate=1673896467183&api=v2)

**Utilizando o Meu RH para Ler e assinar documentos enviados do TAE(Totvs assinatura eletrônica).**

Possibilita ao usuário, visualizar e realizar assinatura de documentos utilizando a integração com a plataforma TAE - TOTVS Assinatura Eletrônica

Para o correto funcionamento da Integração, o servidor que hospeda o aplicativo do MEURH deve estar apto a realizar requisições no seguinte endereço:

* [https://totvssign.totvs.app](https://totvssign.staging.totvs.app/)

**EXEMPLO DE UTILIZAÇÃO**  
Ao selecionar o menu Assinatura eletrônica será possível visualizar o DashBoard de documentos do colaborador logado no MeuRH, visualizar e realizar a assinatura de um determinado documento.

Abaixo vídeo contendo a demonstração da utilização.  
[Demo Review TAE.mkv](https://tdn.totvs.com/download/attachments/733186927/Demo%20Review%20TAE.mkv?version=1&modificationDate=1673955236443&api=v2)

## **TELA DE VISUALIZAÇÃO DO DASHBOARD E LISTAGEM DE DOCUMENTOS**

**![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-13_15-50-17.png?version=1&modificationDate=1673635819573&api=v2)****![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-13_15-52-10.png?version=1&modificationDate=1673635931700&api=v2)****![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-13_15-56-59.png?version=1&modificationDate=1673636220843&api=v2)**

**Principais Campos e Parâmetro**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14438600262807)

## **TELA DE AUTENTICAÇÃO PARA ACESSO AO DOCUMENTO**

**![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-13_15-59-38.png?version=1&modificationDate=1673636380043&api=v2)****![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-16_9-9-29.png?version=1&modificationDate=1673870972277&api=v2)****![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-16_9-9-58.png?version=1&modificationDate=1673871000847&api=v2)****![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-16_9-11-11.png?version=1&modificationDate=1673871074267&api=v2)**

* Caso o usuário tente reenviar o código por e-mail por mais de duas tentativas, será apresentado a informação de Atenção.

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Código Token | Campo alfanumérico que deve ser preenchido com as informações que foram encaminhadas por e-mail. |

Exemplo de E-mail

![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-16_9-26-56.png?version=1&modificationDate=1673872018893&api=v2)

## **TELA PREVIEW, ASSINATURA E DOWNLOAD DO DOCUMENTO**

**![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-13_16-13-49.png?version=1&modificationDate=1673637231027&api=v2)****![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-13_16-14-18.png?version=1&modificationDate=1673637260420&api=v2)****![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-13_16-15-26.png?version=1&modificationDate=1673637343880&api=v2)****![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-13_16-17-0.png?version=1&modificationDate=1673637421857&api=v2)**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| CPF | Caso o usuário publicador (TAE) não tenha informado o CPF, no momento da assinatura o usuário logado no APP será obrigado a informar o CPF |
| Baixar Documento | Caso o usuário logado no App queira realizar o download do arquivo. |
| Declaro que lí e estou de acordo | Somente será habilitado o botão de assinatura caso o usuário logado no App marque esta opção. |

Exemplo de E-mail documento finalizado.

![](https://tdn.totvs.com/download/attachments/733186927/image2023-1-16_10-36-45.png?version=1&modificationDate=1673876207687&api=v2)

**Aviso Importante****:**

* Para a integração com o TAE (TOTVS Assinatura Eletrônica) obrigatoriamente deverá ter o protocolo SSL configurado, caso contrário o TAE não aceitará as requisições vindas de um protocolo sem SSL.

## 

Para mais informações acesse:

* [Manual operacional](https://tdn.totvs.com/display/public/TAE/Manual+Operacional)
* [How to](https://tdn.totvs.com/pages/releaseview.action?pageId=606837574)
* [Documentação das API´S](https://totvs-sign.readme.io/reference/gettings-started)
* [Integrações Totvs Assinatura eletrônica](https://tdn.totvs.com/pages/releaseview.action?pageId=607585319)
* [Integração Meu RH x TAE - RM](https://tdn.totvs.com/pages/viewpage.action?pageId=733186927)
