---
article_id: 11962492615319
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: d586193fc849cd8d7925e962de1d5edc2d018dba7e58ec647311cc9bd2d18625
fetched_at: '2026-06-28T22:42:02.461995+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Todos os pontos de entrada disponibilizados para o Sped Fiscal.
type: support-article
updated_at: '2025-09-12T18:52:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11962492615319-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Todos-os-pontos-de-entrada-disponibilizados-para-o-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34901936128023) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Quais os pontos de entrada disponibilizados para o Sped Fiscal?  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

Os pontos de entrada disponibilizados para o Sped Fiscal são:

**1** - Ponto de entrada **SPDFIS03 -** Permite alterar a classificação fiscal dos produtos na geração do **SPEDFISCAL**.

-  [PE - SPDFIS03 - SPEDFISCAL / EFD Contribuições- Altera a Situação Tributária dos Impostos ICMS, IPI, PIS e COFINS](https://tdn.totvs.com/pages/viewpage.action?pageId=706922950)

**2** -  Ponto de entrada **SPDFIS08** tem como objetivo gravar informação no Registro **C100**, o campo **DT\_E\_S** (Data da entrada e saída) customizado pelo cliente.

[- PE - SPDFIS08 - SPEDFISCAL - Grava Informação no Registro C100](https://tdn.totvs.com/pages/viewpage.action?pageId=706923173)

**3** - Ponto de entrada **SPDFIS04** altera a descrição do produto no registro C170 da geração do arquivo magnético para o Sped Fiscal.

* [PE - SPDFIS04 - Altera a descrição do produto](https://tdn.totvs.com/pages/viewpage.action?pageId=649309906)

**4** - Ponto de entrada **SPDFIS05** possibilita a alteração dos seguintes campos do registro C100 do SPED IPI/ICMS:

A - 13 - IND\_PGTO (Indicador do tipo de pagamento);

B - 17 - IND\_FRT (Indicador do tipo de frete)**e**/**ou**

C - 03 - IND\_EMIT (Indicador do emitente do documento fiscal).

* [PE - SPDFIS05 - Altera o indicador de pagamento e indicador de frete e/ou indicador do emitente do documento fiscal](https://tdn.totvs.com/pages/viewpage.action?pageId=706922940)

**5** - Ponto de entrada **SPDFIS06** permite a geração de apenas um campo com as informações de endereço e número do cadastro dos participantes, registro 0150.

* [PE - SPDFIS06 - Informações de endereço e número do cadastro dos participantes](https://tdn.totvs.com/pages/viewpage.action?pageId=706922693)

**6** - Ponto de entrada **SPDFIS07**, que possibilita a customização do Código da Conta Contábil no registro H010 do SPED Fiscal.

* [PE - SPDFIS07 - Registro H010 Conta Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=702821885)

**7** - Ponto de entrada **SPDFIS09**, grava informações nos Registros:

A - C140 - FATURA (CÓDIGO 01)

B - C141 - VENCIMENTO DA FATURA (CÓDIGO 01) 

* [PE - SPDFIS09 - Grava informações nos Registros C140 e C141](https://tdn.totvs.com/pages/viewpage.action?pageId=706923174)

**8** - Ponto de entrada **SPDFIS10** aplicado no SPEDFISCAL permite gravar as informações do Registro 1600: Total de operações com cartão de crédito e/ou débito.

* [PE - SPDFIS10 - SPEDFISCAL - Registro 1600 Total de operações com cartão de crédito ou débito](https://tdn.totvs.com/pages/viewpage.action?pageId=706923145)

**9** - Ponto de entrada **SPDFIS11** permite alterar Serie da nota, nos registros do SPED FISCAL e Contribuições.

* [PE - SPDFIS11 - Tratamento para alterar impressão da serie nos registros de EFD SPED Contribuições e SPED Fiscal](https://tdn.totvs.com/pages/viewpage.action?pageId=619139743)

**10** - Ponto de entrada **SPDFIS27** no SPED Fiscal para que seja possível manipular a escrituração do código da conta contábil.

Com este ponto de entrada é possível alterar a escrituração do código da conta contábil dos registros de nota **C170, C300, C350, D100, D500 e D300** do SPEDFISCAL.

Também é possível manipular a escrituração do código da conta contábil do registro de CADASTRO DE BENS OU COMPONENTES DO ATIVO IMOBILIZADO **0300** e por consequência a mesma conta será considerada na geração do PLANO DE CONTAS CONTÁBEIS registro 0500.

* [PE - SPDFIS27 - SPEDFISCAL - Alterar a escrituração do código da conta contábil dos registros de nota](https://tdn.totvs.com/pages/viewpage.action?pageId=706922972)

**11** - Ponto de Entrada **SPED0150** pode ser utilizado para alterar as informações dos registros **0150** gerados para o **SPEDFISCAL** e **SPED Contribuições**.

* [PE - SPED0150 - SPEDFISCAL - Alterar informações do registro 0150](https://tdn.totvs.com/pages/viewpage.action?pageId=706922521)

**12** - Ponto de entrada **SPED0205** retorna um array com informações da alteração do produto, caso o procedimento padrão não atenda o cliente para geração do registro**0205 - Alteração do Item**.

Neste Ponto de Entrada é passado como parâmetro a data inicial, data final da geração do arquivo magnético e o código de produto que está sendo processado no momento, desta forma é possível identificar o produto e retornar as informações de alterações, caso existam.

* [PE - SPED0205 - SPEDFISCAL/EFD Contribuições - Registro 0205 - alteração do item](https://tdn.totvs.com/pages/viewpage.action?pageId=706921537)

**13** - Ponto de Entrada **SPED1300** para inclusão dos registros 1300, 1310, 1320, 1350, 1360 e 1370.

Panorama geral:

Registro apresentado pelos contribuintes do ramo varejista de combustíveis (postos de combustíveis), refere-se  
à movimentação diária de combustíveis, havendo apenas um registro por tipo de combustível e por data do  
fechamento da movimentação (campo COD\_ITEM e campo DT\_FECH), independente de ocorrerem intervenções.  
Não pode haver mais de um registro com o mesmo código de combustível e mesma data de fechamento.

* [PE - SPED1300 - SPEDFISCAL- Movimentação diária de combustíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=645917395)

**14** - Ponto de Entrada **SPED1390** para gerar os registros 1390 (Controle de Produção de Usina) e 1391 (Produção Diária da Usina) para o SPED Fiscal.

* [PE - SPED1390 - SPEDFISCAL - Registro 1390 e 1391](https://tdn.totvs.com/display/PROT/PE+-+SPED1390+-+SPEDFISCAL+-+Registro+1390+e+1391)

**15** - Ponto de entrada **SPED1400** disponibilizado para geração manual do Registro **1400** do Sped Fiscal.

* [PE - SPED1400 - Informação Sobre Valores Agregados](https://tdn.totvs.com/pages/viewpage.action?pageId=706922994)

**16** - Ponto de entrada **MATUCOMP** utilizado para alterações automáticas nos complementos dos documentos fiscais após a emissão das Notas Fiscais.

Este Ponto de Entrada é executado após gravação de todos os dados da NF de saída ou entrada digitadas no modulo fiscal, faturamento e compras.

* [PE - MATUCOMP - Alterações automáticas de Complemento de Documentos Fiscais](https://tdn.totvs.com/pages/viewpage.action?pageId=642645988)

**17** - Ponto de Entrada **SPED1601** aplicado no SPEDFISCAL que grava as informações do Registro 1601: Operações com Instrumentos de Pagamentos eletrônicos.

* [PE - SPED1601 - SPEDFISCAL - Registro 1601 - Operações com Instrumentos de Pagamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=651921344)

**18** - Ponto de Entrada **SPEDALTH** para processamento do registro H010 SPED FISCAL.

Neste ponto de entrada será gerado arquivo temporário para processamento da rotina SPED FISCAL.

* [PE - SPEDALTH - SPEDFISCAL - Registro H010](https://tdn.totvs.com/display/PROT/PE+-+SPEDALTH+-+SPEDFISCAL+-+Registro+H010)

**19** - Ponto de Entrada **SPEDFANT** para permitir informar o conteúdo do campo 02 FANTASIA para geração do registro 0005 - Dados Complementares Contribuinte.

* [PE - SPEDFANT - Alterar Nome Fantasia do SPEDFISCAL](https://tdn.totvs.com/display/PROT/PE+-+SPEDFANT+-+Alterar+Nome+Fantasia+do+SPEDFISCAL)

**20**- Ponto de entrada **SPEDG126** para gerar informações do registro **G126** do **SPEDFISCAL**.

* [PE - SPEDG126 - SPEDFISCAL - Geração do Registro G126](https://tdn.totvs.com/pages/viewpage.action?pageId=706924094)

**21**- Ponto de Entrada **SPEDH020** aplicado no SPEDFISCAL para geração do Registro H020 - Informação complementar do Inventário.

* [PE - SPEDH020 - SPEDFISCAL - Registro H020](https://tdn.totvs.com/display/PROT/PE+-+SPEDH020+-+SPEDFISCAL+-+Registro+H020)

**22** - Ponto de entrada **SPEDPROD** tem como finalidade retornar um **Array** com as informações do produto para os clientes que possuem uma forma diferente do padrão de compor o código do produto.

* [PE - SPEDPROD - Retorna Array de Informações do Produto](https://tdn.totvs.com/pages/viewpage.action?pageId=706922410)

**23**- Ponto de entrada **SPEDPTMS** permite informar participantes / transporte na geração do SPEDFISCAL.

* [PE - SPEDPTMS - Participantes e Transporte](https://tdn.totvs.com/display/PROT/PE+-+SPEDPTMS+-+Participantes+e+Transporte)

**24**- Ponto de entrada **SPEDR450** permite gravar informações complementares dos lançamentos fiscais dos documentos no registro 0450, em complemento ao ponto de entrada SPEDRTMS os registros do tipo D100 possuem o campo 22-COD\_INF - Código da informação complementar do documento.

* [PE - SPEDR450 - SPEDFISCAL - Grava informações dos lançamentos fiscais no registro 0450](https://tdn.totvs.com/pages/viewpage.action?pageId=706924119)

**25**- Ponto de entrada **SPEDR460** usado para gravar observações dos lançamentos fiscais dos documentos no registro 0460, em complemento ao ponto de entrada SPEDRTMS onde os registros do tipo D190 possuem o campo 09-COD\_OBS - Código da observação do lançamento fiscal.

* [PE - SPEDR460 - SPEDFISCAL - Registro 0460 Descrição da observação vinculada ao lançamento fiscal](https://tdn.totvs.com/pages/viewpage.action?pageId=706924534)

**26**- Ponto de entrada **SPEDREGD** para inclusão dos registros referentes ao Bloco **D350** e registros filhos no **SPEDFISCAL**, respeitando a hierarquia dos registros conforme Guia pratico.

* [PE - SPEDREGD - SPEDFISCAL - Geração de registros Bloco D350 - Documentos Fiscais de Serviços.](https://tdn.totvs.com/pages/viewpage.action?pageId=698289088)

**27**- Ponto de entrada **SPEDRTMS** tem como finalidade permitir a manipulação com as informações envolvendo Conhecimentos de Transporte para os clientes que possuem movimentos gerados sem integração com o ambiente **SIGATMS - Gestão de Transportes**

Sendo utilizado na geração do Bloco documentos fiscais II serviço (ICMS)" para os Registros:**D100, D110, D120, D130, D140, D150, D160, D161, D162 e D190**.

* [PE - SPEDRTMS - Geração dos registros D100 e filhos no SPEDFISCAL com os movimentos de CTE](https://tdn.totvs.com/pages/viewpage.action?pageId=696687353)

**28**- Ponto de Entrada **SPDPISIC** utilizado para geração do Registro A110 e/ou Registro C110 de forma alternativa as regras existentes no parâmetro **MV\_SPDIFC**, automaticamente será gerado um registro 0450 referente ao código de Informação Complementar utilizado e para a geração do TXT\_COMPL do 0450 será considerado o conteúdo do campo CEE\_ utilizado 

* [PE - SPDPISIC - SPEDFISCAL - Informações complementares registro C110.](https://tdn.totvs.com/pages/viewpage.action?pageId=706917404)

**29**- Ponto de Entrada **SPDIMP** utilizado para processamento do registro C120.  
Será utilizado nos casos em que o usuário não possui integração com SIGAEIC e não utiliza tabela CD5 (Complemento de Importação).

* [PE - SPDIMP - Complemento de Importação para SPED](https://tdn.totvs.com/pages/viewpage.action?pageId=642844654)

**30** - Ponto de entrada **SPDFIS02** - Este ponto de entrada permite alternar a unidade de medida e respetiva quantidade do item no documento.

Por padrão é assumida sempre a primeira unidade de medida e a primeira quantidade (cadastradas na tabela SB1). No entanto, alguns registros do **SPED FISCAL** permitem a apresentação utilizando uma unidade de medida diferente daquela definida como unidade de estoque. Para utilizar a segunda unidade de medida e a segunda quantidade, é preciso realizar o tratamento utilizando este ponto de entrada.

Os seguintes registros/campos possuem suporte para a utilização do ponto de entrada **SPDFIS02**:

**0190**  
**0220**  
**C170**  
**C425**  
**G140**  
**H010**  
**K200**

<https://tdn.totvs.com/display/public/PROT/PE+-+SPDFIS02+-+Unidade+de+medida+e+quantidade+do+item+do+documento>
