---
article_id: 360055230453
category: REQUISIÇÕES
content_hash: 0ed02a9d0fc175447025f10befb32433f0598569221e5f2e17168bb19051f3f9
fetched_at: '2026-06-28T22:44:37.670596+00:00'
product: protheus
section_id: 10299632459799
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como configurar o E-mail de Workflow de solicitações
  do MEU RH
type: support-article
updated_at: '2025-09-16T17:11:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055230453-RH-Linha-Protheus-MEU-RH-Como-configurar-o-E-mail-de-Workflow-de-solicita%C3%A7%C3%B5es-do-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19448576054295)Tempo aproximado para leitura: 00:05:00 min****Dúvida**Como configurar o E-mail de *Workflow* de solicitações do MEU RH?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – Todas às versões  
  
**Solução**Para configurar o E-mail de *Workflow* de solicitações do MEU RH é necessário que verifique todos os passos indicados abaixo.  
 **IMPORTANTE: O Workflow é um E-mail disparado para as solicitações realizadas através do MEU RH que seguem um fluxo de hierarquia de aprovação, esse E-mail serve somente como acompanhamento e não executa aprovações, sendo necessário que o Usuário acesse o MEU RH para aprovar ou reprovar as solicitações.**  
Abaixo trazemos um passo a pass*prints* o com dessa configuração levando em consideração o provedor de *E-mail Office365*. Porém, neste caso você deve consultar internamente em sua Empresas as informações do seu provedor de E-mail e ajustar essa configuração.

**1º Passo:** Grave os arquivos **Awfsolicportal.html** e **Wfsolicportal.html** na pasta *Workflow* existente dentro da Protheus\_Data.  
  
**OBSERVAÇÃO:** Esses arquivos são baixados junto aos arquivos *WEB* disponível na Central de *Downloads* da TOTVS e normalmente ficam dentro da pasta PP. Uma cópia dos arquivos **Awfsolicportal.htm**l e **Wfsolicportal.html** está anexada a esse artigo, se necessário, basta clicar no link disponível no final deste artigo para realizar o download.  
  
**2ª Passo:** Através do Configurador (SIGACFG) acesse as opções "Ambiente > *Workflow* > Contras de E-mail" e cadastre seu E-mails com as informações do seu provedor de E-mail, conforme exemplo abaixo:  
​![B04Yg5JYac.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500010179061)​

**3º Passo:** Caso esteja tudo certo na sua configuração, quando realizar uma Solicitação no MEU RH, que segue um fluxo de hierarquia de aprovação, será enviado um *E-mail* ao destinatário cadastrado no cadastro Funcionário (SRA) e no Participante (RD0) da Matrícula Responsável do departamento do Solicitante informando a pendência para análise.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091349253)​  
  
Caso a Matrícula Responsável ou o RH reprove a solicitação será enviado um *E-mail* ao destinatário cadastrado no cadastro Funcionário (SRA) e no Participante (RD0) do Solicitante.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091349333)  
  
Para entender o fluxo de hierarquia de aprovação das solicitações do MEU RH verifique os artigos relacionados abaixo:  
  
**[MP - MEU RH - Como funciona os Níveis e Fluxo de aprovação de Solicitações Sem Visão?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044589134)**  
**[MP - MEU RH - Como funciona os Níveis e Fluxo de aprovação de Solicitações Com Visão?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047331074)**  
​  
**OBSERVAÇÃO:** No caso do específico do provedor de *E-mail GMAIL* pode ocorrer o erro abaixo, para isso você deverá seguir as próprias instruções do *Google* e habilitar os *APPs* menos seguros na configuração de Segurança do *GMAIL*, lembrando que cada provedor de E-mail pode ter suas particularidades:  
  
![](https://totvssuporte.zendesk.com/attachments/token/wz85SuaRz0v6CMej8PceMzQGS/?name=inline-1229320738.png)​  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19448582282647)  
  
**IMPORTANTE**:  
Se houver erros no disparo do e-mail, neste processo do Esqueceu a Senha pelo Meu RH, e para trazer, ao Suporte uma evidência, com um nível de detalhamento nos *logs* gerados no **MEU RH** é necessário adicionar uma chave na sessão [*MAIL]* chamada *VERBOSE=1* no arquivo de configuração ***appserver.ini do MEU RH*****:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19448576061591)  
  
Segue abaixo, um pouco mais sobre este chave a ser inserida:  
**[Como evidenciar nos logs elementos de disparo de e-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19429764987159)**  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)  
  
**Seguem os arquivos Awfsolicportal.html e Wfsolicportal.html:**
