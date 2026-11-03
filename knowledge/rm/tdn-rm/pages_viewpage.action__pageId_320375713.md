---
content_hash: edd8ba635f0165ba97ed5cd91aaf5c5791678796f26abe892548769d40849be5
fetched_at: '2026-06-29T00:08:47.736592+00:00'
page_id: '320375713'
product: rm
source: tdn-rm
title: DT Parametrização de Valores de Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=320375713
version: 50
---

# Parametrização de valores de integração

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Configuração* | *Parametrização TOTVS Educacional* | |
| **Cadastros Iniciais:** | *Valor de integração financeira* |
| **Parâmetro(s):** | *Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin - Vlrs. Opcionais / Integração* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | DEDUINTEGRACOES-1069, DEDUINTEGRACOES-1070 |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *N/A* |
| **Tabelas Utilizadas:** | *SPARAM* |
| **Sistema(s) Operacional(is):** | *N/A.* |

## Descrição

Com o objetivo de flexibilizar a integração entre os módulos Educacional e Financeiro foi implementado o  e a parametrização desses valores, através dos parâmetros Educacionais, retirando a limitação que existia na utilização de valores opcionais.

Parâmetros | Educacional | Integração | Financeiro

**Configuração no TOTVS Educacional**

Em todo ponto do parametrizador onde era possível a parametrização de um valor opcional, foi criada uma opção para a parametrização de um valor de integração.

Para uma maior usabilidade e compreensão esses parâmetros foram agrupados  em: Parâmetros | Educacional | Integração | Financeiro | Fin - Vlrs. Opcionais / Integração 1/3 ,   
                                                                                                                                         Parâmetros | Educacional | Integração | Financeiro | Fin - Vlrs. Opcionais / Integração 2/3,  
                                                                                                                                         Parâmetros | Educacional | Integração | Financeiro | Fin - Vlrs. Opcionais / Integração 3/3

Parâmetros | Educacional | Integração | FinanceiroParâmetros | Educacional | Integração | FinanceiroFin - Vlrs. Opcionais / Integração 1/3

Na etapa Fin - Vlrs. Opcionais / Integração 1/3 foram disponibilizados os campos *"Pagamento a maior (Integração)"* e *"Pagamento a menor (Integração)"* referente ao valores opcionais / integração do TOTVS Gestão Financeira.

Fin - Vlrs. Opcionais / Integração 2/3Fin - Vlrs. Opcionais / Integração 2/3

Na etapa Fin - Vlrs. Opcionais / Integração 2/3 foram disponibilizados os campos *"Valor integração de acréscimo"* e *"Valor integração de desconto"* referente aos valores opcionais/integração utilizados em cobranças retroativas.

Fin - Vlrs. Opcionais / Integração 3/3Fin - Vlrs. Opcionais / Integração 3/3

Na etapa Fin - Vlrs. Opcionais / Integração 3/3 foram disponibilizados os campos *"Bolsas incondicionais (Integração)"* e *"Bolsas condicionais (Integração)"* (caso esteja selecionada a opção de utilização de bolsas condicionais).

* Com a liberação da parametrização de valores de integração os parâmetros correspondentes aos valores opcionais passam a ser bloqueados para novas parametrizações.
* Nas opções referentes aos parâmetros de valores de integração serão listados os registros previamente inseridos no cadastro de "Valores de integração financeira" e com base na característica do campo.
  + Por exemplo, o parâmetro "Pagamento a maior (Integração )" irá listar as opções de valores do tipo Acréscimo, já que valores pago a mais pelo aluno serão acrescentados à sua conta-corrente.
  + parâmetro "Pagamento a menor (Integração)" irá listar as opções de valores do tipo Desconto.
  + parâmetro "Valor de integração de acréscimo" irá listar as opções de valores do tipo Acréscimo.
  + parâmetro "Valor de integração de desconto" irá listar as opções de valores do tipo Desconto.
  + parâmetro "Bolsas incondicionais (integração)" irá listar as opções de valores do tipo Desconto.
  + parâmetro "Bolsas condicionais (integração)" irá listar as opções de valores do tipo Desconto.
