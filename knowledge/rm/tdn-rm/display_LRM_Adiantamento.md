---
content_hash: 9d15e932035975d749db696128787667c0b3689f0760207a40920b14b5fff7d2
fetched_at: '2026-06-29T00:09:18.117247+00:00'
page_id: '421388672'
product: rm
source: tdn-rm
title: Adiantamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Adiantamento
version: 21
---

Corresponde a um valor dado como Adiantamento, que será confrontado com outros Lançamentos Financeiros no processo de Baixa, Emissão de Cheques e integrações bancárias.

**Aplicabilidade**

* Adiantamento para Viagem;
* Adiantamento a Fornecedores;
* Adiantamento de Clientes, etc.

Ao incluir um Lançamento de Adiantamento e baixá-lo será gerado um novo Lançamento classificado como "Crédito de Adiantamento". Este novo Lançamento será confrontado com outros de valor igual, maior ou menor. É através do "Crédito de Adiantamento" que será gerenciada toda a dinâmica do processo.

**Pré-requisito**

* Tipo de Documento classificado com "Adiantamento";
* Tipo de Documento específico, classificado como "Crédito de Adiantamento"
* Utilizar eventos contábeis associado à Tabela Opcional ou ao Tipo de Documento para automatizar a Contabilização.
* A Classificação do Cliente/Fornecedor (pasta identificação do cadastro do Cliente fornecedor) deverá ser AMBOS.

**Procedimento**

1. Incluir um Lançamento a pagar, Tipo de Documento "Adiantamento". Exemplificaremos o gerenciamento de um Adiantamento para Viagem.
2. Baixar este Lançamento:  Na baixa será gerado um Lançamento do tipo "Crédito de Adiantamento" com natureza (pagar/receber) inversa à natureza do Lançamento de Adiantamento, com os mesmos dados do lançamento de adiantamento.
3. Incluir um Lançamento a Pagar correspondente à despesa.

Ao baixar o Lançamento referente à despesa, o sistema identificará que existe um Adiantamento que poderá ser vinculado e exibirá uma tela para que o vínculo seja estabelecido. O vínculo também poderá ser feito antes do processo de baixa, através do menu Processos | Vincular lançamentos.

Feito isso, o valor do crédito de Adiantamento será confrontado com a despesa, sendo:

1.000,00 Valor do Crédito de Adiantamento

 -800,00 Valor da despesa efetiva.

 200,00 Parte do Crédito de Adiantamento passível de vinculo

**Efeitos**

A baixa do Lançamento correspondente à despesa será zerada, pois o valor do Adiantamento foi maior do que a efetiva despesa. Nesse caso não gera extrato de caixa correspondente.  
No lançamento referente ao Crédito de Adiantamento ficará armazenada a diferença de R$200,00, que poderá ser utilizado numa próxima operação de vinculo (outro adiantamento de viagem). Se não houver mais operação de Adiantamento para este Fornecedor, o valor da diferença então poderá ser devolvido para a Conta Caixa.   
Para isto, basta baixar o Crédito de Adiantamento.

**Outras possibilidades**

Se a Despesa for maior do que o Adiantamento (considerando que estejam vinculados): A baixa será realizada pela diferença e será gerado o respectivo extrato de caixa.

1.000,00  Valor do Crédito de Adiantamento

1.800,00  Valor da despesa efetiva.

  800,00  = Valor da baixa do Lançamento correspondente à despesa. Extrato de Caixa de mesmo valor.

Se a despesa for o mesmo valor do Adiantamento (considerando que estejam vinculados): A baixa será com valor zero.

1.000,00 - Valor do Crédito de Adiantamento 1000,00  Valor da despesa efetiva.

      0,00  = Valor da baixa do Lançamento correspondente à despesa. Não será gerado Extrato de Caixa.

**Observações:**

* Crédito de Adiantamento não irá possuir valor de baixa e assim, a coluna Valor Baixado na visão de lançamentos não será preenchida.
* O item de baixa que é criado para o Crédito de Adiantamento quando o vínculo é total não deve possuir valor de baixa, visto que o mesmo não cria Extrato de Caixa e o valor em si já foi baixado no Adiantamento.
* Consequentemente se não possui valor de baixa, nenhum campo referente a valor baixado irá ser preenchido para o Crédito.
* O valor presente em FLANBAIXA.VALORVINCULO será considerado no cálculo do campo FLANBAIXA.VALORBAIXA dos lançamentos de crédito de adiantamento.
* O valor baixa é utilizado para calcular o saldo inicial do relatório de fluxo de caixa.
* Lançamentos de adiantamento, que possuam a parametrização do Rateio centro de custo/Natureza orçamentária parametrizada para usar o rateio "Ambos" ou "Natureza" e não possuir os defaults parametrizados, será considerado o comportamento já existente no sistema.
* Para lançamentos de adiantamento, que possuam a parametrização do Rateio centro de custo/Natureza orçamentária parametrizada para usar o rateio "Ambos" ou "Natureza" e possuir os defaults de "Natureza orçamentária default de crédito de adiantamento a receber" e "Natureza orçamentária default de crédito de adiantamento a pagar" informados, ao realizar a baixa do lançamento de adiantamento, o sistema irá considerar a natureza orçamentária parametrizada para gerar o lançamento de crédito de adiantamento.
* Não será permitido a geração de Borderô de pagamento para lançamentos com valor líquido igual a 0 (zero), com data de referencia a sua data de vencimento.
* É possível vincular o lançamento pertinente ao crédito de adiantamento com outro cujo o Cliente/Fornecedor seja diferente, desde que o parâmetro "Não Permite vínculo de Lançamentos entre Cliente/Fornecedores Diferentes' esteja desmarcado. Para visualizar este parâmetro, acesse o menu Ambiente | Parâmetros | TOTVS Gestão Financeira | Avançar | Contas a Receber (ou Contas a Pagar) | Avançar | Etapa Baixa 2/6.

**Cálculo do valor baixa:**

FLANBAIXA.VALORBAIXA = FLANBAIXA.VALORORIGINAL - FLANBAIXA.VALORVINCULADO - FLANBAIXA.VALORESQUEDESCONTAM + FLANBAIXA.VALORESQUEACRESCENTAM

O processo "Ajustar Valor Baixado em Lançamentos Vinculados" tem como objetivo percorrer todos os lançamentos vinculados de crédito de adiantamento, devolução ou nota de crédito que já foram baixados e ajustar o seu valor, para que obedeçam as regras acima exemplificadas. O processo pode ser executado em paralelo com o sistema em produção, porém, dependendo da quantidade de lançamentos, pode tomar um tempo considerável.

**Contabilização de baixa de crédito de adiantamento**

Para que seja contabilizada a baixa com crédito de adiantamento é preciso que o parâmetro "Contabilizar crédito de adiantamento em filiais distintas" esteja marcado. Essa parâmetro do sistema é apresentado desmarcado como default.

Será preciso cadastrar um evento contábil de baixa e informar esse evento como default de contabilização em uma das tabelas opcionais usadas ou no tipo de documento que será usado, para que seja aplicado na contabilização do lançamento de crédito de adiantamento quando realizada a baixa da nota vinculada.

A contabilização será realizada somente quando a operação é entre filiais distintas.

Exemplo do cliente. Ele é um prestador de serviços de saúde.   
O cliente dele fecha um pacote na filial 1, mas vai na filial 2 para fazer um exame.   
Então o propósito é fazer o acerto contábil do recebimento do adiantamento em filial diferente daquela que ocorreu a prestação   
do serviço.

**Adiantamento Gerador de IR**

A partir da versão **12.1.2209**, torna-se possível que adiantamentos a pagar para **fornecedores pessoa jurídica** possam ser geradores de imposto de renda. Visando este objetivo, o cadastro de [tipo de documento](https://tdn.totvs.com/pages/viewpage.action?pageId=421388695) passou a dispor do novo campo "Gera IRRF" na aba "Dados Adicionais", que passa a ser apresentado quando a classificação é "Adiantamento".

Ao incluir novo lançamento a pagar, para um Cliente/Fornecedor 'Pessoa Jurídica', usando o tipo de documento de classificação "Adiantamento", com o atributo "Gera IRRF" habilitado, será habilitada o botão "Exibir dados para cálculo de IRRF", onde deverá ser informado o respectivo Código de Receita. O lançamento será incluído com a classificação "Adiantamento e Gerador de IR", e o respectivo lançamento de imposto com classificação "IRRF PJ" também será gerado.

Ao baixar o lançamento de classificação "Adiantamento e Gerador de IR", ocorrerá a geração de lançamento de natureza inversa, com classificação "Crédito de Adiantamento", como qualquer outro lançamento de classificação "Adiantamento", e poderá ser utilizado em vínculos normalmente.

Quando ocorrer o vínculo deste crédito de adiantamento com um lançamento com classificação "Gerador de IR", o imposto já retido pelo adiantamento será deduzido do IR gerado pelo lançamento vinculado. Este vínculo somente será permitido se no momento do vínculo o lançamento de classificação "IRRF PJ" associado ao lançamento de classificação "Gerador de IR" esteja em aberto, e não tenha sido incluído em nenhuma guia pelo TOTVS Gestão Fiscal.

 Informações Complementares

* [Vincular e desvincular lançamentos de adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053464674-Cross-Segmentos-Backoffice-Linha-RM-FIN-Como-realizar-vinculo-de-adiantamento-devolu%C3%A7%C3%B5es-entre-lan%C3%A7amentos-com-Clientes-Fornecedores-distintos)
* [Defaults de natureza orçamentária financeira créditos de adiantamento](http://tdn.totvs.com/pages/viewpage.action?pageId=286522237)
* [DT- Contabilização de baixa de crédito de adiantamento](http://tdn.totvs.com/pages/viewpage.action?pageId=286522237)

Veja Também

* [Cadastro Tabelas Opcionais](http://tdn.totvs.com/display/LRM/FIN+-+Tabelas+Opcionais)
* [Cadastro Tipo de Documento](http://tdn.totvs.com/pages/viewpage.action?pageId=421388695)
* [Parâmetro para contabilização da baixa do crédito de adiantamento](http://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar)
