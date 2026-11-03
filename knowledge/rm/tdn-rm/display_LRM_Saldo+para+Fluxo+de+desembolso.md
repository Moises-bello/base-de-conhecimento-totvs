---
content_hash: 7e2020ef7266b2ea01838c1910a6064d819a0cb8c662d4f7485673748c98557f
fetched_at: '2026-06-29T00:09:14.751864+00:00'
page_id: '421385246'
product: rm
source: tdn-rm
title: Saldo para Fluxo de desembolso
type: documentation
url: https://tdn.totvs.com/display/LRM/Saldo+para+Fluxo+de+desembolso
version: 104
---

O controle de Fluxo de Caixa permite que os desembolsos de um projeto sejam provisionados no sistema financeiro integrado ao Totvs Obras e Projetos.

É um processo responsável por efetuar e manter os lançamentos no sistema financeiro.

E permite também visualizar na tela dividido em etapas os lançamentos feitos.

Uma das principais funções desse processo é apurar o saldo disponível no momento da execução do mesmo projetando o futuro para que sempre exista capital de giro acessível tanto no custeio da operação da empresa (folha, impostos , fornecedores entre outros) quanto para investimentos (pintura, reforma etc).

**Fluxo**:

* Parametrização
* Linha Base
* Saldo

**Parametrização:**

Para utilizar esse processo é importante atentar as premissas:

**Backoffice Protheus:**

Quando essa integração está ativa é necessário executar o configurador que cadastra os parâmetros e adapters do pacote utilizado. Detalhes**:**

**Veja também:** Documentação Processo de Saldo de Fluxo de Desembolso quando integrado com o Backoffice Protheus:

Nesse link será possível ver todo conteúdo necessário para integrar o TCOP X  Backoffice Protheus.

Para quem possui apenas o backoffice RM segue as premissas abaixo:

**Backoffice RM**

Para utilização do processo é necessário realizar parametrização:

Passos para parametrização

1-  Parametrizar (F6) - Parâmetros do Projeto a opção dos parâmetros (Integração/Financeiro/Saldo para Fluxo de Desembolso).

2- Parametrizar  (F6) - Parâmetros do Projeto a opção de integração com Financeiro(Integração/Financeiro/Geral).

3- Parametrizar  (F6) - Parâmetros do Projeto a integração com o Suprimento e Faturamento (Integração /Financeiro / Suprimento/ Faturamento).

Não é possível a execução do processo de Saldo de Fluxo de Desembolso sem a devida parametrização , é necessário que o usuário tenha as devidas permissões e que tenha configurado todos os itens abaixo:

Centro de custo do projeto definido.

Filial do projeto definida.

Permissão para calcular projeto.

Integração com o Suprimento e Faturamento.

Integração com o Financeiro.

Tipo de documento de linha base.

Tipo de documento de saldo.

Código de cliente e fornecedor.

IntegraçãoSuprimento / Faturamento

**Informar parâmetros em "Integração | Suprimento / Faturamento | Geral":**

Habilitar a integração com o Suprimento e Faturamento;

Informar a condição de pagamento.

Para mais detalhes de como configurar a integração com o Suprimento e Faturamento acesse: [BackOffice Suprimentos/Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=421385523)

FinanceiroGeral

**Informar parâmetros em "Integração | Financeiro | Geral":**

Habilitar a integração com o Financeiro.

Saldo para Fluxo de Desembolso

**Informar parâmetros em "Integração | Financeiro | Saldo par Fluxo de Desembolso":**

Habilitar geração do saldo de fluxo de desembolso do projeto.

O Tipo de documento de lançamento de linha base.

Tipo de documento de lançamento de saldo.

Código do cliente (receita).

Código do fornecedor (despesa).

**Opcional:**

Calcular o projeto automaticamente antes da execução do processo.

Agrupara os lançamentos financeiros por obra.

Opção "Editável"

Para cada parâmetro informado, poderá optar em permitir a edição / mudança no momento da execução do processo, para isto deve marca a opção "Editável" para o campo desejado.

**Informar parâmetros em "Integração | Financeiro | Saldo par Fluxo de Desembolso | Tabelas Opcionais":**

Permitir informar um registro default relacionado as tabelas opcionais.

**Processo**  
O processo "Saldo do Projeto para Fluxo de Desembolso" (Projetos > Construção e Projetos > Controle > Saldo para Fluxo de Desembolso)

Ao acionar a opção Saldo para Fluxo de Desembolso o sistema exibe a tela do processo, e sua primeira etapa consiste em conferir os parâmetros definidos no projeto e que serão usados nos lançamentos, além de algumas opções :

Todos os campos dos parâmetros acima, foram informados nos Parâmetros do Projeto > Integração > Financeiro.

