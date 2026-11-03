---
content_hash: 709a8d82a6a4427c7eb56f6e110dc451651caf3740c8088ae098d5631c653ad1
fetched_at: '2026-06-29T00:11:05.191420+00:00'
page_id: '628375009'
product: rm
source: tdn-rm
title: Cópia de DT_ACOMPANHAMENTO_BOLSISTA_FREQUENCIA_WF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628375009
version: 1
---

# **ACOMPANHAMENTO DE BOLSISTA (FREQUÊNCIA)**

## **Características do Requisito**

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | ***********Inovação,********** Pesquisa e Extensão* |
| **Rotina:** | *Acompanhamento de Bolsista (Frequência)* |
| **Cadastros Iniciais:** | *Cadastro de Projetos* |
| **Requisito (ISSUE):** | *PCREQ-5448* |
| **País(es):** | *Informe o(s) Pais(es).* |
| **Banco(s) de Dados:** | *Brasil* |
| **Tabelas Utilizadas:** | *SPROJFREQUENCIA, SPROJSOLICITACAOPGTO,*  *SPROJSOLICITPGTOTIPOBOLSA, SPROJDESISTENCIABOLSISTA* |
| **Versões/Release:** | *12.1.15* |

## **Descrição**

Possibilita ao usuário gerenciar seus processos referentes ao acompanhamento de frequência do bolsista, permitindo realizar o cadastro, submeter a análise e avaliação utilizando-se do processo de aprovação através do FLUIG.  
Pré-requisitos para utilizar a funcionalidade de acompanhamento de bolsista (frequência)

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: [http://tdn.totvs.com/display/fluig/Como+Instalar-TOTVS%7C+Developer+Studio+](http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio)
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de acompanhamento de bolsista (frequência). É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis).
  + Código = **pesquisador**| Descrição = **Pesquisador**
  + Código = **reitoria\_pesquisa** |Descrião = **Reitoria de Pesquisa**
  + Código = **reitoria\_extensao**|Descrição =**Reitoria de Extensão**
  + Código = **coordenador\_extensao**| Descrição = **Coordenador de Extensão**
  + Código = **coordenador\_pesquisa**| Descrição = **Coordenador de Pesquisa**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Importar o fluxo de "acompanhamento bolsista (frequência)" para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos do fluxo "acompanhamento bolsista (frequência)".
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## **Procedimento para Utilização**

O usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Acompanhamento Bolsista (Frequência) | Acompanhamento Bolsista (Frequência)". É necessário estar vinculado ao papel de "Pesquisador" para realizar essa solicitação.  
Após preencher as informações necessárias ao acompanhamento do bolsista o usuário enviará a solicitação para "Confirmar Frequência", onde o coordenador do projeto vai verificar as informações preenchidas. O coordenador do projeto será identificado automaticamente e o fluxo será encaminhado para ele ao avançar a etapa.  
Após validar as informações preenchidas pelo bolsista, o coordenador do projeto terá três opções

* Solicitar o pagamento das bolsas O coordenador do projeto deverá aprovar/reprovar cada atividade informada pelo bolsista. Caso alguma atividade seja reprovada, será necessário informa uma justificativa. O coordenador do projeto deverá avançar para a etapa de "Solicitar Pagamento".
* Retornar o fluxo ao bolsista para algum ajuste que ele julgue necessário O coordenador do projeto poderá, antes de realizar a aprovação/reprovação das atividades, solicitar que o bolsista insira ou altere alguma informação que ele julgue necessária. Ao avançar para "Início - Retorno" o fluxo será devolvido para o bolsista que deverá realizar todo o procedimento novamente para devolver a solicitação ao coordenador do projeto.
* Finalizar como "Ajuste Retroativo de Frequência (pagto bolsa já efetuado)" Nesse caso, o coordenador estará aprovando uma frequência retroativa, ou seja, alguma atividade do bolsista que ficou com status "Não Iniciada" ou "Em Execução" e precisa ser encerrada. O sistema verificará se já houve solicitação de pagamento aprovada para o mês dessa atividade que está sendo lançada e informará ao coordenador caso o mesmo tente enviar novamente para a tarefa "Solicitar pagamento".

