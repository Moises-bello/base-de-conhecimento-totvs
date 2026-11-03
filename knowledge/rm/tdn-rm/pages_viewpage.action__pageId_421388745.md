---
content_hash: 077a7013e8a5225289352ad8978fd28a15aa8e5db6d91f49503607fb30ea198b
fetched_at: '2026-06-29T00:09:18.678974+00:00'
page_id: '421388745'
product: rm
source: tdn-rm
title: Relatório Extrato Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388745
version: 11
---

O relatório fixo demonstrará exclusivamente a posição financeira por Cliente/Fornecedor em determinado período.  Este relatório é uma versão simplificada do "Relatório Razão", sem dependências com integração com tabelas contábeis ou com tabelas da Gestão de Estoques Compras e Faturamento, sendo denominado "Extrato de Cliente/Fornecedor".

Para que os lançamentos sejam apresentados no relatório, será preciso marcar a opção "Considerar no Relatório Extrato de Cliente/Fornecedor" disponível no cadastro do Tipo de Documento usado nos lançamentos.  
Parâmetros para a montagem dos filtros:

Filiais 

Será preciso definir se o sistema irá buscar lançamentos de todas as filiais ou de alguma específica na geração do relatório.

Cliente/Fornecedor

Será preciso definir se o sistema irá buscar lançamentos de todos os Clientes / Fornecedores ou de algum específico na geração do relatório.

Critério de ordenação 

Por default o relatório será ordenado pelo código do Cliente/Fornecedor, mas será possível ordenar também pelo nome fantasia.

Intervalo de datas 

Será preciso informar a data inicial e final onde serão apresentados no relatório todos os lançamentos que tenham a data selecionada e que esteja dentro do período informado.

Data Considerada no Extrato 

Serão apresentadas duas opções para seleção:

* Data de Emissão Serão apresentados no relatório todos os lançamentos que tenham a data de emissão que esteja dentro do período informado.
* Data opcional Todos os lançamentos incluídos com a data opcional cadastrada serão carregados para o relatório gerado. Para esta opção existe um parâmetro que determina se é utilizada alguma Data Opcional e também a descrição que será apresentada, através do menu Parâmetros | Manutenção de Lançamentos |Datas Opcionais.

**Tabela Opcional**

Nesta etapa serão disponibilizadas as opções de filtrar os lançamentos conforme o conteúdo de uma das tabelas opcionais ou pelo Tipo de Cliente/Fornecedor. Para cada uma das tabelas opcionais existe um parâmetro que determina se é utilizada e um parâmetro que determina a descrição que deve ser apresentada, estas definições serão feitas através do menu Ambiente |Parâmetros | Totvs Gestão Financeira |Tabelas Opcionais.

Valor da Tabela Opcional

Este campo mostra as opções de valor da tabela opcional selecionada, que será critério de seleção dos lançamentos que serão impressos neste relatório.

Status (Classificação)

Neste campo será preciso selecionar a classificação dos lançamentos, do Cliente/Fornecedor e o Tipo Contábil que deverão ser impressos no relatório.

Relatório a ser utilizado

Será necessário selecionar um relatório do RM Reports que seja do tipo "EXTRATOCLIFOR".

Gerar Relatório

Ao executar esta opção o relatório listará os extratos do(s) Cliente(s) /Fornecedor (es) de acordo com os parâmetros definidos e serão exibidos de acordo com as seguintes colunas:

* Ref -  Corresponde a referência do lançamento.
* Data - Corresponde a data de emissão se o lançamento estiver em aberto ou a data da baixa se baixado.
* Inclusão - Corresponde aos lançamentos em aberto, o valor será igual ao valor original do lançamento. Baixa Corresponde aos lançamentos baixados, o valor será igual ao valor baixado do lançamento.
* Saldo Acumulado -  Corresponde ao acréscimo ou decréscimo das colunas de Inclusão e Baixa.

Considerar Valor do Adiantamento para obter o valor do lançamento

Quando o parâmetro estiver selecionado, o sistema irá considerar o valor do lançamento subtraído do valor do vínculo realizado.

Exemplo:  
Lançamento x:  
Tipo documento: Adiantamento  
Valor original = R$ 500,00

Lançamento y:  
Tipo documento: Sem classificação  
Valor original = R$ 100,00

