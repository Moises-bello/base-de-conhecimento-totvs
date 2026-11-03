---
content_hash: 4d62c1c7d95757ef527263eb9b76e8758647a2e625197c0b9b960d124e1fa75a
fetched_at: '2026-06-29T00:09:29.231309+00:00'
page_id: '423938844'
product: rm
source: tdn-rm
title: Novidades   
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938844
version: 7
---

12.1.28 - [Novidades da ECD](https://tdn.totvs.com/x/15mFI)

12.1.28 - O processo de "Alteração do Período para Manutenção de Lançamentos contábeis" foi evoluído. Agora o usuário consegue alterar o período de manutenção de lançamentos contábeis através do processo citado anteriormente e através do cadastro de usuário, sem a necessidade dos os usuários que sofreram alterações "saírem" do sistema. A alteração acontece simultaneamente mesmo com o usuário utilizando o sistema.

12.1.27 - [Demostrações Consolidadas](https://tdn.totvs.com/x/R2f6Hg)

12.1.26 - [Equivalência Patrimonial](https://tdn.totvs.com/x/VRSLHg)

12.1.22 - Cópia do Mapeamento do Plano de Contas Consolidado

12.1.22 - Gerar o Plano de Contas Paralelo a partir do Plano de Contas Contábil

12.1.20 - Bloco K - Conglomerados Econômicos

Deverão preencher este bloco as empresas controladoras obrigadas a apresentar demonstrações consolidadas de acordo com a legislação societária (Lei no 6.404/76 e Pronunciamento Técnico CPC 36 – Demonstrações Consolidadas).

12.1.20 - Exportação de Lançamentos Contábeis

12.1.19 - A forma de utilizar o  filtro de "Histórico Padrão" nos relatórios contábeis foi evoluída. A partir desta versão (12.1.19), será possível selecionar mais de um histórico e enviá-los simultaneamente para a lista dos históricos que serão utilizados para geração dos relatórios. É importante que fique claro que, a forma antiga de seleção do filtro de históricos será descontinuada, portanto, a lista de histórico salva na preferência antiga será perdida, sendo necessário refazê-la.

12.1.19 - Inativação/Ativação de Contas Gerenciais

Essa implementação funciona de forma similar ao processo de Inativação/Ativação de Contas Contábeis, porém para contas gerenciais.

12.1.16 - Implementações nos relatórios contábeis

* **Tamanho da fonte:** Com exceção do relatório de Consistência de saldo, todos os outros relatórios poderão ser gerados em mais de um tamanho de fonte. Foram disponibilizados quatro tamanhos para o usuário (de 5 a 8). A opção para alteração do tamanho da fonte está disponível nos atributos de página dos relatórios;
* **Liberado o tamanho máximo das linhas quando o tipo de saída for TXT:** Quando o tipo de saída dos relatórios for TXT, o sistema deve permitir qualquer tamanho de linha, ou seja, a soma do tamanho das colunas poderá ultrapassar o tamanho máximo da linha. Obs: Essa implementação foi realizada nos relatórios contábeis fixos: Balancete, Razão, Diário, Balanço Patrimonial, Acompanhamento Orçamentário e Listagem de Lançamentos.
* **Orientação do relatório de Retrospectiva de Saldos:** Foi disponibilizado no relatório a opção do usuário escolher qual orientação deseja utilizar, retrato ou paisagem;
* **Relatório Retrospectiva de Saldos em doze meses:** Agora é possível que o usuário gere o relatório para um período de até 12 meses, contudo, o usuário deve se atentar ao tamanho da fonte, quantidades de margens utilizadas e também alguns campos opcionais (Cod. Reduzido, Descrição e Total do Período). Essas opções podem diminuir o espaço para que se apresente os dados de 12 meses e com isso o relatório não será gerado;
* **Reajustar o tamanho das colunas automaticamente:** Foi adicionado na aba campos dos relatórios contábeis, uma opção que permita o ajuste automático do tamanho das colunas. Essa opção deverá ajustar as colunas de complemento, histórico e descrição.

Caso o relatório possua dois ou mais campos citados anteriormente, o redimensionamento deverá priorizar as colunas na seguinte ordem, complemento, histórico e descrição. O campo de maior prioridade deverá receber a diferença entre o tamanho máximo da linha e o tamanho total das demais colunas.

Se o tamanho total das demais colunas seja maior ou igual ao tamanho total da linha, deverá ser apresentada uma mensagem ao usuário avisando que aquela formatação não é possível.  
Obs: Essa opção se aplica apenas aos relatórios (Balancete, Razão, Diário, Balanço Patrimonial, Acompanhamento Orçamentária e Listagem de Lançamentos).

* **Razão com impressão de contas sem movimentações e sem saldo:** Foi implementada a opção "Conta(s) sem movimentação e sem saldo(s)" nos relatórios Razão Contábil Analítico e Razão Contábil Sintético. Se ela estiver marcada as contas sem movimentação e sem saldo (zeradas) deverão ser impressas.

12.1.15 - Atualização de Datas e Valores da Capa do Lote

Houve a necessidade de criação de um parâmetro para que a capa do lote não atualize automaticamente conforme movimentações no lote. O parâmetro da a possibilidade do usuário atualizar a capa do lote conforme sua necessidade.

12.1.14 - Importação via Conceito - Orçamento

A fim de aumentar a qualidade da nossa importação de dados, foi realizada uma implementação no conceito referente a importação de Orçamento, houve a inclusão de novos campos e novos posicionamentos de alguns campos.

12.1.12 - Relatório Listagem de Lançamentos

Possibilita imprimir lançamentos e rateios distribuídos entre suas contas.

12.1.11 - Geração Automática de Orçamento

Possibilita a geração de novos orçamentos baseados na movimentação das contas contábeis selecionadas.

12.1.10 - Relatório Acompanhamento Orçamentário

O Relatório acompanhamento orçamentário permite a visualização dos valores orçados e movimentados, das contas com distribuição gerencial, com totalização pelas contas contábeis selecionadas.

12.1.10 - Razão Auxiliar de SubContas

O livro razão auxiliar das subcontas será implementado na ECD – Escrituração Contábil Digital, a partir de janeiro de 2016. Portanto, as empresas obrigadas ao livro razão auxiliar, conforme Instrução Normativa RFB 1.515/2014, transmitirão o livro "Z" na ECD de 2016 (ano-calendário 2015). A funcionalidade foi implementada para atender a obrigatoriedade no controle de subcontas no "ajuste a valor presente" e "avaliação a valor justo".

12.1.9 - Relatório Razão Auxiliar - Parametrização

Com o objetivo de simplificar a parametrização e geração do relatório "Razão Auxiliar" para o SPED contábil, realizamos uma evolução no módulo para que não seja mais necessário utilizar o RM Gerador. A partir de agora a parametrização do relatório pode ser feita diretamente no cadastro da escrituração contábil clicando na aba "Layout do Relatório Razão Auxiliar". Para utilizar o novo recurso acesse o cadastro de escrituração contábil do SPED Contábil e realize a parametrização.

12.1.6 - Balancete Orçamentário

O relatório de Balancete Orçamentário permitirá a visualização e controle dos Orçamentos confrontados com as contabilizações realizadas.

12.1.6 - Otimização dos relatórios

Os relatórios de Balancete, Razão, Diário, Balanço Patrimonial, Plano de Contas e Lançamentos Duplicados passam a possuir Orientação de impressão em formato Retrato e Paisagem, e outras melhorias, detalhadas dentro de cada página de Help destes relatórios.

12.1.5 - Relatório Balanço Patrimonial

O balanço patrimonial é uma demonstração contábil que tem por finalidade apresentar a posição contábil, financeira e econômica de uma entidade em determinada data, representando uma posição estática (posição ou situação do patrimônio em determinada data). Ele apresenta os ativos (bens e direitos), passivos (exigibilidades e obrigações) e o patrimônio líquido, que é resultante da diferença entre o total de ativos e o total de passivos.

12.1.5 - Relatório Razão Cliente Fornecedor/Contábil

O Razão Cliente/Fornecedor – Contábil reflete o resumo dos valores lançados, organizados por contas contábeis e em seguida por cliente/fornecedor. Esse relatório tem o objetivo de imprimir somente contas contábeis de clientes/fornecedores, portanto, preferencialmente devem ser selecionadas as contas contábeis de clientes/fornecedores na aba Filtro.

12.1.5 - Escrituração SCP Mantida pelo Sócio Ostensivo

Quando duas ou mais pessoas, sendo ao menos uma comerciante, se reúnem, sem firma social, para lucro comum, em uma ou mais operações de comércio determinadas, trabalhando um, alguns ou todos, em seu nome individual para o fim social, esta associação toma o nome de Sociedade em Conta de Participação (SCP). A SCP modificou a geração do SPED Contábil Layout 3.0 e sua Escrituração.   12.1.5 - Apuração Virtual O módulo de Apuração Virtual que possibilita criar estruturas de apuração contábil que poderão ser utilizadas na ECF ou como apoio gerencial. A Apuração Virtual calcula virtualmente o valor do resultado conforme as regras de cálculo, sem gerar nenhum impacto na escrituração contábil, ou seja, não gera nenhum lançamento contábil, apenas processa o valor.

12.1.4 -  Relatório Retrospectiva de Saldos

O objetivo do relatório de Retrospectiva é a fornecer ao usuário a possibilidade de consultar e imprimir, de forma retrospectiva, informações de lançamentos contábeis, independente do período em que as partidas tenham sido registradas, totalizando-os mensalmente e organizando-os em níveis de agrupamento que poderão representar Contas Contábeis, Contas Gerenciais ou Centros de Custo, de acordo com os parâmetros que forem determinados, obedecendo um formato de exibição baseado em uma série de outras configurações que o usuário indicar.

12.1.4 - Relatório Lançamentos Duplicados

O Relatório de Lançamentos Duplicados permitirá a identificação de Lançamentos criados em duplicidade, de acordo com a análise e seleção de alguns campos na geração do relatório.

12.1.4 - Filtros por Lote

Os relatórios Balancete, Razão e Diário, terão a possibilidade de seleção de mais de um Filtro de Lote, permitindo a combinação de Lançamentos com um ou vários Lotes N e Lote Zero.

12.1.3 - Zerar Orçamento

Esta funcionalidade permitirá o usuário excluir ou zerar, por ano/mês, lançamentos de orçamento baseado no Plano de Contas Contábil.

12.1.3 - Relatório Plano de Contas

Esta funcionalidade tem a finalidade listar as contas cadastradas em uma determinada coligada, ou contas globais.

A partir da versão 12.1.1 todos os menus em .NET só estarão disponíveis através da MDI.Net e os antigos módulos só conterão funcionalidades ainda não migradas ou com restrições em suas versões .Net. Para maiores informações, favor consultar o help do RM Conversor.

12.1.1 -

Migrado o Relatório "Consistência de Saldos", visando fornecer em listagem, uma verificação da exatidão e coerência dos saldos dos lançamentos, apurando possíveis inconsistências. Nele serão impressas todas as contas que possuírem saldos divergentes de sua natureza.

12.1.1 - Relatório Razão

Migrado o relatório "Livro Razão", o mesmo é obrigatório pela legislação comercial e tem a finalidade de demonstrar a movimentação analítica das contas escrituradas nos diários e constantes do balanço. Para a impressão deste relatório, selecione o item "Relatórios" no Menu principal da nova MDI e em seguida a opção Razão. Atualmente é possível a emissão de quatro Tipos de razão:

* Razão Analítico; (oficial para legislação)
* Razão Gerencial / Contábil;
* Razão Contábil / Gerencial;
* Razão Centro de Custo / Contábil;

12.1.1 - Relatório Diário

Migrado o Relatório "Livro Diário", sendo este um relatório obrigatório, exigido pela legislação contábil em vigor. O Diário possui a finalidade de demonstrar a movimentação contábil diária da empresa conforme as filtragens feitas através do relatório.

12.1.1 - Relatório Balancete

O Balancete é um relatório contábil oficial exigido pela Legislação. Ele reflete a contabilidade de uma empresa ou organização num determinado período conforme as apurações realizadas internamente no sistema.
