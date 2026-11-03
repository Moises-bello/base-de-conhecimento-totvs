---
content_hash: b900036382747218cdc5531968bfb88a9dc5e24dab5e70b9c48f6fb109fde5a0
fetched_at: '2026-06-29T00:11:05.200235+00:00'
page_id: '628375023'
product: rm
source: tdn-rm
title: Cópia de DT_GRUPOS_DE_PESQUISA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628375023
version: 1
---

# Cadastro de Grupos de Pesquisa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | **Pesquisa, Extensão e Inovação** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de Grupos de Pesquisa* | *Cadastro de Grupos de Pesquisa* | |
| **Cadastros Iniciais:** | *Área de conhecimento*  *Sub-área de conhecimento*  *Pesquisador*  *Linha de Pesquisa* |
| **Requisito (ISSUE):** | *PCREQ-5446* |
| **País(es):** | *Brasil* |
| **Tabelas utilizadas:** | *SPESGRUPOPESQUISA, SPESGRUPOLINHAPESQUISA,*  *SPESINTEGRANTEGRUPO, SPESCONFIRMAGRUPO* |
| **Versões/Release:** | *12.1.7* |

## Descrição

Possibilita ao usuário gerenciar seus processos referentes a um grupo de pesquisa, permitindo realizar o cadastro, submeter a análise e avaliação utilizando-se do processo de aprovação através de FLUIG.

Pré-requisitos para utilizar a funcionalidade de cadastro de grupos de pesquisa

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de cadastro de grupos de pesquisa. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis).
  + Código = **pesquisador**| Descrição = **Pesquisador**
  + Código = **reitoria**| Descrição = **Reitoria**
  + Código = **pro-reitoria**| Descrição = **Pró-Reitoria**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Importar o fluxo de cadastro de grupos de pesquisa para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos do cadastro de grupos de pesquisa.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

O usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Grupos de Pesquisa | Grupos de Pesquisa". É necessário estar vinculado ao papel de "Pesquisador" para realizar essa solicitação.

O formulário de cadastro será aberto com o código do pesquisador vinculado ao usuário do FLUIG, sendo esse o usuário que será cadastrado como solicitante do grupo no TOTVS Educacional.

Após preencher as informações do cadastro o usuário enviará a solicitação para "Confirmar Cadastro Grupo", onde um usuário, vinculado ao papel de "Reitoria", vai verificar as informações preenchidas.

Nessa etapa, o usuário vinculado ao papel de "Reitoria" terá três opções:

* Avançar etapa para "Cadastro de Grupo Reprovado"  
  O grupo não será cadastrado e uma justificativa deverá ser informada pelo usuário vinculado ao papel de "Reitoria". O fluxo é concluído.
* Avançar etapa para "Cadastrar Grupo CNPq"  
  O grupo será cadastrado no TOTVS Educacional e passará para etapa onde o usuário vinculado ao papel de "Reitoria" solicitará o cadastro no CNPq.
* Avançar etapa para "Aprovação Cadastro Grupo".  
  Caso seja necessário, o usuário vinculado ao papel de "Reitoria" poderá solicitar uma segunda aprovação do cadastro para a Pró-reitoria. Outro usuário vinculado ao papel de "Pró-reitoria" terá duas opções:
  + Avançar etapa para "Cadastrar Grupo CNPq"  
    O grupo será cadastrado no TOTVS Educacional e passará para etapa onde o usuário vinculado ao papel de "Reitoria" solicitará o cadastro no CNPq.
  + Avançar etapa para "Cadastro de Grupo Reprovado"  
    O grupo não será cadastrado e uma justificativa deverá ser informada pelo usuário vinculado ao papel de "Reitoria". O fluxo é concluído.

 Ao chegar na etapa de "Cadastrar Grupo CNPq", o usuário vinculado ao papel de "Reitoria" solicitará o cadastro no CNPq (entidade e/ou sistema externo ao fluxo) e enviará o fluxo para a etapa "Solicitar Certificação Grupo". Esse etapa será automaticamente assumida pelo usuário que originalmente iniciou a solicitação e que no diagrama acima, está representado pelo papel do "Pesquisador".

Ao solicitar a certificação do grupo, o usuário vinculado ao papel de "Pesquisador" enviará o fluxo para a etapa de "Confirmar Certificação Grupo".

O usuário vinculado ao papel de "Reitoria" terá então três opções:

* Avançar etapa para "Certificação de Grupo Reprovado"  
  O grupo não será certificado e uma justificativa deverá ser informada pelo usuário vinculado ao papel de "Reitoria". O fluxo é concluído.
* Avançar etapa para "Certificar Grupo CNPq"  
  O grupo será certificado no TOTVS Educacional e passará para etapa onde o usuário vinculado ao papel de "Reitoria" solicitará a certificação no CNPq.
* Avançar etapa para "Aprovação Certificação Grupo".  
  Caso seja necessário, o usuário vinculado ao papel de "Reitoria" poderá solicitar uma segunda aprovação da certificação para a Pró-reitoria. Outro usuário vinculado ao papel de "Pró-reitoria" terá duas opções:
  + Avançar etapa para "Certificar Grupo CNPq"  
    O grupo será certificado no TOTVS Educacional e passará para etapa onde o usuário vinculado ao papel de "Reitoria" solicitará a certificação no CNPq.
  + Avançar etapa para "Certificação de Grupo Reprovado"  
    O grupo não será certificado e uma justificativa deverá ser informada pelo usuário vinculado ao papel de "Reitoria". O fluxo é concluído.

Ao chegar na etapa de "Certificar Grupo CNPq"o usuário vinculado ao papel de "Reitoria" solicitará a certificação no CNPq (entidade e/ou sistema externo ao fluxo) e enviará o fluxo para a etapa final, onde será concluído.

Durante toda a execução do fluxo são gerados registros de histórico por etapa. Esse histórico é gravado na tabela SPESCONFIRMAGRUPO e contém informações sobre o usuário que movimentou a etapa, qual etapa foi movimentada, data da movimentação, justificativas, dentre outras.
