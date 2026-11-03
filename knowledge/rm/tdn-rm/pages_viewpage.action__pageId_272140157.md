---
content_hash: e7f700b641d931a4f4ec867dc1129c7c53aedc6dba5dca4f88b6e5ee7d91416e
fetched_at: '2026-06-29T00:08:29.007780+00:00'
page_id: '272140157'
product: rm
source: tdn-rm
title: MCP-1743 ER Eliminação de Resíduos - Integração Protheus (Stored Procedure)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272140157
version: 102
---

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Pedido de Material |
| **Segmento Executor** | Construção & Projetos | | |
| **Chamado/Ticket** | Não se aplica | | |
| **País** | (X) Brasil  (X) Argentina  (X) México  (X) Chile  (X) Paraguai  (X) Equador  (X) Colômbia | | |

   

## Objetivo

Processo disponibilizado na visão da funcionalidade de Pedidos de Materiais do TOTVS Obras e Projetos, e que tem como objetivo verificar a existência de resíduos eliminados no Protheus e atualizar a quantidade estornada do respectivo item no pedido, o que possibilitará que essa quantidade estornada possa ser pedida novamente. Esta rotina pode ser executada através da visão de pedidos de materiais ou ser agendada em ambiente configurado em três camadas. 

## Definição da Regra de Negócio

**Importante**: Este processo aplica-se somente em ambiente onde a integração entre o TOTVS Obras e Projetos e o Backoffice Protheus esteja sendo realizada via stored procedure.

## Configuração:

Acesse o Módulo ***Integração*** do RM, vá em ***"Ferramentas | Parâmetros"*** e clique em 'Avançar'.

Marque a integração ***"50.06 - TOTVS Obras e Projetos x BackOffice Protheus"*** e clique novamente no botão 'Avançar'.

Clique em ***"Configuração 2/2"*** e informe o Linked Server da Base Protheus.

Para mais informações sobre Linked Server acesse:

* MSSQL: <https://msdn.microsoft.com/pt-br/library/ff772782.aspx>;
* ORACLE: <https://docs.oracle.com/cloud/latest/db112/SQLRF/statements_5005.htm#SQLRF01205>.

O campo 'Usa Tabela Única PROTHEUS' se marcado indica que na base Protheus existe uma tabela para várias empresas, enquanto que, estando desmarcado, indica que cada empresa possui uma tabela.

Caso o campo 'Usa Tabela Única PROTHEUS' seja marcado, o sistema automaticamente habilitará os campos "Tabela Única Solicitações" e "Tabela Única Pedidos", para que sejam informados os nomes das respectivas tabelas que são utilizadas em todas as empresas.

Caso não utilize tabela única, informe as tabelas de Solicitações (SC1) e de Pedidos (SC7) para cada coligada.

Após ter fornecido essas informações, clique em 'Salvar Tabela(s)'.

Caso deseje, após ter salvo as tabelas poderá executar um teste através do botão 'Teste Conexão'.

Clique em 'Avançar' e em 'Concluir' para finalizar a parametrização.

## Utilização:

**Na Visão de Pedidos de Materiais**

1. Execute os processos necessários para eliminação de resíduos no Protheus (para maiores informações, pesquise por eliminação de resíduos em [http://tdn.totvs.com](http://tdn.totvs.com/));
2. Acesse a visão de pedidos de materiais  e selecione o pedido integrado com o Protheus;
3. Execute o processo "Verificar Eliminação de Resíduos". A execução dessa rotina não bloqueia o usuário, podendo o mesmo utilizar simultaneamente outras rotinas do sistema;
4. Analise a quantidade estornada dos itens do pedido.

Quando executada pela visão de pedidos, o sistema permite a escolha de um ou vários pedidos na Eliminação de Resíduos, sendo que todos os pedidos selecionados serão processados mesmo que já tenham sido processados anteriormente. Este comportamento visa possibilitar a atualização da quantidade estornada quando uma nota fiscal é excluída após o processo de Eliminação de Resíduos já ter sido executado no Protheus.

##### Agendamento (Somente Ambiente 3 Camadas)

1. Utilize o menu "Executar" à direita da aplicação RM;
2. Pesquise por "Verificar Eliminação de Resíduos - Agendamento" e execute;
3. Informe os dados necessários para o agendamento. Este processo necessita que sejam informadas a coligada e o projeto, porém, caso o usuário esteja logado no TOTVS Obras e Projetos em algum projeto, os sistema automaticamente terá essa informação;
4. Após a execução, analise a quantidade estornada dos itens do pedido.

Na execução por agendamento são verificados todos os pedidos do projeto que não tenham sido analisados em processamentos anteriores, o que significa que a execução por agendamento controla os pedidos verificados, ou seja, caso tenham sido finalizados ou já tenha ocorrido a sua eliminação de resíduos no Protheus o pedido não será reprocessado.

Quando processados via agendamento, os itens dos pedidos são marcados para não serem reprocessados de acordo com as seguintes regras:

* Considera que o pedido foi totalmente atendido, caso a totalidade da quantidade solicitada tenha sido contemplada na emissão da nota fiscal;
* Considera que houve eliminação de resíduos de acordo com a marcação nas tabelas do Protheus.

Após identificada a quantidade atendida, será automaticamente atualizado o campo quantidade estornada dos itens do pedido de material. Desta forma esta quantidade fica disponível para ser novamente utilizada em um novo pedido.

A exclusão da nota fiscal ou pedido do Protheus, interfere no saldo do pedido no TOTVS Obras e Projetos e neste caso, deve ser utilizada a sua visão de pedidos para filtrar aqueles que foram afetados pela exclusão e acionar o processo “Verificar Eliminação de Resíduos” para que o seu saldo seja atualizado.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Verificar Eliminação de Resíduos | Criação | Planejamento | Geração de Pedidos | Processos | Verificar Eliminação de Resíduos | Conforme descritas nesse documento |
| Verificar Eliminação de Resíduos - Agendamento | Criação | Executar | Verificar Eliminação de Resíduos - Agendamento | Conforme descritas nesse documento |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
