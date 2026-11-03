---
content_hash: 4301ee0c28b1f5fcdacd5c6c6f77a8649fd8b184db71fcacde542e00631ab698
fetched_at: '2026-06-29T00:06:23.344587+00:00'
page_id: '224100700'
product: rm
source: tdn-rm
title: DT_PDI_Integracao_com_Competencias
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_PDI_Integracao_com_Competencias
version: 4
---

# PDI INTEGRAÇÃO COM COMPETÊNCIAS

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Gestão de Pessoas** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Acompanhamento* | *PDI* | |
| **Versões/Release:** | 12.1.9 |

## Descrição

O TOTVS Gestão de Pessoas disponibiliza o desenvolvimento de competências através do PDI. Também é possível gerar todo o PDI automaticamente através do mapa de conhecimento estabelecido.

## Procedimento para Utilização

O PDI (Plano de Desenvolvimento Individual) foi alterado para possibilitar o desenvolvimento de competências através de metas no processo de PDI. Para isso foi disponibilizado no cadastro de PDI que se encontra no caminho **RH / Gestão de Pessoas / Acompanhamento / PDI** uma série de configurações para o desenvolvimento de competências através de metas como:

•Utiliza metas para desenvolvimento de competências  
•Preenchimento de competência obrigatório  
•Habilitar sugestão de competências para o funcionário  
•Exibir somente competências definidas na meta  
•Exibir somente competências definidas no mapa de conhecimento do funcionário  
•Exibir somente competências definidas na meta e que estejam definidas no mapa de conhecimento do funcionário

Como o desenvolvimento de competências é através de metas, foi criado um novo anexo chamado **"Competências Vinculadas"** que é somente leitura e exibe somente as competências vinculadas da meta selecionada. De forma similar ao funcionamento de requisito de acesso vinculados a meta, as competências somente serão vinculadas através de processo, por isso foi criado um processo chamado **"Vincular/Desvincular Competências a Meta"**. Este processo disponibiliza as competências e as metas para o usuário realizar o vínculo e funciona de forma similar ao processo de vinculação de requisitos de acesso, porém realizando a vinculação de competências a meta.

 

No portal onde se encontram as funcionalidade de PDI, também foram feitas modificações. Temos na opção de lançamento de ações a opção de preencher também escolhendo competências. É similar a escolha de requisito de acesso que já existe hoje no sistema, porém funciona com competências. O Usuário só pode lançar ações para competências ou para requisitos de acesso, para isso temos uma opção de escolha no momento de lançamento da ação, se o usuário escolher lançar competências será carregado as opções de competências disponíveis de acordo com as configurações realizadas no PDI anteriormente.  
Também foi  alterado no portal a opção de sugestões da ação. No menu **"Carregar Sugestões de Requisito de Acesso"** surge somente ações relacionadas com requisitos de acesso, seu comportamento não sofrerá mudanças. Foi criado um novo menu chamado **"Carregar Sugestões de Competências"** que sugere as ações relacionadas com as competências, essa funcionalidade  funciona de forma similar ao de sugestão de requisito de acesso.  
Caso as opções de competências não estejam marcadas no cadastro de PDI as opções relacionadas a competências do PORTAL não devem ser exibidas. 

Questionários do PDI, serve para ter informações específicas da empresa registradas dentro do PDI.  
Se já houver respostas para o questionário não é permitido remover o vínculo. 

Para definir ações do PDI vinculado a um questionário, é preciso responde-lo por ação respeitando as regras do questionário (obrigatoriedade e formato)

Para ter acesso fácil as informações preenchidas, o sistema permite a visualização das informações descritas no questionário e da ação ao clicar em um ícone na visão de ações do PDI

O sistema permite o usuário acessar o PDI e complementar informações como: competências, requisitos de acesso, prazo, questionário e objetivo. Para isso ele tem que seguir as regras já existentes no PDI, inserir competência ou requisito, se não tiver informado, conseguir preencher o questionário, para gerado pelo processo ou pela sugestão. Se vincular um questionário após já ter ações, a primeira vez que abrir a ação irá fazer a inscrição e permitir responder o questionário.

Gerar PDI a partir de um mapa de conhecimento pode ser por requisito de acesso ou por competências. Para direcionar o que as pessoas da empresa deverão desenvolver.  
Este processo tem duas opções de escolha para execução: "Gerar ações do PDI para Competências" e "Gerar ações do PDI para Requisitos de Acesso" podendo ser ambos.    
Os parâmetros deste processo estão disponíveis somente se estiverem habilitados no PDI através dos parâmetros: "Utilizar Requisitos de Acesso", "Utilizar Competências".   
O processo também tem que seguir as regras configuradas no PDI relativa a competências e, ou, relativas a requisito de acesso, definido o resultado de ações a serem geradas para o PDI do participante.   
Caso tenha mais de uma opção de requisito ou competência para a mesma ação, não deverá preencher a opção (será preenchido mais tarde pelo portal).  
O status da ação no PDI será "Ação aguardando Complemento".   
Caso a mesma competência/requisito esteja vinculada a N ações. deverão ser geradas todas as ações com a competência/requisito que está vinculada.

Na alteração não pode ser alterado competência, req acesso ou ação. O funcionamento da geração de ações pelo mapa de conhecimento.  
Se não tiverem competências/requisitos associados a meta, não serão geradas as metas. Mas deverá ser registrado via LOG no processo: "Não foi gerada a competência/requisito X para a pessoa Y pois não existem metas associadas".   
Se houver ações status diferente de "Ação aguardando Complemento" o processo não poderá ser executado.   
Quando o processo for executado novamente, serão excluídas todas as ações e regeradas conforme regras já definidas.
