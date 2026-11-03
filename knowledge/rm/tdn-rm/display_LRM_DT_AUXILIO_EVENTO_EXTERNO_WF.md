---
content_hash: 9e1be02308d43c21fbccf0c7d8dbf9e1bac12fc10bbce5477e578aa206605829
fetched_at: '2026-06-29T00:08:32.565345+00:00'
page_id: '273991070'
product: rm
source: tdn-rm
title: DT_AUXILIO_EVENTO_EXTERNO_WF
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_AUXILIO_EVENTO_EXTERNO_WF
version: 3
---

# Auxílio para eventos externos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | ***********Inovação,********** Pesquisa e Extensão* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Auxílio para eventos externos* | **Auxílio para eventos externos** | |
| **Cadastros Iniciais:** | *Pesquisador* |
| **Requisito (ISSUE):** | *PCREQ-5449* |
| **País(es):** | *Brasil* |
| **Tabelas Utilizadas:** | *SEXTAUXILIOVISITA e SEXTTIPOAUXILIO* |
| **Versões/Release:** | *12.1.15* |

## Descrição

O auxílio para eventos externos permite ao usuário gerenciar as solicitações de reembolso realizadas através de solicitações do FLUIG.

Pré-requisitos para utilizar a solicitação de auxílio para eventos externos

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de solicitação de visitas técnicas/participação em eventos. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.
  + Código = **aprov\_evento\_externo**| Descrição = **Aprovador de evento externo**
  + Código = **aprov\_evento\_externo\_doc**| Descrição = **Aprovador de documentação**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Importar o fluxo de solicitação de visitas/eventos para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos da solicitação de visitas/eventos.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

O usuário, vinculado ao papel "Pesquisador", deverá iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Visita Técnica/Evento | Auxílio para eventos externos". Ao selecionar esse fluxo será apresentado um formulário com o código do pesquisador vinculado ao usuário do FLUIG. Nele deverão ser informados os dados referentes ao auxílio do evento externo, tais como: Título do evento, local do evento, data inicial, data final, tipos de auxílios, etc, . Após o preenchimento do formulário, o fluxo avançará para a atividade "Aprovar solicitação de auxílio", onde um usuário vinculado ao papel "Aprovador evento externo" deverá validar os dados referentes a aprovação da solicitação e preencher os dados referentes ao lançamento a ser gerado, tais como: Coligada do pesquisador, filial do pesquisador, cliente/fornecedor, data de vencimento e valor do lançamento. Após entrar com as informações necessárias ele terá 3 opções:

* Retornar para a atividade "Solicitar auxílio (retorno)";
* Reprovar a solicitação;
* Avançar para a atividade "Analisar documentação".

Na atividade "Analisar documentação" o usuário, vinculado ao papel "Aprovador de documentação", deverá validar a documentação que foi anexada na solicitação e definir encaminhar a solicitação para 3 opções:

* Retornar para a atividade "Solicitar auxílio (retorno)"
* Cancelar a solicitação.
* Avançar para a atividade "Gerar lançamento".

Na atividade "Gerar Lançamento" será gerado lançamento a pagar (a instituição paga ao solicitante). Durante a geração dos lançamentos poderão surgir mensagens de aviso devido a falta de parametrização de dados, conforme nota abaixo: 

Lançamento a pagar

Para a correta geração do lançamento financeiro a pagar é necessário verificar alguns itens:

* A pessoa associada ao usuário do FLUIG (solicitante do auxílio de evento externo) deve ter um cliente/fornecedor vinculado, classificado como "Fornecedor". Esse vinculo deve ser feito através do processo "Vincular/Desvincular Cli/For" na visão de pessoa do TOTVS Educacional.
* Caso essa pessoa seja um funcionário da instituição, o vínculo do cliente/fornecedor deverá ser feito através do cadastro de funcionário.
* O cliente/fornecedor vinculado deve ter Defaults de Cli/For definidos para "Tipo de Documento".
