---
content_hash: 7ef133bc059415b0c4af6ca547f57a6fd1970fdbce7281cb6c0f2684ad05bbf0
fetched_at: '2026-06-29T00:09:24.492987+00:00'
page_id: '423937926'
product: rm
source: tdn-rm
title: Motivo de Referência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937926
version: 30
---

Como não podem ser criados ou alterados, por se tratar de uma tabela fixa com operações pré-definidas para que seja possível efetuar as consistências legais, este cadastro será apenas visualizado. Ele também utiliza uma configuração única, com o objetivo de parametrizar os tipos de movimentos que irão utilizar o processo de "Cópia por Referência".   
São  através  destes motivos  que  diversos  processos  do  sistema  são  feitos,  como Devoluções,  Simples Remessa,  Nota  Fiscal  Complementar  de  Imposto,  Remessa,  Retorno,  dentre  outras  mais  que  serão explicados em seus processos correspondentes.   
Estes Motivos por Referência são informados no Tipo de Movimento através do menu Assistente | Parâmetros | Gestão de Estoque, Compras e Faturamento | edite o Tipo de Movimento | 04.09 - Outras Movimentações | Etapa 06 - Movimento – Outros Dados, campos "Usar Cópia  de Movimentos por Referência" e "Motivo de Referência". Nesta opção, será visualizado o Motivo de Referência.   
***Observação**:*Os motivos de referência estão em uma tabela fixa com operações pré-definidas para que seja possível efetuar as consistências legais. Utilizam uma configuração única, com o objetivo de parametrizar os tipos de movimentos que irão utilizar o processo de "Cópia por Referência".

**Inclusão de Motivos de Referência:**Este processo possibilita a inclusão de motivos de referência não existentes na coligada atual ou em todas as coligadas, considerando os campos Código da Coligada e sequencial. Serão alterados apenas os registros que não satisfaçam os valores default marcados. O processo de Inclusão de Motivos será realizado automaticamente para a Coligada atual ao serem executados os seguintes processos:

* Assistente de Cópia por Referência.
* Cópia de Movimento a partir de outro Movimento.
* Inclusão de Movimento.
* Inclusão do Item de Movimento.
* Na pesquisa de Motivo de Referência nos parâmetros por Tipo de Movimento na Etapa 6 - Movimento  - Outros Dados.

***Observações**:*Na cópia de Movimento a partir de outro Movimento, inclusão de movimento e itens de movimento, somente serão considerados para inclusão automática de motivos de referência, os tipos de movimento que estiverem com Motivo de Referência parametrizado na Etapa 6 - Mov-Outros Dados.

**Cópia Simples:**Este motivo possui as seguintes características:

* Copia os dados dos movimentos (1º selecionado) e dos itens;
* Será permitido selecionar N movimentos para efetuar a cópia.  
  ***Observações**::*Os campos do novo movimento obedecerão à parametrização do tipo de movimento que será criado. No caso de seleção de mais de um movimento serão carregados os dados do 1º movimento selecionado.  
  Os campos pertencentes ao movimento selecionado para cópia e que não fazem parte da parametrização do movimento atual serão ignorados na cópia. Além disso, campos pertinentes à numeração e natureza de operação não serão copiados.

**Simples Remessa:**Este motivo possui as seguintes características:

* Copia os dados dos movimentos (1º selecionado) e dos itens;
* Permite selecionar N movimentos para efetuar a cópia;
* Todos os movimentos devem ser do mesmo fornecedor;
* Tem natureza específica que será selecionada;
* Pode excluir item mas não pode incluir;
* Pode alterar a quantidade para menos;
* Apresenta controle de quantidades;
* Pode alterar data de entrada/saída e data de emissão;
* Nova nota e novo número de série;
* Não pode alterar o destinatário.

**NF acompanhamento de Cupom Fiscal:**Este motivo possui as seguintes características:

* Copia os dados do movimento e dos itens;
* Permite selecionar 1 movimento para efetuar a cópia;
* Os dados são idênticos e não podem ser alterados embora tenha nova numeração.

**Devolução de Mercadorias - Compra e Venda:**Estes motivos possuem as seguintes características:

* Copia os dados dos movimentos (1º selecionado) e dos itens;
* Permite selecionar N movimentos para efetuar a cópia;
* Todos os movimentos devem ser do mesmo fornecedor;
* Pode excluir item mas não pode incluir;
* A quantidade poderá ser alterado para menos;
* Apresenta controle de quantidades;
* Pode alterar data de entrada/saída e data de emissão;
* Nova nota e novo número de série;