Uma decisão automática será executada baseado na identificação de bolsista voluntário (solicitação com plano de trabalho sem bolsa vinculada).

* Caso o bolsista seja voluntário, não será necessário realizar nenhum pagamento para o mesmo. O fluxo é concluído como "Bolsista Voluntário (Sem Pagamento)".
* Caso o bolsista **NÃO** seja voluntário, será necessário enviar o fluxo para a etapa "Solicitar Aprovação Pagamento", onde o coordenador (Pesquisa ou Extensão), verificará as bolsas a serem pagas e solicitará aprovação de pagamento.

Após solicitar aprovação de pagamento, o fluxo será encaminhado para o papel da "Reitoria" (Pesquisa ou Extensão) que realizará a aprovação dessa solicitação de pagamento. Nessa etapa o usuário terá as seguintes opções:

* Reprovar o pagamento concluindo o fluxo como "Pagamento Reprovado". Os dados são gravados na base RM com a solicitação de pagamento reprovada (SPROJSOLICITACAOPGTO).
* Enviar o fluxo para a etapa de "Realizar Pagamento Interno". Após o pagamento interno, caso existam bolsas de pagamento de fomento externo, o fluxo será encaminhado para a etapa "Realizar Pagamento Externo" (Atribuído ao último executor da atividade de aprovação de pagamento), caso não exista pagamento externo, o fluxo é encerrado na etapa "Pagamento Concluído".

Na etapa de "Realizar Pagamento Interno" o processamento acontecerá de forma automática (decisão automática), ou seja, o fluxo fará a geração do lançamento financeiro a pagar para cada bolsa de fomento interno que estiver associada à solicitação de pagamento. Nessa etapa o fluxo terá as seguintes opções:

* Caso aconteça algum erro na geração do(s) lançamento(s) financeiro(s), o fluxo permanecerá na etapa "Aprovar Solicitação Pagamento", onde o usuário vinculado ao papel de "Reitoria" (Pesquisa ou Extensão) deverá averiguar o problema e enviar novamente para a etapa de "Realizar Pagamento Interno".
* Se não houver nenhum problema na geração do(s) lançamento(s) financeiro(s), o fluxo terá duas opções:
  + Enviar para etapa de "Realizar Pagamento Externo" O fluxo verificará automaticamente se existem bolsas de fomento externo vinculados a solicitação de pagamento e enviará o fluxo para a etapa de "Realizar Pagamento Externo" (Atribuído ao último executor da atividade de aprovação de pagamento).
  + Concluir o fluxo como "Pagamento Concluído" Caso não existam bolsas de fomento externo, o fluxo será concluído como "Pagamento Concluído".

Para a correta geração do lançamento financeiro a pagar é necessário verificar alguns itens:

* A pessoa associada ao usuário do FLUIG deve ter um cliente/fornecedor vinculado, classificado como "Fornecedor". Esse vinculo deve ser feito através do processo "Vincular/Desvincular Cli/For" na visão de pessoa do TOTVS Educacional.
* Caso essa pessoa seja um funcionário da instituição, o vínculo do cliente/fornecedor deverá ser feito através do cadastro de funcionário.
* O cliente/fornecedor vinculado deve ter Defaults de Cli/For definidos para "Tipo de Documento".

As informações serão gravadas na base RM, vinculando o lançamento financeiro à bolsa de fomento interno e solicitação (SPROJSOLICITPGTOTIPOBOLSA e  SPROJSOLICITACAOPGTO)  
Na etapa de "Realizar Pagamento Externo" o coordenador de pesquisa terá apenas a opção de concluí-la como "Pagamento Concluído", visto que esse processo de pagamento externo será realizado por outro sistema fora das soluções TOTVS.
