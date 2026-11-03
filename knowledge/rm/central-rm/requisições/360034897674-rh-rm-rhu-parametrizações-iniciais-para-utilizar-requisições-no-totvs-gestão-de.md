---
article_id: 360034897674
category: Requisições
content_hash: e419d24e595e2300d1d6fac024d89b28e500f1c2da9d9e0dfac1fca6c310c1fd
fetched_at: '2026-06-28T22:47:25.356667+00:00'
product: rm
section_id: 1500000861382
source: central-rm
title: RH - RM - RHU - Parametrizações iniciais para utilizar requisições no TOTVS
  Gestão de Pessoas
type: support-article
updated_at: '2025-09-12T14:59:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034897674-RH-RM-RHU-Parametriza%C3%A7%C3%B5es-iniciais-para-utilizar-requisi%C3%A7%C3%B5es-no-TOTVS-Gest%C3%A3o-de-Pessoas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15864046173719) Tempo aproximado para leitura: 00:02:30 min**

**Dúvida**Como configurar a utilização de requisições no Totvs Gestão de Pessoas (RM Vitae)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - Todas as versões  
  
**Solução**Para configurar o processo de utilização da requisição, confira as orientações descritas nos passos abaixo:

1. Deve ser mapeada a árvore de chefe e supervisor. Para mapear, acesse o menu **Gestão Organizacional | Chefes e Supervisores**.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27466475795351)  
     
   É necessário que, além do cadastro de chefes e supervisores, o usuário envolvido no fluxo da requisição, também tenha um atendente criado no **RM Agilis**. Para isso confira o passo 7.
2. Além da utilização do cadastro de chefes e supervisores padrão, também é possível utilizar o cadastro da Gestão por Hierarquia marcando o parâmetro **Habilita uso da Hierarquia nas Requisições** no parametrizador do módulo.  
     
   Neste caso é possível utilizar ou não o fluxo do Agilis. Para entender melhor, consulte a documentação disponível em '**Saiba Mais**'.
3. As requisições devem estar ativas e com seu mapeamento do fluxo criado.  Para conferir, acesse o menu **Configurações | Tipos de Requisição**. Selecione e edite uma requisição e na aba identificação confira se a flag 'Ativo' está marcada:  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27466475797655)
4. Clique na **Mapeamento Fluxo** e confira se o mapeamento está criado, com os status do parecer **aprovado, reprovado e em andamento:**  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27466475799959)
5. Caso não tenha os tipos de requisições criados, execute o processo 'Acerto nos tipos de Requisição'. Para realizar o processo clique no botão Executar e no campo localizar digite 'Acerto' e em Recursos Humanos clique sobre processo 'Acerto nos tipos de Requisição'.     
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27466438833303)  
     
   O processo será executado internamente e assim irá criar os tipos padrões automaticamente. Após a execução, faça logout/login no sistema e acesse o menu Tipos de Requisições e valide se os tipos abaixo foram criados:  
     
   Aumento de quadro;  
   Alteração de dados funcionais;  
   Desligamento;  
   Transferência;  
   Transferência com Alteração de Dados Funcionais.  
   Substituição;  
   Treinamento;  
   Geral.
6. Definir as parametrizações de utilização das requisições. Para isso acesse o menu Configurações | Parametrizador  | Ao abrir o assistente clique em avançar e selecione o processo 07.00.02 - Requisições e clique em avançar:

     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27466438837015)  
     
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27466475814039)
7. O usuário da pessoa envolvida (criador ou aprovador) no fluxo da requisição, deverá estar vinculado a um atendente do Agilis. Para criá-lo basta acessar Configurações | Criar Atendente no RM Agilis:  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27466438840087)  
     
   Este módulo tem como objetivo criar atendentes no RM Agilis para que os mesmos sejam utilizados no fluxo de workflow de requisições criadas/manipuladas pelo RM Portal/App Meu RH.  
     
   Ao acessar o módulo, serão listados todos os funcionários que possuem usuário de acesso ao portal. Para efetuar a criação dos atendentes, basta escolher o usuário e executar o processo.

**Importante**  
Para aprovação da requisição, o sistema considerará o Tipo de Atendimento apontado no tipo de requisição. Este tipo de Atendimento é uma ferramenta do modulo Totvs Aprovação e Atendimento.   
  
Para validar, acesse no Agilis o menu Workflow/Grupos | selecione o grupo referente a requisição do Vitae | Anexos | Tipos de Atendimento do Grupo de Atendimento e valide se o grupo de atendimento informando nos tipos de requisição do Vitae esta vinculado ao grupo do Agilis:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27466438841751)  
  
**Saiba Mais**Para maiores informações sobre chefes/supervisores, acesse o link abaixo:  
[Chefes e Supervisores](https://tdn.totvs.com/display/LRM/Chefes+e+Supervisores)  
  
Para maiores informações sobre utilizar as Requisição na Gestão por Hierarquia, acesse o link abaixo:  
[RH - RM - RHU - Utilizar requisição na gestão por hierarquia](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6582907821975-RH-RM-RHU-Utilizar-requisi%C3%A7%C3%A3o-na-gest%C3%A3o-por-hierarquia)  
  
Para detalhes da funcionalidade de cada parâmetro, acesse o link abaixo:  
[Parâmetros da utilização das requisições](https://tdn.totvs.com/pages/viewpage.action?pageId=452719581)  
  
Para maiores informações sobre requisições, acesse os links abaixo:  
[Tipos de Requisição](https://tdn.totvs.com/pages/viewpage.action?pageId=452719406)  
[Gerenciamento dos tipos de requisições](https://tdn.totvs.com/pages/viewpage.action?pageId=452719602)  
  
Para obter informações mais detalhadas sobre cada tipo de requisição, acesse os links abaixo:  
[Requisição de Aumento de Quadro](https://tdn.totvs.com/pages/viewpage.action?pageId=452719206)  
[Alteração de dados funcionais](https://tdn.totvs.com/pages/viewpage.action?pageId=452719411)  
[Desligamento](https://tdn.totvs.com/pages/viewpage.action?pageId=452719603)  
[Transferência](https://tdn.totvs.com/pages/viewpage.action?pageId=452719426)  
[Transferência com Alteração de Dados Funcionais.](https://tdn.totvs.com/pages/viewpage.action?pageId=452719580)  
[Substituição](https://tdn.totvs.com/pages/viewpage.action?pageId=452719216)  
[Treinamento](https://tdn.totvs.com/pages/viewpage.action?pageId=452719447)  
[Geral](https://tdn.totvs.com/pages/viewpage.action?pageId=452719380)
