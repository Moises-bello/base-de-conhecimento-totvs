---
content_hash: 7c6d9b9065bc13efb70e1d5b2cee10baaadfcfa7369ce98d84e0e96a2a46ae9b
fetched_at: '2026-06-29T00:09:10.950527+00:00'
page_id: '403737188'
product: rm
source: tdn-rm
title: FISCAL01-6355 ER Rotina Federal SISCOSERV - Atualização do manual versão 11
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403737188
version: 106
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Totvs Gestão Fiscal |
| **Segmento Executor** | Serviços | | |
| **Requisito/Story/Issue1** | FISCAL01-6355 | **Subtarefa1** | FISCAL01-6440 |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Atender as determinações legais impostas pela 11ª Edição do Manual do Módulo de Aquisição/Venda da Rotina Federal SISCOSERV.

Definição da Regra de Negócio

O Sistema Integrado de Comércio Exterior de Serviços, Intangíveis e Outras Operações que Produzam Variações no Patrimônio (Siscoserv) é um sistema informatizado, desenvolvido pelo Governo Federal como ferramenta para o aprimoramento das ações de estímulo, formulação, acompanhamento e aferição das políticas públicas relacionadas a serviços e intangíveis, bem como para a orientação de estratégias empresariais de comércio exterior de serviços e intangíveis. O Siscoserv guarda conformidade com as diretrizes do Acordo Geral sobre Comércio de Serviços (GATS) da Organização Mundial do Comércio (OMC), aprovado pelo Decreto Legislativo no 30, de 15 de dezembro de 1994, e promulgado pelo Decreto no 1.355, de 30 de Dezembro de 1994.

## Alterações a serem realizadas

1. #### Alteração no Lançamento Fiscal

Deverá ser criado dois enumerados, para preencher o campo “Modo de Prestação” do lançamento fiscal, existem opções distintas entre o lançamento de entrada e de saída.

Para o Lançamento Fiscal de Entrada, deverão conter as seguintes opções:

1- Comércio Transfronteiriço

2- Consumo no Exterior;

4-   Movimento Temporário de Pessoas Físicas

Para o Lançamento Fiscal de Saída, deverão conter as seguintes opções:

1- Comércio Transfronteiriço

2- Consumo no Brasil;

4- Movimento Temporário de Pessoas Físicas

#### 2.  Alterações nos XML's do Módulo de Aquisição

* + XML "incluir\_RAS.xml":  
      
    - Alterada a estrutura do arquivo, foi criado o grupo “IdentificadorFiscal” que irá conter as tags “Nif” ou “MotivoNaoPreenchimentoNif”;             - Criada a tag “TipoVinculacao”;

                          - Alterar o nome da tag “NumeroServAdqEmpresa” para “NumeroOperacaoEmpresa” no grupo Operação;

                          - Após a tag de Valor, foi criada a tag “CnpjGastoPessoal” no grupo Operação;

                          - Incluídas as tags “VinculacaoNumRE” e “VinculacaoNumDI” no grupo Operação;

                          - Retirado o grupo “VincImportacaoBens”

       - XML da 11ª edição do Manual:

|  |  |  |  |
| --- | --- | --- | --- |
| Nome da tag | Descrição da tag | Obrigatoriedade | Preenchimento da tag |
| IdentificadorFiscal | Estrutura contendo obrigatoriamente uma e apenas uma das seguintes tags:Nif ou MotivoNaoPrenchimentoNif. | (TAG OBRIGATÓRIA) | Não se aplica |
| Nif | Número de identificação fiscal do residente ou domiciliado no exterior vendedor do serviço. | (TAG OBRIGATÓRIA SE OCORRER) | Considerar o Código informado no Cadastro do Cli\For – Sub Pasta Dados Fiscais\Outros Dados “Campo NIT”.  **FCFO.NIF**  obs.: Preencher o campo quando a Situação do Nif do Cadastro de Cli/For for igual a "Informar numero de Identificação Fiscal". |
| MotivoNaoPrenchimentoNif | MotivoNaoPrenchimentoNif– Motivo do não preenchimento da tagNif os valores válidos para esta tag são:  1 – Residente ou domiciliado no exterior dispensado do NIF;  2 – País não exige NIF. | (TAG OBRIGATÓRIA SE OCORRER) | **FCFO.SITUACAONIF**  obs.: Preencher o campo quando a Situação do Nif do Cadastro de Cli/For for diferente de "Informar numero de Identificação Fiscal". |
| TipoVinculacao | Vinculação do adquirente residente ou domiciliado no Brasil ao vendedor do serviço residente ou domiciliado no exterior. Os valores válidos para esta tag são:   * 0 – Não há vinculação; * 1 – Filial; * 2 – Sucursal; * 3 – Controlada; * 4 – Outros. | (TAG OBRIGATÓRIA quando o adquirente domiciliado no Brasil for pessoa jurídica, a tag não deve ser utilizada quando este adquirente for pessoa física) | Criar Campo complementar no Cadastro Cli/For "**TIPOVINCSISCOSERV**" com os valores da Lista:   * 0 – Não há vinculação; * 1 – Filial; * 2 – Sucursal; * 3 – Controlada; * 4 – Outros. |
| CnpjGastoPessoal | CNPJ da empresa brasileira em nome da qual os gastos pessoais, representados pela operação, foram incorridos. A existência desta tag caracteriza a operação como um gasto pessoal a serviço do empregador. | (TAG NÃO OBRIGATÓRIA - Esta tag aplica-se apenas aos registros de pessoas físicas não sendo permitido em registros de pessoas jurídicas.) | **Não aderência do produto.** |
| VinculacaoNumRE | Registro de Exportação (RE) de movimentação temporária de bens vinculada à operação. O campo contém 12 dígitos e deve ser informado com máscara conforme exemplo: 11/1111111111 | (TAG NÃO OBRIGATÓRIA) | **Não aderência do produto.** |
| VinculacaoNumDI | Declaração de Importação (DI) de movimentação temporária de bens vinculada à operação. O campo contém 10 dígitos e deve ser informado com máscara conforme exemplo: 11/1111111-1 | (TAG NÃO OBRIGATÓRIA) | Considerar o Número da DI informada na pasta Exterior dos lançamentos Fiscais.  **DLAFEXTERIOR.NUMERODI** |

* + XML "inclusao\_pagamento.xml":

                         - Incluída a tag “IdItemPagamentoEmpresa” no grupo do ItemPagamento;

                         - Alterado o nome da tag “NumOpAdqEmpresa” para “NumeroOperacaoEmpresa” no grupo ItemPagamento;

- Incluída a tag "ValorPagoRecMantidoExt" no grupo ItemPagamento;

                         - Retiradas as tags “VinculacaoNumRE” e “VinculacaoNumDI”;

                         - XML da 11ª edição do Manual:

|  |  |  |  |
| --- | --- | --- | --- |
| Nome da tag | Descrição da tag | Obrigatoriedade | Preenchimento da tag |
| ValorPagoRecMantidoExt | Valor do pagamento da operação mantido no exterior. Formato do campo: 1000.00, o ponto é o separador para os centavos. | (TAG NÃO OBRIGATÓRIA) | Gerar com o mesmo valor gerado na tag **ValorPago** |
| IdItemPagamentoEmpresa | Identificador unívoco do pagamento dentro do registro (o identificador pode repetir-se em registros distintos). Gerado pelo usuário sem quaisquer restrições de formato a não ser aquelas declaradas nos arquivos XSD. No caso de retificação, o pagamento será identificado através dele. | (TAG OBRIGATÓRIA) | **DITEM.NUMITEM** |

#### 3. Alterações nos XML's do Módulo de Venda

* + XML "incluir\_faturamento.xml":

                         - Incluída a tag “IdItemFaturaEmpresa” no grupo do ItemFatura;

                         - Incluída a tag "ValorMantidoExterior" no grupo ItemFatura;

                         - Retiradas as tags “VinculacaoNumRE” e “VinculacaoNumDI”;

                         - XML da 11ª edição do Manual:

|  |  |  |  |
| --- | --- | --- | --- |
| Nome da tag | Descrição da tag | Obrigatoriedade | Preenchimento da tag |
| ValorMantidoExterior | Valor do faturamento da operação mantido no exterior. Formato do campo: 1000.00, o ponto é o separador para os centavos. | (TAG NÃO OBRIGATÓRIA) | Gerar com o mesmo valor gerado na tag **ValorFaturado** |
| IdItemFaturaEmpresa | Identificador unívoco do faturamento dentro do registro (o identificador pode repetir-se em registros distintos). Gerado pelo usuário sem quaisquer restrições de formato a não ser aquelas declaradas nos arquivos XSD. No caso de retificação, o faturamento será identificado através dele. | (TAG OBRIGATÓRIA) | **DITEM.NUMITEM** |

