---
article_id: 4403547339927
category: Meu RH - Gestor
content_hash: bec6f9f0939707117e9162bee56962a8241dcef71528d2322a0394f7c41d0dba
fetched_at: '2026-06-28T22:47:32.413738+00:00'
product: rm
section_id: 1500000861742
source: central-rm
title: RH - RM - Meu RH - Como restringir / bloquear a visualização de determinados
  Subordinados na visão do Gestor?
type: support-article
updated_at: '2026-06-16T15:15:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403547339927-RH-RM-Meu-RH-Como-restringir-bloquear-a-visualiza%C3%A7%C3%A3o-de-determinados-Subordinados-na-vis%C3%A3o-do-Gestor
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22211272435863) Tempo aproximado para leitura: 00:04:22 min**

**Dúvida**  
Como bloquear a visão do Gestor para alguns subordinados? Exemplo: Autônomos, PJ, Diretor e etc...  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) – Meu RH – Todas Versões.  
  
**Solução**  
Para realizar a restrição na visualização de subordinados no Meu RH, somente para um Chefe em específico, deverá ser criado um filtro dentro do "usuário" vinculado ao Chefe, caso queira colocar a restrição para todos os Chefes, o Filtro deverá ser criado dentro dos "Perfis" vinculado aos Chefes.  
  
Mostrando a criação do Filtro pelo **Usuário** caso seja um Chefe em específico:

* Acesse o módulo **Serviços Globais** / **Segurança** / **Usuários**;
* Selecione o **Sistema** ao qual o usuário pertence;
* Selecione o **usuário** do chefe.
* Clique em **Editar**;
* Em **Anexos** selecione **Filtro por usuário**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403544286359)

* Clique em **Incluir**
* Selecione a **Tabela** que contém as informações que deseja filtrar;
* Cliente em **Novo**;  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22211242157847)
* Adicione um **filtro**, selecionando as informações que deseja filtrar e clique em **Executar**;  
  ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403552152983)
* Neste exemplo o filtro foi criado com a finalidade de **Não** exibir os funcionários com código de tipo A, ou seja, funcionários do tipo Autônomos.

Na visão anterior no App Meu Rh era apresentado apenas os funcionários do tipo autônomo, utilizando o filtro de exemplo os funcionários do tipo autônomos não são mais apresentados.  
  
![testes.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4403545338647)

Mostrando a criação do Filtro pelo **Perfil** caso queira realizar o bloqueio para todos os Chefes.  
  
Caso deseje, também é possível realizar o mesmo tipo de filtro para um **Perfil.**

* Acesse o módulo **Serviços Globais** / **Segurança** / **Perfis**;
* Selecione o **Sistema** ao qual o usuário pertence;
* Selecione o **Perfil** vinculado aos Chefes.
* Clique em **Editar**;
* Em **Anexos** selecione **Filtro por usuário**;

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403552517911)

* Os procedimentos serão os mesmos feitos como demonstrado acima, porem em vez de ser aplicado apenas ao usuário escolhido, neste caso será aplicado o filtro para todos que estão utilizando este perfil.
