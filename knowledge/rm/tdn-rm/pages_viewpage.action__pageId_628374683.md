---
content_hash: 19af936e005380bf52df43b71b505cc608c247fbf94309c3d91099253fb1984f
fetched_at: '2026-06-29T00:11:05.082341+00:00'
page_id: '628374683'
product: rm
source: tdn-rm
title: Cópia de DT_GRUPOS_DE_PESQUISA_WF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628374683
version: 1
---

# Cadastro de Grupos de Pesquisa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | ************Inovação,********** Pesquisa e Extensão** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de Grupos de Pesquisa* | *Cadastro de Grupos de Pesquisa* | |
| **Cadastros Iniciais:** | *Área de conhecimento*  *Sub-área de conhecimento*  *Pesquisador*  *Linha de Pesquisa* |
| **Requisito (ISSUE):** | *PCREQ-5446* |
| **País(es):** | *Brasil* |
| **Tabelas utilizadas:** | *SPESGRUPOPESQUISA, SPESGRUPOLINHAPESQUISA,*  *SPESINTEGRANTEGRUPO, SPESCONFIRMAGRUPO* |
| **Versões/Release:** | *12.1.15* |

## Descrição

Possibilita ao usuário gerenciar seus processos referentes a um grupo de pesquisa, permitindo realizar o cadastro, submeter a análise e avaliação utilizando-se do processo de aprovação através do FLUIG.

Pré-requisitos para utilizar a funcionalidade de cadastro de grupos de pesquisa

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de cadastro de grupos de pesquisa. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis).
  + Código = **pesquisador**| Descrição = **Pesquisador**
  + Código = **reitoria\_pesquisa**| Descrição = **Reitoria de Pesquisa**
  + Código = **pro\_reitoria**| Descrição = **Pró-Reitoria**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Importar o fluxo de cadastro de grupos de pesquisa para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos do cadastro de grupos de pesquisa.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

O usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Grupos de Pesquisa | Grupos de Pesquisa". É necessário estar vinculado ao papel de "Pesquisador" para realizar essa solicitação.

O formulário de cadastro será aberto com o código do pesquisador vinculado ao usuário do FLUIG, sendo esse o usuário que será cadastrado como solicitante do grupo no TOTVS Educacional.

Após preencher as informações do cadastro o usuário enviará a solicitação para "Confirmar Cadastro Grupo", onde um usuário, vinculado ao papel de "Reitoria de Pesquisa", vai verificar as informações preenchidas.

Nessa etapa, o usuário vinculado ao papel de "Reitoria de Pesquisa" terá três opções:

* Avançar etapa para "Cadastro de Grupo Reprovado"  
  O grupo não será cadastrado e uma justificativa deverá ser informada pelo usuário vinculado ao papel de "Reitoria de Pesquisa". O fluxo é concluído.
* Avançar etapa para "Cadastrar Grupo CNPq"  
  O grupo será cadastrado no TOTVS Educacional e passará para etapa onde o usuário vinculado ao papel de "Reitoria de Pesquisa" solicitará o cadastro no CNPq.
* Avançar etapa para "Aprovação Pró-Reitoria (Cadastro)".  
  Caso seja necessário, o usuário vinculado ao papel de "Reitoria de Pesquisa" poderá solicitar uma segunda aprovação do cadastro para a Pró-reitoria. Outro usuário vinculado ao papel de "Pró-reitoria" terá duas opções:
  + Avançar etapa para "Cadastrar Grupo CNPq"  
    O grupo será cadastrado no TOTVS Educacional e passará para etapa onde o usuário vinculado ao papel de "Reitoria de Pesquisa" solicitará o cadastro no CNPq.
  + Avançar etapa para "Cadastro de Grupo Reprovado"  
    O grupo não será cadastrado e uma justificativa deverá ser informada pelo usuário vinculado ao papel de "Pró-reitoria". O fluxo é concluído.

 Ao chegar na etapa de "Cadastrar Grupo CNPq", o usuário vinculado ao papel de "Reitoria de Pesquisa" solicitará o cadastro no CNPq (entidade e/ou sistema externo ao fluxo) e enviará o fluxo para a etapa "Certificar Grupo CNPq". 

O usuário vinculado ao papel de "Reitoria de Pesquisa" terá então três opções:

* Avançar etapa para "Certificação de Grupo Reprovado"  
  O grupo não será certificado e uma justificativa deverá ser informada pelo usuário vinculado ao papel de "Reitoria de Pesquisa". O fluxo é concluído.
* Avançar etapa para "Grupo Cadastrado/Certificado"  
  O grupo será certificado e atualizado no TOTVS Educacional e o fluxo será concluído.
* Avançar etapa para "Aprovação Pró-reitoria (Certificação)".  
  Caso seja necessário, o usuário vinculado ao papel de "Reitoria de Pesquisa" poderá solicitar uma segunda aprovação da certificação para a Pró-reitoria. Outro usuário vinculado ao papel de "Pró-reitoria" terá duas opções:
  + Retornar para a etapa "Certificar Grupo CNPq"  
    O responsável por essa solicitação poderá inserir uma observação na solicitação e retornar para a etapa anterior (Certificar Grupo CNPq) que irá solicitar a certificação no CNPq.
  + Avançar etapa para "Certificação de Grupo Reprovado"  
    O grupo não será certificado e uma justificativa deverá ser informada pelo usuário vinculado ao papel de "Pró-reitoria". O fluxo é concluído.

Durante toda a execução do fluxo são gerados registros de histórico por etapa. Esse histórico é gravado na tabela SPESCONFIRMAGRUPO e contém informações sobre o usuário que movimentou a etapa, qual etapa foi movimentada, data da movimentação, justificativas, dentre outras.
