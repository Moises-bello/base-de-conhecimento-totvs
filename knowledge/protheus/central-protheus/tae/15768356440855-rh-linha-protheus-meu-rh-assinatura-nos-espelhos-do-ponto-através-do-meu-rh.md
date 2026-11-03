---
article_id: 15768356440855
category: TAE
content_hash: 1899e2eaf8ea33058f88556e677233d604e55f6190a9d07d692a0eac363a2075
fetched_at: '2026-06-28T22:44:30.106152+00:00'
product: protheus
section_id: 32238506930583
source: central-protheus
title: RH - Linha Protheus - Meu RH - Assinatura nos Espelhos do Ponto através do
  Meu RH
type: support-article
updated_at: '2025-09-16T17:12:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15768356440855-RH-Linha-Protheus-Meu-RH-Assinatura-nos-Espelhos-do-Ponto-atrav%C3%A9s-do-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15768333066007) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Assinatura nos Espelhos do Ponto através do Meu RH  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**Possibilita ao usuário, visualizar e realizar assinatura de documentos utilizando a integração com a plataforma **TAE - TOTVS Assinatura Eletrônica.**Para o correto funcionamento da Integração, **o servidor que hospeda o aplicativo do MEU RH deve estar apto a realizar requisições aos seguintes endereços:**

* <https://totvssign.staging.totvs.app/>
* [https://totvssign.totvs.app/](https://totvssign.totvs.app)

Ao selecionar o menu Assinatura eletrônica será possível visualizar o *DashBoard* de documentos do colaborador logado no Meu RH, **visualizar e realizar a assinatura de um determinado documento.**Abaixo, segue documentação de três parâmetros que precisarão ser configurados para utilização dessa integração entre o TAE x Meu RH:  
<https://tdn.totvs.com/pages/viewpage.action?pageId=741337177>  
  
Os parâmetros **MV\_RHTAEUS** e **MV\_RHTAEPW**devem ter os valores armazenados de forma criptografada, e por esse motivo eles não podem ser preenchidos por meio do módulo Configurador.   
  
A configuração desses parâmetros deverá ser feita por qualquer uma dessas rotinas abaixo:

* SIGAGPE / Miscelânea / Cálculos / Férias, no menu Outras Ações terá a opção **Config. Assina. Eletr.**
* SIGAPON / Atualizações / Lançamentos / Controle de Espelho de Ponto, no menu Outras Ações terá a opção **Config. Assina. Eletr.**

Importante, no cadastro do funcionário deve esta vinculado o *e-mail*.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15767926256791)  
\*\*\* Utilize sempre o *e-mail* com letras minúsculas e, sem espaço após o final do endereço.  
  
**Orientações para inclusão manual de Documento TAE**Acessar a Plataforma do TAE com a conta do Publicador.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15768023521431)  
  
Clicar no botão adicionar documento, preencher o envelope, incluir o anexo e clicar no botão próxima etapa.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15768039695255)

Em seguida clicar no botão "Novo destinatário"  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15768047716631)  
  
IMPORTANTE:  
**O *E-mail* informado deve ser o mesmo utilizado no cadastro de funcionário.**  
Clicar em **Autenticação** = **Enviar código por** ***e-mail;***Preencher as demais informações e clicar em **Incluir** e, em seguida, **Enviar Documento**.  
  
Neste momento, quando o usuário logar no Meu RH, conseguirá verificar o documento para assinatura.  
Ao realizar a solicitação de assinatura pelas funções de **geração do espelho de ponto**, **recibo e aviso de férias,** dentro do Protheus, **ainda não será possível a visualização pelo Meu RH**, a publicação do documento, somente terá acessibilidade se for feito pela plataforma TAE com o tipo de autenticação (Enviar código via e-mail).  
  
Para a integração com o TAE (TOTVS Assinatura Eletrônica) **obrigatoriamente deverá ter o protocolo SSL configurado**, caso contrário o TAE não aceitará as requisições vindas de um protocolo sem SSL.  
  
**Saiba mais:**  
**Informações sobre o TAE, clique [aqui](https://produtos.totvs.com/ficha-tecnica/tudo-sobre-o-totvs-assinatura-eletronica/)  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
