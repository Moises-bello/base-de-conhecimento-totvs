---
content_hash: 6dfd032e65dbebf69db67cf1f5f8f01a11b48f3398f4bc9e6b1f05c5d1e70d42
fetched_at: '2026-06-29T00:09:15.567297+00:00'
page_id: '421385412'
product: rm
source: tdn-rm
title: Liberação de Retenção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385412
version: 10
---

Liberar as retenções de um período.

Será considerado na liberação de retenções contratuais o rateio por estado\município informado no momento da retenção.

Para Liberar um período parcialmente. Pode gerar vários movimentos até o saldo disponível para liberação.

Pode-se agrupar varias medições e gerar apenas 1 movimento ou pode-se agrupar varias medições e gerar vários movimentos, até o saldo disponível para liberação.

Pode-se criar vários movimentos para uma mesma retenção, existe a opção para visualizar esse movimento.

Para realizar a liberação de uma retenção é necessário que seja informado um valor/percentual de retenção para o contrato, que seja liberado um período do contrato, para que então seja criado o período com o valor da retenção que será liberado.

O valor da retenção pode ser informado na edição do contrato na aba default ou através do processo "Liberar Período" onde aparecerá uma tela que encontra-se a aba Detalhamento de retenção, em que é possível inserir o valor ou percentual da retenção. Para que a retenção seja realmente atribuída é necessário executar a liberação, mas não é necessário que sejam marcadas as opções de Liberação para o Totvs Obras e Projetos ou para o Totvs Gestão Financeira.

Para realizar a liberação da retenção é necessário selecionar o período de retenção que se encontra no Anexo | Retenções Contratuais, da visão de contratos e acionar o processo "Liberação de Retenção". A retenção irá considerar o estado/município, centro de custo e departamentos informados no anexo do contrato, e irá considerar apenas o produto informado no ato da liberação ou o que esta definido como default do contrato.

Se nos  , na parte de   a checkbox "Discriminar valores de retenção e dedução" estiver marcada (Acesso: F6>>Contratos>>Discriminar valores de retenção e dedução), os produtos considerados na geração do movimento são os mesmos utilizados, no movimento que foi gerado ao liberar a medição do período. Essa informação será exibida na tela do processo.

**Rateio por estado e município**  
A obtenção dos itens do rateio por estado e município serão obtidos seguindo a seguinte precedência:  
1.Obtém o rateio de estado/município por contrato, gerando *n* movimentos quantos forem os estados/municípios informados no contrato.  
2.Caso não tenha obtido rateio no passo 1 obter  Estado/município cadastrados no projeto, gerando 1 movimento.

**Rateio por produtos**  
A obtenção dos itens do rateio por produtos serão obtidos seguindo a seguinte precedência:  
1.Obter produto default (definido no processo).  
Será gerado apenas um item de movimento referente ao produto informado no default do contrato ou no momento da realização do processo.

**Rateio por departamento**  
A obtenção dos itens do rateio por departamentos serão obtidos seguindo a seguinte precedência:  
1.Obtém rateio de departamento por contrato.

**Rateio por centro de custos**  
A obtenção dos itens do rateio por centro de custo serão obtidos seguindo a seguinte precedência:  
1.Obtém rateio de centro de custo por contrato.  
2.Caso não tenha obtido rateio no passo 1 obter centro de custo default (definido no processo).  
  
Os seguintes campos serão preenchidos ao liberar a retenção. Através destes serão definidos valores default para os atributos referentes.

Tipo de movimento a ser gerado

Produto

Filial

Local de estoque

Centro de custo do movimento

Condição de Pagamento (Opcional)

Caso exista integração com Protheus/EMS o campo referente ao Tipo de movimento, ficará desabilitado, caso o período for de estorno o campo de observação ficará desabilitado.   
A aba "Tabelas opcionais" não será exibida quando houver integração com Protheus/EMS ou quando nenhuma tabela estiver sendo utilizada no movimento.  
A utilização ou não de uma tabela será definida no Suprimentos/Faturamento em: Parâmetros/RM Nucleus/Parâmetros Gerais/Tabelas/Classificação. Para uma tabela ser exibida, o parâmetro "Usar no movimento" deve estar selecionado.    
Em Parâmetros/RM Nucleus, após selecionar um Tipo de movimento e acessar a opção Mov - Tab – Classificação é possível definir um valor default para cada tabela, valor com o qual a tabela (lookup) vira preenchida.   
Além disso, será possível definir o tipo de edição de cada tabela:

**Não Edita**: O campo referente à tabela não será exibido.

**Edita**: O campo será exibido e poderá ser editado.

**Mostra**: O campo será exibido, mas não poderá ser editado.

O preenchimento dos campos da aba de "Tabelas opcionais" não é obrigatório.  
Os valores extras serão parametrizados de acordo com o tipo de movimento no Suprimento/Faturamento em: Parâmetros/RM Nucleus, após selecionar um Tipo de movimento e acessar a opção "Mov – Valores Financeiros".  
A aba "Valores extras" não será exibida quando não estiver sendo utilizado nenhum valor extra.  
O nome de cada campo poderá ser customizado de acordo com o nome definido no campo nome referente ao valor extra.  
A exibição dos campos Percentual e Valor de cada valor extra, será definido através da opção "Tipo Valor Extra" sendo definida como:

**Percentual**: só exibe o campo Percentual

**Valor**: só exibe o campo Valor

**Ambos**: exibe os campos Percentual e Valor

O preenchimento dos campos da aba de "Valores extras" não é obrigatório. 

**Cancelamento de Liberação de Retenção**

Pode-se cancelar um período ou mais para o movimento.

Informações - Natureza Orçamentária

Para que a Natureza Orçamentária/Financeira seja enviada no item de movimento, é necessário que o Tipo de Movimento esteja parametrizado para utilizá-la:

A definição dos parâmetros abaixo é prioritária em relação a parametrização da aba Orçamento, isto é, a busca da Natureza nas entidades "Grupo de Custo/Insumo", "Projeto" e "Tarefa" somente será realizada se os mesmos não estiverem definidos:

Se os parâmetros acima não estiverem definidos, a origem da Natureza Orçamentária/Financeira que será enviada no item do movimento, depende da parametrização definida nos Parâmetros de Projeto abaixo:

Algumas regras devem ser consideradas para a definição da Natureza:

* Contrato com itens associados (Tarefas):
  + Grupo de Custo/Insumo: Através do produto, o insumo é encontrado onde existe a Natureza definida ou no seu Grupo de Custo;
  + Projeto: Natureza definida no cadastro do Projeto;
  + Tarefa: Natureza definida no cadastro da Tarefa.

* Contrato com objetos associados (Insumos):
  + Grupo de Custo/Insumo: Deve ser considerada a Natureza do insumo consumido ou seu Grupo de Custo;
  + Projeto: Natureza definida no cadastro do Projeto;
  + Tarefa: Natureza definida no cadastro da Tarefa utilizada no consumo.
