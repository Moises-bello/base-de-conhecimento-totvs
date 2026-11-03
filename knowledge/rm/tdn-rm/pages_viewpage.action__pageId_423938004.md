---
content_hash: 088fd3834d351171cd8e3cd732cb6b886fa9c26a0870ec41dd5cac3a8cd267e2
fetched_at: '2026-06-29T00:09:24.711810+00:00'
page_id: '423938004'
product: rm
source: tdn-rm
title: Novidades Versão PAT 11.50
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938004
version: 17
---

**11.52.56** - [Integração com o Totvs Gestão de Compras](http://tdn.totvs.com/x/6shEGQ)  
Adicionado no processo de integração de aquisição de itens do movimento (Nucleus) a opção "Trazer o rateio de centro de custo do item de movimento para o rateio gerencial do Patrimônio" Caso este parâmetro esteja marcado, o sistema deverá pegar as contas gerenciais vinculada ao centro de custo do rateio de centro de custo do item e gerar como rateio do patrimonnio que será criado.

* Cadastros de Patrimônio
* Implentada a funcionalidade que permite alterar o código do patrimônio.
* Implementado o campo "Valor Base de Depreciação" no cadastro de patrimônios, que será preenchido automaticamente com o conteúdo do campo "Valor de Aquisição". Todos os processos (Geração das moedas/índices, cálculo de depreciação) que forem aplicados sobre os patrimônios, passarão a ser feitos sobre o "Valor Base de Depreciação" e não mais sobre o "Valor de Aquisição". Atualmente este campo não pode ser editado, entretanto esta demanda estará liberada em versões futuras. Caso deseje antecipar a utilização do mesmo, é necessário entrar em contato com o suporte e solicitar um script que liberá a edição do campo.

**11.52.50 -** Geração de Relatórios.Net  
Os relatórios do book foram aprimorados para a utilização em .Net, sendo estes liberados nesta versão. Para emitir-los deve ser utilizado o [RM Reports](http://tdn.totvs.com/x/v8dEGQ). Na primeira utilização é necessario importar os arquivos dos relatórios, que estão disponioveis no diretório padrão: C:\totvs\CorporeRM\_ImpExp\Sugeridos

**11.51.45 –** Melhorias internas no sistema**.**  
   
**11.51.40 -** Importação/Exportação de Conceito  
Liberados os arquivos (.icp) que permite a utilização da ferramenta [Conceito](http://tdn.totvs.com/x/I8lEGQ) para importar e exportar dados.  
   
**11.51.35** - Alteração de Múltiplos Patrimonios  
Implementada a funcionalidade que permite alterar informações de um ou mais registros de forma simultânea.  
   
**11.50.0** - Cadastros Patrimônio  Migração do cadastro e processos relacionados aos Bens, bem como alteração de sua identificação (passando a se chamar Patrimônio) de forma a se adequar ao Patrimônio.Net.  
Taxas de Depreciação Atualização do cadastro de taxas de depreciação de forma que os cálculos relacionados aos patrimônios respeitem as taxas e as moedas associadas a ele.  
Grupo de Patrimônio Migração do cadastro referente ao grupo de contas bem como alteração de sua identificação (passando a se chamar grupo de patrimônio) a fim de atender as regas do Patrimônio.Net.  
Saldo do Patrimônio em Moeda/ìndices: Implementado o cadastro de saldo do patrimônio por moeda de forma a permitir que sejam incluídos, alterados e excluídos os saldos respeitando as particularidades referentes aos cálculos associados ao patrimônio.  
Cenários de cálculos Implementado o cadastro de cenários onde se podem associar cálculos, moedas e índices com o objetivo de serem utilizados nos patrimônios.  
Cálculos Implementada a funcionalidade referente ao cadastro de cálculos de forma a permitir que sejam definidas informações como o tipo de cota e inicio da periodicidade a serem, posteriormente, utilizados para calcular os valores dos patrimônios.  
Cálculo de depreciação Adaptado o cálculo referente aos valores de depreciação e correção de patrimônios, tanto de moeda quanto de índice, que sofreram ou não alterações decorrentes de ocorrências para atender ao Patrimônio.Net.  
Apólice de Seguros Implementados o cadastro referente a apólices de seguros e o processo que permite associar as apólices aos patrimônios existentes na base de dados baseando-se nas regras do Patrimônio.Net.  
Motivos de Baixa Atualização do cadastro referente aos motivos de baixas de forma a atender as regras do Patrimônio.Net.  
Default Contábil Migração do cadastro de default contábil de forma a serem exibidos no Grupo de Patrimônio, Patrimônio, Motivo de Baixa e Cenários atendendo as exigências do Patrimônio.Net.  
Controle de Garantias do Patrimônio Implementado o Controle de Garantia do Patrimônio de forma que seja possível incluir, alterar ou excluir uma garantia partir da tela do Patrimônio.Net.

**11.50.0** - Ocorrências  
Baixa, Acrescimo e Transferência Monetária  
Migração do processo de ocorrências referente às Baixas Automáticas (Parcial e Total), Acréscimos e Transferências Monetárias (parcial e total) bem como suas respectivas exclusões de forma a se adequar as novas regras do Patrimônio.Net.  
Consulta de Ocorências: Realizada da migração da visão de ocorrências (Baixa - Parcial e Total, Acréscimo e Transferência Monetária - Parcial e Total).  
Transferência de Controle  
Migração do processo de Transferência Física de bens para o novo processo chamado Transferência de Controle de forma a atender a estrutura do Patrimônio.Net  
[Exclusão de cálculos](http://tdn.totvs.com/x/Q8lEGQ) Implementado o processo que permite realiza a exclusão de cálculos de um ou vários patrimônios bem como suas ocorrências (somente para Baixa e Acréscimo) no período de cálculo atual.

**11.50.0** - Inventário  
Layout de Inventário Migração do processo responsável pela importação de inventário bem como os cadastros relacionados a este recurso de forma a se adequar ao Patrimônio.Net.

**11.50.0** - Integração com o Totvs Gestão de Compras  
[Integrar Aquisições Compras](http://tdn.totvs.com/x/6shEGQ) Migrado o processo que permite realizar integração de imobilizados adquiridos através do Totvs Gestão de Compras.  
[Integrar Aquisições Pendentes](http://tdn.totvs.com/x/8MhEGQ) Implementado processo que permite completar informações e integrar as aquisições pendentes adquiridas através do Totvs Gestão de Compras.

**11.50.0** - Integração com o Totvs Gestão Contábil  
Contabilização: Migração dos processos que permitem realizar a contabilização de Aquisição de patrimônios, Ocorrências (Baixa, Acréscimo e Transferência Monetária), Depreciação/Correção e Transferência de Controle a fim de que, posteriormente, sejam integrados ao sistema contábil.  
Visualização de Contabilizações Recurso implemtentado com a finalidade de exibir todas as informações referentes as contabilizações (aquisição, ocorrências, transferências e depreciação/correção) realizadas no período de cálculo atual.

**11.50.0**- Geração de Patrimonio por lote  
[Geração de Patrimônios em Lote](http://tdn.totvs.com/x/58hEGQ) Migração do processo que permite gerar um ou mais patrimônios a partir de um patrimônio selecionado.

**11.50.0** - Alocação de Patrimônio  
[Alocação de Patrimônio](http://tdn.totvs.com/x/bclEGQ) Implementado o processo referente a alocação externa, interna e de retorno para controle atual de patrimônio.

Consulta de Transferências e [Alocações](http://tdn.totvs.com/x/bclEGQ)  
Implementados os recursos que permitem visualizar as transferências de controle e as alocações realizada no patrimônio de forma a manter um controle das informações dos processos já executados.  
11.50.0 - Liberação de Competência e Fechamento de Período Implementados os processos de Liberação de Competência e Fechamento de Período referentes ao encerramento do período de cálculo de forma a substituir o processo de Liberação de Período.

Máquina de cálculo do Patrimônio Criação do processo (máquina de cálculo) responsável por realizar todos os cálculos de depreciação e correção envolvidos em situações como inclusão de patrimônio e ocorrências considerando as regras do Patrimonial.Net.

**11.50.0** - Relatórios  
[Ficha de Imobilizado](http://tdn.totvs.com/x/38hEGQ) Implementado relatório que permite realizar a conferência de todas as movimentações patrimoniais agrupadas pelos grupos de patrimônios.
