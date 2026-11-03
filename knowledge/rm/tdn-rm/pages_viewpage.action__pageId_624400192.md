---
content_hash: a67ab50d8a4280f8eb10bf5ca0485151e2fcc4bc4125df2629b31b745b361c91
fetched_at: '2026-06-29T00:11:03.560932+00:00'
page_id: '624400192'
product: rm
source: tdn-rm
title: Triangulação de Mercadorias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=624400192
version: 83
---

Venda à ordem, também adotadas as expressões venda a termo ou operação triangular, é a denominação dada à venda cuja mercadoria permanece na posse do vendedor e será entregue, por conta e ordem do adquirente, a outro estabelecimento da mesma empresa ou em estabelecimento de terceiros.

Pelo fato de serem reguladas pelo mesmo dispositivo legal, Livro II, art. 59, I do Regulamento do RICMS, aprovado pelo Decreto nº 37699/97-RICMS, esta venda não deve ser confundida com a operação de venda para entrega futura, porquanto, naquela o vendedor se compromete a entregar a mercadoria em certo prazo e nesta a entrega ocorre no ato da compra.

Link da legislação: <http://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/ricms_2002_seco/anexoix2002_9.html>.

Ou seja, é uma operação de movimentação de mercadorias que envolve mais de duas empresas, conforme exemplos abaixo:

Exemplo 1: **Industrialização realizada por terceiros**

***Fornecedor***: Empresa que vende as matérias primas.

***Cliente***: Empresa que adquire as matérias primas.

***Indústria***: Empresa que industrializa a matéria prima adquirida pelo ***Cliente***.

A diferença deste processo ao processo de estoque de/com terceiros é que a matéria prima adquirida do ***Fornecedor*** transita diretamente para a ***Indústria***, com isso o ***Cliente*** que adquiriu não terá custo de transporte com o envio da mercadoria.

Exemplo 2: **Revenda de produto**

***Fornecedor***: Empresa que vende os produtos.

***Cliente*:** Empresa que adquire os produtos e revende para o ***Cliente Final***.

***Cliente Final:*** Empresa que adquire os produtos.

Nos dois exemplos citados acima as mercadorias não são enviadas aos adquirintes e sim enviadas a uma terceira empresa (indústria ou cliente final).

Segue abaixo orientações para parametrizações dos dois processos exemplificados acima.

1Triangulação para Industrialização

O processo descrito abaixo é considerado nas situações onde as três empresas utilizam o ERP RM, caso uma delas não utilize basta desconsiderar.

A sequência apresentada é a mais usual do processo.

**Notas Fiscais Emitidas pelo Fornecedor**

1) ***Fornecedor*** emite nota fiscal de venda da matéria prima, onde o destinatário é a empresa que adquiriu as matérias primas, destacando a empresa que receberá as matérias primas para o processo de industrialização.

Deverá ser criado um tipo de movimento para registro das notas fiscais de vendas com as principais parametrizações abaixo:

Regras do Tipo de Movimento

Emitente: Empresa (***Fornecedor***)

Destinatário: Cliente (***Cliente***)

Local de Entrega: Empresa (***Indústria***) - Habilitar Etapa 19\ Utiliza Endereço de Entrega

Estoque -  Saldo Atual:  Não Afeta

2) ***Fornecedor*** emite nota fiscal de remessa de mercadoria por conta e ordem onde o destinatário é a empresa ***Indústria*** que realizará a industrialização, informando na nota fiscal os dados da nota fiscal de venda da matéria prima.

Deverá ser criado um tipo de movimento para registro das notas fiscais de saídas por conta e ordem com as principais parametrizações abaixo:

Este movimento será inserido a partir do processo de Assistente de Cópia por Referência.

Regras do Tipo de Movimento

Emitente: Empresa (***Fornecedor***)

Destinatário: Cliente (***Indústria***)

