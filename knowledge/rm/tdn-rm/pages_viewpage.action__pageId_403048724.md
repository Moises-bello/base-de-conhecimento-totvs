---
content_hash: 6dc9f0174ba183b0abba5a9237f5217c7a0209baf6c31ec855a364cec0a42cff
fetched_at: '2026-06-29T00:09:10.715661+00:00'
page_id: '403048724'
product: rm
source: tdn-rm
title: FISCAL01-6374 ER Portaria CAT 42/2018 SP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403048724
version: 83
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão Fiscal |
| **Segmento Executor** | Serviços | | |
| **Requisito/Story/Issue** | FISCAL01-6374 | **Subtarefa** | FISCAL01-6456 |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

Atender a Portaria CAT 42/2018 - Sistema de apuração e Ressarcimento ou complemento do ICMS retido por substituição tributária.

## Definição da Regra de Negócio

Em 22/05/2018 o Governo Estadual de SP publicou a Portaria CAT 42/2018 que instituiu um novo método para o Sistema de Ressarcimento ou Complemento do ICMS Retido por Substituição Tributária. A CAT 42 estabelece as regras e procedimentos deste novo método a serem executadas por contribuintes de ICMS que receberam mercadorias sob o regime de substituição tributária e que por motivo qualquer não tenham o fato gerador do imposto cobrado antecipadamente concluído.

## Exigência

A entrega da obrigação acessória entrou em vigor de forma retroativa em 01/05/2018. Porém as disposições transitórias autorizam o contribuinte a continuar entregando pela EFD ICMS IPI utilizando as diretrizes da Portaria CAT 158/2015 até 31/12/2018. A partir de janeiro/2019 será obrigatório o procedimento da Portaria CAT/SP 42/20118

## Legislação