A condição de pagamento exibida é cadastrada em Parâmetros do projeto > Integrações > Suprimentos/Faturamento > Geral.

É obrigatória na geração do Saldo para Fluxo de desembolso.

Discriminar Valores - Etapa a etapa.

<https://tdn.totvs.com/x/74PDIQ>

Tipo de LançamentoTipo de LançamentoTipo de lançamentowLinha base

As informações iniciais para o processo são recuperadas do cálculo da Curva "S". Com isso, os valores e datas das necessidades consideram automaticamente o prazo de ressuprimento dos insumos. Para o processo, será considerado o primeiro dia do mês como referência para o cálculo da data de pagamento ou recebimento, que poderá variar devido às condições de pagamento.

O lançamento de Linha Base é feito apoiando-se no planejamento do projeto e é utilizado para estabelecer um critério de comparação para o andamento do desembolso do projeto. Ele é composto por três etapas: geração do histograma (Curva S), geração do cronograma de desembolso e, por fim, se houver um lançamento de linha base feito anteriormente, ele é apagado e o um novo lançamento financeiro é gerado.

Para que o histograma seja gerado corretamente, é necessário que o projeto esteja calculado, bem como a Curva ABC de Insumos. Desta forma, a Curva ABC de Insumos é calculada automaticamente nesta fase e há também a opção de calcular o projeto através deste processo.  Em sua última fase, o processo exclui os lançamentos de linha base anteriores, de acordo com o tipo de documento, e gera novos lançamentos, baseados no cronograma de desembolso calculado.

Saldo

As informações iniciais para o processo são recuperadas do cálculo da Curva "S". Com isso, os valores e datas das necessidades consideram automaticamente o prazo de ressuprimento dos insumos. Para o processo, será considerado o primeiro dia do mês como referência para o cálculo da data de pagamento ou recebimento, que poderá variar devido às condições de pagamento.

O lançamento de Saldo é utilizado para atualizar o fluxo de caixa com os dados dos desembolsos já efetuados, a fim de se ter controle sobre o saldo do projeto comparado ao planejado feito inicialmente (Lançamento de Linha Base).  
 No cálculo são considerados além das etapas executadas no lançamento de linha base, outros aspectos do projeto, como as quantidades contratadas, as quantidades comprometidas em Suprimentos/Faturamento e os valores previstos em períodos de contratos.

O processo de geração dos lançamentos de saldo irá atualizar os lançamentos no financeiro, esse lançamento pode ser feito "a Pagar" ou "a Receber", O tipo será definido de acordo com o tipo da tarefa, presente no cronograma de desembolso, que irá compor o lançamento. Tarefas do tipo receita irão dar origem a lançamentos a receber enquanto as demais tarefas irão gerar lançamentos a pagar. Lançamentos a receber possuirá apenas natureza orçamentária do tipo a receber enquanto lançamentos a pagar possuirá apenas natureza orçamentária a pagar.

Quando o usuário solicita a geração de lançamento de saldo "a Pagar", o TOP irá recuperar todo o planejado através do Histograma, verificando os valores planejados comparando com os valores realizados.

É importante esclarecer que apenas movimentos faturados terão abatimento no saldo, portanto, movimentos de solicitação não terão abatimento.

Os processos que possuem abatimento na linha de saldo são:

**Contrato: Através de Movimento faturados**  
**Pedido: Através de Movimento faturados**  
**Apropriação: Através de apropriações realizadas pelo Totvs Obras e Projetos.**

Quando o usuário solicita a geração de lançamento de saldo "a Receber", o TCOP irá recuperar todo o planejado através do Histograma, verificando os valores planejados com as movimentações de contratos "a receber".

Quando encontrado os movimentos faturados, o TOP irá abater os valores planejados com os valores realizados.

O processo de saldo no momento do abatimento dos valores realizados x os valores planejados, serão verificados apenas os totais dos lançamentos.

O TCOP não irá verificar a relação das datas do movimento em relação aos períodos do projeto.

Como o controle de saldo apenas demonstra os gastos financeiros do projeto e o cronograma planejado ao longo do tempo tende a ser igualado ao realizado do projeto, torna-se necessário a cada replanejamento o envio da Linha Base e após a Linha de Saldo.  
Como a Linha de saldo considera o planejamento de Obra, e todo planejamento é baseado no quantitativo previsto do projeto, torna-se necessário o fluxo de caixa trabalhar da mesma maneira.

Ao final o processo "Saldo"  gera um log que consiste em um resumo do que foi considerado durante sua execução:

Esse resumo| log  é composto por:

Valores calculados:

**Valor inicial (histograma):** nesse item ele recorda o valor inicial planejado baseando-se no histograma.

