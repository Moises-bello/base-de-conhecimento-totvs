---
content_hash: 841e846ac84bbcd392471f2fddf5b5d451120bb12a38434488c10af3a53decea
fetched_at: '2026-06-29T00:08:32.500044+00:00'
page_id: '273988706'
product: rm
source: tdn-rm
title: DT_SOLICITACAO_PARCERIA_WF
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_SOLICITACAO_PARCERIA_WF
version: 3
---

# Solicitação de Parceria

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional.* |
| **Módulo:** | ************Inovação,********** Pesquisa e Extensão** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Solicitação de Parceria* | *Solicitação de Parceria* | |
| **Cadastros Iniciais:** | *Cadastro de Pesquisador*  *Cadastro de Função* |
| **Requisito (ISSUE):** | **PCREQ-5446** |
| **País(es):** | *Brasil* |
| **Tabelas utilizadas:** | *SPROJSOLICITACAOPARCERIA, SPROJSOLICITACAOAVALIACAO, SPROJSOLPARDESEMBOLSO,*  *SPROJSOLPARENVOLVIDOS, SPROJSOLPARCERIAETAPA, SPROJSOLPARRECEITA* |
| **Versões/Release:** | *12.1.15* |

## Descrição

Possibilita ao usuário gerenciar seus processos referentes a solicitação de parcerias, permitindo realizar a apresentação, análise e avaliação utilizando-se do processo de aprovação através do FLUIG.

Pré-requisitos para utilizar a funcionalidade de solicitação de parcerias

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de solicitação de parceria. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis).
  + Código = **pesquisador**| Descrição = **Pesquisador**
  + Código = **aprov\_parceria**| Descrição = **Aprovador de parceria**
  + Código = **contrato\_parceria**| Descrição = **Contrato de parceria**
  + Código = **juridico**| Descrição = **Jurídico**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Importar o fluxo de solicitação de parcerias para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos da solicitação de parcerias.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

O usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Solicitação de Parceria | Solicitação de Parceria". É necessário estar vinculado ao papel de "Pesquisador" para realizar essa solicitação.

O formulário de cadastro será aberto com o código do pesquisador vinculado ao usuário do FLUIG, sendo esse o usuário que será cadastrado como pesquisador da solicitação de parceria no TOTVS Educacional.

Após preencher as informações do cadastro o usuário enviará a solicitação para "Negociação de Parceria", onde um usuário, vinculado ao papel de "Aprovador de parceria", vai verificar as informações preenchidas.

Nessa etapa, o usuário vinculado ao papel de "Aprovador de parceria" terá duas opções:

* Avançar etapa para "Montar Plano de Trabalho"
* Avançar etapa para "Fim", onde a solicitação de parceria não é aprovada e o fluxo é  finalizado.

Na etapa de "Montar Plano de Trabalho", o usuário vinculado ao papel de "Pesquisador", preencherá as informações necessárias e avançará para etapa de "Aprovar Plano de Trabalho", onde outro usuário, vinculado ao papel de "Aprovador de parceria" poderá aprovar esse plano de trabalho ou retornar o fluxo ao pesquisador para realizar ajustes. Esse processo pode acontecer quantas vezes for necessário até as informações do plano de trabalho estarem corretas.

Se tudo estiver correto, o usuário vinculado ao papel de "Aprovador de parceria" avançará etapa para "Elaborar Instrumento", onde o usuário vinculado ao papel "Contrato de parceria", fará a elaboração do contrato (convênio) entre as partes. Nessa etapa é obrigatório a inclusão do contrato como anexo para futura aprovação/reprovação. 

Ao avançar etapa para "Avaliar Minuta", o usuário vinculado ao papel de "Jurídico" deverá verificar se o contrato criado está de acordo e, caso precise de algum ajuste, deverá retornar o fluxo para a etapa "Elaborar Instrumento". Esse processo pode acontecer quantas vezes for necessário até as informações do contrato estarem corretas.

Se tudo estiver correto, o usuário vinculado ao papel de "Jurídico" avançará etapa para "Assinar Instrumento" (entidade e/ou sistema externo ao fluxo), onde o usuário vinculado ao papel de "Aprovador de parceria" assinará o contrato juntamente com o parceiro e o pesquisador. Caso seja encontrado alguma incoerência, o fluxo poderá ser retornado à etapa "Elaborar Instrumento" e deverá passar por todo o processo descrito acima novamente.

Após a assinatura do contrato, o fluxo seguirá para a etapa de "Liberar Minuta", onde o usuário vinculado ao papel "Contrato de parceria" se certificará que está tudo correto e concluirá o fluxo. Nessa etapa ainda existe a possibilidade de encontrar alguma incoerência, nesse caso o fluxo pode ser enviado à etapa "Elaborar Instrumento" novamente.

Durante toda a execução do fluxo são gerados registros de histórico por etapa de aprovação. Esse histórico é gravado na tabela SPROJSOLICITACAOAVALIACAO e contém informações sobre o usuário aprovador, a etapa movimentada, parecer, data da aprovação, dentre outras.

 

Cancelamento do processo no Fluig

Caso o processo no Fluig seja cancelado, a solicitação de parceria receberá o status de "**Cancelada**", mas não será excluída da base de dados do TOTVS Educacional.
