---
article_id: 7917580297623
category: GESTOR
content_hash: a359e295b378c53c5341d14da98409b690f285a71c1d19eace3273ea8c67a378
fetched_at: '2026-06-28T22:44:35.544538+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como configurar a hierarquia por departamentos
  (MV_ORGCFG=0)
type: support-article
updated_at: '2026-06-19T15:56:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7917580297623-RH-Linha-Protheus-MEU-RH-Como-configurar-a-hierarquia-por-departamentos-MV-ORGCFG-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19369171700631) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida:**  
Como configurar a hierarquia de departamento para o Meu RH?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Causa**  
Como configurar a hierarquia de departamento corretamente para gestão de time no MEU RH  
  
**Solução**  
Para configurar a hierarquia por departamento é necessário seguir algumas premissas. Para montagem da Hierarquia é utilizada o conceito do Parâmetro **MV\_ORGCFG = 0**, neste conceito as tabelas que serão utilizadas são a de **Funcionários** (SRA) e **Departamentos** (SQB). A montagem da hierarquia é realizada pelos departamentos, onde a premissa será de informar em cada departamento inferior os campos de Filial Responsável, Matrícula Responsável e Departamento Superior Responsável.  
  
Como não é utilizado o conceito de visão pelo módulo de Arquitetura Organizacional, não será necessário ter uma visão cadastrada e muito menos informá-la no cadastro de menus do portal.  
  
Outra premissa de montagem da hierarquia de Estrutura de Departamento é que pelo menos tenha 2 departamentos no mínimo **onde há separação** do Líder **que difere** do departamento do funcionário.  Também será necessário que o último nível da estrutura, o nível mais alto não tenha informações do campo Departamento Superior Responsável (QB\_DEPSUP).  
  
Temos a Montagem dos Departamentos com o seguinte exemplo:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7917670310167)  
  
Presidente      → 000000001  
Gerente          → 000000002  
Coordenador  → 000000003  
Líder               → 000000004  
Funcionários   → 000000005  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7917484731671)  
  
Primeiro é preciso definir quem será o departamento responsável pela base, no nosso exemplo o departamento funcionários (000000005), terá como departamento superior a ele o departamento Líder (000000004), portanto a matrícula responsável por este departamento também pertencerá ao departamento superior (Líder):

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7921386431255)  
  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7923728537239)  
  
O próximo departamento é o Líder (000000004), o apontamento deste departamento segue o mesmo principio do anterior, logo ele terá como departamento superior o departamento Coordenador (000000003) e a matricula responsável (Gestor) pertencerá a este mesmo departamento superior (Coordenador):

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7921733773847)  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7923817144087)  
  
O próximo departamento é o Coordenador (000000003), o departamento superior será o Gerente (000000002) e a matrícula responsável deste departamento (Coordenador), pertencerá ao departamento Gerente (000000002):  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7922185584023)  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7923919599255)  
  
O próximo departamento é o Gerente(000000002), o departamento superior será o Presidente (000000001) e a matrícula responsável deste departamento (Gerente), pertencerá ao departamento superior Presidente (000000001):![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7922494255255)  
  
![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7924035178519)  
  
O próximo departamento é o **último da estrutura hierárquica**, nele existem duas exceções, este será o único departamento da estrutura que não terá o campo departamento superior preenchido e também é o único que poderá ter no apontamento da "Matrícula Resp." um funcionário que pertence a este mesmo departamento.  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7922957078935)  
  
![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7924035843863)

Com esses apontamentos o sistema criará automaticamente uma chave de busca na tabela departamento (**QB\_KEYINI**), essa chave é muito importante para sequencia correta do fluxo das solicitações, Exemplo:

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7924136013591)  
  
Caso tenha seguido corretamente, a visualização dos gestores será da seguinte forma:

**Presidente:**

![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7926957266199)  
  
**Gerente**:  
![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7927135049111)  
  
**Coordenador**:  
![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7927142175383)  
  
**Líder**:  
![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7927239063575)  
  
A seguir temos um link compartilhado para um vídeo no *YouTube* onde explicamos detalhadamente, em formato de **tira-dúvidas/webinar**, como funciona a hierarquia por departamento. No vídeo, abordamos o conceito e tiramos as principais dúvidas sobre o processo.  
<https://www.youtube.com/watch?v=JoDeAZ5T5DE&t=6s>   
  
Também temos outro *link* com um vídeo no *YouTube*, que apresenta um *how-to* simples e rápido sobre como configurar a hierarquia por departamento.  
  
O objetivo destes vídeos, divididos em 4 partes, é mostrar em partes rápidas e de forma prática, como realizar essa configuração de maneira eficiente.  
Parte 1: <https://www.youtube.com/watch?v=2_cBN4Plu8w>  
Parte 2: <https://www.youtube.com/watch?v=5hBMB0BW4y4>  
Parte 3: <https://www.youtube.com/watch?v=qNDnWhmqE78>  
Parte 4: <https://www.youtube.com/watch?v=U9FqhYXheDk>   
  
**Algumas regras importantes e, obrigatórias, sobre o cadastro dos departamentos.**

* Quando temos um Departamento topo da hierarquia, ou seja, que não possui Departamento Superior cadastrado, o funcionário responsável por ele, precisa ser do mesmo Departamento.
* Quando temos um Departamento com responsável de outro Departamento, precisa cadastrar o Departamento Superior deste funcionário responsável.
* Salvo topo da hierarquia, o funcionário nunca poderá ser responsável pelo próprio Departamento
* Definindo a estrutura de departamentos, não alterar o cadastro diretamente na SRA - tabela de funcionários
* Os funcionários precisarão ser alocados nos novos departamentos, via processo de Transferência no GPE
* Os participantes que serão Gestores, terão um outro usuário do portal com as permissões Meu RH, do Grupo Gestão habilitadas

[**MEU RH - Não mostra funcionário na Minha equipe quando MV\_ORGCFG=0**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25744857444631-RH-Linha-Protheus-MEU-RH-N%C3%A3o-mostra-funcion%C3%A1rio-na-Minha-equipe-quando-MV-ORGCFG-0)  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