* Não poderá ser alterado o destinatário.  
  ***Observações**:*  
  O Cliente/Fornecedor do tipo de movimento que utiliza este motivo de referência deverá ser do tipo "ambos".   
  No caso de exclusão de movimentos que possuam movimentos devolvidos, o movimento de devolução deve ser excluído antes do movimento de origem.  
  Para movimentos classificados com o motivo de referência "Devolução de Venda" serão disponibilizados no filtro do assistente movimentos do tipo 2.  
  Para movimentos classificados com o motivo de referência "Devolução de Compra" serão disponibilizados no filtro do assistente movimentos do tipo 1.  
  Ao incluir um movimento de devolução de compras ou de vendas pelo processo de cópia por referência, o sistema apresentará a condição de pagamento que foi informada na nota fiscal emitente, não considerando os tipos de planos da condição de pagamento.

**NF Complementar / Retificadora:**Este motivo possui as seguintes características:

* Não copia informações dos itens;
* Permite selecionar 1 movimento para efetuar a cópia;
* Não Consiste Cliente/Fornecedor.  
  A utilização deste motivo é indicada quando for necessário alterar algum dado da Nota Fiscal contendo as devidas correções necessárias, substituindo a utilização de carta de correção.

**Remessa para Concerto:**Este motivo possui as seguintes características:

* Copia os dados do movimento (1º selecionado) e dos itens;
* Permite selecionar N movimentos para efetuar a cópia;
* Poderá inserir itens no movimento destino;
* Não deixará alterar os itens do movimentos originados de outros;
* Poderá excluir o item;
* A quantidade poderá ser alterada para menos;
* Apresenta controle de quantidades;
* Pode alterar data de entrada/saída e data de emissão;
* Nova nota e novo número de série;
* Não poderá ser alterado o destinatário.

**Devolução Material Recebido, Conta e Ordem:**A princípio, o funcionamento desse tipo de cópia é o mesmo da Devolução de Compra de Mercadorias. É o tipo de devolução que pode ser utilizada em uma operação triangular de industrialização por encomenda. Isso ocorre quando um cliente (autor da encomenda) de uma indústria solicita a produção de determinado produto e esta indústria solicita ao mercado a aquisição de diversos materiais (matérias-primas) que são enviados por diversos fornecedores para a indústria por conta e ordem do autor da encomenda.  
Ao final do processo de produção, todo material adquirido nesta modalidade e que não foi utilizado é então devolvido, não para os fornecedores, mas para o autor da encomenda. Este motivo de cópia por referência é distinto do motivo de Devolução de Compra de Mercadorias porque pode agrupar em uma única nota fiscal de devolução, os materiais adquiridos por conta e ordem do autor da encomenda. Além disso, ela não exige que os movimentos de entrada tenham o mesmo Cliente/Fornecedor.

**Produção:**Esse tipo de cópia é utilizado para o processo de produção simples. A geração do movimento de entrada do produto acabado deverá ser feita por cópia a partir do movimento de ordem de produção, utilizando-se esse motivo de referência. Possui as seguintes características:

* Nova nota e novo número de série.

**Retorno de Remessa:**Esse tipo de cópia é utilizado no processo de controle de estoque de terceiros ou em poder de terceiros. Esta opção será utilizada tanto no processo da empresa remetente quanto da empresa recebedora.  
Na empresa remetente, o movimento de entrada referente ao retorno de mercadoria remetida anteriormente será gerado com base no movimento de saída referente à remessa. Na empresa recebedora, o movimento de saída referente ao retorno de mercadoria recebida anteriormente será gerado com base no movimento de entrada referente ao recebimento.  
Possui as seguintes características:

* Copia os dados dos movimentos (1º selecionado) e dos itens;
* Permite selecionar N movimentos para efetuar a cópia;
* Todos os movimentos devem ser do mesmo cliente/fornecedor;
* Pode excluir item mas não pode incluir;
* Pode alterar a quantidade para menos;
* Apresenta controle de quantidades;
* Nova nota e novo número de série;
* Não pode alterar o destinatário.

**Retorno de Mercadoria Não Aplicada na Industrialização:**Esse tipo de cópia é utilizado no processo de controle de estoque de terceiros ou em poder de terceiros. Esta opção será utilizada pela empresa remetente. O movimento de entrada da mercadoria remetida para industrialização e não aplicada no processo será gerado com base no movimento de saída referente à remessa para industrialização.  
Possui as seguintes características:

* Copia os dados dos movimentos (1º selecionado) e dos itens;
* Permite selecionar N movimentos para efetuar a cópia;
* Todos os movimentos devem ser do mesmo fornecedor;
* Pode excluir item mas não pode incluir;
* Pode alterar a quantidade para menos;
* Apresenta controle de quantidades;
* Nova nota e novo número de série;
* Não pode alterar o destinatário.

**Retorno de Remessa para Industrialização:**Esse tipo de cópia é utilizado no processo de controle de estoque de terceiros ou em poder de terceiros.  
Esta opção será utilizada pela empresa recebedora. O movimento de retorno simbólico da mercadoria utilizada na industrialização e o movimento de retorno da mercadoria não aplicada na industrialização serão gerados com base no movimento de entrada referente ao recebimento da mercadoria para industrialização.  
Possui as seguintes características:

* Copia os dados dos movimentos (1º selecionado) e dos itens;
* Permite selecionar N movimentos para efetuar a cópia;
* Todos os movimentos devem ser do mesmo cliente;
* Pode excluir item;
* Pode incluir item;
* Pode alterar a quantidade para menos;
* Apresenta controle de quantidades;
* Nova nota e novo número de série;
* Não pode alterar o destinatário.

**Devolução Simbólica de Mercadoria em Consignação:**Esse tipo de cópia é utilizado no processo de controle de estoque de terceiros ou em poder de terceiros.  
Esta opção será utilizada tanto no processo da empresa remetente quanto da empresa recebedora.  
Na empresa remetente, o movimento de devolução simbólica da mercadoria vendida pelo consignatário será gerado com base no movimento de remessa da mercadoria para consignação.  
Na empresa recebedora, o movimento de devolução simbólica da mercadoria vendida recebida em consignação será gerado com base no movimento de recebimento da mercadoria recebida em consignação.   
Possui as seguintes características:

* Copia os dados dos movimentos (1º selecionado) e dos itens;
* Permite selecionar N movimentos para efetuar a cópia;
* Todos os movimentos devem ser do mesmo cliente/fornecedor;
* Pode excluir item, mas não pode incluir;
* Pode alterar a quantidade para menos;
* Apresenta controle de quantidades;
* Nova nota e novo número de série;
* Não pode alterar o destinatário.

**Venda de Mercadoria Consignada:**Esse tipo de cópia é utilizado no processo de controle de estoque de terceiros ou em poder de terceiros.  
Esta opção será utilizada pela empresa remetente. O movimento de venda de mercadoria consignada será gerado com base no movimento de remessa da mercadoria para consignação.  
Possui as seguintes características:

* Copia os dados dos movimentos (1º selecionado) e dos itens;
* Permite selecionar N movimentos para efetuar a cópia;
* Todos os movimentos devem ser do mesmo cliente;
* Pode excluir item mas não pode incluir;
* Pode alterar a quantidade para menos;
* Não pode alterar o lote do produto;
* Apresenta controle de quantidades;
* Nova nota e novo número de série;
* Não pode alterar o destinatário.

**Devolução de Mercadoria Consignada não Comercializada:**Esse tipo de cópia é utilizado no processo de controle de estoque de terceiros ou em poder de terceiros.  
Esta opção será utilizada tanto no processo da empresa remetente quanto da empresa recebedora.  
Na empresa remetente, o movimento de devolução da mercadoria consignada não comercializada será gerado com base no movimento de remessa da mercadoria para consignação.  
Na empresa recebedora, o movimento de devolução da mercadoria recebida em consignação não comercializada será gerado com base no movimento de recebimento da mercadoria recebida em consignação.   
Possui as seguintes características:

* Copia os dados dos movimentos (1º selecionado) e dos itens;
* Permite selecionar N movimentos para efetuar a cópia;
* Todos os movimentos devem ser do mesmo cliente/fornecedor;
* Pode excluir item, mas não pode incluir;
* Pode alterar a quantidade para menos;
* Apresenta controle de quantidades;
* Nova nota e novo número de série;
* Não pode alterar o destinatário.

**Devolução por Recusa:**Este motivo possui as seguintes características:

