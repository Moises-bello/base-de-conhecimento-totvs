---
article_id: 16786087683351
category: TAE
content_hash: ae05531ad5640ac1d78abc3b9d69958339a95ca6a397fe52ad73a7c92aaee8bd
fetched_at: '2026-06-28T22:44:30.145562+00:00'
product: protheus
section_id: 32238506930583
source: central-protheus
title: RH - Linha Protheus - MEU RH - Integração da ferramenta TAE com o Meu RH para
  assinatura de documentos
type: support-article
updated_at: '2025-12-05T16:23:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16786087683351-RH-Linha-Protheus-MEU-RH-Integra%C3%A7%C3%A3o-da-ferramenta-TAE-com-o-Meu-RH-para-assinatura-de-documentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16786121058327) Tempo aproximado para leitura: **06:00 min**  
  
**Dúvida**  
**Integração** da ferramenta **TAE (TOTVS Assinatura Eletrônica)** com o **Meu RH**, para **assinatura digital de documentos**  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**  
O App Meu RH passa a integrar com o [**TAE - TOTVS Assinatura Eletrônica**](https://produtos.totvs.com/ficha-tecnica/tudo-sobre-o-totvs-assinatura-eletronica/), de forma que os usuários poderão realizar **assinaturas eletrônicas nos documentos** a serem disponibilizados por essa plataforma.  
  
Para a integração **com o TAE,** obrigatoriamente deverá ter configurado o [**protocolo SSL**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042649133-RH-Linha-Protheus-MEU-RH-Como-configurar-o-SSL-HTTPS-para-o-MEU-RH), caso contrário o TAE não aceitará as requisições vindas de um protocolo sem SSL.  
  
Inicialmente, via módulo 18 - SIGATCF do Protheus, habilitar **na rotina Permissões Meu RH**, as liberações da Assinatura Eletrônica:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16788603980055)  
  
Parâmetros a serem configurados:  
**MV\_SIGNURL** - possibilitar a integração do Protheus com o TAE  
Conteúdo padrão do campo: [https://totvssign.totvs.app/](https://totvssign.staging.totvs.app/)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16788768583447)  
  
**MV\_RHTAEUS** e **MV\_RHTAEPW**, estes dois parâmetros são, respectivamente, **o usuário e a senha** de um acesso cujo possui a permissão para subir os documentos no **TAE**.  
  
IMPORTANTE:  
Os parâmetros **MV\_RHTAEUS** e **MV\_RHTAEPW**devem ter os valores armazenados de forma criptografada, e por esse motivo eles **não podem ser preenchidos** por meio do módulo **Configurador**.  
  
A configuração desses parâmetros **deverá ser feita** por qualquer uma dessas rotinas abaixo:

* SIGAGPE / Miscelânea / Cálculos / Férias, no menu Outras Ações terá a opção **Config. Assina. Eletr.**
* SIGAPON / Atualizações / Lançamentos / Controle de Espelho de Ponto, no menu Outras Ações terá a opção **Config. Assina. Eletr.**

No cadastro do funcionário deverá estar vinculado o *e-mail*, que terá acesso ao TAE e que fora configurado no parâmetro **MV\_RHTAEUS**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16789120649879)  
  
Com todas as amarrações e cadastros, será possível, **o** ***login*** **na Plataforma TAE**, através:  
- do *link* configurado no parâmetro **MV\_SIGNURL**  
- do *e-mail* de usuário cadastrado no parâmetro **MV\_RHTAEUS**  
- da senha deste usuário cadastrada no parâmetro **MV\_RHTAEPW**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16789159705495)  
  
Com isso, **ao logar na Plataforma TAE**, será possível **o envio do documento para um funcionário** realizar a assinatura pelo App Meu RH, via *web* ou celular.  
  
Ao clicar em Adicionar Documentos, abrirá a tela abaixo para um título do documento e **seleção de um arquivo de texto gravado no computador.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16789472246551)  
  
Após a visualização em tela do documento, escolher o **destinatário** que o receberá para assinar. **Necessariamente** o **destinatário** do documento precisa possuir em seu **Cadastro de Funcionário**, no **Protheus**, o preenchimento do campo *e-mail*:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16789595969943)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16789659864727)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16789733841559)  
  
Ao logar no Meu RH, o usuário receberá um alerta que possui um documento pendente para assinatura.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16789777990551)  
  
Ao clicar, o usuário terá a opção de **Acessar o Documento** inserido pela Plataforma TAE e, **assinar eletronicamente**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16789817742487)  
  
Digitar o código de verificação de 6 dígitos que, a Plataforma TAE enviará ao *e-mail*:  
  
*![](https://centraldeatendimento.totvs.com/hc/article_attachments/16789868009111)*  
  
Selecione a opção "**Declaro que li e estou de acordo**" e clicar no botão **Assinar**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16789937185943)  
  
Para realizar a integração do **espelho de ponto, aviso de férias e recibo de férias com o Meu RH** acessar os *links* abaixo:  
  
- integração do **Espelho de ponto, gerado no módulo 16 - SIGAPON, diretamente com o Meu RH via TAE**, acessar o *link* abaixo:  
[Como assinar eletronicamente o espelho de ponto que foi gerado pelo SIGAPON no Meu RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22217150879895)  
  
- integração do **Aviso de férias/Recibo de férias, gerados no módulo 07 - SIGAGPE com Meu RH via TAE**, acessar o *link* abaixo:  
[Como assinar eletronicamente o aviso de férias que foi gerado pelo SIGAGPE no Meu RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22220915685399)

**Saiba Mais**  
[**Integração Meu RH x TAE - Protheus**](https://tdn.totvs.com/pages/viewpage.action?pageId=741337177)  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