Ao realizar o vínculo de R$ 60,00 do lançamento com tipo de documento sem classificação ao lançamento de Credito de adiantamento gerado pela baixa do adiantamento, o Extrato do Cliente/Fornecedor irá considerar o valor do lançamento y com o valor de R$ 40,00, pois o valor do vínculo do lançamento foi de R$ 60,00 restando somente em aberto o valor de R$ 40,00 no lançamento de tipo de documento sem classificação.

Quando o parâmetro não estiver selecionado, o sistema irá considerar seu valor original no Extrato Cliente/Fornecedor.

O valor exibido, tanto nas movimentações como no saldo anterior, será composto pelo Valor Original mais as composições de valores opcionais e valores de integração (dos módulos Financeiro ou Educacional) configuradas para afetar o cálculo. Para tratar o flag "Até o vencimento" e o campo "Dias em atraso" destes valores o sistema toma como data base do cálculo a data final informada na geração do relatório.

Para mais informações acesse 

* Valores de Integração: [https://tdn.totvs.com/pages/releaseview.action?pageId=532041706](https://tdn.totvs.com/pages/releaseview.action?pageId=532041706 "Follow link")
* Parametrização de Valores Opcionais:

**Observações**:

* Lançamento de Crédito de Adiantamento, não e apresentado no Extrato do Cliente/Fornecedor.
* Quando a opção de  **[Histórico do Controle de Alterações de Lançamentos/ Extrato de Caixa e Baixas](https://tdn.totvs.com/pages/viewpage.action?pageId=421388636)** está habilitada para todos os registros e o parâmetro *Contas a Receber | Manutenção de Lançamentos | Cliente/Fornecedor | [Habilita o uso dos dados do Histórico de Alteração dos Lançamentos no Relatório de Extrato de Cliente/Fornecedor](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+receber)* estiver habilitado, a geração do relatório buscará os dados na posição financeira do lançamento no período informado tomando como data base a data final informada na geração do relatório.

Subtrair impostos e tributos do valor do lançamento

Quando o parâmetro estiver selecionado, o sistema irá gerar o relatório extrato cliente/fornecedor descontando do valor original do lançamento.  
Os impostos são: IRRF, INSS e Tributos (PIS, COFINS e CSLL).

Mostrar devoluções nos lançamentos só a pagar ou só a receber no relatório de extrato cliente/fornecedor

Quando este parâmetro estiver marcado o sistema deverá mostrar as devoluções no relatório de razão quando forem marcados lançamentos só a pagar ou só a receber.

Informações adicionais:

Caso 1:  
Marcando a flag "A Receber "e a flag "Mostrar devoluções nos lançamentos só a pagar ou só a receber no relatório de extrato cliente/fornecedor" é apresentado os lançamentos à receber dentro da data definida mais os lançamentos à pagar com tipo documento "Devolução". 

Caso 2:  
Caso marque a flag de "à Pagar" e a flag "Mostrar devoluções nos lançamentos só a pagar ou só a receber no relatório de extrato cliente/fornecedor" estiver marcada será apresentado os lançamentos à Pagar dentro da data definida mais os lançamentos à Receber com tipo documento "devolução". Os lançamentos com tipo de documento devolução serão apresentados na coluna "Baixa".

Caso 3:  
Caso marque a flag de "à Pagar e à Receber" e a flag "Mostrar devoluções nos lançamentos só a pagar ou só a receber no relatório de extrato cliente/fornecedor" estiver marcada será apresentado os lançamentos à Pagar e à  Receber dentro da data definida. Os lançamentos de tipo documento Devolução não serão apresentados.

Caso 4:  
Caso marque a flag de "à Pagar e à Receber" e a flag "Mostrar devoluções nos lançamentos só a pagar ou só a receber no relatório de extrato cliente/fornecedor" estiver desmarcada será apresentado todos os lançamentos à Pagar e à Receber mais os lançamentos de devolução de cada natureza marcada.

Apresentar os lançamentos de vencimento de fatura quando for de cli/for diferente

A marcação desse parâmetro possibilitará que os lançamentos de vencimento de fatura sejam apresentados no relatório, quando o **cliente/fornecedor do(s) lançamento(s) original(is) for diferente do cliente/fornecedor do vencimento de fatura**.

Ex:  
Cliente/Fornecedor "A" - Lançamento   
Cliente/Fornecedor "B" - Lançamento   
Cliente/Fornecedor “C” - Inclusão de fatura

O(s) lançamento (s) de vencimento de fatura do cliente/fornecedor "C" será apresentado no relatório, caso o parâmetro seja marcado.
