---
article_id: 360044227453
category: LOGIN
content_hash: 60cb5b83bbba305792abe99fd1a7c85d4642fa018da1bc2bee3c24c426c0403c
fetched_at: '2026-06-28T22:44:40.687187+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Configuração para Login no MEU RH
type: support-article
updated_at: '2025-12-16T11:57:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044227453-RH-Linha-Protheus-MEU-RH-Configura%C3%A7%C3%A3o-para-Login-no-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30646903615255) Tempo aproximado para leitura: 00:03:00 min**  
  
**Dúvida**  
Configuração para Login no MEU RH  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
O processo detalhado da configuração está disponível na [**Documentação de Referência do MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421).  
  
Cadastre todos os usuários informados abaixo atentando-se às particularidades informadas em cada passo desta documentação.   
  
Mesmo que sua Empresa já utilize o Portal de Gestão de Capital Humano é importante que valide as informações abaixo devido algumas configurações novas que não eram necessárias no portal GCH e se necessário, redefinir os acessos de seus Usuários.  
  
Abaixo deixamos disponíveis uma série de vídeos que foram publicados no canal do YouTube [**TOTVS Soluções**](https://www.youtube.com/channel/UChsYWCL7MFkDM4OsK7de8dw) referente a configuração dos Usuários para acesso ao MEU RH:  
  
Parte 1: Configuração do Usuário Protheus, configuração do Usuário do Portal e configuração de permissões de acesso.  
[**RH - Linha Protheus - MEU RH - Como cadastrar um Usuário do Protheus via Configurador para acesso ao MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729194)  
[**RH - Linha Protheus - MEU RH - Como associar o Usuário do Protheus ao Usuário do Portal para acesso ao MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043730394)  
  
  
  
Parte 2: Configuração do Participante, relacionamento de participantes e configuração de acesso para Autônomos/PJ e de demitidos.  
[**RH - Linha Protheus - MEU RH - Como associar o Usuário do Portal ao Cadastro de Participante para acesso ao MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043731394)  
  
Parte 3: Configuração do LOGIN e SENHA para acesso ao MEU RH.  
[**RH - Linha Protheus - MEU RH - Como “Iniciar usuário” e “Gerar Senhas” para o primeiro acesso ao MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044236953)  
  
Parte 4: Configuração para reset ou alteração de senhas já criadas  
[**RH - Linha Protheus - MEU RH - Quais são as formas de alterar a senha de acesso ao MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004233282)  
  
**ATENÇÃO:** Certifique-se sempre de estar com seu ambiente atualizado, pois são disponibilizados periodicamente atualizações com melhorias e correções no MEU RH.  
[**RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
[**RH - Linha Protheus - MEU RH - Pacote de acumulado do RH no Portal de Cliente**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282)  
  
**IMPORTANTE:**  
O campo RD0\_LOGIN ele **somente é preenchido**, se a Empresa vier **migrada do Portal GCH para o Meu**  
**RH**, porém para os novos funcionários, o campo NÃO é preenchido, somente **se num primeiro acesso ao Portal GCH**, nem no App Meu RH, o usuário opta pelo **login unificado**, com isso, o RD0\_LOGIN é composto pelo login unificado que ele escolher.  
  
Veja mais em:  
[RH - Linha Protheus - PORTAL GCH - Como alterar o login do usuário no Portal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046023853-RH-Linha-Protheus-PORTAL-GCH-Como-alterar-o-login-do-usu%C3%A1rio-no-Portal)  
  
Pela rotina do módulo 18, não temos como alterar esse campo mais, porque **o Meu RH não utiliza esse campo de forma padrão**. O Meu RH até considera esse campo, caso ele já tenha conteúdo, mas não tem como preencher ele mais de forma padrão, se o funcionário só usar o Meu RH.  
  
O Sistema sempre, irá utilizar para **login no Meu RH uma sequência condicional**:   
*login* se tiver **RD0\_LOGIN**  
se não tiver, *login* utilizando **RD0\_CIC**  
se não tiver, *login* utilizando **RD0\_EMAIL**  
  
Isso porque, se preencher d**e qualquer outra forma o campo RD0\_LOGIN, ou vier migrado do Portal GCH**, ele pode usar o mesmo conteúdo do campo *login* para acessar o Meu RH também.  
  
Orientamos sempre, realizar a operação de "Iniciar Usuário", que limpa esse campo, no módulo SIGATCF.  
Veja nossa documentação sobre: [RH - Linha Protheus - MEU RH - Como “Iniciar usuário” e “Gerar Senhas” para o primeiro acesso ao MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044236953-RH-Linha-Protheus-MEU-RH-Como-Iniciar-usu%C3%A1rio-e-Gerar-Senhas-para-o-primeiro-acesso-ao-MEU-RH?source=search)  
  
Abaixo, compartilhamos dois vídeos compartilhados no canal da TOTVS no *Youtube*, dos quais demonstram o passo a passo do que deverá ser realizado.  
***How To*** **| MEU RH Como corrigir o vínculo do participante - Parte 1/2**  
<https://youtu.be/SjH-bc_pTac>   
***How To*** **| MEU RH Como corrigir o vínculo do participante - Parte 2/2**  
<https://youtu.be/n6vBE8ZSn0w>   
  
**Dúvidas Frequentes**  
[**RH - Linha Protheus - MEU RH - Como relacionar os Participantes**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050255013)  
[**RH - Linha Protheus - MEU RH - Como trocar a senha inicial**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050094714)  
[**RH - Linha Protheus - MEU RH - Como configurar o Esqueceu a Senha do MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052543934)  
[**RH - Linha Protheus - MEU RH - Configuração de permissão de acesso as funcionalidades e menu do MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033892693)  
  
**Saiba Mais:**  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referência sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
