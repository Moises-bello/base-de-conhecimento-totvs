---
content_hash: 3974514e031e26f47e95e0ab5a2c0d402d752e96ada636d225d1b321b892190f
fetched_at: '2026-06-29T00:08:56.551143+00:00'
page_id: '351381319'
product: rm
source: tdn-rm
title: RMSAU-3334 DT Integração PEP 2 com mais coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351381319
version: 9
---

# INTEGRAÇÃO PEP 2 COM MAIS COLIGADAS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Exportação de dados para a Central de Documentos do Pep |  |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Parâmetros de Integração Multi PEP. |  | |  |  | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMSAU-3334 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta funcionalidade tem o objetivo de compartilhar as informações contidas no PEP de uma coligada com a outra coligada através dos documentos na central de documentos do PEP. Os pacientes cadastrados em uma coligada serão copiados para a outra, assim como os atendimentos da coligada principal será transferida através de documentos.

Esta integração ocorrerá através de Jobserver agendados.

## Procedimento para Utilização

IntegracaoParametrizacaoParametrição

Para configurar a integração é necessário informar em cada coligada, qual será a coligada de destino em que os pacientes e atendimentos serão transferidos. Para isso, acesse o menu na nova MDI Opções / Parâmetros de Integração multi-Pep, pelo RMSaude.exe no menu Opções / Parâmetros / Parâmetros de Integração multi-Pep

A imagem abaixa indica que a coligada atual (2), se integra com a coligada 1 e 3.

Cada coligada ou empresa, deverá estar corretamente parametrizada com seus respectivos endereços do PEP e seus serviços. Para isso, acesse o menu Opções / Parâmetros / Parâmetros Gerais, página Integração, sub-página PEP 2. O campo em destaque é o endereço do serviço que receberá os arquivos com os dados dos atendimentos.

O processo pode ser agendado para executar automaticamente através de um JobServer . Para habilitar esta configuração deve utilizar o ambiente em 3 camadas, conforme o manual no link abaixo:

exportacaoExportação

EXECUTANDO O PROCESSO

Para executar o processo acesse RM.exe → Utilitários / Assistente de Exportação de dados para a Central de Documentos (PEP 2.0)

Parâmetros:

1 - Tipo de Relatório: Define o agrupamento dos atendimentos enviados no arquivo

(paciente) - envia um arquivo por paciente com os atendimentos do paciente agrupados

(atendimento) - envia um arquivo por cada atendimento

2- Relatório : Seleção do relatório que será gerado

3- Pasta de armazenamento na Central de Documentos: Informar a pasta onde os arquivos serão guardados (no local do PEP2)

4- Período da Exportação: Seleciona o período do qual os atendimentos serão exportados.

(Dia) - Envia apenas os atendimentos do dia atual

(Dia Anterior) - Envia apenas os atendimentos do dia anterior

(Carga Inicial (Todos os Registros)) - Irá enviar todos os atendimentos da base (ATENÇÃO, ESTE PROCESSO PODE DEMORAR ALGUMAS HORAS, DEVE SER FEITO APENAS NA PRIMEIRA EXPORTAÇÃO) recomendável executar com o tipo de relatório paciente para reduzir a quantidade de arquivos exportados.

Ao avançar (se configurado o ambiente em 3 camadas JobServer) selecione para executar "Agora" e clique em executar. Caso contrário o processo irá pular esta etapa.

O processo irá enviar arquivos para o PEP2 contendo os atendimentos do período selecionado, para os pacientes ainda não cadastrados na coligada de destino a exportação irá cadastra-los automaticamente e associar os documentos exportados a eles.

\* Para consistir os pacientes a serem cadastrados serão verificados os dados (Nome do Paciente, Data de Nascimento e Nome da Mãe)

O processo será realizado com sucesso (no caso de erro os logs serão gravados na tabela SZLOG)

AGENDANDO O PROCESSO

Para agendar o processo siga os mesmos passos da execução anterior, porém na tela de "Agendamento do processo" selecione a data desejada para que o processo aconteça e configure a frequência com a qual deseja que o mesmo seja realizado, em seguida clique em Executar (o processo não será disparado de imediato, somente na data ou período agendado).

Para verificar os processo agendados acesse Ambiente \ Gerenciamento de Jobs

O processo será mostrado como Exportação de Documentos para Central (PEP2)

Os arquivos exportados poderão ser visualizados no PEP2 da coligada de destino na aba DOCUMENTOS DO PACIENTE, onde haverá uma pasta com o nome informado anteriormente (Pasta de armazenamento na Central de Documentos) com os arquivos agrupados por paciente ou atendimento, e no layout do relatório informado na exportação.