Motivo de Referência: 35 - Remessa por Conta e Ordem (este motivo de referência buscará de forma automática a empresa informada no campo Transporte / Coleta e Entrega / Local de Entrega do movimento que foi selecionado como origem).

Estoque -  Saldo Atual:  Diminui 

**Regras do Motivo de Referência**

Remessa por Conta e Ordem

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

**Nota****Fiscal Registrada pelo Cliente**

1) Empresa ***Cliente*** insere no sistema nota fiscal de compras emitida pelo fornecedor.

Deverá ser criado um tipo de movimento para registro das notas fiscais de compras com as principais parametrizações abaixo:

Regras do Tipo de Movimento

Emitente: Empresa (***Fornecedor***)

Destinatário: Filial (***Cliente***)

Local de Entrega: Empresa (***Indústria***) - Habilitar Etapa 19\ Utiliza Endereço de Entrega

Estoque - Saldo Atual:  Aumenta

Estoque - Tipo de Controle Estoque Terceiros - Remessa/Entrada para Industrialização Triangulação

                                                                             Efeito sobre o Saldo **COM** Terceiros: Aumenta

A utilização do controle de estoque terceiro "Remessa/Entrada para Industrialização Triangulação" realizará o registro do estoque Com terceiros para o Cli/For que foi informado no local de entrega e obrigará o preenchimento do Ci/For no campo local de entrega.

**Nota****Fiscal Registrada pela Indústria**

1) Empresa ***Indústria*** registra a entrada das matérias primas recebidas da empresa ***Fornecedor*** pertencentes a empresa ***Cliente***.

Deverá ser criado um tipo de movimento para registro das notas fiscais de entrada de mercadoria por conta em ordem com as principais parametrizações abaixo:

Regras do Tipo de Movimento

Emitente: Empresa (***Fornecedor***)

Destinatário: Filial (***Indústria***)

Local de Entrega: Empresa (***Cliente***) - Habilitar Etapa 19\ Utiliza Endereço de Entrega

Estoque - Saldo Atual:  Não Afeta

Estoque - Tipo de Controle Estoque Terceiros - Remessa/Entrada para Industrialização Triangulação

                                                                             Efeito sobre o Saldo **DE** Terceiros: Aumenta

A utilização do controle de estoque terceiro "Remessa/Entrada para Industrialização Triangulação" realizará o registro do estoque DE terceiros para o Cli/For que foi informado no local de entrega e obrigará o preenchimento do Ci/For no campo local de entrega.

**Nota****Fiscal Emitida pela Indústria**

1) Empresa ***Indústria*** emite nota fiscal para remessa simbólica das matérias primas da empresa ***Cliente***.

Deverá ser criado um tipo de movimento para registro das notas fiscais de remessa simbólica com as principais parametrizações abaixo:

Este movimento será inserido a partir do processo de Assistente de Cópia por Referência.

Regras do Tipo de Movimento

Emitente: Empresa (***Indústria***)

Destinatário: Cliente (***Cliente***)

Motivo de Referência: 36 - Retorno de Remessa para Industrialização por Conta e Ordem (este motivo de referência buscará de forma automática a empresa informada no campo Transporte / Coleta e Entrega / Local de Entrega do movimento que foi selecionado como origem).

**Regras do Motivo de Referência**

Retorno de Remessa para Industrialização por Conta e Ordem:

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

Estoque - Saldo Atual:  Não Afeta

Estoque - Tipo de Controle Estoque Terceiros - Remessa/Entrada para Industrialização Triangulação

                                                                             Efeito sobre o Saldo **DE** Terceiros: Diminui

2) Empresa ***Indústria*** emite nota fiscal referente a prestação de serviços prestados para a empresa ***Cliente***.

Deverá ser criado tipo de movimento com as parametrizações necessárias para emissão da(s) notas fiscais conforme regra fiscal da empresa.

**Nota****Fiscal Registrada pelo Cliente**

2) Empresa ***Cliente*** registra retorno simbólico das matérias primas enviadas para industrialização.

