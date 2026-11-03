---
article_id: 32581645799063
category: RH - Smart View
content_hash: 12a92b0490ca525b872069aca4b50a833d05dcd3d65ce0995d0effbac49ab27f
fetched_at: '2026-06-28T22:43:08.017413+00:00'
product: protheus
section_id: 30156203821463
source: central-protheus
title: RH - Linha Protheus - GPE - Como criar Restrição/Privilégio para relatórios
  Smartview
type: support-article
updated_at: '2026-04-23T19:24:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32581645799063-RH-Linha-Protheus-GPE-Como-criar-Restri%C3%A7%C3%A3o-Privil%C3%A9gio-para-relat%C3%B3rios-Smartview
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32581683849367) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como criar Restrição/Privilégio para acesso aos relatórios Smartview?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para **permitir ou bloquear o acesso** de usuários aos **relatórios Smartview**, é necessário criar um **Privilégio** para liberar o acesso aos Objetos de Negócio Nativos (fontes do Smartview) e rotinas do módulo através do Configurador, e vincular este Privilégio ao usuário ou grupo de usuários.   
Existe a possibilidade de definir estes acessos para todos os relatórios do Smartview, ou apenas os que forem necessários, conforme os passos abaixo:  
  
**1 -** Acesse o **Configurador > Usuário > Senhas > Privilégios > Incluir.**  
Na coluna **Transação/Rotina**, após dar um duplo clique, selecione em **Menu** a opção **Smartview** e localize o relatório que precisa:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32581645758743)  
  
  
  
**2 -** Após selecionar o relatório que precisa, na coluna **Acesso** o Administrador pode escolher pelas opções **[Permitido/Não Permitido/Negado conforme conceito do Framework](https://tdn.totvs.com/pages/releaseview.action?pageId=271389653).**  
Esta ação **libera/bloqueia** inicialmente o acesso ao **Objeto de Negócio Nativo**, que se trata do **fonte do Smartview:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32581645759511)  
  
  
  
**3 -** Após definir quais Objetos de Negócio terão acesso Permitido, **é necessário também liberar o acesso às rotinas de relatório específicas do módulo**, por exemplo: para o relatório de **Afastamentos**, é preciso liberar o acesso a rotina **GPERSV580** **que se trata do fonte do relatório Protheus/RH**, e também **rotinas correlatas usadas na impressão do relatório**, neste caso, pensando nos *lookups* (filtros) que precisam de preenchimento, é necessário liberar acesso nas rotinas GPEA240 (Processos) e GPEA430 (Tipos de Ausências). Estas inclusões podem ser feitas manualmente digitando o fonte da rotina ou dando um duplo clique > Menu Gestão de Pessoal > buscar pela rotina:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32581645762327)  
  
  
  
**4 -** Após cadastrar o **Privilégio**, você pode **vincular** ele ao cadastro de um **usuário** específico ou a um **grupo de usuários**. Neste cenário de teste, o vínculo será feito em um grupo de usuários através do menu Usuários > Senhas > Grupos > posicionar sobre o grupo e clicar em Outras Ações > Privilégios > na coluna Regra selecionar o Privilégio cadastrado. Você pode definir uma data de validade ou para quais grupos de empresa/filiais ele será válido. Caso não queira que o Privilégio expire e que ele seja válido para qualquer grupo/filial, basta deixar os campos em branco:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32587734584215)  
  
  
  
**5 -** Por fim, verifique se no cadastro do usuário em **Usuários > Senhas > Usuários**, o grupo que o Privilégio foi vinculado consta na aba Grupos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32587748392343)  
  
  
  
**6 -** Quando for feito acesso ao Protheus com o usuário vinculado ao Privilégio, o relatório de Afastamentos será impresso normalmente:![](https://centraldeatendimento.totvs.com/hc/article_attachments/32587734589591)  
  
  
O relatório **Recibo de Pagamento** que foi configurado para que o **usuário não tenha acesso**, após o preenchimento dos parâmetros **vai exibir em tela que o usuário não possui acesso ao Objeto de Negócios:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32587748397079)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32587748406551)  
  
  
Para carregar todos os relatórios Smartview na rotina de Privilégios de uma única vez, clique em **Incluir > Outras Ações > Menu > Avançar > selecione o menu SMARTVIEW > Finalizar**. Após isso, basta seguir as mesmas configurações citadas a partir do passo 2.  
  
  
**Saiba Mais:**  
[Controle de Privilégios nos Objetos de Negócio Nativos](https://tdn.totvs.com/pages/releaseview.action?pageId=830953329)  
[Configurar Privilégio para controlar acesso a rotinas](https://tdn.totvs.com/pages/releaseview.action?pageId=271389653)  
[Página Centralizadora - Recursos Humanos | Protheus - SmartView](https://tdn.totvs.com/display/public/PROT/Recursos+Humanos+%7C+Protheus+-+SmartView)
