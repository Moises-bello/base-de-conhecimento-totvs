---
article_id: 360050238493
category: LOGIN
content_hash: 8ada08de7195e12c20692fbe8b96cc48b71df0c5d7499169fde4e417eb438588
fetched_at: '2026-06-28T22:44:40.648031+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - O que fazer quando não consigo acessar o MEU
  RH
type: support-article
updated_at: '2025-12-23T16:51:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050238493-RH-Linha-Protheus-MEU-RH-O-que-fazer-quando-n%C3%A3o-consigo-acessar-o-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23861944975511)Tempo aproximado para leitura: 00:05:00 min**  
  
**Dúvida**  
O que fazer quando não consigo acessar o MEU RH?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – Todas às versões  
  
**Solução**  
Há diferentes situações que podem causar erro ao tentar acessar o MEU RH, segue abaixo alguns exemplos e como proceder para tratá-los:  
  
**1- PROBLEMA NO USUÁRIO -** No momento em que é preenchido o Login e Senha é apresentado alguma das mensagens abaixo:  
  
1.1- **Login Inválido:** Esse problema ocorre quando é digitado o usuário ou senha incorretos, em muitos casos mapeados, deve ser verificado se foi vinculado o usuário do portal (RD0\_PORTAL) e filial do usuário do portal (RD0\_FILRH) no cadastro de participantes.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8821203860887)  
  
**Para saber mais sobre as amarrações de usuários acesse:**  
[MEU RH - Amarrações de usuários](https://tdn.totvs.com/pages/viewpage.action?pageId=497469540#Passosparaconfigura%C3%A7%C3%A3o-1)  
  
**OBS:** Na situação da mensagem acima o problema normalmente está na configuração do Usuário, é necessário avaliar as configurações do artigo abaixo, na maioria dos casos é a falta de alguma permissão ou de algum relacionamento entre os Usuários necessários para o acesso ao MEU RH.  
  
[**RH - Linha Protheus - MEU RH - Configuração para Login no MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044227453)  
  
1.2 **- Usuário sem acesso à empresa/filial:** Neste caso é necessário verificar o usuário do Protheus criado via Configurador (SIGACFG) pois, na opção Restrições de acessos e filiais deverá ser marcado para acesso à todas as empresas, assim como para todos os ambientes e possuir todos os acessos marcados.  
  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8866117918103)**  
  
**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8866515154455)**  
  
**Para saber mais sobre a configuração do usuário no SIGACFG acesse:**  
[**RH - Linha Protheus - MEU RH - Como cadastrar um Usuário do Protheus via Configurador para acesso ao MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729194)  
  
1.3 - **Mensagens no console.log:** *Login* inválido é apresentado mensagem informando que usuário informado esta incorreto.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8821212503575)  
  
**2- PROBLEMA NA CONFIGURAÇÃO DO AMBIENTE -** No momento de preencher o *Login* e a Senha é apresentado alguma das mensagens abaixo:  
  
2.1- **Tela em branco:** A tela em branco está associado a configuração incorreta do arquivo **properties.json**, normalmente as informações do ***rootContext*** ou o **contexto** na *URL* do **REST** foram preenchidos incorretamente e fora do padrão.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8821976188311)  
  
**Para saber mais sobre a configuração do properties.json acesse:**  
[RH - Linha Protheus - MEU RH - Qual deve ser o conteúdo do arquivo PROPERTIES.JSON](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049493314-RH-Linha-Protheus-MEU-RH-Qual-deve-ser-o-conte%C3%BAdo-do-arquivo-PROPERTIES-JSON?source=search)  
[RH - Linha Protheus - MEU RH - Como configurar o APPSERVER.INI, PROPERTIES.JSON e URL do QRCODE para acesso ao MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044715514-RH-Linha-Protheus-MEU-RH-Como-configurar-o-APPSERVER-INI-PROPERTIES-JSON-e-URL-do-QRCODE-para-acesso-ao-MEU-RH?source=search)  
  
2.2- **Servidor não está respondendo:** Essa mensagem ocorre pois o MEU RH não está conseguindo localizar o serviço **REST** ou está fora indisponível, nesse caso será necessário verificar se o *REST* está ativo e verificar se foi configurado corretamente os endereços de acesso no **appserver.ini e** ***properties.json*****.**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8822162948503)  
  
2.3- ***Internal Server Error*****:** Normalmente o "*Internal Server Error*" está associado com alguma configuração incorreta no appserver.ini, como por exemplo a tag ***PrepareIn*** ou no arquivo ***properties.json*** na *tag **rootContext.***  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8822258256535)  
  
**Para saber mais sobre a configuração do appserver.ini acesse:**  
[**RH - Linha Protheus - MEU RH - Como configurar o APPSERVER.INI, PROPERTIES.JSON e URL do QRCODE para acesso ao MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044715514-RH-Linha-Protheus-MEU-RH-Como-configurar-o-APPSERVER-INI-PROPERTIES-JSON-e-URL-do-QRCODE-para-acesso-ao-MEU-RH?source=search)  
  
2.4- **Ocorreu um erro ainda não conhecido. Entre em contato com o suporte:**  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019525901)  
  
2.5- **The server Can't find The Resquested:**  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074201714)  
  
**OBS:** Na situação das mensagens acima o problema normalmente está na configuração do Ambiente do MEU RH,  é necessário avaliar as configurações conforme artigo abaixo, na maioria dos casos é falha na configuração através do [APWebWizard ou SRVWizard](https://tdn.totvs.com/display/public/NPR/Passo+3%3A+Configurando+REST), então sugerimos que revise e faça a manutenção diretamente através nos arquivos ***APPSERVER.INI e PROPERTIES.JSON**.*  
[**RH - Linha Protheus - MEU RH - O que devo configurar para acessar o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050243093)  
  
**Caso o erro persista**, abra um Ticket ao time de Suporte, e para uma análise assertiva é importante que descreva corretamente seu cenário e encaminhe evidências, segue abaixo informações que auxiliam na análise:

1. [Arquivo com a data de suas rotinas do RPO do MEU RH](https://tdn.totvs.com/x/nYPxF);
2. [Data dos arquivos do portal MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059194334);
3. Arquivos APPSERVER.INI e PROPERTIES.JSON, deixe claro qual é o endereço interno e externo, quantos arquivos do portal você tem e o endereço que está realizando o teste;
4. [Arquivo Console.log demonstrando a tentativa de autenticação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416746889751);
5. Informe se o erro ocorre com todos Usuários ou somente para algum específico;
6. Informe se o erro ocorre no acesso via Navegador, Celular, ou em ambos;
7. Se for o caso, print da configuração do Ambiente e URL (*Qrcode*) do aparelho Celular;
8. Se o problema só ocorrer no celular, informe o modelo e versão do Sistema Operacional do aparelho e a versão do app MEU RH instalada.

**ATENÇÃO:** Certifique-se sempre de estar com seu ambiente atualizado, pois são disponibilizados periodicamente atualizações com melhorias e correções no MEU RH.  
[**RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
[**RH - Linha Protheus - MEU RH - Pacote de acumulado do RH no Portal de Cliente**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282)  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