* Copia os dados dos movimentos (1º selecionado) e dos itens;
* Permite selecionar N movimentos para efetuar a cópia;
* Os movimentos não precisam ser do mesmo fornecedor;
* Pode excluir item mas não pode incluir;
* A quantidade poderá ser alterado para menos;
* Apresenta controle de quantidades;
* Pode alterar data de entrada/saída e data de emissão;
* Nova nota;

Poderá ser alterado o destinatário.  
***Observações**:*  
O Cliente/Fornecedor do tipo de movimento que utiliza este motivo de referência deverá ser do tipo "ambos" ou "cliente".   
No caso de exclusão de movimentos que possuam movimentos devolvidos, o movimento de devolução deve ser excluído antes do movimento de origem.  
Para movimentos classificados com o motivo de referência "Devolução de Venda" serão disponibilizados no filtro do assistente movimentos do tipo 2.  
Ao incluir um movimento de devolução por recusa pelo processo de cópia por referência, o sistema apresentará a condição de pagamento que foi informada na nota fiscal emitente, não considerando os tipos de planos da condição de pagamento.

**Devolução de Empréstimo:**Este motivo tem as mesmas características da Devolução de compras com exceção do lote de controle do produto que poderá ser alterado. O código deste motivo é o 31.  
Seguem características deste motivo:

* Copia os dados dos movimentos (1º selecionado) e dos itens;
* Permite selecionar N movimentos para efetuar a cópia;
* Todos os movimentos devem ser do mesmo fornecedor;
* Pode excluir item mas não pode incluir;
* A quantidade poderá ser alterado para menos;
* Apresenta controle de quantidades;
* Pode alterar data de entrada/saída e data de emissão;
* Pode alterar o lote de controle do produto;
* Nova nota e novo número de série;
* Não poderá ser alterado o destinatário.

***Observações**:*  
O Cliente/Fornecedor do tipo de movimento que utiliza este motivo de referência deverá ser do tipo "ambos".   
No caso de exclusão de movimentos que possuam movimentos devolvidos, o movimento de devolução deve ser excluído antes do movimento de origem.  
Com o motivo de referência "Devolução de Empréstimo" serão disponibilizados no filtro do assistente movimentos do tipo 1.

**NF Complementar com Cópia de Itens:**Este motivo possui as seguintes características:

* Copia os dados do movimento e dos itens;
* A quantidade do item pode ser 0(zero), conforme parametrização do tipo de movimento:  
  Etapa Mov - Outros Dados: "Usar Cópia de Movimentos por referência" marcado; Motivo de Referência igual a "27 - NF Complementar com Cópia de Itens."  
  Etapa Item - Identificação 2/2: "Permitir Item com Quantidade Zero" marcado.  
  Etapa Item - Preços: "Editar Preço Total" marcado; "Aceitar Preço Zero" marcado.  
  Etapa Estoque - Estoque 1/3: "2 - Saldo Atual" igual a Aumenta;  
  Etapa Estoque - Estoque 2/3: "Saldo Financeiro Efeito sobre o Saldo Atual" igual a Aumenta; "Fórmula do Valor Financeiro": Valor Total do Item, conteúdo na fórmula TABITM ('VALORTOTALITEM' , 'V').  
  Observação: Quando o movimento de NF Complementar Permitir Item com Quantidade Zero e o Efeito Saldo for igual a Aumenta e o Valor Financeiro com Sinal for maior que zero, serão atualizados os dados de entrada na tabela Ficha Física/Financeira dos Produtos.

**Remessa por Conta e Ordem:**Este motivo possui as seguintes características:

* Copia os dados do movimento e dos itens;
* Parametrização do Tipo de Movimento de Origem:
  + Precisa ser um Tipo de Movimento de Venda (2.2)
  + Etapa Mov - Transporte 2/3: Utiliza Endereço de Coleta e Entrega como Destinatário definido como "Usa".
* Parametrização do Tipo de Movimento:
  + Precisa ser um Tipo de Movimento de Venda (2.2)
  + Etapa Mov - Emitente/Destinatário 1/2: Emitente definido como "Empresa".
  + Etapa Mov - Emitente/Destinatário 1/2: Destinatário definido como "Cliente".
  + Etapa Mov - Emitente/Destinatário 2/2: Consiste Fornecedor definido como "Não Consiste".
  + Etapa Mov - Emitente/Destinatário 2/2: Edição do Cliente Fornecedor definido como "Mostra".
  + Etapa Mov - Outros Dados: Usar Cópia de Movimento por referência definido como "Habilitado"
  + Etapa Mov - Outros Dados: Motivo de Referência definido como "35 - Remessa por Conta e Ordem".
  + Etapa Estoque - Estoque 1/3: Saldo Atual definido como "Diminui.

