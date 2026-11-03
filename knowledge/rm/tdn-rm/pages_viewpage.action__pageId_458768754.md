---
content_hash: 912a9db7110711191b70ef1667d6ffc85c65464c353ebe1257434b1994f23531
fetched_at: '2026-06-29T00:10:13.888017+00:00'
page_id: '458768754'
product: rm
source: tdn-rm
title: DT Alteração de contextos dos módulos do Educacional (Educacional/Processo
  Seletivo/Avaliação e Pesquisa/Biblioteca)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458768754
version: 91
---

# ALTERAÇÃO DOS CONTEXTOS DOS MÓDULOS DO EDUCACIONAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Totvs Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Alteração de contexto* | **Alteração de contexto do Educacional** | |
| **Cadastros Iniciais:** | * *Cadastro de coligada;* * *Cadastro de filial;* * *Cadastro de nível de ensino;* * *Cadastro de unidade bibliotecária.* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *EDUCACIONAL01-8110* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows 7, 8 e 10* |

## Descrição

Criação de um processo para a simplificação da alteração do contexto nos módulos do Educacional. Entre eles: Gestão Educacional, Processo Seletivo, Avaliação e Pesquisa e Gestão Bibliotecária.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.24.

Alteração de contexto

De forma a simplificar a alteração de contexto dos módulos do Educacional, foi criado um processo que permite a alteração de todos os itens que fazem parte do contexto em uma mesma tela.

Hoje, temos 04 sistemas que compõem os módulos do Educacional: Gestão Educacional, Processo Seletivo, Avaliação e Pesquisa e Gestão Bibliotecária.

Cada sistema possui seu nível de contexto que podem chegar a 3 níveis.

Entre eles:

* Gestão Educacional: Coligada, Filial e Nível de ensino.
* Processo Seletivo: Coligada e Filial (**OBS.:** Podendo ser selecionado o nível de ensino por compartilharem o mesmo código de sistema)
* Gestão Bibliotecária: Coligada, Filial e Unidade Bibliotecária.
* Avaliação e Pesquisa: Coligada

O menu para acionamento do processo de alteração de contextos dos módulos do Educacional será localizado ao lado do menu de alteração de contexto global, conforme imagem abaixo:

Caso a filial, o nível de ensino ou a unidade bibliotecária contenha apenas um 01 item para seleção, esse será carregado automaticamente, sem a necessidade de uma seleção.

**Busca rápida de contexto:**

A busca rápida de contexto permite a busca de um contexto de forma geral, o campo busca pelo valor informado em todos as opções possíveis de contexto, ou seja, irá buscar em todos os campos do contexto do módulo.

A medida que for inserido o termo a ser pesquisado, o sistema irá retornar e filtrar os valores, pode ser informado um ou mais termos separados por espaço, o sistema irá fazer o refinamento do filtro conforme os valores pesquisados, sendo necessário somente clicar no valor retornado para alterar o contexto.

Exemplo: se for informado no campo de busca o valor "Ensino" no contexto do TOTVS Educacional ou TOTVS Processo Seletivo, a busca será feita no campo coligada, filial e nível de ensino, assim, retornando todos os valores onde o termo for encontrado, no caso do TOTVS Gestão Bibliotecária será considerados os campos coligada, filial e unidade bibliotecária, para o TOTVS Avaliação e Pesquisa somente o campo coligada. .

Ao parar o ponteiro do mouse sobre os itens retornados, será exibido o código e descrição do item onde o ponteiro do mouse se encontra.

# Versão 12.1.25

À partir da versão 12.1.25 o sistema irá permitir a definição de contextos favoritos e também uma lista de últimos contextos acessados. 

**Favoritos**

Ao clicar no ícone de favorito (estrela) nas linhas retornadas pela busca, o sistema grava o contexto como favorito ou remove o favorito se este for um contexto favorito.

Ao lado do campo de busca o sistema irá listar todos os favoritos definidos pelo usuário, sendo que é possível também remover o item do favoritos, sendo necessário somente clicar no ícone favorito que instantaneamente o contexto é removido da lista de contextos favoritos.

**Últimos contextos**

O sistema irá listar em ordem do mais recente, os contextos acessados pelo usuário, na lista de últimos contextos, também é possível marcar ou desmarcar um contexto como favorito.

Além das funcionalidades acima mencionadas, foi disponibilizado o menu cascata o mesmo é um facilitador na troca de contexto do Educacional. A cascata será exibida ao clicar no ícone sinalizado abaixo.

No menu cascata também é exibido o campo de busca rápida (Buscar contexto:) com o mesmo comportamento do que foi disponibilizado na tela de troca de contexto.

Uma lista de contextos favoritos e uma lista de últimos contextos acessados é exibida neste menu, sendo limitado a dez favoritos e cinco últimos acessados. Entretanto, se o número de favoritos for menor que dez, o mesmo será utilizado pela lista de últimos acessos.

Ao clicar no botão **mais contextos...** é exibido a tela de contextos, conforme abaixo.

  

divs
