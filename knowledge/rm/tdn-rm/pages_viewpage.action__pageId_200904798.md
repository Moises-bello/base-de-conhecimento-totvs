---
content_hash: 58bbacc32419026c8793c66cc129cbefe7e08247fc846761afbf9446a94f09ef
fetched_at: '2026-06-29T00:06:04.028065+00:00'
page_id: '200904798'
product: rm
source: tdn-rm
title: DT_Alocação_de_Acomodação_para_Paciente_Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=200904798
version: 9
---

# Alocação de Acomodação para paciente externo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Atendimento |
| **Rotina:** | |  | | --- | | **Rotina** | | Alocar acomodação |  |  | | --- | | **Rotina(s) envolvida(s)** | | Classe de leito, Painel de classificação de risco | |
| **Cadastros Iniciais:** | Cadastros de classes de leito, cadastro de leitos |
| **Requisito (ISSUE):** | [PCREQ-6796](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-6796 "PCREQ-6796") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.7 |

## Descrição

Esta melhoria possibilita a alocação de acomodações do tipo "Leito virtual" para pacientes de pronto atendimento a partir do painel de classificação de risco. Para que este processo seja possível, é necessário criar uma classe de leito que caracterize os "leitos" do PA e informar o tipo de acomodação como "**ACOMODAÇÃO PARA PACIENTE EXTERNO**". Somente os leitos caracterizados com essas classes é que serão exibidos para alocação.

No Painel de Classificação de Risco, após o médico colocar o paciente em observação, esse paciente já poderá ser alocado em um leito. Para isso, o usuário deve ser do perfil de enfermagem ou técnico em enfermagem e acessar o painel de classificação de risco. Ao selecionar a unidade de atendimento, aparecerá a página Pacientes em Observação. Selecionando o paciente, o botão **Alocar Acomodação** ficará habilitado. Será exibido o Painel de Leitos, basta selecionar um leito.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação da BibliotecaRM 12.1.7

1. Aplique o patch do chamado e execute uma vez a rotina do Painel de Classificação de Risco.

## Procedimento para Utilização

       1.            No menu **Cadastros / Registro e Controle /Classes de Leito**, crie classes de leito com o tipo de acomodação "**ACOMODAÇÃO PARA PACIENTE EXTERNO**".

       2.            No menu **Cadastros / Registro e Controle / Leitos**, crie os leitos, box para a acomodação dos paciente de pronto atendimento informando a classe de leito criada no item 1.

       3.            Para utilizar esses leitos, o sistema disponibiliza um botão no Painel de Classificação de Risco. Acesse com um perfil de enfermagem e será exibida a página Pacientes em observação. Somente os pacientes em observação é que podem ser alocados nesses "leitos".

       4.            Selecione um paciente em observação, clique no botão "**Alocar Acomodação**" e será exibida um painel com os leitos classificados como o cadastrado no item 1.

       5.            Selecione um leito livre e o mesmo será alocado para o paciente.

       6.            Utilizando o processo de alta, o "leito" será liberado na saída do paciente.