* Todos os parâmetros de valor de integração listarão apenas os valores do módulo TOTVS Educacional, a exceção é o parâmetro "Bolsas condicionais (Integração)". Ele listará os valores dos módulos TOTVS Educacional e se a opção "Mantém fórmula default para valor opcional / integração de bolsas condicionais" estiver selecionada listará apenas os valores do módulo TOTVS Gestão Financeiro, já que somente valores desse módulo podem ser associados a fórmulas.

O TOTVS Financeira possibilita a inclusão de valores de integração default para lançamentos gerados a partir de outros módulos, ou seja todo lançamento gerado para Educacional poderá ser criado possuindo um valor de integração  
com regra especifica determinada pelo cliente, que pode ser definidas manualmente ou por fórmula.

Observação:  
Este recurso foi disponibilizado para as versões 12.1.25 e superiores ou igual a 12.1.28, para habilitar a opção entre em contato com o Suporte.  
Para saber mais detalhes consulte [FIN - Valores de Integração Financeiro](https://tdn.totvs.com/pages/viewpage.action?pageId=532041706).

* Ao selecionar a primeira parametrização de um valor de integração será exibida uma mensagem questionando o usuário se deseja prosseguir com a parametrização.

* Cada parâmetro de valor de integração armazenará a data em que foi realizada a sua parametrização. Isso é necessário pois as funcionalidades que dependem do parâmetro continuarão a utilizar os valores opcionais previamente parametrizado para os dados legados. Apenas os dados gerados após a data de parametrização de um valor de integração utilizarão essa parametrização. É possível visualizar a data dessa parametrização pelo hint do parâmetro.

* Para evitar impactos colaterais em lançamentos previamente existentes, a data assumida para parametrização será baseada na existência de lançamentos gerados. Caso exista algum lançamento gerado na data de parametrização o sistema poderá assumir a data posterior, caso contrário não será possível salvar a parametrização.

* Se não existir lançamentos gerados na data em que a parametrização estiver sendo realizada, os dados serão salvos normalmente e a data de parametrização será a utilizada.
* Assim como já acontecia com os valores opcionais, os parâmetros de valores de integração serão bloqueados para alteração assim que alguma funcionalidade utilize esse parâmetro. Por exemplo, os parâmetros de valores de integração referente a bolsa serão bloqueados para alteração assim que existir um lançamento utilizando bolsa após a parametrização desses campos. Os parâmetros de valores de integração referente a integração financeira e cobrança retroativa serão bloqueados assim que existir movimentação de conta corrente, baseado no tipo, após a parametrização dos campos.

Com a implementação da utilização dos campos de Valores de Integração no Educacional, o parâmetro “Utilizar bolsas condicionais” que anteriormente estivesse desmarcado porem bloqueado, passa a ficar liberado na base de dados para que seja possível a indicação de um campo de Valor de Integração para controlar as Bolas condicionais, então, mesmo que anteriormente o parâmetro “Utilizar bolsas condicionais” estivesse desmarcado, indicando não haver controle dos valores de bolsas condicionais em algum campo específico de Valor Opcional, é possível agora passar a fazer este controle para os novos lançamentos em um campo específico de Valor de Integração. Se desejar, marque o parâmetro “Utilizar bolsas condicionais” e associe um campo de Valor de Integração para controle dos valores de Bolsas condicionais.

Depois de parametrizado, assim que for gerado um novo lançamento com Bolsa condicional não será possível modificar esta parametrização.

Geração / Regeração de Lançamento

A geração de lançamentos Financeiros pelo Educacional foi evoluída para contemplar o novo recurso de valor de integração disponível nas parametrizações do Educacional. Informações de valores do Educacional que são controladas através dos campos de valores opcionais  do TOTVS Gestão Financeira, tais como:

Bolsa condicional, bolsa incondicional, pagamento a maior, pagamento a menor, acréscimo de cobrança retroativa para débito (conta corrente), desconto de cobrança retroativa para crédito (conta corrente).

A partir de agora estes valores poderão ser controlados através dos valores de integração.

Como vai funcionar?

* Clientes que já utilizam valor opcional:

Para estes clientes será possível parametrizar qualquer uma das informações acima para utilizar um valor de integração cadastrado no Educacional, seguindo a seguinte regra:

- Depois de parametrizado, todo o lançamento incluído pelo Educacional a partir da data da parametrização passa a controlar o valor no campo do valor de integração parametrizado.

- Para lançamentos que já foram gerados e necessitam de ser regerados o sistema vai considerar a data de parametrização do valor de integração para saber ser vai utilizar o valor opcional ou não, por exemplo:

→ Lançamento 1 gerado com data de criação no dia 10/03/2017 utilizando valor opcional.

→ Dia 01/04/2017 o sistema foi parametrizado para utilizar no campo “Bolsa incondicional” o valor de integração X.

→ Se for preciso regerar o lançamento 1 o sistema não vai utilizar o valor de integração parametrizado e sim o valor opcional utilizado antes da mudança da parametrização.

- Não será obrigatório fazer com que todos os campos utilizem valor de integração, ou seja, a migração poderá ser aos poucos.

- Uma vez que tenha lançamentos gerados utilizado o valor de integração não será possível modificar a parametrização.

* Clientes que irão implantar o sistema:

Para estes clientes será possível realizar a parametrização do sistema utilizando apenas valor de integração cadastrado no Educacional. Lembrando que se já existir lançamentos gerados utilizado o valor de integração não será possível modificar a parametrização.

Após a geração dos lançamentos utilizando valor de integração, os valores poderão ser consultados no lançamento gerado e irão refletir no cálculo do valor líquido do lançamento, veja:

Ao clicar no ícone "Exibir cálculo do valor liquido" no lançamento.

Observação:

Se o sistema estiver parametrizado para utilizar o valor de integração para pagamento a maior ou menor, sempre ao gera o lançamento o sistema adicionará no valor de integração do lançamento um valor para pagamento a maior e menor com valor igual a zero. Isto é necessário pois na baixa do lançamento este valor poderá ser editado.

Cancelamento de Lançamento

O cancelamento de lançamento proveniente do Educacional manteve o seu comportamento atual mesmo com a evolução para contemplar o novo recurso de valor de integração disponível nas parametrizações do Educacional. O cancelamento de lançamento sempre voltará com os registros de aproveitamento para a conta corrente do aluno.

Baixa de Lançamento

A baixa dos lançamentos financeiros provenientes do TOTVS Educacional foi evoluída para contemplar o novo recurso de valor de integração disponível nas parametrizações do TOTVS Educacional. Informações dos valores do Educacional que são afetados pela baixa de lançamento no TOTVS Gestão Financeira controlados através dos campos de valores opcionais, são:

Bolsa condicional, bolsa incondicional, pagamento a maior, pagamento a menor.

A partir de agora estes valores poderão ser baixados através dos valores de integração.

Como vai funcionar?

* Clientes que já utilizam valor opcional:

Para estes clientes a baixa do lançamento financeiro irá respeitar a parametrização presente nos parâmetros "Educacional | Integração | Financeiro | Fin - Vlrs Opcionais / Integração", seguindo a seguinte regra:

 - Depois de parametrização, toda baixa de lançamento do Educacional no TOTVS Gestão Financeira a partir da data da parametrização passa a efetuar a baixa do valor no campo do valor de integração parametrizado.

 - Para as baixas dos lançamentos que já foram gerados antes da parametrização, continuaram a efetuar a baixa do valor no campo valor opcional configurado antes da data da parametrização, por exemplo:

Exemplo 1:

 → Lançamento 1 gerado com data de criação no dia 10/03/2017 utilizando valor opcional.

 → Dia 01/04/2017 o sistema foi parametrizado para utilizar o campo "Pagamento a maior" no valor de integração X.

 → Na baixa do lançamento 1 o sistema não vai utilizar o valor de integração parametrizado para efetuar a baixa do valor, e sim o valor opcional utilizado antes da mudança da parametrização.

Exemplo 2:

→ Lançamento 2 gerado com data de criação no dia 05/04/2017 utilizando valor opcional para "Pagamento a menor" e valor de integração para "Pagamento a maior".

→ Dia 01/04/2017 o sistema foi parametrizado para utilizar o campo "Pagamento a maior" no valor de integração X.

→ Dia 06/04/2017 o sistema foi parametrizado para utilizar o campo "Pagamento a menor" no valor de integração Y.

→ Na baixa do lançamento 2 o sistema não vai utilizar o valor de integração parametrizado para efetuar a baixa do valor "Pagamento a menor", e sim o valor opcional utilizado antes da parametrização. E no valor "Pagamento a maior", o sistema irá efetuar a baixa usando o valor de integração parametrizado para o "Pagamento a maior".

Não será obrigatório fazer com que todos os valores sejam baixados pelo valor de integração, ou seja, a migração poderá ser aos poucos juntamente com a geração / regeração de lançamento.

Vale ressaltar que após lançamentos serem gerados com utilização de valor de integração não será possível modificar a parametrização, e seus valores serão baixados pelo valor de integração parametrizado.

* Clientes que irão implantar o sistema:

Para estes clientes a baixa do lançamento financeiro irá respeitar a parametrização presente nos parâmetros "Educacional | Integração | Financeiro | Fin - Vlrs Opcionais / Integração". Lembrando que se já existir lançamentos gerados utilizado o valor de integração não será possível modificar a parametrização.

Na baixa dos lançamentos utilizando valor de integração, os valores poderão ser consultados na etapa de "Edição do Lançamento" na aba "Saldo dos Valores de Integração" e irão refletir no cálculo do valor líquido na baixa lançamento, veja:

Ao clicar no ícone "Exibir cálculo do valor liquido" no lançamento.

Cancelamento de Baixa de Lançamento

O cancelamento de baixa de lançamento proveniente do Educacional manteve o seu comportamento atual mesmo com a evolução para contemplar o novo recurso de valor de integração disponível nas parametrizações do Educacional.

Aproveitamento de Conta Corrente

O aproveitamento de valores em conta corrente do aluno manteve o seu comportamento atual mesmo com a evolução para contemplar o novo recurso de valor de integração disponível nas parametrizações do Educacional.

Inclusão / Exclusão de Bolsa Retroativa

Ao incluir ou excluir uma bolsa retroativa o sistema altera o lançamento financeiro, incluindo o valor da respectiva bolsa no campo opcional parametrizado para armazenar o valor (bolsa condicional e incondicional), se o lançamento estiver baixado o valor recebido da bolsa também é lançado no campo pagamento a menor ou a maior (dependendo da operação inclusão ou exclusão) e dependendo da parametrização este valor vai ser transportado para a conta corrente do aluno.

Caso o sistema esteja parametrizado para utilizar valor de integração em alguns dos campos opcionais (bolsa condicional, bolsa incondicional, pagamento menor ou maior, desconta ou acrescenta conta corrente) o que muda é que ao invés do valor ser controlado no campo opcional ele vai ser controlado no campo correspondente ao valor de integração parametrizado no Educacional.

Retorno Bancário

Foi realizada uma evolução no processo de Retorno Bancário, que passa a reconhecer a configuração de Valores de Integração para Pagamentos a Maior e/ou Pagamentos a Menor, caso o lançamento tenha sido criado pelo Educacional.

Se o retorno se referir a um lançamento do Educacional que utiliza Valores Opcionais (lançamento gerado pelo Educacional em data anterior à data de parametrização da base para utilizar valores de integração) as diferenças a maior ou a menor serão tratadas conforme o default definido na parametrização do TOTVS Gestão Financeira referente à Cobrança Eletrônica (parâmetros do Fluxus - 02.02.04.01 - Cobrança Eletrônica), que poderá conter a indicação de valores opcionais específicos para onde a diferença deverá ser lançada, ou a indicação de Não Baixar caso encontre diferenças.

Se o retorno se referir a um lançamento do Educacional que utiliza Valores de Integração (lançamento gerado pelo Educacional em data posterior à data de parametrização do sistema para utilizar valores de integração) as diferenças serão lançadas nos respectivos Valores de Integração parametrizados na base do Educacional para registrar pagamentos efetuados a maior e a menor, e neste caso, a conta corrente dos alunos serão automaticamente atualizados com os respectivos valores, gerando débitos ou créditos.

Qualquer que seja o caso, se ao executar o Retorno Bancário seja indicada a opção "Não Baixar" em caso de Pagamento a Maior e/ou Pagamento a Menor, o comportamento do sistema NÃO executará a baixa, registrando em log a situação para atuação do operador.

**Informações complementares:**

---

**HOW TO**

**1) Valores de Integração - Cadastro e Parametrização**

****2) Valores de Integração - Geração de Lançamento****

**3) Valores de Integração - Baixa de Lançamento**

**4) Valores de Integração - Aproveitamento de conta corrente**
