---
content_hash: 0d324f87c665bef5ca4e18bc1ec23df4efff1094926402d9ff87c888ed81a9be
fetched_at: '2026-06-29T00:08:33.984989+00:00'
page_id: '274639385'
product: rm
source: tdn-rm
title: DT Implementação do Parametrizador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274639385
version: 118
---

# Implementação do Parametrizador

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Gestão de Custos Hospitalares |
| **Rotina:** | |  | | --- | | **Rotina** | | Assistente de Implantação de Processos - Gestão de Custos |  |  | | --- | | **Rotina(s) envolvida(s)** | | Esquemas de Apuração | | Fechamento de Período | |
| **Requisito/S****tory/Issue:** | Informe o requisito relacionado (Issue). |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER®  Oracle® |
| **Tabelas Utilizadas:** | SZ0PARAMETRO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Foi implementado o parametrizador do módulo Gestão de Custos com o objetivo de habilitar a configuração dos parâmetros utilizados no sistema de forma nativa. A antiga tela de parâmetros será removida e toda a configuração já realizada será transferida para  a nova tela.

Para acessar o parametrizador, basta ir no menu "Sistema" > Ambiente > Parâmetros > Gestão de Custos.

O Parametrizador do Gestão de Custos está dividido em 3 grupos:

**Esquemas de Apuração**

Parâmetros relacionados ao processo de apuração dos esquemas (importação de dados de outros sistemas).  
Parâmetros configuráveis:

* Tamanho do Batch Size: este parâmetro tem a finalidade de indicar quantos registros serão enviados ao banco de dados para atualização (inclusão, alteração e/ou exclusão) na apuração dos esquemas com destino "Consumo Hospitalar".

**Fechamento do Período**  
Parâmetros relacionados aos processos do fechamento do período, como o processo do rateio, calculo dos custos de doação, refeição etc.  
Parâmetros configuráveis:

* Conta Custo Matmed: Indica as contas de custo que serão utilizadas no cálculo do custo variável indireto. Só devem ser informadas contas de custo do tipo "variável".
* Conta Custo Refeição: Indica as contas de custo que serão utilizadas no cálculo da refeição.
* Conta Custo Repasse: Indica as contas de custo que serão utilizadas no cálculo da refeição.
* Valor da doação e desconto deverá ser deduzido do custo variável durante o processo do calculo do rateio: Indica se o custo da doação será deduzido do custo variável no cálculo do rateio, dessa forma afetando o custo variável atribuído aos centros de custos e seu respectivo custo unitário (quando considerado o custo variável).
* Utiliza cálculo de Doação e Desconto: Indica se o cálculo de doação e desconto será utilizado. Ativando esse parâmetro a opção da execução desse cálculo será exibida no processo de fechamento do período.
* Sentença do Custo da Doação: código da sentença sql (cadastrada no sistema) que retornará o valor total de doação e desconto. Esta sentença será utilizada no processo do cálculo do custo da doação e desconto, no fechamento do período.
* Utiliza cálculo da Refeição: Indica se o cálculo de refeição e desconto será utilizado. Ativando esse parâmetro a opção da execução desse cálculo será exibida no processo de fechamento do período.
* Utiliza cálculo do Repasse: Indica se o cálculo de repasse e desconto será utilizado. Ativando esse parâmetro a opção da execução desse cálculo será exibida no processo de fechamento do período.
* Tipo de Custo do MatMed: Indica o tipo de custo do MatMed, sendo "Custo Médio" e "Último Preço". Este parâmetro é utilizado no cálculo do Custo Variável Direto e vai indicar de onde o sistema irá recuperar o custo do matmed, se do cadastro do custo médio ou se irá recuperar o último custo informado no consumo hospitalar.

**Relatórios**  
Parâmetros utilizados na geração dos relatórios através do RM Reports.

* Código Critério Rateio da Área Ocupada: Indica o critério de rateio utilizado nos relatórios.
* Código Critério Rateio do Número de Funcionários: Indica o critério de rateio utilizado nos relatórios para exibir a quantidade de funcionários de um centro de custos. Exemplo de relatório que utiliza o parâmetro: Distribuição de Custos do Centro de Custo.

## Procedimento para Utilização

1. No módulo Gestão de Custos Hospitalares acesse Sistema > Ambiente > Parâmetros > Gestão de Custos.
2. Na janela que será aberta clique em "Avançar".
3. Escolha o processo que deseja configurar.  
   Pode ser selecionado um processo específico ou pode ser selecionada a opção "Gestão de Custos" para exibir todos os parâmetros de uma só vez.
4. Configure os parâmetros desejados.
5. Clique em "Avançar".
6. Valide as alterações que serão realizadas.  
   Parâmetros em forma de lista (como a lista de conta de custos) não são exibidos nessa tela.
7. Clique em "Concluir".
8. Clique em 'Sim" na mensagem exibida.

divs
