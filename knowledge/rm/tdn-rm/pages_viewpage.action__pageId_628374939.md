---
content_hash: d171b7da99de3a607edc92feb95abb2e2a2e57914efeb34f1d3afb64c9ca0dc3
fetched_at: '2026-06-29T00:11:05.145424+00:00'
page_id: '628374939'
product: rm
source: tdn-rm
title: Cópia de DT_PROJETO_INOVACAO_WF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628374939
version: 1
---

# Projeto de Inovação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | **Inovação, Pesquisa e Extensão** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Projeto de Inovação* | *Projeto de Inovação* | |
| **Cadastros Iniciais:** | *Cadastro de Pessoa* |
| **Requisito (ISSUE):** | **PCREQ-5447** |
| **País(es):** | *Brasil* |
| **Tabelas utilizadas:** | *SINOVINVENTO, SINOVINVENTOR,* *SINOVINVENTOTIPOPROGRAMA,*  *SINOVINVENTOAPLICACAO, SINOVPARECER, SINOVPROTOCOLO, PPESSOA* |
| **Versões/Release:** | *12.1.15* |

## Descrição

O projeto de inovação permite ao usuário gerenciar (solicitar, aprovar e registrar) as atividades de inovações tecnológicas, podendo ser classificados em Cultivares/Biológicos, Desenho, Engenharia,  Marcas, Obras literárias e Software.

Pré-requisitos para utilizar o projeto de inovação

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo do projeto de inovação. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.
  + Código = **gestor\_processo**| Descrição = **Gestor de Processo**
  + Código = **inovacao**| Descrição = **Inovação**
  + Código = **contrato\_inovacao**| Descrição = **Contrato de Inovação**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Importar o fluxo do projeto de inovação para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos do projeto de inovação.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

O usuário deverá iniciar o projeto de inovação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Projeto de Inovação | Projeto de Inovação". Ao selecionar essa opção será aberto um formulário com o código do usuário logado e a data corrente. Nele deverão ser informados os dados do invento e dos inventores da tecnologia. Após registrar o processo o fluxo avançará para a atividade "Avaliar Invento", onde um usuário vinculado ao papel "Inovação" terá duas opções:

* Avançar para a atividade "Invento Aprovado".
* Avançar para a atividade "Invento Reprovado", onde o invento será reprovado e o fluxo finalizado.

Na etapa "Invento Aprovado" será verificado o valor do campo "Inventor independente", existente no formulário de cadastro. Se ele estiver desmarcado o fluxo avançará para a atividade "Assinar Declaração de Inventores e/ou Contrato", porém, se o campo estiver marcado o fluxo será encaminhado para a atividade "Elaborar Contrato", onde um usuário vinculado ao papel "Contrato de Inovação" irá elaborar o contrato para inventores independentes. Esse processo pode ocorrer quantas vezes forem necessárias, até que o contrato esteja de acordo com o solicitado.

Após a criação do contrato ele será anexado ao processo e o fluxo avançará para a atividade "Avaliar Contrato", onde um usuário vinculado ao papel "Inovação" irá verificar se o contrato está condizente para assinatura do inventor. Esse processo pode ocorrer quantas vezes forem necessárias, até que o contrato esteja de acordo com o solicitado. Passando por essa avaliação o fluxo será encaminhado para a atividade "Assinar Declaração de Inventores e/ou Contrato", que será assumida pelo inventor que iniciou o processo. Se ele for um inventor independente o contrato e a declaração de inventores deverão ser assinados, porém se o inventor não for independente será necessário assinar apenas a declaração de inventores. Assim que a declaração de inventores for assinada o fluxo avançará para a atividade "Avaliar Documentação (Inovação)", onde o usuário vinculado ao papel "Inovação" irá avaliar a documentação e definirá se ela está pertinente. Ele terá três opções:

* Avançar para a atividade "Avaliar Documentação (Gestor)".
* Avançar para a atividade "Solicitar Pedido de Reconsideração", caso a documentação seja reprovada.
* Avançar para a atividade "Solicitar Documentação para Depósito".

Na etapa "Avaliar Documentação (Gestor)" um usuário vinculado ao papel "Gestor de processo" irá avaliar toda a documentação e definirá se ela está pertinente. Caso ela seja aprovada, o fluxo será encaminhado para a atividade "Solicitar Documentação Para Depósito", caso contrário o fluxo avançará para a atividade "Solicitar Pedido de Reconsideração". Na etapa "Solicitar Pedido de Reconsideração" o inventor que iniciou o processo irá avaliar as considerações pela reprovação da documentação e realizará os ajustes necessários para solicitar nova avaliação. Após avaliar a documentação na etapa "Avaliar Pedido de Reconsideração", o usuário vinculado ao papel "Gestor de processo" terá três opções:

* Retornar para a atividade "Solicitar Pedido de Reconsideração".
* Avançar para a atividade "Processo Arquivado", onde o processo será arquivado e o fluxo finalizado.
* Avançar para a atividade "Solicitar Documentação para Depósito".

Na etapa "Solicitar Documentação para Depósito" o usuário, vinculado ao papel "Inovação", indicará ao solicitante a documentação necessária para realizar o depósito. Assim que documentação for indicada, o fluxo será encaminhado para a atividade "Providenciar Documentação Para Depósito". Nessa etapa o inventor que iniciou o processo deverá providenciar toda documentação para realizar o depósito do invento. Esse processo pode ocorrer quantas vezes forem necessárias, até que a documentação esteja de acordo com o solicitado. Após providenciar a documentação o fluxo avançará para a atividade "Analisar Documentação", onde u usuário vinculado ao papel "Inovação" deverá verificar a documentação entregue. Assim que a análise chegar ao fim o usuário terá duas opções:

* Retornar para a atividade "Providenciar documentação para depósito".
* Avançar para a atividade "Reunião Para Elaboração do Relatório".

Na etapa "Reunião Para Elaboração do Relatório" o inventor que iniciou o processo deverá convocar uma reunião com os interessados. Após a elaboração do relatório o fluxo deverá seguir para a atividade "Registrar/Manter INPI". Nessa etapa o usuário vinculado ao papel "Inovação" deverá preencher os dados referentes aos protocolos do INPI. Assim que esses protocolos forem preenchidos, o usuário terá duas opções:

* Avançar para a atividade "Agendar Vencimentos".
* Finalizar o fluxo.

Na etapa "Agendar Vencimentos" o usuário vinculado ao papel "Inovação” poderá finalizar o processo ou criar dados de alerta (Atividades Ad-Hoc), assim serão geradas novas tarefas para o responsável ficar ciente dos compromissos futuros para as patentes. Assim que todos os responsáveis concluírem suas tarefas o fluxo poderá ser finalizado.

Cancelamento do processo no Fluig

Caso o processo no Fluig seja cancelado, a solicitação de registro receberá o status de "**Cancelada**", mas não será excluída da base de dados do TOTVS Educacional.
