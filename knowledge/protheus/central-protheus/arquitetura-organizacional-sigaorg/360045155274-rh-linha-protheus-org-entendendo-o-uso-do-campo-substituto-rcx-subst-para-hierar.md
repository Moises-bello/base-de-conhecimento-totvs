---
article_id: 360045155274
category: Arquitetura Organizacional (SIGAORG)
content_hash: 45d9d7618d47baccf6920e2a3f1e7875e2d1fa4b12ebb25a10621f4a331b5720
fetched_at: '2026-06-28T22:42:52.944922+00:00'
product: protheus
section_id: 1500000904101
source: central-protheus
title: RH - Linha Protheus - ORG - Entendendo o uso do campo Substituto (RCX_SUBST)
  para Hierarquia de Postos
type: support-article
updated_at: '2021-07-29T21:07:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045155274-RH-Linha-Protheus-ORG-Entendendo-o-uso-do-campo-Substituto-RCX-SUBST-para-Hierarquia-de-Postos
---

**Dúvida**Entendendo o uso do campo  **Substituto** (RCX\_SUBST) para Hierarquia de Postos  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Arquitetura Organizacional – Todas as versões  
  
**Solução**O campo Substituto (RCX\_SUBST) é utilizado para alterar o responsável do Posto que poderá gerenciar ou não as equipes de hierarquia.  
Procedimentos para Utilização:  
Em Arquitetura Organizacional (SIGAORG) acesse Atualizações > Movimentos > Postos (ORGA030).  
O sistema apresenta os postos que estão Movimentados e criados anteriormente pela Movimentação de Departamentos, cada posto tem a possibilidade de ter como Responsável 1 pessoa no qual poderá ser responsável ou não por Equipes na Hierarquia.  
Ao Selecionar a opção de Atualizar temos a possibilidade de efetuar as Movimentações do Posto (Ocupar, Desocupar, Congelar, Cancelar e Solicitar mais postos).  
Para utilização da Hierarquia no Portal Gestão Capital Humano o sistema entende que somente o líder que não está como substituto e ocupante principal do posto deverá ter acesso às informações de solicitações da equipe. Veja no exemplo abaixo:  
  
Temos 2 funcionários que ocupam o mesmo posto, na imagem abaixo o funcionário de matrícula 000007 está como o principal ocupante. O segundo ocupante, ao ser cadastrado no posto, automaticamente virá registro como **Substituto** (RCX\_SUBST) até que o ocupante principal não faça mais parte da equipe, posto e departamento.

![](https://tdn.totvs.com/download/attachments/485854388/image2019-4-23_11-50-24.png?version=1&modificationDate=1556033200053&api=v2)  
  
No Acesso da Hierarquia criada através do Cadastro de Estrutura de Visão temos o funcionário do campo **Código de Identificação** (RD4\_CODIDE) deverá ser o mesmo posto do campo **Posto** (RCX\_POSTO):

![](https://tdn.totvs.com/download/attachments/485854388/image2019-4-23_12-6-11.png?version=1&modificationDate=1556033200020&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/485854388/image2019-4-23_12-6-32.png?version=1&modificationDate=1556033199983&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/485854388/image2019-4-23_12-7-26.png?version=1&modificationDate=1556033199837&api=v2)  
  
Para entendermos a Hierarquia utilizada no portal devemos entender quem é responsável por cada departamento. Iremos utilizar esses 3 Departamentos marcados:  
  
![](https://tdn.totvs.com/download/attachments/485854388/image2019-4-23_13-52-35.png?version=1&modificationDate=1556038355617&api=v2)  
  
Departamento 000000004 tem como responsável seu coordenador (Depto Nível Acima):

![](https://tdn.totvs.com/download/attachments/485854388/image2019-4-23_13-53-52.png?version=1&modificationDate=1556038432397&api=v2)  
  
Departamento 000000006 - Também possui o mesmo coordenador como responsável (Depto Nível Acima):

![](https://tdn.totvs.com/download/attachments/485854388/image2019-4-23_13-55-16.png?version=1&modificationDate=1556038516960&api=v2)  
  
Abaixo desses 2 departamentos que possuem o nível de Liderança temos o departamento dos funcionários, nele está informado o funcionário que está alocado no departamento 000000004:

![](https://tdn.totvs.com/download/attachments/485854388/image2019-4-23_13-56-44.png?version=1&modificationDate=1556038604393&api=v2)  
  
No caso da estrutura do Portal Gestão Capital Humano o sistema entende que a informação de líder é apenas direcionada ao funcionário que está alocado com primeiro no posto em questão. Acessando com o funcionário matricula 000007 o sistema deverá trazer os dados de sua equipe, já que no caso do Cadastro de Posto campo Substituto (RCX\_SUBST) ele está como Principal:

![](https://tdn.totvs.com/download/attachments/485854388/image2019-4-23_14-0-22.png?version=1&modificationDate=1556038822773&api=v2)  
  
Acessando com o suposto líder que "está como substituto", campo Substituto (RCX\_SUBST=SIM), o sistema entende que ele ainda não está liderando a equipe e sua hierarquia, portanto, ainda não deverá ter acessos para efetuar qualquer tipo de solicitação:

![](https://tdn.totvs.com/download/attachments/485854388/image2019-4-23_14-2-41.png?version=1&modificationDate=1556038961467&api=v2)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o SIGAORG](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206968028-RH-Arquitetura-Organizacional)  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