**Valor associado em contratos a ser abatido do histograma:** Considera os valores que foram associados no contrato e que serão abatidos no histograma.

**Valor faturado abatido:** Considera os valores faturados (Pedidos)

**Valores das apropriações abatidas:** Considera os valores de apropriações abatidas.

**Valor adicionado previsto em contratos:** É a soma dos valores informados na edição dos períodos de contrato no campo "Previsto".(Lembrando que este valor informado no previsto só é considerado se o contrato estiver calculado)

**Valor medido dos contratos a ser abatido na previsão:** Consiste no valor que tem medido/consumido.

**Valor do desembolso:** Valor a ser desembolsado

Exclusão de lançamentos

Ao habilitar essa opção o sistema exclui os lançamentos no Financeiro com status excluído referentes ao saldo e a linha de base.

Cliente / Fornecedor

Como os lançamentos gerados serão todos de provisão, neste momento não é possível definir para qual cliente/fornecedor irá cada lançamento. Sendo assim todos os lançamentos a pagar serão gerados para um mesmo Fornecedor, enquanto todos os lançamentos a receber serão gerados para um mesmo cliente, uma vez que esta informação é obrigatória para inclusão de um lançamento financeiro.   
  
Tanto o cliente quanto o fornecedor poderá ser informado na tela do processo ou através dos parâmetros do projeto. A informação de um único cliente/fornecedor não irá interferir no fluxo de caixa.

**Código do Cliente/Fornecedor(Receita)/(Despesa)**  
   
É um campo onde é possível parametrizar um fornecedor padrão para o processo.

Opções

**Dentro de opções é possível habilitar**

Agrupar lançamentos financeiros por obra: Caso esteja habilitado o sistema agrupa por obra os lançamentos financeiros que foram gerados pelo processo de saldo para fluxo de desembolso.

Calcular o projeto antes da geração (que é o recomendado): Caso esteja marcado, realiza o cálculo do projeto antes da execução do processo de geração do saldo pra fluxo de desembolso.

Discriminar Valores - Etapa a etapa.

<https://tdn.totvs.com/x/74PDIQ>InformaçõesaCadastro de Insumo

Ao informar a natureza financeira será aplicado o filtro de acordo com o tipo do insumo (Receita/Derivado/Normal) e o nível da natureza financeira (Sintético/Analítico). Sendo:  
·          Insumos do Tipo Receita serão naturezas financeiras analíticas a receber;  
·         Demais insumos serão financeiras naturezas analíticas a pagar;

Cliente / Fornecedor

Como os lançamentos gerados serão todos de provisão, neste momento não é possível definir para qual cliente/fornecedor irá cada lançamento. Sendo assim todos os lançamentos a pagar serão gerados para um mesmo Fornecedor, enquanto todos os lançamentos a receber serão gerados para um mesmo cliente, uma vez que esta informação é obrigatória para inclusão de um lançamento financeiro.   
  
Tanto o cliente quanto o fornecedor poderá ser informado na tela do processo ou através dos parâmetros do projeto. A informação de um único cliente/fornecedor não irá interferir no fluxo de caixa.

Natureza Orçamentaria

Conforme mencionado anteriormente, os lançamentos serão obtidos através do cronograma de desembolso. A partir dos lançamentos do cronograma de desembolso a Natureza Orçamentária enviada em cada lançamento será obtida na seguinte ordem:  
  
Verifica se existe Natureza definida no produto principal associado ao Insumo;  
Caso a natureza não for obtida no passo 1, Verifica se existe Natureza definida no Insumo;  
Caso a natureza não for obtida no passo 2, Verifica se existe Natureza definida no Grupo de Custo;  
Caso a natureza não for obtida no passo 3, Verifica se existe no Parâmetro.  
  
Para tarefas de valor cotado a Natureza do lançamento será obtida a partir da Natureza Orçamentária definida na tarefa. Caso não esteja definido, o sistema pega a definida no parâmetro.  
  
Para contratos o sistema utiliza a Natureza informada no parâmetro.

Contrato

Como os lançamentos do fluxo de desembolso recupera os dados através do cronograma de desembolso e o cálculo de desembolso considera o valor dos contratos, surgiu-se a necessidade de se verificar os contratos no envio de Linha Base. O contrato será considerado na Linha Base apenas se não houver agrupamento por obra, pois quando se utiliza este agrupamento as tarefas não são consideradas.

**Contrato de Serviço, Parcela Fixa e Marco Contratual:**

Quando processo de Linha Base for executado será analisado apenas as tarefas associadas ao contrato de Serviço, Parcela fixa ou Marco contratual, nesta análise será considerado a Natureza Orçamentaria vinculada aos produtos do rateio. Como o módulo de contrato possui uma visão de rateio de produtos, todas as tarefas que contiverem o produto associado no rateio terão seus lançamentos levado em consideração.   
  