* + XML "incluir\_registro.xml":

                         - Alterada a estrutura do arquivo, foi criado o grupo “IdentificadorFiscal” que irá conter as tags “Nif” ou “MotivoNaoPreenchimentoNif”;

                         - Criada a tag “TipoVinculacao”;

                         - Incluídas as tags “VinculacaoNumRE” e “VinculacaoNumDI” no grupo Operação;

                         - Retirado o grupo “VincImportacaoBens”;

                         - XML da 11ª edição do Manual:

|  |  |  |  |
| --- | --- | --- | --- |
| Nome da tag | Descrição da tag | Obrigatoriedade | Preenchimento da tag |
| IdentificadorFiscal | Estrutura contendo obrigatoriamente uma e apenas uma das seguintes tags:Nif ou MotivoNaoPrenchimentoNif. | (TAG OBRIGATÓRIA) | Não se aplica |
| Nif | Número de identificação fiscal do residente ou domiciliado no exterior vendedor do serviço. | (TAG OBRIGATÓRIA SE OCORRER) | Considerar o Código informado no Cadastro do Cli\For – Sub Pasta Dados Fiscais\Outros Dados “Campo NIT”.  **FCFO.NIF**  obs.: Preencher o campo quando a Situação do Nif do Cadastro Cli/For for igual a "Informar numero de Identificação Fiscal". |
| MotivoNaoPrenchimentoNif | MotivoNaoPrenchimentoNif– Motivo do não preenchimento da tagNif os valores válidos para esta tag são:  1 – Residente ou domiciliado no exterior dispensado do NIF;  2 – País não exige NIF. | (TAG OBRIGATÓRIA SE OCORRER) | **FCFO.SITUACAONIF**  obs.: Preencher o campo quando a Situação do Nif do Cadastro Cli/For for diferente de "Informar numero de Identificação Fiscal". |
| TipoVinculacao | Vinculação do adquirente residente ou domiciliado no Brasil ao vendedor do serviço residente ou domiciliado no exterior. Os valores válidos para esta tag são:   * 0 – Não há vinculação; * 1 – Filial; * 2 – Sucursal; * 3 – Controlada; * 4 – Outros. | (TAG OBRIGATÓRIA quando o adquirente domiciliado no Brasil for pessoa jurídica, a tag não deve ser utilizada quando este adquirente for pessoa física) | Criar Campo complementar no Cadastro de Cli/For "TIPOVINCSISCOSERV" com os valores da Lista:   * 0 – Não há vinculação; * 1 – Filial; * 2 – Sucursal; * 3 – Controlada; * 4 – Outros. |
| VinculacaoNumRE | Registro de Exportação (RE) de movimentação temporária de bens vinculada à operação. O campo contém 12 dígitos e deve ser informado com máscara conforme exemplo: 11/1111111111 | (TAG NÃO OBRIGATÓRIA) | Considerar o Número RE informada na pasta Exportação dentro de itens do lançamento Fiscais.  **DITEM.NUMERORE** |
| VinculacaoNumDI | Declaração de Importação (DI) de movimentação temporária de bens vinculada à operação. O campo contém 10 dígitos e deve ser informado com máscara conforme exemplo: 11/1111111-1 | (TAG NÃO OBRIGATÓRIA) | Considerar o Número da DI informada na pasta Exterior dos lançamentos Fiscais.  **DLAFEXTERIOR.NUMERODI** |

#### Obs.: Para preenchimento do campo TipoVinculacao deve-se criar um campo complementar com o nome TIPOVINCSISCOSERV no Cadastro de Cliente Fornecedor conforme telas abaixo.

#### 4. Implementação do processo de Retificação

Uma vez gerado os arquivos  do RVS (módulo de venda) ou RAS ( módulo de aquisição) os mesmos não podem ser cancelados, devem ser retificados em casos onde é necessário realizar uma alteração nas informações.

              O layout da retificação é baseado no da inclusão (exceto pelas ressalvas apresentadas nas Orientações Específicas) dentro de uma estrutura principal identificada por <RetificarNOMEARQUIVO/> (ex: <RetificarRVS/>, <RetificarRAS/>)

              Nas estruturas <RetificarNOMEARQUIVO/>  e <Operacao/> além das tags que identificam o RVS/RAS e a operação, <NumeroOperacaoEmpresa/>, devem estar presentes apenas as tags das informações que serão retificadas.

              As tags <NumeroRVSEmpresa/> ou <NumeroRASEmpresa/> e <NumeroOperacaoEmpresa/> são de preenchimento obrigatório e seus dados não são passíveis de retificação.

              Não se pode retificar o mesmo RVS/RAS mais de uma vez dentro do mesmo arquivo de lote.

   Processo será visualizado na tela de lançamento fiscal.

  Na tela do processo o cliente irá escolher o tipo de retificação a ser realizada:

* + Para Lançamentos Fiscais de Entrada ( módulo de Aquisição ), devem ser gerados retificações de RAS ou de Pagamento;
  + Para Lançamentos Fiscais de Saída ( módulo de Venda ), devem ser gerados retificações de RVS ou de Faturamento;

O processo irá comparar o XML de inclusão que foi salvo no momento do processo de geração da SISCOSERV e um novo XML gerado no momento da retificação. Esta comparação irá verificar se existe alguma alteração no conteúdo das tags do XML. Havendo alterações, estas tags alteradas serão montadas no formato do XML de retificação e salvo em um caminho definido pelo cliente nos parametros do Fiscal.

Caso haja diferença nos XML's de inclusão, este XML deve ser atualizado na tabela DARQUIVOSSISCOSERV.

#### Orientações Especificas

1. Arquivo RVS:

IdentificadorFiscal - Para alterar o NIF ou motivo do seu não preenchimento, deve ser apresentado a estrutura IdentificadorFiscal informando o Nif ou o MotivoNaoPreenchimentoNif , conforme as instruções na seção Inclusão de RVS.

Enquadramento -

* + Para alterar um número do registro de crédito de um enquadramento, deve ser apresentado o código informado inicialmente e o novo número RC.
  + Para incluir enquadramentos, deve-se acrescentar nova estrutura Enquadramento com o mesmo leiaute da inclusão de RVS.
  + Para excluir enquadramentos, deve ser incluída nova tag, exclusao, na estrutura Enquadramento:

* VinculacaoNumRE e VinculacaoNumDI - Para incluir vinculações a RE o DI, converte-se as tags VinculacaoNumRE e  VinculacaoNumDI em estruturas contendo uma nova tag, NumeroRE e NumeroDI, respectivamente:

Para excluir vinculações a RE ou DI, utiliza-se a mesma estrutura usada para incluir vinculações acrescida de nova tag, exclusao .

2. Arquivo RAS:

Todas as validações descritas no item do RVS.

ExcluirGastoPessoal - Para desassociar a operação do CNPJ de uma empresa brasileira, descaracterizando a operação como gasto pessoal a serviço do empregador, deve-se utilizar a estrutura ExcluirGastoPessoal com a tag exclusao:

3. Arquivo Faturamento:

A retificação de RF adota as mesmas tags da Inclusão de RF (exceto pelas ressalvas apresentadas nas Orientações Específicas abaixo) dentro de uma estrutura principal identificada por RetificarFatura.

 Nas estruturas RetificarFatura e ItemFatura além das tags que identificam o RF ( NumeroRVSEmpresa e IdFaturaEmpresa) e o faturamento da operação ( NumeroOperacaoEmpresa e IdItemFaturaEmpresa), devem estar presentes apenas as tags das informações que serão retificadas.

As tags NumeroRVSEmpresa, IdFaturaEmpresa, NumeroOperacaoEmpresa e  IdItemFaturaEmpresa são de preenchimento obrigatório e seus dados não são passíveis de retificação.

Não se pode retificar o mesmo RF mais de uma vez dentro do mesmo arquivo de lote.

4. Arquivo Pagamento:

A retificação de RP adota as mesmas tags da Inclusão de RP (exceto pelas ressalvas apresentadas nas Orientações Específicas abaixo) dentro de um bloco principal identificado por RetificarPagamento

Nas estruturas RetificarPagamento e ItemPagamento além das tags que identificam o RP ( NumeroRASEmpresa e IdPagamentoEmpresa) e o pagamento da operação (NumeroOperacaoEmpresa e  IdItemPagamentoEmpresa), devem estar presentes apenas as tags das informações que serão retificadas.

As tags NumeroRASEmpresa, IdPagamentoEmpresa, NumeroOperacaoEmpresa e IdItemPagamentoEmpresa são de preenchimento obrigatório e seus dados não são passíveis de retificação.

Não se pode retificar o mesmo RP mais de uma vez dentro do mesmo arquivo de lote.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
