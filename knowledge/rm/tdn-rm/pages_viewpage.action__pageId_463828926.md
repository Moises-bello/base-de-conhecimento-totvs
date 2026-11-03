---
content_hash: e9ea16bd5afce6d20a6ce20ba40cdefc1fb026b0d0de1560a63f2e2674f522e8
fetched_at: '2026-06-29T00:10:15.307651+00:00'
page_id: '463828926'
product: rm
source: tdn-rm
title: DT Cálculo de Pagamento da Folha de Produtividade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463828926
version: 14
---

# CÁLCULO DE PAGAMENTO DA FOLHA DE PRODUTIVIDADE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **Gestão de Obras e Projetos*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Pagamento por Produtividade | Pagamento por Produtividade | |  |  | |
| **Cadastros Iniciais:** | Projeto, Insumos, Funções, Equipe de Mobilidade, Tarefas |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Tickets relacionados** | *Não se aplica.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | TOPORCAPLAN001-6688 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | **SQL Server e Oracle** |

## Descrição

Será criada uma nova tela onde serão gerados os valores referentes aos pagamentos da folha de produtividade.

Nesta nova tela poderá ser observado os arquivos gerados com seus devidos detalhamentos por funcionário e tarefa.

Para acessar a tela será utilizado o menu

: 

Nova tela criada:

## Processo para geração dos dados de um novo arquivo

Será criado um processo para a geração dos dados de um novo arquivo. Este processo terá como parâmetros data inicial e final, ano, mês e período de competência, evento da folha de pagamento e data de pagamento.

Após a geração dos dados, será possível gerar o arquivo com os dados do pagamento para a importação do mesmo.

Para o campo "Evento", existe o parâmetro de projeto em Mobilidade/Folha Tarefa que é o valor padrão que será considerado no processo. Para permitir a alteração desse valor na tela, é necessário alterar a permissão de alteração no cadastro de perfis do usuário.

Após a execução do processo, é exibido no log do mesmo, todo o relato do cálculo do pagamento para os funcionários:

## Cálculo dos valores a serem gerados

O percentual do Avanço Físico depende do período de apuração selecionado, como no exemplo abaixo:

* 30% em 01/01/2019
* 40% em 03/01/2019
* 50% em 05/01/2019
* 70% em 20/01/2019
* Ex.1: Período de Apuração: 05/01/2019 à 31/01/2019
  + Percentual real: 70 - 40 = 30%
* Ex.2: Período de Apuração: 01/01/2019 à 31/01/2019
  + Percentual real: 70%

## Processo para geração de um novo arquivo

O arquivo poderá ser gerado no formato para RM ou Protheus.

Foi criado um novo processo para geração do arquivo com os dados do pagamento de Produtividade, Menu Controle | Mobilidade | Pagamento por Produtividade | Processos | Gerar Arquivo de Pagamento por Produtividade;

Para execução do processo de geração de arquivo foi criado um objeto gerencial '**TOPLAY0005 - Exportação de Dados- Pagamento Por Produtividade**';

* Informe o Layout Gerador de Saida;
* Informe o local onde serão gerado o(s) arquivo(s);

O arquivo RM deve respeitar o seguinte layout: <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.LayoutFichaFinanceira.aspx>

**Importação do Arquivo - Folha de Pagamento**

Para realizar a importação do(s) arquivo(s) gerado(s), deve-se cadastrar um layout de importação. No módulo de Folha de Pagamento acesse Menu Configurações | Importações | Layout de Importações;

O cadastro deve seguir a seguinte estrutura:

Após o cadastro o sistema estará apto a receber a importação para o Envelope de Pagamento. Acesse Menu Configurações | Importações | Layout de Importações | Processos | Importação da Ficha Financeira;

* Selecione o arquivo gerado através do processo;
* Escolha a ação desejada referente a importação para o envelope;
* Executar;

Procedimento para importação no Proheus:
