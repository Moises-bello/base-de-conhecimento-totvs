---
content_hash: 572223fc85a30ba717f69bc88f667dda71012e9999f6a40218ef769ee6ea6e97
fetched_at: '2026-06-29T00:09:17.068218+00:00'
page_id: '421388571'
product: rm
source: tdn-rm
title: FIN - Acordo
type: documentation
url: https://tdn.totvs.com/display/LRM/FIN+-+Acordo
version: 30
---

O Acordo é uma modalidade de negociação que consiste em formalizar um novo plano de pagamento para o(s) Lançamento(s) Financeiro(s). Através do Template de Acordo será possível determinar descontos, acréscimos, juros, parcelamentos, prazos, entre outros. Com essas informações disponíveis o usuário poderá escolher o melhor plano para gerar o Acordo.

Pode ser:

**Simples:** Quando os lançamentos selecionados pertencerem ao mesmo Cliente/Fornecedor, o processo seguirá independente da regra do Template de Acordo permitir ou não alterar o Cliente/Fornecedor. Caso sejam selecionados lançamentos de Cliente/Fornecedor distintos, o sistema permitirá seguir com o processo somente se a flag 'Permitir Alterar Cliente/Fornecedor' estiver marcada no Template de Acordo selecionado.

**Em Lote:** Quando houver lançamentos para Clientes/Fornecedores distintos na seleção. Nesse caso, o sistema agrupa os lançamentos por Cliente/Fornecedor para processar o Acordo e o critério adotado (juros, desconto, número de parcelas entre outros) prevalecerá para todos os lançamentos selecionados. Este processo será executado conforme a regra citada acima somente quando forem selecionados lançamentos de Clientes/Fornecedores distintos. Caso sejam selecionados lançamentos de Clientes/Fornecedores iguais, o sistema seguirá o processo de Acordo Simples. Outra validação importante no Acordo em Lote é a regra do Template de Acordo informado pelo usuário, pois poderá ser utilizado somente o Template que estiver com a flag 'Permitir Alterar Cliente/Fornecedor' desmarcada.

O Acordo em Lote será utilizado sempre que houver a necessidade de se adotar o mesmo critério de negociação para todos os Lançamentos, como por exemplo, concessão de desconto de mesmo valor para todos os clientes que estiverem com seus pagamentos em dia. Nesse caso, a regra adotada no processo será válida para todos os Clientes/Fornecedores da seleção de lançamentos. Durante o processo, o(s) lançamento(s) financeiro(s) "objeto(s) do Acordo" será (ão) quitado (s), terão status alterado para "Baixados por Acordo" e o (s) valor (es) não afeta (rão) os saldos da Conta/Caixa. Serão gerados novos lançamentos conforme os critérios adotados. Os novos lançamentos classificados como "Gerados pelo Acordo" ainda poderão ser renegociados gerando novos Acordos.

Para gerar o Acordo em Lote de Cliente/Fornecedor igual é necessário que o tipo contábil dos lançamentos sejam o mesmo ou Contábil/Baixa Contábil ou Não Contábil/A Contabilizar, não podendo ser "Contábil" ou "Baixa Contábil" junto com "Não Contábil" ou "A Contabilizar", por exemplo.

**Observações:**

* O Acordo poderá ser gerado com juros Simples ou Composto. Esta definição implica na atualização dos lançamentos gerados pelo Acordo.

* Nos lançamentos gerados pelo acordo, onde se incluem os não efetivados, o campo Tipo Contábil será preenchido de acordo com a seguinte ordem: 1) para acordo com origem no Portal Educacional ou app Meu eduCONNECT busca do serviço vinculado a parcela; 2) valor informado no campo Tipo Contábil da tela do processo de geração do acordo; 3) com "Baixa Contábil" caso lançamento origem seja "Contábil" ou "Baixa Contábil"; 4) com o Tipo Contábil do lançamento origem.

* Durante o processo, se houver edição de alguma parcela com alteração de valor, o sistema irá recalcular o valor do Capital rateando a diferença entre as parcelas não editadas.

* Os valores correspondentes a Juros, Acréscimo e Desconto do Acordo serão gravados nos(s) Lançamento(s) "Gerado(s) por Acordo" e para visualizá-los basta editar o lançamento, pasta Valores / Acordo.

* É permitido cancelar um Acordo, desde que nenhum lançamento gerado esteja incluído em uma das categorias que restringem o cancelamento do lançamento gerado por Acordo. Ao cancelar um Acordo, a baixa dos lançamentos geradores será automaticamente cancelada e os lançamentos gerados serão também cancelados.

* No processo de carga de dados do acordo, a Filial será preenchida na seguinte ordem: 1) lançamentos (quando a filial for igual em todos selecionados); 2) default informado no Template de Acordo; 3) filial informada no contexto do sistema.
* Caso os valores de integração estejam parametrizados, eles serão carregados por default nos lançamentos gerados pelo acordo e poderão ser editados.

Recursos:

* Cálculo por Juros simples .
* Cálculo por Juros compostos .
* Valores/Percentual a Acrescentar .
* Valores/Percentual a Descontar .
* Agrupamento de Lançamentos para geração de parcela única.
* Desmembramento do Lançamento financeiro em parcelas com alteração de regras de atualização.

Consistências para o processo Acordo .

* Os lançamentos devem ter a mesma Natureza (Pagar/Receber).
* Os lançamentos devem ter mesmo Tipo Contábil, exceto no caso de combinação entre lançamento "Contábil" e "Baixa Contábil", onde prevalecerá o tipo "Baixa Contábil", já que são considerados equivalentes no contexto do Acordo.
* Os lançamentos devem ter o mesmo Aplicativo de Origem.
* O lançamento deve estar com status "Em Aberto" ou "Parcialmente Baixado".
* O lançamento não pode estar Faturado.
* O lançamento não pode ser um Vencimento de Fatura.
* O lançamento não pode estar Vinculado (Adiantamento, Nota de Crédito e Devolução).
* O lançamento não pode ter um Cheque emitido.
* O lançamento não pode estar Bloqueado (baixa e alteração).
* O lançamento não deve ser uma Baixa Pendente\* .
* O lançamento não deve ser Previsão (tipo de documento com classificação 'Previsão').
* Caso o usuário selecione um Template de Acordo que permita alteração do Cliente/Fornecedor (no caso de Cli/For Pessoa Jurídica, é permitido somente cadastros com a mesma raiz de CNPJ):
  + O lançamento selecionado não pode ser oriundo do TOTVS Educacional ou do TOTVS Construção e Gestão de Imóveis (módulo Imobiliário).
  + O sistema não permitirá seguir no processo caso exista integração ativa do RM com o Protheus.
  + Se a regra de efetivação do Template estiver marcado para utilizar aprovação no Fluig, será apresentado a informação de troca do Cliente/Fornecedor com o (s) cadastro (s) associado (s) no (s) lançamento (s) original (ais) e o que será utilizado no (s) lançamento (s) gerado (s).
* Os lançamentos não podem estar vinculados a um [boleto partilhado](https://tdn.totvs.com/pages/viewpage.action?pageId=865420413).

Atenção

O TOTVS Educacional possui uma parametrização para os acordos gerados via Negociação Online, onde é possível definir que os lançamentos gerados pelo acordo tenham o mesmo Tipo Contábil definido no Serviço utilizado no Acordo. Para mais detalhes acesse a documentação do TOTVS Educacional, [clicando aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=494962674).

Caso um ou mais lançamentos tenham tributação associada:

* Deve existir uma única Alíquota para cada Código de Tributo .
* Deve existir um único Código de Retenção para cada Código de Tributo e deve existir um único CST para cada Código de Tributo.

Os lançamentos devem ser compatíveis quanto à Geração de IR, ou seja, se IR não é gerado na baixa ou  todos os lançamentos são geradores de IR com mesma natureza Cliente/Fornecedor (Pessoa Física ou Jurídica) e mesmo código de receita ou todos os lançamentos não geradores de IR.

Os lançamentos com data de vencimento futuro e QRCode gerados podem ser utilizados para geração de acordo.

O lançamento com boleto associado:

* Boleto Registrado Online: Ao realizar o Acordo do lançamento o Status CNAB do boleto é alterado para Pendente de Remessa e continuará associado ao lançamento permitindo que seja cancelado posteriormente. Ao cancelar o Acordo, o boleto retorna ao Status CNAB Registrado Online.

* Boleto Não Remetido: Ao realizar o Acordo do lançamento o boleto é cancelado e continuará associado ao lançamento permitindo que seja excluído posteriormente.

**Cálculo do Juros**

- Valor capital da parcela:  
Valor de cada parcela sobre o montante negociado (valor líquido dos lançamentos origem)  
Exemplo: negociando 1.000,00 em 4 parcelas o valor capital de cada parcela será 250,00.

- Número de dias  
Define o intervalo de dias entre a data do acordo até o vencimento da parcela. O vencimento de cada parcela depende da configuração do Template de Acordo (Intervalo em dias e Prazo).

- Cálculo da taxa (lembrando que a taxa de juros informada é ao dia)  
JUROS SIMPLES  
Taxa Juros = (Taxa Juros Dia / 100) \* número de dias

JUROS COMPOSTOS  
Taxa Juros = Potência do número resultante de *1 + (Taxa Juros Dia / 100)* elevado ao número de dias, do resultado subtrai-se 1

- Cálculo do juros da parcela  
Valor capital da parcela aplicada a taxa arredondado pelo número de casas decimais parametrizado.

**Baixa Pendente ocorre nas seguintes situações**

1. Quando o Aluno paga sua parcela no portal Educacional, o status do Lançamento é alterado para "Em Aberto" e permanece desta forma até que se finalize o processo de efetivação e posterior baixa pelo Gestão Financeira.

2. Consistência de Baixa Pendente para lançamentos financeiros gerados através do TOTVS Gestão Fiscal: Ao definir que uma Guia que gerou um lançamento financeiro será uma Guia de Débito no processo de Compensações de Tributos Federais do TOTVS Gestão Fiscal, não será possível Editar, Baixar, Emitir/Receber Cheque, gerar Acordo ou Remeter para banco este Lançamento Financeiro. Esses processos só serão permitidos novamente para o lançamento após a execução do processo "Finalização do Cálculo da Compensação" do Gestão Fiscal.

3. Quando gerado acordo com Template de Acordo configurado para efetivar no pagamento da primeira parcela (BAIXAPENDENTE = 3 - Efetivação Acordo). O processo "Regerar Contabilização de Inclusão" foi evoluído para permitir que seja regerada a contabilização, porém o regerar contabilização na edição do lançamento foi mantida.

**Cancelamento do Acordo**

Para cancelar um Acordo acesso o Menu - Conta a Pagar - Receber | Acordo  | Gerenciar Acordo. Selecione o registro desejado para realizar o processo. Será possível executar o cancelamento de duas maneiras: "Varredura de Lançamentos" e "Cancelamento visão do Acordo".

Varredura de Lançamentos será utilizada quando a primeira parcela do Acordo já estiver vencida em um número de dias maior conforme o prazo que será definido na execução, sendo assim o sistema varrerá os Lançamentos Financeiros identificando o Acordo e cancelando o mesmo.

**Cancelamento pela visão de Acordo no Menu Processos**

Em ambos os casos a regra para cancelamento será a mesma: Lançamentos gerados pelo Acordo não podem estar baixados nem cancelados. O cancelamento do Acordo irá disparar um processo para que o módulo que fez o Acordo faça suas validações e também execute as regras de cancelamento em suas entidades (caso exista alguma).

O cancelamento somente será possível se todos os lançamentos gerados por Acordo atenderem a condição de cancelamento, do contrário o sistema não permitirá a conclusão do processo.

Na tela de cancelamento, o campo 'Motivo do Cancelamento',  será informado no processo e será armazenado e exibido nos dados do acordo juntamente com a Data do Cancelamento e o Usuário (campo da última alteração no registro). Esses estarão visíveis na tela de edição do acordo somente se o status for cancelado.

Para excluir um Acordo, que deverá estar cancelado, utilize o botão "Excluir".

**Observação**

Através do "Anexos" serão exibidos os Lançamentos do Acordo, Lançamentos gerados pelo Acordo e também os Lançamentos Gerados por Acordo não Efetivados.

**Percentual da primeira parcela**

É possível definir um percentual a ser considerado na geração da primeira parcela do acordo.  
Este percentual será informado no [Template de Acordo](https://tdn.totvs.com/x/muEdGQ) no campo 'Primeira Parcela (%)' (aba "Regras"), o valor informado será aplicado sobre o valor total da negociação na geração da primeira parcela, o valor do campo poderá ser nulo, maior que zero, menor ou igual a 100.

Na geração do acordo, tanto no TOTVS Gestão Financeira quanto na Negociação Online do Porta Educacional, quando selecionado o Template de Acordo com essa configuração de percentual para a primeira parcela, o valor será aplicado sobre o valor total de negociação e atribuído à primeira parcela e o valor restante será distribuído igualmente para as demais parcelas. Na tela de geração do acordo o valor da primeira parcela poderá ser editado, mas somente para valor igual ou superior ao configurado no Template.

Veja Também

 Informações Complementares

* [BT - Gerar Acordo Financeiro](http://tdn.totvs.com/display/LRM/RMFIN00001_FIN_BT_Acordo_Financeiro_FIN000287?preview=/185756519/185670778/FIN_BT_Acordo_Financeiro_FIN000287.pdf)
* [Acordo via Web Service](https://tdn.totvs.com/display/LRM/Acordo+via+Web+Service)
