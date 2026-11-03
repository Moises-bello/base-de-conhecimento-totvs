---
content_hash: d14f7159c80f59ad67633bc84b41ad8e49fb530c27cd3c37df0b046688f970be
fetched_at: '2026-06-29T00:11:05.259703+00:00'
page_id: '628377802'
product: rm
source: tdn-rm
title: Cópia de DT_CADASTRO_BOLSISTA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628377802
version: 46
---

# CADASTRO DE BOLSISTA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **TOTVS Educacional** |
| **Módulo:** | ***Pesquisa, Extensão e Inovação*** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Cadastro de Bolsista* | *Cadastro de Bolsista.* | |
| **Cadastros Iniciais:** | *Cadastro de Projetos* |
| **Parâmetro(s):** | *Informe os parâmetros utilizados.* |
| **Requisito (ISSUE):** | *PCREQ-5448* |
| **País(es):** | *Brasil* |
| **Tabelas Utilizadas:** | *SPROJBOLSISTA* |
| **Versões/Release:** | *12.1.9* |

## Descrição

Possibilita ao usuário gerenciar seus processos referentes ao cadastro do bolsista, permitindo realizar o cadastro, submeter a análise e avaliação utilizando-se do processo de aprovação através de FLUIG.

Pré-requisitos para utilizar a funcionalidade de cadastro de bolsista

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de cadastro de bolsista. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis).
  + Código = **pesquisador**| Descrição = **Pesquisador**
  + Código = **reitoria**| Descrição = **Reitoria**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Importar o fluxo de "Cadastro bolsista" para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos do fluxo "Cadastro de bolsista".  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

O usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Bolsista | Cadastro de Bolsista". É necessário estar vinculado ao papel de "Pesquisador" para realizar essa solicitação.

Serão listados apenas os projetos onde o usuário logado seja coordenador.

Após preencher as informações necessárias ao cadastro do bolsista o usuário enviará a solicitação para "Confirmar Cadastro Bolsista", onde um usuário vinculado ao papel de reitoria vai verificar as informações preenchidas e confirmar esse cadastro. Existe a opção também de recusar esse cadastro. Nesse caso o fluxo será concluído com "Cadastro Recusado".

Caso a solicitação esteja sendo feita para um bolsista já existente, as bolsas serão listadas na primeira etapa e o usuário poderá alterar a data inicio e data fim dessas bolsas, incluir novas bolsas ou excluir bolsas existentes.

Bolsas com lançamento financeiro vinculado (campo IDLAN preenchido na tabela SPROJSOLICITPGTOTIPOBOLSA) não poderão ser excluídas do cadastro do bolsista.

Ao avançar para a etapa "Confirmar" o fluxo verificará se o pesquisador que está sendo cadastrado como bolsista é maior de idade. Caso seja maior de idade, o fluxo será redirecionado para o bolsista onde o mesmo realizará o aceite dos termos do bolsista. Caso seja menor de idade, o fluxo identificará, através do RA preenchido pelo pesquisador, qual é o responsável acadêmico desse candidato a bolsista, e redirecionará o termo de aceite para ele.

Nas duas situações, "Aceite dos Termos pelo Bolsista" e "Aceite dos Termos pelo Responsável", após o aceite desses termos, o fluxo será encaminhado para o coordenador do projeto para que o mesmo possa confirmar o termo de aceite e concluir o fluxo como "Cadastro Confirmado".

Nessas três etapas "Aceite dos Termos pelo Bolsista", "Aceite dos Termos pelo Responsável" e "Aceite dos Termos", existe a ação de recusar o termo, "Termo de Aceite Não Confirmado", onde o fluxo é concluído sem que o bolsista seja cadastrado como ativo.

divs
