---
content_hash: dab31f82b9939df5a221397529f305c6ccbf50b3effeec99d07039ccaa9d359b
fetched_at: '2026-06-29T00:08:17.870371+00:00'
page_id: '259555849'
product: rm
source: tdn-rm
title: TVQIPW_DT_Envio_Email_Automatico_Avalicao_Pesquisa_Opiniao
type: documentation
url: https://tdn.totvs.com/display/LRM/TVQIPW_DT_Envio_Email_Automatico_Avalicao_Pesquisa_Opiniao
version: 121
---

#### EXECUÇÃO DE PROVAS - ENVIO DE E-MAIL AUTOMÁTICO AO FINALIZAR AVALIAÇÃO DO TIPO PESQUISA DE OPINIÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Avaliação e Pesquisa** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Execução de avaliações do tipo pesquisa de opinião* | *N/A* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | ***Envio de e-mail automático ao finalizar a avaliação*** | *N/A* | | ***Execução de avaliações pelo executor desktop (.exe)*** | *N/A* | | ***Execução de avaliações pelo executor web*** | *N/A* | | ***Execução de avaliações institucionais do TOTVS Educacional através do portal educacional*** | *N/A* | |
| **Cadastros Iniciais:** | *Cadastrar na central de notificações um e-mail (assunto e conteúdo) que será utilizado no e-mail, caso não exista o e-mail o sistema não fará a tentativa de envio.**Deve ser marcado o parâmetro de envio automático para avaliações do tipo 'Pesquisa de opinião' nos parâmetros de provas.**A pessoa que for executar a avaliação deve possuir um e-mail cadastrado no cadastro de pessoas.* |
| **Parâmetro(s):** | *Parâmetros | Parâmetros do sistema *|* Prova *|* Enviar e-mail após finalização para avaliações do tipo 'Pesquisa de opinião'* |
| **Ponto de Entrada:** | *Sistema:**Cadastros | Mensagens de notificação**Cadastros | Provas**Cadastros | Pessoas* |
| **Chamados Relacionados** | **TVYFXC** |
| **Requisito (ISSUE):** | - |
| **País(es):** | - |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *-* |
| **Sistema(s) Operacional(is):** | - |

## Descrição

Por padrão o TOTVS Avaliação e Pesquisa só faz o envio de e-mails automáticos quando a avaliação é do tipo 'avaliação de conhecimento' configurada para exibir resultados, com o parâmetro de envio de e-mail automático marcado e quando a avaliação é executada pelo executor desktop via webservice. Foi implantada uma melhoria no sistema para que faça o envio de e-mails automáticos também para avaliações do tipo 'pesquisa de opinião', sendo que este envio será feito pelo executor desktop (somente webservice) e pelo executor web (inclui avaliação institucional executada pelo portal educacional), não será feito o envio quando a avaliação for executada via arquivo offline através do executor desktop.

**Observação**: o envio automático **não será feito** quando a avaliação de pesquisa de opinião for configurada como "**confidencial**".

## Procedimento para Implantação

O envio automático de e-mails para avaliações do tipo pesquisa de opinião estará disponível a partir da versão 12.1.14, sendo necessário somente seguir os passos abaixo para configurar o envio.

## Procedimento para Utilização

## Sistema

É necessário ativar o parâmetro conforme abaixo: Parâmetros | Parâmetros do sistema | Prova |

### Mensagem que será utilizada para o envio

Se a mensagem não existir, é necessário criar uma nova, caso já exista edite conforme o padrão desejado.

Para criar ou editar acesse: Cadastros| Mensagens de notificação

Liste todas as mensagens, se não existir, crie uma nova ou edite a mensagem existente:

Selecione o tipo de mensagem: "E-mail para executores com informações sobre o final da avaliação do tipo pesquisa de opinião".

Informe o assunto da mensagem, informe o conteúdo da mensagem e caso necessário utilize o botão "Tags Disponíveis" para inserir valores de texto que serão substituídos pelos respectivos valores correspondente a prova e ao candidato que estiver executando no momento.

divs