**Retorno de Remessa para Industrialização por Conta e Ordem:**Este motivo possui as seguintes características:

* Copia os dados do movimento e dos itens;
* Parametrização do Tipo de Movimento de Origem:  
  + Etapa Mov - Transporte 2/3: Utiliza Endereço de Coleta e Entrega como Destinatário definido como "Usa".
  + Etapa Estoque - Estoque 1/3: Saldo Atual definido como "Não Afeta".
  + Etapa Estoque - Estoque 2/3: Tipo Controle de Estoque Terceiros definido como "Remessa/Entrada para Industrialização Triangulação"
  + Etapa Estoque - Estoque 2/3: Efeito sobre o saldo de terceiros definido como "Aumenta".
* Parametrização do tipo de movimento:
  + Etapa Mov - Emitente/Destinatário 1/2: Emitente definido como "Empresa".
  + Etapa Mov - Emitente/Destinatário 1/2: Destinatário definido como "Cliente".
  + Etapa Mov - Emitente/Destinatário 2/2: Consiste Fornecedor definido como "Não Consiste".
  + Etapa Mov - Emitente/Destinatário 2/2: Edição do Cliente Fornecedor definido como "Mostra".
  + Etapa Mov - Outros Dados: Usar Cópia de Movimento por referência definido como "Habilitado"
  + Etapa Mov - Outros Dados: Motivo de Referência definido como "36 - Retorno de Remessa para Industrialização por Conta e Ordem".
  + Etapa Mov - Transporte 2/3: Utiliza Endereço de Coleta e Entrega como Destinatário definido como "Usa".
  + Etapa Estoque - Estoque 1/3: Saldo Atual definido como "Não Afeta".
  + Etapa Estoque - Estoque 2/3: Tipo Controle de Estoque Terceiros definido como "Remessa/Entrada para Industrialização Triangulação"
  + Etapa Estoque - Estoque 2/3: Efeito sobre o saldo de terceiros definido como "Diminui".

**Destinação de item para consumo pessoal:** Estes motivos possuem as seguintes características:

* Copia os dados dos movimentos (1º selecionado) e dos itens;
* Permite selecionar N movimentos para efetuar a cópia;
* Os movimentos podem ser de fornecedores diferentes.
* Pode excluir item mas não pode incluir;
* A quantidade poderá ser alterado para menos;
* Apresenta controle de quantidades;
* Nova nota e novo número de série;
* Deverá ser alterado o destinatário.
* Pode alterar data de entrada/saída e data de emissão;

**Nota de Débito referente a Juros e Multa:**Este motivo possui as seguintes características:

* Copia os dados do movimento selecionado e dos itens;
* Não permite selecionar 'N' movimentos para geração do movimento destino (ND);
* O movimento origem deve ser do tipo de venda (2.2);
* Não permite alterar o destinatário (cli/for) do movimento;
* Quantidade dos Itens no movimento destino (ND) será igual a 1;
* O preço unitário deve ser maior que zero;
* Não permite incluir e excluir itens.

* Parametrização do tipo de movimento:
  + Mov - Identificação: Edita Numeração como "Mostra";
  + Mov - Datas 1/2: Data Emissão como "Mostra";
  + Mov - Outros Dados: Usar Cópia de Movimentos por Referência como "Habilitado";
  + Mov - Outros Dados:    Motivo de Referência como "Nota de Débito Juros e Multa";
  + Item - Preços 1 / 2 : Edição do Preço como "Edita";
  + Item - Preços 1 / 2 : Aceita Preço  Zero como "Desabilitado";
  + Fin - Faturamento 1 / 6 : Fatura do Movimento como  "Desabilitado";
  + Fis - NF-e : Referência Nota Fiscal Eletrônica como "Habilitado";
  + Fis - NF-e : Débito / Crédito como "Débito";
  + Fis - NF-e : Tipo Débito / Crédito como "04 Multa e Juros".

Observação

Os motivos **Remessa por Conta e Ordem**e  **Retorno de Remessa para Industrialização por Conta e Ordem**estão disponíveis a partir da versão 12.1.32 do RM.

Documentos Relacionados

[Relacionamento de Movimentos com Cópia por Referência](https://tdn.totvs.com/pages/viewpage.action?pageId=843138521)