Se o parâmetro de projeto "permitir contratação de serviços com valor superior ao orçado" estiver ativo, o lançamento para fluxo de desembolso será o valor total contratado, mas caso o usuário não tenha associado nenhum produto no rateio da tarefa, o que exceder o valor planejado na planilha será realizado um lançamento do valor restante na natureza padrão cadastrada nos parâmetros de projeto. 

Exemplo:

Cenário: Lançamento de Linha Base - Total R$ 6.000  
    Linha Base: valor da tarefa R$ 10,00    
                        Período             1(01/03)           2(01/04)           3(01/05)  
                        Quantid.            100                 200                  300  
                        Valor                 R$ 1.000         R$ 2.000           R$ 3.000  
  
    Realizar um movimento no dia 26/03 de quantidade 300, faturando no valor de R$50,00 (Produto). Total da Fatura R$ 9000.   
   Quando for enviado a Linha de Saldo pelo Totvs Obras e Projetos, o mesmo irá verificar a quantidade do movimento em relação a quantidade prevista que no cenário acima foi 300.  
   Linha de Saldo: valor da tarefa R$ 10,00    
                        Período             1(01/03)           2(01/04)           3(01/05)  
                        Quantid.            0                     0                      300  
                        Valor                 R$ 0                R$ 0                 R$ 3.000  
Neste exemplo, está faltando 300 de quantidade a ser pedida na Obra, independente do valor faturado. O pedido de quantidade 300 no valor de R$ 9000, foi abatido no 1º(01/03) e 2º(01/04) Período.  
  
As quantidades contratadas deverão ser abatidas do saldo do projeto. Na associação de itens de contratos ativos a pagar, ao associarmos uma tarefa, será estornado do valor contratado o valor de qualquer insumos já comprometidos e realizados. Este processo será executado da seguinte forma:

É verificada a existência de rateio no item associado no contrato.

Caso o rateio exista, uma verificação deve ser feita se o(s) insumo(s) existente(s) no item está(ão) vinculado(s) ao produto rateado.   
Caso o(s) insumo(s) NÃO estiver(em) vinculado(s) ao produto considera-se que seja(m) mão de obra; neste caso a busca deve retornar a quantidade dos insumos de mão de obra (percentual associado em cima da quantidade dos insumos), excluindo a mão de obra na proporção da quantidade contratada.

Fórmula para o Cálculo: Qtde Insumo - (Qtde Rateio)⁄(Qtde Tarefa)) \* Qtde do Insumo na Tarefa.

Se o(s) insumo(s) estiver(em) vinculado(s) ao produto de rateio, uma busca da quantidade usada desse insumo será feita através do produto de forma que retorne a quantidade a ser estornada das liberações.   

(Produto -> Insumo) ou (Insumo = mão de obra)

De forma semelhante, as quantidades comprometidas em Suprimentos/Faturamento devem ser abatidas. É verificado no módulo de Suprimentos/Faturamento as quantidades/valores de pedidos que já geraram ordem de compra, abatendo também do histograma. Considerando a estrutura do histograma, é realizado o abatimento das quantidades. Se a quantidade pedida ultrapassar o valor já existente, a quantidade fica com o valor 0,00; pois não existirão quantidades negativas neste caso. Na geração de pedidos, serão levados em consideração os produtos associados no rateio do item de contrato e não serão gerados pedidos para os insumos correspondentes.

Por fim, serão abatidos os valores previstos em períodos de contratos. Nesta etapa, é feita uma verificação dos valores previstos em contratos, adicionando estes valores ao cronograma de desembolso, por tarefa, de forma proporcional. O processo obedece as seguintes regras:

Os contratos devem estar com status "Em Negociação" ou "Em Andamento" e devem ser do tipo a pagar. • O cálculo será realizado de acordo com os valores previstos informado nos períodos dos contratos. • Se em algum período o campo de valor previsto não for informado, o mesmo recebera o valor rateado do restante do valor total do contrato. • Caso os valores informados no campo valor previstos ultrapassem o valor total do contrato, o valor será rateado por igual para todos os períodos de acordo com o valor total do contrato. • Caso algum período esteja liberado, o valor da liberação deve ser abatido no valor total do contrato.  
Em seguida, estes valores, caso sejam maiores que 0,00, são mesclados ao cronograma de desembolso. E, por fim, de forma semelhante ao que ocorre no processo de lançamento de linha base, os lançamentos anteriores são apagados e novos são feitos no módulo financeiro.

Escolha o tipo de geração:saldo
