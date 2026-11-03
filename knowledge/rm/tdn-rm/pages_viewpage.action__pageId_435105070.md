---
content_hash: e04577433dc3d0cd73d1bdbb8d181e7f13ead0402d982003ce5d8e8809e41c3d
fetched_at: '2026-06-29T00:09:47.775003+00:00'
page_id: '435105070'
product: rm
source: tdn-rm
title: Relatórios - Plano Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105070
version: 12
---

O Plano Financeiro é o resultado final do trabalho de um planejamento financeiro. No Plano financeiro serão apresentadas todas as informações relevantes levantadas durante o processo de planejamento, como o fluxo de caixa, o orçamento e o balanço patrimonial, elaborados para a análise dos dados, estratégias desenvolvidas e a agenda de implantação e revisões periódicas do plano. O plano financeiro é a ferramenta que de fato permite acompanhar e mensurar a evolução do trabalho de planejamento financeiro ao longo do tempo e avaliar se a pessoa está ou não tendo sucesso na execução de seu planejamento financeiro.

**Pré-Condições:**

**1-** Ter permissão para Executar o processo [Importar Relatórios] do RM Reports. Para obter a permissão acesse: TOTVS RM/ Serviços Globais/ Segurança/ Perfis/ Contexto- [Projeto/ Incorporação]. Edite o perfil e acesse: Acesso a Menus / Gestão/ Ferramentas de Análise/ RM Reports/ Processos/ Importar Relatórios. 

**2-** Ter importado a estrutura dos relatórios abaixo  pelo caminho: TOTVS RM/ Projetos/ Incorporação/ Gestão/ RM Reports/ Processos/ Importar Estrutura de Relatório:

* FF001 Ficha Financeira Analítica
* FF002 Ficha Financeira Sintética
* FFSPF002 Ficha Financeira Sintética
* PA003 Parcelas em Aberto
* PE001 Pagamentos Efetivos
* RD001 Registros Diários

**Executando os relatórios do Plano Financeiro**

**Passo 1-** Acesse: TOTVS RM/ Projeto/ Incorporação/ Relatórios/ Plano Financeiro.

**Passo 2-** Será exibido o formulário responsável por gerar o relatório desejado. Os  campos de preenchimento obrigatório são exibidos na ela destacados em negrito. Os campos do formulário são:

* **Relatório:** Campo responsável por definir qual relatório será executado, de acordo com as estruturas de relatório que foram importadas na pré-condição 2.
* **Data base:** Informe uma data para verificar os valores de Juros de Mora e Multa.
* **Imprimir Resíduo:** Caso houver resíduo calculado, será impresso no relatório o valor do resíduo.
* **Considerar Multa e Juros:** Com este parâmetro marcado, o Juros e a Multa serão calculados na data base informada.
* **Filtrar por:**  Exibida a opção  de filtrar por Empreendimento ou por Cliente
* **Empreendimento/Cliente:** Campo qual deve ser informado  um código de Empreendimento se for definido o filtro por Empreendimento  ou  então  informado o código do Cliente  se for definido o filtro por Cliente.
* **Venda:** Campo responsável por filtrar o relatório para recuperar dados de uma venda específica
* **Situação da venda/aluguel:** Informe qual a situação da venda será exibida no relatório.
* **Início e Fim:**  Campos responsáveis por permitir ao usuário selecionar um período. Este campo será exibido se for selecionado o relatório de Registros Diários.

**Passo 3-** Selecione o [Relatório], Selecione o radioButton [Empreendimento] ou [Cliente]. 

**Passo 4-** Informe  o [Empreendimento ou Cliente]. 

**Passo 5-** Informe a [Venda] e clique em [Executar].
