---
content_hash: fbc2261de518b43412e679ffea8934a5f8629e5a472085a64f32c0f4dd60fc3f
fetched_at: '2026-06-29T00:09:15.336188+00:00'
page_id: '421385350'
product: rm
source: tdn-rm
title: Contrato Utilizando Moeda Diferente
type: documentation
url: https://tdn.totvs.com/display/LRM/Contrato+Utilizando+Moeda+Diferente
version: 2
---

Essa implementação visa incluir a opção para que determinados contratos possam trabalhar com moedas que serão cotadas de forma diferente em relação a moeda utilizado no projeto e essa moeda do contrato ser prioritária em relação a do projeto.  
 **Parâmetros:**  
 Foi criado o parâmetro "Utilizar moeda no contrato" na aba Geral nos parâmetros do Contrato para que seja possível no cadastro de contratos, a informação de uma moeda diferente da moeda definida no Projeto.   
 Ao marcar esse parâmetro, é obrigatório a informação de uma "Data base de conversão da Moeda". Esse parâmetro se faz necessário para a busca da cotação das moedas a partir dessa data, quando houver necessidade de conversão.  
 Obs: Se existir algum contrato que possua alguma moeda definida, esse parâmetro não poderá ser desmarcado.  
 No cadastro de contratos deverá ser possível informar a moeda que será adotada para o Contrato. Exemplo: U$ DOLLAR.  
 Obs: Contratos com insumos ou tarefas associadas, não poderão ter moeda do contrato alterada.

**Associação de Itens/Objetos aos Contratos**   
 Na associação de itens ao contrato, a associação irá considerar a moeda definida no Contrato. As opções de associação por "Valor Unitário (Com BDI), Custo Unitário e Nenhum" ficarão desabilitadas quando o projeto utilizar moeda no contrato diferente da do projeto e o valor a ser associado deverá ser informado manualmente já na moeda do Contrato. **Obs: Esse caso, também será considerado na Associação de Objetos ao Contrato.**

**Importante:** A associação de tarefas, continua considerando o parâmetro "Permitir contratação de serviços com o Valor Superior ao Orçado (Contrato a Pagar)". Porém, irá considerar a cotação cadastrada para as moedas de Projeto para moeda do Contrato.

**Exemplo:   Moeda do Projeto = R$ (Real)** **Moeda do Contrato = U$ (Dólar)** **Cotação cadastrada: 1,00 Dólar = 4,00 Reais**  
Nesse caso, se a tarefa é 1000,00 Reais, o máximo a ser associado na moeda do contrato é 250,00 Dólares.

**Importante:** Foi definido uma margem de erro para casos em que o valor fica com casas decimais, tendo a seguinte regra:  
Considerando o exemplo acima, o valor associado poderá ser no máximo 251,00 Dólares, pois a margem de erro é considerada 1000,00 Reais do valor da tarefa + UMA unidade da Moeda do Contrato.

**Ou seja: 1000,00 + 4,00 = 1004,00 / 4 (U$) = 251,00 U$.**  
 Se a associação for feita acima de 251,00 U$ o sistema vai consistir em cima do parâmetro marcado, informando que está acima do orçado.  
 Esses valores de moedas diferentes, poderão ser visualizados através das colunas "Valor Unitário Orçado e Custo Unitário Orçado", estes, mostram a moeda do contrato e projeto.  
 **Liberação de Período**  
 No processo de liberação de período, os valores utilizados, todos serão considerados os de medição, nos quais, já na moeda do contrato.  
 Essa liberação, vai enviar para o financeiro a moeda do contrato.  
 **Reajuste do Contrato**  
 O processo de reajuste do contrato e do item do contrato, vai considerar a moeda do contrato para aplicação de seu fator.  
 **Geração de Integração com Suprimento/Faturamento**  
 Nesse processo, os valores enviados serão os valores da liberação do contrato, não tendo necessidade de conversão, uma vez que na medição, os valores já estão na moeda do contrato.  
 A moeda do contrato deverá ser enviada, juntamente com os parâmetros e valores que atualmente são enviados para o movimento. Isso também ocorrerá com a **liberação da Retenção.**  
 **Cronograma**   
 No processo de atualizar cronograma pelos lançamentos da medição, haverá uma conversão de valores no momento em que esses valores são lançados no cronograma quando a moeda do contrato for diferente da do projeto. A data de referência para essa conversão sempre vai ser a Data Início do Período.  
 **Insumo Derivado** Existe a possibilidade de vincular um contrato de serviço de qualquer projeto na regra de derivação. Existem três funções de fórmulas que complementam essa derivação de contratos que deverão ter o retorno dos valores, previsto, medido e liberado, convertidos de acordo com a moeda do contrato em relação à moeda do projeto do insumo. A data base para a conversão deverá ser a **data de início do período** do contrato:

* VLRPDOCNTPLAN(TIPOBUSCA): Resgata o **valor previsto** do contrato para o período de cronograma;
* VLRPDOCNTMED(TIPOBUSCA): Resgata o **valor medido** do contrato para o período de cronograma;
* VLRPDOCNTREAL(TIPOBUSCA): Resgata o **valor liberado** do contrato para o período de cronograma.

**Pedido de Material / Pedido de Material Extra**  
 Na geração do pedido de material, os itens incluídos serão considerados com moeda definida no Contrato e valor dessa moeda de acordo com o que foi associado.  
 Já no pedido de material extra, ao efetuar o vínculo com o contrato que tenha moeda diferente, esse item associado neste pedido extra, deverá vir com o valor já convertido de acordo com a moeda e item associado ao contrato.  
 Para esses dois tipos, ao gerar um movimento, esse movimento não será separado de acordo com a moeda, pois o processo já agrupa os movimentos separadamente em relação ao contrato vinculado.  
 **Cronograma de Desembolso**  
 Ao calcular o cronograma de desembolso considerando os contratos, vai acontecer a conversão do **Valor Unitário Contrato** de cada insumo contratado utilizando o parâmetro **Data Base de Conversão da Moeda** como referência e também do **Valor Previsto do Contrato**, porém essa conversão irá utilizar a **Data Início** do período do contrato.  
 **Saldo para Fluxo de Desembolso**  
 No processo de saldo para fluxo de desembolso, ao obter a natureza orçamentária relacionada ao contrato, o valor medido/liberado ou o valor atual de cada item associado, deverá ser convertido para a moeda do projeto. Considerando sempre a **Data Início** do período do cronograma como referência, e o mesmo deverá acontecer para o valor do contrato e valor previsto que também são utilizados para o cálculo do fluxo.  
 **Relatórios**                     
 Os seguintes relatórios foram apresentarão a moeda do contrato ao lado dos valores exibidos:  
 **Medição Completa:** Medição Completa e Medição Completa com Detalhamento de Retenção.  
 **Genéricos:** Contratos por Projeto, Itens do Contrato, Relação de Contratos por Projeto, Itens Medidos, Pagamento de Medição, Resumos de Medições do Projeto por Contrato e Evolução Financeira.

**Importante:** Não é possível criar contratos de licitação em projetos que tenham contratos com moedas diferentes do projeto. O processo de **Gerar Contrato** não é possível informar a moeda do contrato.

Como Fazer

---

 

 

Atualiza Cronograma pelos Lançamentos de Medição

  

Associar Períodos do Contrato à periodos do Cronograma

 

Liberar Período
