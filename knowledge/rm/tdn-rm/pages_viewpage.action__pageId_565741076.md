---
content_hash: 9a6fa1ace8eb2351b68f4facac57bb624176d2c06c42b58843ecfa5b9c13b577
fetched_at: '2026-06-29T00:10:51.282332+00:00'
page_id: '565741076'
product: rm
source: tdn-rm
title: Geração de Borderô em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=565741076
version: 21
---

O processo de inclusão de Borderô de Pagamentos em lote consiste em gerar borderô de pagamento multi-coligada. O processo visa gerar as remessas bancárias em um único processo para todas as suas coligadas agilizando assim as rotinas de integração bancária, gerando de uma só vez as informações de todas as coligadas.

Com a utilização de um filtro genérico juntamente com o banco vinculado à conta caixa, o processo irá permitir ao usuário gerar borderô de pagamentos para cada coligada e convênio presente nos lançamentos a pagar selecionados. O processo está disponível no menu Movimentações Bancárias → Borderô de Pagamentos (clicar na seta localizada ao lado desta opção).

Regras de utilização

Só será permitido a inclusão de borderô para lançamentos a pagar em aberto ou parcialmente baixado;  
- Só será permitido a inclusão de borderô quando o campo relativo à “Forma de Pagamento” for preenchido no (s) lançamento (s). Este campo se encontra na aba “Integração Bancária” do lançamento em “Dados Bancários”, o cadastramento do campo será no cadastro do Cliente Fornecedor.  
- Só será permitido a inclusão de borderô para lançamento a pagar que utilize conta caixa com o banco informado no castrado da conta caixa.  
- Só será habilitado o processamento em lote se o usuário logado tiver permissão de acesso configurado no perfil do usuário.

Lançamentos não passiveis de geração de borderô

O lançamento não pode estar faturado;   
O lançamento não ter cheque emitido;   
O lançamento não está bloqueado;  
O lançamento sem dados bancários informados;   
O lançamento de moeda diferente de real;   
O lançamento com forma de pagamento igual a cartão de crédito;   
O lançamento não pode ser de previsão;   
O lançamento não ter baixa pendente;   
O lançamento oriundo de movimento não pode estar bloqueado;  
O lançamento não pode está vinculado em outro borderô de pagamento;  
O lançamento não pode ser lançamento de repasse.

Processamento em lote

Na aba "Dados do Borderô de pagamento em lote" será preciso informar "Banco". Para o processamento em lote somente será aceito e permitido pelo sistema banco vinculado à conta caixa presente no lançamento a pagar.

Obs.: Lançamentos com conta caixa vinculada com banco diferente do banco informado na tela de processamento em lote, não serão processados.

O campo "Descrição" é livre para preenchimento e controle interno do usuário.

No campo "Data Pagamento" a data selecionada será utilizada para cálculo do valor liquido dos lançamentos e como base para cumulatividade de retenção. No processo de remessa de pagamento essa mesma data será utilizada.

A opção de data informada nesse campo corresponderá a data informada nos lançamentos selecionados, sendo assim quando selecionada a data de pagamento do tipo emissão, por exemplo, o sistema irá buscar a data de emissão dos lançamentos para geração do borderô. As opões de preenchimento de data são:

* Vencimento
* Emissão
* Previsão de Baixa

**Observação:**No processo em lote não será disponibilizada a opção de "Datas opcionais", pois para cada coligada pode ser que tenha parametrização diferente em cada data opcional.

No campo "Filtro genérico" o usuário irá selecionar o filtro desejado para retornar os lançamentos a pagar para a inclusão dos borderôs de pagamentos por coligada e convênio. Recomenda-se que o filtro selecionado referencie o código da coligada para execução do processo. Caso contrário o sistema efetuará o processo para todas as coligadas. A montagem do filtro referencia a tabela de lançamentos do sistema e deve ser gerado atentando se as regras de geração do processamento em lote, lançamentos a pagar, em aberto, etc.

Caso esteja parametrizada a "Contabilização de Mútuo" disponível em Integração Contábil | Contabilização, o borderô poderá conter para um único convênio, lançamentos de diversas coligadas. Isso ocorrerá nas situações onde, junto à parametrização da Contabilização de Mútuo, o usuário associar o convênio à lançamentos de coligadas diferentes da coligada proprietária dele.

Autorização do Borderô

A autorização de um borderô deve ser processada para que seja permitido gerar Remessa de Pagamento (envio do arquivo de dados ao banco). A autorização poderá ser realizada no momento de geração do borderô em lote, bastando selecionar a opção "Autorização" e informar uma data válida no campo "Data de Validade". Quando não selecionada a opção de autorização na tela de execução do processo de geração do borderô em lote, a mesma também poderá ser feita na visão de Borderô através do menu de Processos → Autorização de Borderô de Pagamentos. A autorização terá validade e a data de validação será informada na tela de processamento da autorização através do campo “Nova Data de Validade da Autorização“.

**Observações:**

A opção "Autorização" ficará disponível somente para usuários com permissão de acesso ao processo “Autorização de Borderô de Pagamentos”. A permissão deverá ser concedida ou negada no módulo de globais através do perfil associado ao usuário de acesso ao sistema.

A data de validade do Borderô de Pagamentos não pode ser menor que a data do sistema.

Fórmula Dados Bancários

No [cadastro de convênio](https://tdn.totvs.com/x/LeIdGQ) aba Dados Adicionais foi criado o campo “Fórmula Dados Bancários” para o Borderô de Pagamentos. Esse campo tem o objetivo de armazenar a fórmula que será utilizada na inclusão do Borderô de Pagamentos e no Vínculo de Borderô de Pagamentos para  obter de forma automática o registro de dados bancários para o lançamento financeiro a pagar. Desta forma será possível personalizar regras para o preenchimento dos dados bancários do lançamento de forma automática. Essa opção trará ao usuário mais agilidade no processo de inclusão de lançamento a borderô ou na geração de um novo borderô fazendo com que o sistema considere a forma de pagamento mais vantajosa em termos de custo financeiro.

O sistema irá carregar para os lançamentos o default que melhor se aplica de acordo com uma determinada regra, definida pela fórmula.

Ex. Para valores até R$4.999,99 será usado a forma de pagamento X, para valores maiores será usado a forma de pagamento Y.

No cadastro de cliente/fornecedor serão definido os dados bancários e o default a ser usado, o mesmo continua sendo carregado ao cadastrar lançamento. Porém, ao executar o processo de geração de borderô ou vinculo de borderô, o sistema irá usar a fórmula configurada e fará a devida alteração no lançamento, gerando o borderô com os valores corretos e a forma de pagamento que melhor se aplica a regra definida.

**Observações:**

* No processo de geração de borderô, caso a fórmula não esteja preenchida para o convênio, a forma de pagamento já existente no lançamento será mantida e o borderô gerado.
* O borderô de pagamento será gerado

 Veja Também

* [Procedimento da integração de Borderô com o Fluig](https://tdn.totvs.com/x/BiYSCw)
* [DT - Inclusão de Borderô de Pagamento em Lote](https://tdn.totvs.com/x/FBudIQ)
* [DT- Fórmula Dados Bancários no Convênio](https://tdn.totvs.com/x/1HrpIQ)
