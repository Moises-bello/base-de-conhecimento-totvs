---
article_id: 1500008082261
category: GESTOR
content_hash: fddc9a0f0e6f862432fc15ddbe4c5a5c2236ca42cc63de526184631804b6ac55
fetched_at: '2026-06-28T22:44:35.599397+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - MEU RH - Definir uma matrícula como gestor no MEU RH
type: support-article
updated_at: '2026-06-22T20:29:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008082261-RH-Linha-Protheus-MEU-RH-Definir-uma-matr%C3%ADcula-como-gestor-no-MEU-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24769033339031) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como definir uma matrícula como gestor no MEU RH?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**1. Para liberar as opções de Gestão no MEU RH, só irão aparecer se o usuário com acesso de gestor/líder estiver dentro de uma estrutura hierárquica na qual possua subordinados diretos, ou seja, abaixo de sua gestão.  
  
Para verificar se o gestor esta como responsável do departamento, acesse no GPE o menu >Atualizações >Cadastros >Departamentos.  
  
Será definido como gestor a matrícula que estiver como responsável do departamento, no campo (Matric. Resp).  
  
![35cGumPsLE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4404549745943)  
  
Caso tenha dúvidas com relação a configuração de hierarquia siga as orientações indicadas no Boletim Técnico: **[Hierarquias - Níveis de fluxo de aprovação de Solicitações](https://tdn.totvs.com/pages/releaseview.action?pageId=500300689)** (ele foi criado para o **Portal GCH**, mas funciona da mesma forma para o **MEU RH**).  
  
Ao configurar a Hierarquia de acordo com os Departamentos da empresa, é necessário configurar os **Níveis de fluxo de aprovação**.  
  
2. Caso utilize o parâmetro MV\_ORGCFG igual a 2(Controle por visão), verifique se o campo **Emp. Resp (QB\_EMPRESP)** esta preenchido com o grupo de empresa corretamente, caso esteja vazio, a opção de Gestão no MEU RH não irá apresentar para o gestor.  
  
Para verificar se o grupo de empresa esta preenchido corretamente no cadastro de departamento, acesse no GPE o menu >Atualizações >Cadastros >Departamentos.  
  
![nKL8qt2Cdq.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4404557031447)  
  
Para saber mais sobre este campo e utilização do MV\_ORGCFG igual a 2 acesse:  
**[Melhoria no cadastro de departamentos que permita escolher um responsável de um grupo de empresas diferente.](https://tdn.totvs.com/pages/releaseview.action?pageId=502463093)  
OBS:** Este boletim foi criado para o **Portal GCH,** mas funciona da mesma forma para o **MEU RH**Seguem abaixo os artigos relacionados:  
**[MP - MEU RH - Como funcionam os Níveis e Fluxo de aprovação de Solicitações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058407953)**  
**[MP - MEU RH - Como funcionam os Níveis e Fluxo de aprovação de Solicitações Sem Visão?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044589134)**  
**[MP - MEU RH - Como funcionam os Níveis e Fluxo de aprovação de Solicitações Com Visão?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047331074)  
  
Saiba Mais:**[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)  
[CLIQUE AQUI para configurar as permissões de acessos ao MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033892693)