Deverá ser criado um tipo de movimento para registro das notas fiscais de remessa simbólica com as principais parametrizações abaixo:

Este movimento será inserido a partir do processo de Assistente de Cópia por Referência, sendo a origem o tipo de movimento da entrada da compra da matéria prima.

Regras do Tipo de Movimento

Emitente: Fornecedor (***Indústria***)

Destinatário: Empresa (***Cliente***)

Estoque -  Saldo Atual:  Diminui

Estoque - Tipo de Controle Estoque Terceiros - Remessa/Entrada para Industrialização Triangulação

                                                                             Efeito sobre o Saldo **COM** Terceiros: Diminui

Motivo de Referência: 36 - Retorno de Remessa para Industrialização por Conta e Ordem (este motivo de referência buscará de forma automática a empresa informada no campo Transporte / Coleta e Entrega / Local de Entrega do movimento que foi selecionado como origem).

3) Empresa ***Cliente*** registra a nota fiscal referente ao serviço prestado pela empresa que realizou a industrialização.

Este movimento poderá ser parametrizado conforme a regra fiscal da nota fiscal recebida e processo da empresa, podendo ser parametrizado a entrada de estoque do produto produzido, geração do lançamento financeiro, contábil e fiscal no mesmo movimento.

A inserção deste movimento será realizada pelo faturamento de um movimento de ordem de compra ou pela insersão direta no tipo movimento criado, estamos avaliando a possibilidade de criar uma chamada deste movimento automaticamente após a inclusão da nota fsical de retorno simbólico da matéria prima.

Triangulação para Revenda

O processo descrito abaixo é considerado nas situações onde as três empresas utilizam o ERP RM, caso uma delas não utilize basta desconsiderar.

A sequência apresentada é a mais usual do processo.

**Notas Fiscais Emitidas pelo Fornecedor**

1) ***Fornecedor*** emite  nota fiscal de venda de produtos onde o destinatário é a empresa ***Cliente*** que adquiriu as produtos, informando a empresa ***Cliente Final*** que receberá os produtos.

Deverá ser criado um tipo de movimento para registro das notas fiscais de vendas com as principais parametrizações abaixo:

Regras do Tipo de Movimento

Emitente: Empresa (***Fornecedor***)

Destinatário: Cliente (***Cliente***)

Local de Entrega: Empresa (**Cliente Final**) - Habilitar Etapa 19\ Utiliza Endereço de Entrega (este motivo de referência buscará de forma automática a empresa informada no campo Transporte / Coleta e Entrega / Local de Entrega do movimento que foi selecionado como origem).

Estoque -  Saldo Atual:  Não Afeta

2) ***Fornecedor*** emite nota fiscal de remessa de mercadoria por conta e ordem onde o destinatário é a empresa ***Cliente Final***, informando na nota fiscal os dados da nota fiscal de venda de produtos.

Deverá ser criado um tipo de movimento para registro das notas fiscais de saídas por conta e ordem com as principais parametrizações abaixo:

Este movimento será inserido a partir do processo de Assistente de Cópia por Referência.

Regras do Tipo de Movimento

Emitente: Empresa (***Fornecedor***)

Destinatário: Cliente (***Cliente Final***)

Motivo de Referência: 35 - Remessa por Conta e Ordem (este motivo de referência buscará de forma automática a empresa informada no campo Transporte / Coleta e Entrega / Local de Entrega do movimento que foi selecionado como origem).

Estoque -  Saldo Atual:  Diminui 

**Regras do Motivo de Referência**

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

**Nota****Fiscal Registrada pelo Cliente**

1) Empresa ***Cliente*** insere no sistema nota fiscal de compras emitida pelo fornecedor.

Deverá ser criado um tipo de movimento para registro das notas fiscais de compras com as principais parametrizações abaixo:

Regras do Tipo de Movimento

Emitente: Fornecedor (***Fornecedor***)

Destinatário: Empresa (***Cliente***)

Estoque - Saldo Atual: Aumenta