* Regras Fiscais: As regras fiscais estão disponíveis no [Manual do Sistema de Apuração do Ressarcimento ou Complemento do ICMS Retido por Substituição Tributária ou Antecipado](https://portal.fazenda.sp.gov.br/servicos/st/Downloads/MANUAL%20Sistema%20Ressarcimento_ICMS_ST.pdf).
* Arquivo magnético: O arquivo magnético deverá ser desenvolvido de acordo com o [Manual de Orientação da Formação do Arquivo Digital do “Sistema de Apuração do Ressarcimento ou Complemento do ICMS Retido por Substituição Tributária ou Antecipado](https://portal.fazenda.sp.gov.br/servicos/st/Downloads/Leiaute_Arquivo_Digital_Sistema%20Ressarcimento_ICMS_ST.pdf).

## Parâmetros

Será criado um parâmetro por filial para informar se a mesma controla o ressarcimento de ICMS ST. O parâmetro será criado na pasta  03.02 - Apuração de Tributos >> 03.02.01 - ICMS >> Apur. ICMS por Filial >> Apuração do ICMS >> criar o campo ***Controla Ressarcimento de ICMS ST.***

## Cadastros

Cadastro da Natureza de Operação

No cadastro da "Natureza de Operação" na pasta "Outros Dados" será renomeado o campo "Operação com Ressarcimento de ST na Compra" para "Operação com Ressarcimento/Complemento de ST".

Figura

Cadastro do Período de Apuração

No cadastro do período de apuração do tributo ICMSST será criado um anexo "Ressarcimento/Complemento de ICMS ST". Este anexo deverá ter uma grid destacando as entradas e saídas por produto e o saldo de imposto que foi suportado na compra.

Criar a tabela DPERIODORESSARCIMENTOICMSST com os seguintes campos

* IDRESSARCIMENTO: Chave primaria da tabela
* IDPER: Identificador do Período
* CODCOLIGADA: Código da Coligada
* CODFILIAL: Código da Filial
* IDPRD: Identificador do Produto
* IDLAF: Identificador do Lançamento
* NUMITEM: Número do Item
* QUANTIDADE: Quantidade do Item
* VLRUNSUPORTADO: Valor unitário do ICMSST suportado na compra
* VLRUNCONFRONTO: Valor unitário do ICMSST confronto na operação
* VLRTOTSUPORTADO: Valor total do ICMSST suportado na compra
* VLRTOTCONFRONTO: Valor total do ICMSST confronto na operação
* VLRRESSARCIMENTOAPURADO: Valor do ressarcimento apurado
* TIPO: Entrada ou Saída
* ENQUADRAMENTOLEGAL: Código de Enquadramento Legal do Ressarcimento ou Complemento que poderá aceitar um dos seguintes valores

  | Código | Hipótese de Ressarcimento ou Complemento de ICMS ST | RICMS SP |
  | --- | --- | --- |
  | 0 | Operação não ensejadora de Ressarcimento ou Complemento de ICMS-ST |  |
  | 1 | Operação ensejadora de Ressarcimento ou Complemento de ICMSST na hipótese do Inciso I do Art. 269 do RICMS | Valor do imposto retido a maior, correspondente à diferença entre o valor que serviu de base à retenção e o valor da operação ou prestação realizada com consumidor ou usuário final; |
  | 2 | Operação ensejadora de Ressarcimento de ICMS-ST na hipótese Inciso II do Art. 269 do RICMS | Valor do imposto retido ou da parcela do imposto retido relativo ao fato gerador presumido não realizado |
  | 3 | Operação ensejadora de Ressarcimento de ICMS-ST na hipótese Inciso III do Art. 269 do RICMS | Valor do imposto retido ou da parcela do imposto retido relativo ao valor acrescido, referente à saída que promover ou à saída subsequente amparada por isenção ou não-incidência |
  | 4 | Operação ensejadora de Ressarcimento de ICMS-ST na hipótese Inciso IV do Art. 269 do RICMS | Valor do imposto retido ou da parcela do imposto retido em favor deste Estado, referente a operação subsequente, quando promover saída destinada a outro Estado |

A grid do anexo deverá apresentar as seguintes colunas.

* Código do produto
* Data do Lançamento Fiscal
* Tipo
* Número inicial do Lançamento Fiscal
* Número do Item do Lançamento Fiscal
* Quantidade
* Valor unitário do ICMSST suportado
* Valor unitário do ICMSST confronto
* Valor total do ICMSST suportado
* Valor total do ICMSST confronto
* Valor do ressarcimento apurado
* Enquadramento Legal

Este anexo deverá ter uma TAG de permissão no perfil de usuário.

## Alteração da Apuração

Será necessário apurar os valores de ICMSST suportado na entrada com os valores efetivos da saída por período e por produto para então calcular o valor de ressarcimento ou complemento de ICMSST. 

Encerramento do Período de Apuração

Para as filiais que estiverem com o parâmetro *"Controla Ressarcimento de ICMS ST"* marcado o calculo do será realizado automaticamente durante o encerramento do período de apuração de ICMSST considerando todas as entradas nas quais ocorreu antecipação ou substituição de ICMSST e as saída dos produtos cujo a tributação foi suportada na entrada.

1. Serão selecionadas as movimentações de entrada e saída com DATALF compreendida no período que está sendo encerrado e com produtos cuja opção "Tributado pelo ICMS-ST" esteja marcada para o estado da Filial no cadastro do produto Anexo "Dados Fiscais por UF"

   Figura
2. Serão selecionados Lançamentos associados a CFOPs cujo Flag "FISCAL" esteja marcado e não serão considerados lançamentos cancelados.
3. Para cada lançamento de entrada selecionado, cujo item tenha valor de ICMS-ST maior do que Zero (0), deverá ser incluído um registro na DPERIODORESSARCIMENTOICMSST conforme abaixo:
   1. NUMITEM: Número do Item no Lançamento Fiscal
   2. QUANTIDADE: Quantidade do Item no Lançamento Fiscal
   3. VLRUNSUPORTADO: Valor unitário do ICMSST + ICMS suportado na compra ((DITEM.VLRICMSSTPRD + DITEM.VLRICMSPRD) / QUANTIDADE)
      * Cada operação gerará um valor do ICMS suportado pelo contribuinte. Este item será a soma de todos os valores de ICMS que compõe a operação.
      * Nas hipóteses de aquisição de mercadoria de substituído, o ICMS suportado será o declarado pelo remetente em informações complementares e nas TAG´s especificas do grupo da NF-e <ICMS60> (Este valor estará no campo de Valor do ST).
      * No caso de incidência do FECP o mesmo deverá ser considerado na composição do ICMS Suportado. Como a orientação neste caso é majorar a alíquota do ST, o valor do FECP já está incluso no valor do ICMS-ST.
   4. VLRUNCONFRONTO: zero
   5. VLRTOTSUPORTADO: Valor total do suportado na compra (VLRUNSUPORTADO \* QUANTIDADE)
   6. VLRTOTCONFRONTO: zero
   7. VLRRESSARCIMENTOAPURADO: zero
   8. ENQUADRAMENTOLEGAL: em branco
4. Serão selecionados lançamento de saída que estejam nas regras 1 e 2 cujos itens tenham referência com itens de entrada. Para cada lançamento de saída selecionado deverá ser incluído um registro na DPERIODORESSARCIMENTOICMSST conforme abaixo:  
   1. NUMITEM: Número do Item no Lançamento Fiscal
   2. QUANTIDADE: Quantidade do Item no Lançamento Fiscal
   3. VLRUNSUPORTADO: Valor unitário do ICMS total suportado na compra
      * O item do lançamento de saída deverá ser referenciado a um ou mais itens dos lançamentos de entrada
      * No caso de incidência do FECP o mesmo deverá ser considerado na composição do ICMS Suportado. Como a orientação neste caso é majorar a alíquota do ST, o valor do FECP já está incluso no valor do ICMS-ST.
      * O valor unitário suportado será uma média ponderada entre os itens de compra referenciados: **(****(****(**"Valor do ST da Compra" + "Valor do ICMS da Compra"**)** / "Quantidade da Venda"**)** / "Quantidade da Compra"**)** \* "Quantidade Referenciada na nota de Saída".

        Exemplo

        **Entradas**

        **Saída**
   4. VLRUNCONFRONTO:
      1. O valor deverá ser calculado nos os casos abaixo conforme a seguinte regra: Valor unitário do ICMSST + ICMS na operação ((DITEM.VLRICMSSTPRD + DITEM.VLRICMSPRD) / QUANTIDADE) (No caso de incidência do FECP o mesmo já está sendo considerado na composição do ICMS de Confronto, uma vez que a alíquota está majorada)  
         * Operação destinada a consumidor final; **OU**
         * Operação destinada à pessoa jurídica amparada pela isenção.
      2. Caso não caia na situação acima, o valor do confronto será igual ao valor suportado nos casos em que for **operação interna** destinada à **pessoa jurídica**;
      3. Quando a operação for **interestadual** destinada à **pessoa jurídica** o valor de confronto será o valor do ICMS unitário das compras relacionadas (item da entrada referenciado, campo DITEM.VLRICMSPRD); e deverá ser lançado como crédito de ICMS (o usuário deverá criar um lançamento de ajuste manualmente);
      4. Caso não caia nos casos acima, será calculado de acordo com o item "i".
   5. VLRTOTSUPORTADO: Valor total do ICMS suportado na compra (VLRUNSUPORTADO \* QUANTIDADE)
   6. VLRTOTCONFRONTO: Valor total do ICMS na operação (VLRUNCONFRONTO \* QUANTIDADE)
   7. VLRRESSARCIMENTOAPURADO: Gerar apenas para lançamentos de saída deverá receber o resultado da conta VLRTOTSUPORTADO - VLRTOTCONFRONTO. Se o resultado for positivo existe valor para ressarcimento, se for negativo o valor será de complemento. O valor será gravado no Banco de Dados com sinal.
   8. ENQUADRAMENTOLEGAL:
      1. **Se** Operação com Ressarcimento/Complemento de ST desmarcado  
         **Então** 0

         Figura

**Senão** Se Regra ICMS Isento OU Não incidência **Então 3**

**Senão Se** Venda Interestadual

**Então** 4

**Senão** **Se** Consumidor Final

**Então** 1

**Senão****Então** 2

Abertura do Período de Apuração

Ao abrir o Período de Apuração os registros criados na tabela DPERIODORESSARCIMENTOICMSST deverão ser apagados.

DPERIODORESSARCIMENTOICMSST 

## Registros

O arquivo será composto dos seguintes registros:

* REGISTRO 0000 - ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DO CONTRIBUINTE
* REGISTRO 0150 - TABELA DE CADASTRO DO PARTICIPANTE
* REGISTRO 0200 - TABELA DE IDENTIFICAÇÃO DO ITEM
* REGISTRO 0205 - CÓDIGO ANTERIOR DO ITEM (Não obrigados ao SPED)
* REGISTRO 1050 - REGISTROS DE SALDOS EM ESTOQUE
* REGISTRO 1100 – REGISTRO DE DOCUMENTO FISCAL ELETRÔNICO PARA FINS DE RESSARCIMENTO DE SUBSTITUIÇÃO TRIBUTÁRIA – SP
* REGISTRO 1200 – REGISTRO DE DOCUMENTO FISCAL NÃO-ELETRÔNICO PARA FINS DE RESSARCIMENTO DE SUBSTITUIÇÃO TRIBUTÁRIA – SP

Campos por registro00REGISTRO 0000 - ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DO CONTRIBUINTE

REGISTRO 0000 - ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DO CONTRIBUINTE

| Ordem | Campo | Descrição | Tipo | Tamanho | Decimal | Obrigatório | Exemplo de Conteúdo | Regras Previstas de Validação | Especificação | Dicas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Abertura do arquivo e identificação do contribuinte | C | 004 |  | O | 0000 | Único conteúdo valido "0000" | Fixo "0000" |  |
| 02 | PERIODO | Período das informações contidas no arquivo | N | 006 |  | O | MMAAAA |  | Será considerado o campo Data inicial da tela de geração |  |
| 03 | NOME | Nome empresarial da entidade. | C | ILIMITADO |  | O | XXXXXXXX |  | Nome da Filial selecionada na tela de geração | Contexto GetFiliais.Nome |
| 04 | CNPJ | Número de inscrição da entidade no CNPJ. | N | 014\* |  | O | 123456789000110 000456789000110 | É conferido o dígito verificador (DV) do CNPJ informado | CNPJ da Filial selecionada na tela de geração | Contexto GetFiliais.Cgc |
| 05 | IE | Inscrição Estadual da entidade. | C | 014 |  | O | 00111111111111 129876543321577 041231237 | É conferido o dígito verificador (DV) da Inscrição Estadual informada, considerando-se a UF do informante. | Inscrição estadual da Filial selecionada na tela de geração | Contexto GetFiliais.InscricaoEstadual |
| 06 | COD\_MUN | Código do município do domicílio fiscal da entidade, conforme a tabela IBGE | 0 | 007\* |  | O | 3500204 | É conferido se o código de município é faz referência ao Estado de São Paulo | Código da tabela de classificação do município da Filial selecionada na tela de geração conforme a tabela de classificação também definida na tela geração | Contexto GetFiliais.CodMunicipio |
| 07 | COD\_VER | Código da versão do leiaute conforme a Tabela de Versão do Leiaute | N | 002 |  | O | 01 | Deve ser informado um código ativo da tabela | Campo da tela de geração |  |
| 08 | COD\_FIN | Código da finalidade do arquivo conforme a Tabela Finalidade de Entrega do Arquivo | N | 002 |  | O | 00 | Deve ser informado um código ativo da tabela | Campo da tela de geração |  |

1REGISTRO 0150 - TABELA DE CADASTRO DO PARTICIPANTE

REGISTRO 0150 - TABELA DE CADASTRO DO PARTICIPANTE

Este registro deve ser gerado apenas na hipótese de emissão de documentos não eletrônicos (Registro 1200). Para os documentos declarados nos registro 1100 é apresentada apenas a chave da NF-e.

| Ordem | Campo | Descrição | Tipo | Tamanho | Decimal | Obrigatório | Exemplo de Conteúdo | Regras Previstas de Validação | Especificação | Dicas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Cadastro de Participante | C | 004 |  | O | 0150 | Único conteúdo valido "0150" | Fixo "0150" |  |
| 02 | COD\_PART | Código de identificação do participante no arquivo | C | 060 |  | O | PARTICIP00001 | O valor informado no campo COD\_PART deve existir em pelo menos um registro dos demais blocos. Não podem ser informados dois ou mais registros com o mesmo Código de Participante. Não devem ser informados como participantes os CNPJ e CPF apenas citados nos registros. referentes a documentos fiscais modelo 02, 2D, 59, 60 e 65 (Documentos Fiscais a Consumidor Final) | Código de identificação do participante.  Participantes sem movimentação no período não devem ser informados neste registro | Participante.Codigo |
| 03 | NOME | Nome pessoal ou empresarial do participante | C | ILIMITADO |  | O | PARTICIPANTE |  | Nome do Participante | Participante.Nome |
| 04 | COD\_PAIS | Código do país do participante, conforme a tabela indicada no item 3.2.1 do Ato COTEPE/ICMS nº 09/2008. | N | 005 |  | OC | 1058 | O valor informado no campo deve existir na Tabela de Países. Informar, inclusive, quando o participante for estabelecido ou residente no Brasil (01058 ou 1058) | Código da tabela de classificação de país conforme a tabela de classificação definida na tela geração | Participante.CodPais |
| 05 | CNPJ | Número de inscrição do participante no CNPJ | N | 014\* |  | OC | 18024414000116 | Será conferido o dígito verificador (DV) do CNPJ informado. Se COD\_PAIS diferente de Brasil, o campo não deve ser preenchido;  Os campos 05 e 06 são mutuamente excludentes, sendo obrigatório o preenchimento de um deles quando o campo 04 estiver preenchido com “01058” ou “1058” (Brasil); Este campos não deve ser preenchido se o participante for pessoa estrangeira | CNPJ do Participantes | Util.If(Participante.Nacional,Participante.CNPJ,null) |
| 06 | CPF | Número do CPF do participante | N | 011\* |  | OC |  | Será conferido o dígito verificador (DV) do CNPJ informado. Se COD\_PAIS diferente de Brasil, o campo não deve ser preenchido;  Os campos 05 e 06 são mutuamente excludentes, sendo obrigatório o preenchimento de um deles quando o campo 04 estiver preenchido com “01058” ou “1058” (Brasil); Este campos não deve ser preenchido se o participante for pessoa estrangeira | CPF do Participante | Util.If(Participante.Nacional,Participante.CPF,null) |
| 07 | IE | Inscrição Estadual do participante | N | 014 |  | OC |  | Valida a Inscrição Estadual de acordo com a UF informada no campo COD\_MUN (dois primeiros dígitos do código de município). Este campos não deve ser preenchido se o participante for pessoa estrangeira | Inscrição Estadual do Participante | Participante.IE |
| 08 | COD\_MUN | Código do município, conforme a tabela IBGE | N | 007\* |  | OC | 3500204 | O valor informado no campo deve existir na Tabela de Municípios do IBGE (combinação do código da UF e o código de município), possuindo 7 dígitos.  Obrigatório se campo COD\_PAIS for igual a “01058” ou “1058” (Brasil). Se for exterior, informar campo “vazio” | Código da tabela de classificação de municípios conforme a tabela de classificação definida na tela geração | Participante.CodMunicipio |

2REGISTRO 0200 - TABELA DE IDENTIFICAÇÃO DO ITEM

REGISTRO 0200 - TABELA DE IDENTIFICAÇÃO DO ITEM

Este registro tem por objetivo informar mercadorias, serviços, produtos ou quaisquer outros itens concernentes às transações comerciais praticadas.

| Ordem | Campo | Descrição | Tipo | Tamanho | Decimal | Obrigatório | Exemplo de Conteúdo | Regras Previstas de Validação | Especificação | Dicas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Identificação do Item | C | 004 |  | O | 0200 | Único conteúdo valido "0200" | Fixo "0200" |  |
| 02 | COD\_ITEM | Código do Item | C | 060 |  | O | ITEM00001 | Só devem ser apresentados itens referenciados nos demais blocos A identificação do item deverá receber o mesmo código em qualquer documento O valor informado neste campo deve existir em pelo menos um registro dos demais blocos | O código de item, campo COD\_ITEM, e a respectiva unidade, campo UNID\_INV, a serem informados deverão ser os utilizados no livro fiscal Registro de Inventário, modelo 7 (Bloco H da EFD). Informar com códigos próprios do informante do arquivo os itens das operações de entradas de mercadorias ou aquisições de serviços; No caso de veículos automotores, será utilizado um código para cada veículo, vedada a reutilização de código de item, sendo recomendável a utilização do próprio número do chassi para essa finalidade. | Produto.CodigoPrd |
| 03 | DESCR\_ITEM | Descrição do item | C |  |  | O | VIBRAQUINS | São vedadas descrições diferentes para o mesmo item ou descrições genéricas; | Se houver um registro 0205 para este item  o campo deve ser preenchido com a atual descrição utilizada no período | Util.Normalizar(Produto.NomeFantasia) |
| 04 | COD\_BARRA | Representação alfanumérica do código de barra do produto | C |  |  | OC |  | Informar o conteúdo do campo somente se o produto possuir esse código | Informar o código GTIN-8, GTIN-12, GTIN-13 ou GTIN-14 (antigos códigos EAN, UPC e DUN-14) | Produto.CodigoBarras |
| 05 | UNID\_INV | Unidade de medida utilizada na quantificação de estoques | C | 006 |  | O | UN |  |  | CodUnd (GetTodosLancamentos.ListaItem) |
| 06 | COD\_NCM | Código da Nomenclatura Comum do MERCOSUL | C | 008 |  | O | 21011110 | Código da Nomenclatura Comum do Mercosul do item | Informar o Código NCM conforme a Nomenclatura Comum do MERCOSUL, de acordo com o Decreto nº 6.006/06 | Produto.NumeroCCF |
| 07 | ALIQ\_ICMS | Alíquota de ICMS aplicável ao item nas operações internas. | N |  | 02 | OC | 18,00 |  | O objetivo do fisco é identificar se este produto possui uma regra especifica de tributação para contribuintes em Regime Normal de Apuração ou é tributado pelo alíquota normal; As operações com contribuintes do Simples Nacional devem apresentar a alíquota de tributação normal. A informação apresentada neste campo será a base para o valor do ICMS que será preenchido nas colunas 15 a 22 da Apuração do Ressarcimento ou Complemento. Definir critérios para a identificação deste campos é primordial para o bom funcionamento da rotina. | VlrDifAliquota (GetTodosLancamentos.ListaItem) |
| 08 | CEST | Código Especificador da Substituição Tributária | 007\* |  |  |  | 1709602 |  | No caso em que mais de um código CEST puder ser atribuído a um único produto no momento da saída, este campo não deve ser informado; | TPRDFISCAL.CODIGOCEST (adicionar no contexto do produto) |

REGISTRO 0205: CÓDIGO ANTERIOR DO ITEM (Não obrigados ao SPED)

Este registro é gerado com base no histórico de alterações do produto e deverá ser geado somente quando ocorrer alteração no código do produto e se o contribuinte for dispensado de entregar o SPED. Na tela de geração haverá um campo para o usuário informar se deseja gerar este registro.

| Ordem | Campo | Descrição | Tipo | Tamanho | Decimal | Obrigatório | Exemplo de Conteúdo | Regras Previstas de Validação | Especificação | Dicas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Identificação do item | C | 004 |  | O |  | Alteração do Item | Fixo "0205" |  |
| 02 | COD\_ITEM | Código do item alterado | C | 060 |  | O |  |  | Código atual do Produto | Contexto GetTodosLancamentos.ListaItem.ListaLogProduto  CodigoPrd |
| 03 | COD\_ANT\_ITEM | Código anterior do mesmo item | C | 060 |  | O |  |  | Código anterior do Produto | Contexto GetTodosLancamentos.ListaItem.ListaLogProduto  Util.If(Util.ValueIn(IdentCampo, "1"), ValorAnterior, "") |
| 04 | DESCR\_ANT\_ITEM | Descrição anterior do mesmo item | C |  |  | O |  | Vedada a alteração para descrição de item diverso | Descrição anterior do Produto | Contexto GetTodosLancamentos.ListaItem.ListaLogProduto  Util.If(Util.ValueIn(IdentCampo, "0"), ValorAnterior, "") |

3REGISTRO 1050 - REGISTROS DE SALDOS EM ESTOQUE

REGISTRO 1050 - REGISTROS DE SALDOS EM ESTOQUE

Deverá ser solicitado um serviço do Nucleus que retornará o estoque inicial e final do período para cada produto que estiver parametrizado com tributação do ICMSST para o estado da filial conforme "Alteração da Apuração → Encerramento do período → Item 1"

| Ordem | Campo | Descrição | Tipo | Tamanho | Decimal | Obrigatório | Exemplo de Conteúdo | Regras Previstas de Validação | Especificação | Dicas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Registro de Saldos | N | 002 |  | O | 1050 | Registros de Saldos em Estoque | Fixo "1050" |  |
| 02 | COD\_ITEM | Código do item conforme Registro 0200 | C | 060 |  | O | ITEM00001 |  | Código do produto | Deverá ser retornado pelo serviço |
| 03 | QTD\_INI | Quantidade inicial do item no início do primeiro dia do período. | N |  | 3 | O | COLUNA 22 |  | Quantidade inicial do produto em estoque no início do primeiro dia do período. | Deverá ser retornado pelo serviço |
| 04 | ICMS\_TOT\_INI | Valor inicial acumulado do total do ICMS suportado pelo contribuinte, relativamente ao item, no início do primeiro dia do período. | N |  | 2 | O | COLUNA 24 | O valor total do ICMS suportado pelo contribuinte é a base de cálculo  do ICMS ST multiplicado pela alíquota interna de venda ao consumidor final, ou seja, a alíquota do registro 0200 deste item | Deste campo será o resultado da somatório do ICMS incidente sobre o item:  - ICMS Próprio; - ICMS Antecipado; - ICMS Retido; - ICMS Recolhido anteriormente | Deverá ser selecionado os itens de entrada suficientes para acobertar a quantidade em estoque. O valor será a soma do ICMS que incidiu na compra dos itens selecionados, mas poderão ser consideradas somente as quantidade dos itens que não tenham sido referenciados aos itens de saída até aquela data |
| 05 | QTD\_FIM | Quantidade final do item no final do último dia do período. | N |  | 3 | O | COLUNA 22 |  | Quantidade final do produto em estoque no final do último dia do período. | Deverá ser retornado pelo serviço |
| 06 | ICMS\_TOT\_FIM | Valor final acumulado do total do ICMS suportado pelo contribuinte, relativamente ao item, no início do primeiro dia do período subsequente. | N |  | 2 | O | COLUNA 24 |  |  | Deverá ser selecionado os itens de entrada suficientes para acobertar a quantidade em estoque. O valor será a soma do ICMS que incidiu na compra dos itens selecionados, mas poderão ser consideradas somente as quantidade dos itens que não tenham sido referenciados aos itens de saída até aquela data |

Observação: Caso o Serviço do Estoque retorne em um dos Itens gerados, nos registros 1100 ou 1200, será gerado um registro 1050, independente do saldo, podendo ter os valores zerados.  Os saldos zerados podem ocorrer quando um determinado produto tem sua entrada e saída na totalidade dentro do mesmo mês, por exemplo.

4REGISTRO 1100 – REGISTRO DE DOCUMENTO FISCAL ELETRÔNICO

REGISTRO 1100 – REGISTRO DE DOCUMENTO FISCAL ELETRÔNICO PARA FINS DE RESSARCIMENTO DE SUBSTITUIÇÃO TRIBUTÁRIA – SP

Gerar para os registros apurados na tabela DPERIODORESSARCIMENTOICMSST apenas para documentos eletrônicos modelo 55, 59 e 65

| Ordem | Campo | Descrição | Tipo | Tamanho | Decimal | Obrigatório | Exemplo de Conteúdo | Regras Previstas de Validação | Especificação | Dicas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "1100" | N | 004 |  | O | 1100 | Registro de documento fiscal eletrônico para fins de ressarcimento de substituição tributária ou antecipação | Fixo "1100" |  |
| 02 | CHV\_DOC | Chave do Documento Fiscal Eletrônico | N | 044\* |  | O | COLUNA 03 | Se o conteúdo do campo 11 - COD\_LEGAL for "2" este campo poderá conter o zero (0) | Assumirá o valor zero (0), na hipótese de não haver emissão de documento fiscal nos termos do § 3º do artigo 3º da Portaria CAT 158/15 | Contexto GetTodosLancamentos  Convert.ToString(ChaveAcessoNFE) |
| 03 | DATA | Data da entrada da mercadoria ou da saída | N | 008\* |  | O | COLUNA 02 | Se o conteúdo do campo 11 - COD\_LEGAL for "2" e o conteúdo do campo 02 - CHV\_DOC for "0" este campo deverá conter o último dia do período. Formato DDMMAAAA. | Data de digitação do documento fiscal na base de dados do sistema no caso dos documentos de entrada ou data de emissão do documento fiscal nos casos de documentos de saída assumirá o valor do último dia do período, na hipótese de não haver emissão de documento fiscal nos termos do § 3º do artigo 3º da Portaria CAT 158/15 | Contexto GetTodosLancamentos  DataES |
| 04 | NUM\_ITEM | Número sequencial do item no Documento Fiscal Eletrônico | N | 003 |  | O |  | Se o conteúdo do campo 11 - COD\_LEGAL for "2" e o conteúdo do campo 02 - CHV\_DOC for "0" este campo deverá conter "999" | número do item registrado no Documento Fiscal Eletrônico assumirá o valor (999), na hipótese de não haver emissão de documento fiscal nos termos do § 3º do artigo 3º da Portaria CAT 158/15 | DPERIODORESSARCIMENTOICMSST .NUMITEM |
| 05 | IND\_OPER | Indicador do tipo de operação: | N | 001 |  | O |  |  | 0- Entrada; 1- Saída | Contexto GetTodosLancamentos  TipoLf  ou  DPERIODORESSARCIMENTOICMSST .TIPO |
| 06 | COD\_ITEM | Código do item conforme Registro 0200 | C | 060 |  | O | ITEM00001 | O valor informado neste campo deve existir no Registro 0200 |  | Contexto GetTodosLancamentos.ListaItem  Produto.CodigoPrd |
| 07 | CFOP | Código Fiscal de Operação e Prestação | N | 004\* | 3 | O |  | Se o conteúdo do campo 11 - COD\_LEGAL for "2" e o conteúdo do campo 02 - CHV\_DOC for "0" este campo deverá conter "5001" | O CFOP será informado sob o enfoque do declarante. Na hipótese de não haver emissão de documento fiscal nos termos do § 3º do artigo 3º da Portaria CAT 158/15 deverá ser informado "5001" | Contexto GetTodosLancamentos.ListaItem  \GetTodosLancamentos\Natureza\CodNatSintetico |
| 08 | QTD. | Quantidade do Item | N |  | 2 | O |  | Este campo não pode conter valores negativos | informe a quantidade do item utilizando a unidade declarada no respectivo registro 0200.  Em caso de conversão em outras unidade de medidas deverá ser utilizada a unidade padrão no estoque devendo esta, preferencialmente, ser a unidade de revenda ou requisição de estoques. | DPERIODORESSARCIMENTOICMSST .QUANTIDADE |
| 09 | ICMS\_TOT | Valor total do ICMS suportado pelo contribuinte nas operações de entrada (v. observação feita para o Registro 1050) | N |  | 2 | OC | COLUNA 12 | Este campo deve ser informado apenas para as notas fiscais de entrada de aquisição da mercadoria e na notas fiscais de saída do tipo devolução de compras |  | DPERIODORESSARCIMENTOICMSST.VLRTOTSUPORTADO |
| 10 | VL\_CONFR | Valor de confronto nas operações de saída | N |  |  | OC | COLUNA 20 OU  COLUNA 21 | Este registro deve ser gerado apenas nas notas fiscais de saída ou notas fiscais de entrada do tipo devolução de vendas. Se o conteúdo do campo 11 - COD\_LEGAL for "2" e o conteúdo do campo 02 - CHV\_DOC for "0" este campo deverá ser informado com o valor do ICMS ST conforme regra do campos. | Informe o valor de confronto nas operações de saídas, quando o Código de Enquadramento Legal do Ressarcimento/Complemento for maior que zero, ou seja, nas operações com direito ao ressarcimento ou obrigação de complemento de ICMS ST ou de ICMS antecipado; | DPERIODORESSARCIMENTOICMSST.VLRTOTCONFRONTO |
| 11 | COD\_LEGAL | Código de Enquadramento Legal do ressarcimento ou Complemento | N | 001 |  | OC |  | Este registro deve ser gerado apenas nas notas fiscais de saída de operação de venda de mercadoria. Não deve ser preenchido nem para as operações de entrada e nem para as notas fiscais de saída de devolução de compras. |  | DPERIODORESSARCIMENTOICMSST.ENQUADRAMENTOLEGAL |

5REGISTRO 1200 – REGISTRO DE DOCUMENTO FISCAL NÃO-ELETRÔNICO

REGISTRO 1200 – REGISTRO DE DOCUMENTO FISCAL NÃO-ELETRÔNICO PARA FINS DE RESSARCIMENTO DE SUBSTITUIÇÃO TRIBUTÁRIA – SP

Gerar para os registros apurados na tabela DPERIODORESSARCIMENTOICMSST apenas para documentos não eletrônicos modelo diferente de 55, 59 e 65.

| Ordem | Campo | Descrição | Tipo | Tamanho | Decimal | Obrigatório | Exemplo de Conteúdo | Regras Previstas de Validação | Especificação | Dicas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "1200" | N | 002 |  | O | 1200 |  | Fixo "1200" |  |
| 02 | COD\_PART | Código de identificação do participante no arquivo conforme Registro 0150 | C | 060 |  | OC | PARTICIP00001 | código de identificação do participante no arquivo conforme Registro 0150. | informe o código de identificação do participante no arquivo conforme Registro 0150 | \GetTodosLancamentos\Participante.Codigo |
| 03 | COD\_MOD | Código do modelo do documento fiscal, conforme a Tabela 4.1.1 do SPED | C | 002 |  | O | 01 |  |  | \GetTodosLancamentos.CodModDoc |
| 04 | ECF\_FAB | Número de série de fabricação do equipamento ECF | C | 021 |  | OC |  | Só será preenchido nos documentos não eletrônicos fiscais emitidos por ECF. |  | Verificar a maquina associada ao lançamento Fiscal e buscar o número de série diretamente no cadastro da maquina  DMAQUINA.NUMEROSERIEFABRICA |
| 05 | SER | Série do documento fiscal | C | 003 |  | OC | 999 |  | Informe a série do Documento Fiscal | GetTodosLancamentos.SerieDoc |
| 06 | NUM\_DOC | Número do documento fiscal | C | 009 |  | O | 999999999 |  | Informe o número do Documento Fiscal | GetTodosLancamentos.DocIni |
| 07 | NUM\_ITEM | Número sequencial do item no documento fiscal | N | 003 |  | O |  |  | informe o número sequencial do item no Documento Fiscal | DPERIODORESSARCIMENTOICMSST .NUMITEM |
| 08 | IND\_OPER | Indicador do tipo de operação: | N | 001 |  | O |  |  | 0- Entrada; 1- Saída | Contexto GetTodosLancamentos  TipoLf  ou  DPERIODORESSARCIMENTOICMSST .TIPO |
| 09 | DATA | Data da entrada da mercadoria ou da saída | N | 008\* |  | O |  | Se o conteúdo do campo 11 - COD\_LEGAL for "2" e o conteúdo do campo 02 - CHV\_DOC for "0" este campo deverá conter o último dia do período. Formato DDMMAAAA. | Data de digitação do documento fiscal na base de dados do sistema no caso dos documentos de entrada ou data de emissão do documento fiscal nos casos de documentos de saída assumirá o valor do último dia do período, na hipótese de não haver emissão de documento fiscal nos termos do § 3º do artigo 3º da Portaria CAT 158/15. | Contexto GetTodosLancamentos  DataES |
|  | CFOP | Código Fiscal de Operação e Prestação | N | 004\* | 3 | O |  | Se o conteúdo do campo 11 - COD\_LEGAL for "2" e o conteúdo do campo 02 - CHV\_DOC for "0" este campo deverá conter "5001" | O CFOP será informado sob o enfoque do declarante. Na hipótese de não haver emissão dedocumento fiscal nos termos do § 3º do artigo 3º da Portaria CAT 158/15 deverá ser informado "5001" | Contexto GetTodosLancamentos.ListaItem  \GetTodosLancamentos\Natureza\CodNatSintetico |
| 11 | COD\_ITEM | Código do item conforme Registro 0200 | C | 060 |  | O | ITEM00001 | O valor informado neste campo deve existir no Registro 0200 |  | Contexto GetTodosLancamentos.ListaItem  Produto.CodigoPrd |
| 12 | QTD | Quantidade do Item | N |  | 2 | O |  | Este campo não pode conter valores negativos | Informe a quantidade do item utilizando a unidade declarada no respectivo registro 0200. Em caso de conversão em outros unidade de medidas deverá ser utilizada a unidade padrão no estoque devendo esta preferencialmente ser a unidade de revenda ou requisição de estoques. | DPERIODORESSARCIMENTOICMSST .QUANTIDADE |
| 13 | ICMS\_TOT | Valor total do ICMS suportado pelo contribuinte nas operações de entrada (v. observação feita para o Registro 1050) | N |  | 2 | OC | COLUNA 12 | Este campo deve ser informado apenas para as notas fiscais de entrada ou para notas fiscais de saída do tipo devolução de compras | Informe, nas operações de entrada, o valor total do ICMS suportado pelo contribuinte, relativamente ao item. | DPERIODORESSARCIMENTOICMSST.VLRTOTSUPORTADO |
| 14 | VL\_CONFR | Valor de confronto nas operações de saída | N |  |  | OC | COLUNA 20 OU  COLUNA 21 | Valor de confronto das operações de saída ou nas devoluções de venda |  | DPERIODORESSARCIMENTOICMSST.VLRTOTCONFRONTO |
| 15 | COD\_LEGAL | Código de Enquadramento Legal do ressarcimento ou Complemento | N | 001 |  | OC |  | Este registro deve ser gerado apenas nas notas fiscais de saída de operação de venda de mercadoria. Não deve ser preenchido nem para as operações de entrada e nem para as notas fiscais de saída de devolução de compras. | Informação disponibilizada pela SEFAZ. Como item de referência ao desenvolvimento esta informação esta disponível no folder "Tabela de Códigos" A decisão da forma como será tratada caberá ao produto. | DPERIODORESSARCIMENTOICMSST.ENQUADRAMENTOLEGAL |

* Obrigatoriedade: “O” = Obrigatório, ou seja, preenchimento obrigatório sempre; “OC” = Obrigatório Condicional, ou seja, preenchimento obrigatório somente quando presente uma determinada condição

## Arquivo Magnético

O arquivo é composto pelos seguintes tipos de registros, classificados na ordem abaixo:

| Tipo Registro | Nome do Registro | Obrigatoriedade | Quantidade por arquivo |
| --- | --- | --- | --- |
| 0000 | Abertura do Arquivo Digital e Identificação do Contribuinte | O | Um |
| 0150 | Tabela de Cadastro do Participante | O | Vários |
| 0200 | Identificação do Item | O | Vários |
| 0205 | Código Item Anterior (não obrigados ao SPED) | OC | Vários |
| 1050 | Registro de Saldos | O | Vários |
| 1100 | Registro de Documento Fiscal Eletrônico Para Fins de Ressarcimento de Substituição Tributária – SP | OC | Vários |
| 1200 | Registro de Documento Fiscal NãoEletrônico Para Fins de Ressarcimento de Substituição Tributária – SP | OC | Vários |

Definições técnicas do arquivo

* Formato ASCII - ISSO 8859-I
* Organização sequencial ascendente (Exceção apenas para o 0200 e 0205 que devem ser apresentados na estrutura pai e fillho)
* Devem ser agrupados todos os registros do mesmo tipo antes de iniciarmos o próximo tipo de produto
* Separação de campos por "|" PIPE
* Não deverá haver um "|" nem no inicio da linha e nem no final
* Quebra de linha por CRLF
* Se um campo não tiver conteúdo deverá haver apenas o "|" deste campo
* Não deverá haver caracteres especiais
* Os números terão separação apenas decimas por ","
* Data seguem o padrão ddmmaaaa
* Período segue o padrão mmaaaa
* Campos de identificação de órgão regulador devem ser apresentados de forma completa, inclusive com zeros a esquerda  sem carácteres de formatação (CNPJ, IE, Código de Município, CEST)

Exemplo: 0000|082018||TOTVS

## Geração do Arquivo Magnético

Para geração do arquivo magnético será criado um layout no Gerador de Saídas contendo os registros mapeados na seção "Registros".

O Layout deverá solicitar os seguintes parâmetros para execução:

* Código da Filial: Lookup para o cadastro da filial
* Data inicial do período: Campo de data
* Data final do período: Campo de data
* Tabela de Classificação de municípios IBGE: Lookup para o cadastro da tabela de classificação de municípios
* Versão do layout: Um campo texto editável quem venha com default 1.0.0
* Gerar 0205: CheckBox para informar se o registro 0205 precisa ser gerado. Este registro deverá ser gerado somente para os clientes dispensados de gerar o SPED e somente para os produto que tiveram alteração de código.
* Finalidade do arquivo: Um combobox com as opções disponibilizadas pela Receita

  | Código | Descrição |
  | --- | --- |
  | 00 | Remessa regular de arquivo |
  | 01 | Remessa de arquivo requerido por intimação específica |
  | 02 | Remessa de arquivo para substituição de arquivo remetido anteriormente. |

## Validação

A SEFAZ SP liberou um arquivo de Pré- Validação que poderá ser utilizado para testes disponível em: <https://www3.fazenda.sp.gov.br/RessarcimentoSTPreValidador/publish.htm>

## Associação de Lançamentos de Saída

O processo de Associação de Lançamentos de Saída deverá ser evoluído para permitir a execução sem selecionar os lançamentos da visão.

Menu

A chamada do processo deverá ser movida para o menu "Utilitários"

Tela

Na tela de execução deverá ser informado um filtro de lançamentos para que o usuário consiga definir para quais lançamentos o processo será executado.

Execução

* A associação dos itens da saída deverá buscar os itens da ultima entrada considerando a data de saída e data de entrada.

  Exemplo
* O processo deverá permitir chamada assíncrona;
* A execução poderá ser agendada através de Job.

## Devolução

Associação de Lançamentos de Saída

O processo de associação de Lançamentos de Saída deverá permitir a associação dos Lançamentos de entrada cuja a devolução dos itens já tenham ocorrido, ou seja, somente Lançamentos gerados após a data da devolução. Contudo o Lançamento de devolução não poderá ser associado à um Lançamento de Saída e nem considerados em cálculos do ICMS Suportado para o registro 1050 após a data da devolução.

O processo de Associação deverá ser alterado para não associar saídas cuja CFOP seja de devolução, pois estas saídas não podem ser associadas as entradas mais recentes e sim a nota que está sendo devolvida. Neste caso a associação deverá ser executada manualmente pelo usuário.

Encerramento do Período

Nas notas de devoluções os valores de ICMS suportado devem ser iguais ao valores gerados na nota original e consequentemente serão gerados no campo ICMS\_TOT dos registros 1100 e 1200.

Na nota de Devolução de Entrada os campos referentes ao valor de confronto e enquadramento legal (COD\_LEGAL e VL\_CONFR) devem ser gerados em branco e consequentemente serão gerados em branco nos registros 1100 e 1200.

No caso da nota de Devolução de Saída o campo referente ao enquadramento legal deve ser gerado normalmente (será igual ao enquadramento da saída). Caso o enquadramento seja diferente de zero, o campo valor de confronto deverá ser geado e consequentemente ambos os campos serão gerados nos registros 1100 e 1200 (COD\_LEGAL e VL\_CONFR).

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
