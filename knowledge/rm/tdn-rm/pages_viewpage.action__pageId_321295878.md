---
content_hash: 012a94d0a62e840355d3e458a7723595ac6940e924ae825073fa2a05c32b00f8
fetched_at: '2026-06-29T00:08:47.973919+00:00'
page_id: '321295878'
product: rm
source: tdn-rm
title: FISCAL01-163 NF-e - Layout 4.00 - Nota Técnica 2016.002
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=321295878
version: 194
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Nota Fiscal Eletrônica (NF-e) - Nota Técnica 2016.002 - Layout 4.00

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Linha do Produto** | RM | | |
| **Seguimento** | BackOffice | | |
| **Módulo** | Nota Fiscal Eletrônica | | |
| **Chamado/Ticket²** | FISCAL01-163 | | |
| **Subtarefa¹** | FISCAL01-2407 | | |
| **País** | Brasil | | |
| **Banco(s) de Dado(s)** | Oracle e SQL | | |
| **Versão Disponível** | 12.1.18.147  12.1.19.108   * Todas as versões superiores citadas acima. | | |
| **Versão do TSS** | 12.1.17 e 3.0 | | |
| **TOTVS Colaboração** | 2.0 | | |

IMPORTANTE

Para a criação dos novos campos que atende a implementação da NF-e 4.0, faz-se necessário a execução do script disponível no Atualizador.   
Passo a passo da execução do script pela nova ferramenta disponível no link: <http://tdn.totvs.com/pages/viewpage.action?pageId=322143046>  
Após atualização é necessária a seleção da versão atual do layout nos parâmetros da NF-e acesse:  
Ambiente | Parâmetros | Gestão de Estoque Compra e Faturamento | 04.03 - Integrações | 04.03.03 - Fical | 04.03.03.01 - Dados Fiscais | Parâmetros por Filial | Editar a Filial | Conexão NF-e.

# Objetivo

A nova versão da**[NF-e 4.0](http://sped.rfb.gov.br/pagina/show/2131)** teve mudanças de *layout*, com a inclusão de novos campos e validações. Todos os detalhes dessas alterações estão na **[Nota Técnica 2016.002 – v 1.40](file:///C:/Users/sheila.gastaldi.BH01/Desktop/NT_2016_002_v1.40.pdf).**As alterações que normalmente acontecem no leiaute da Nota Fiscal Eletrônica tem como objetivo tornar esse processo mais padronizado, aumentando a segurança e o controle do fisco sobre a circulação de mercadorias. Além disso, novos modelos como a versão da NF-e 4.0, pretendem favorecer a redução da manutenção nos sistemas de emissão de NF-e para as empresas e para as SEFAZ.

Sobre as Alterações do Layout (versão 4.0)

A seguir serão listadas as alterações e demonstrado a utilização dos campos no sistema.

Aviso

Informamos que em algumas UF 's podem apresentar erro de validação no envio da NF-e, visto que alguns estados ainda não se adequaram as novas implementações.

Neste caso será apresentanda a mensagem:

Consultar autorização: NF-e foi rejeitada. Erro: Rejeicao: Falha no Schema XML do lote de NFe  
999 - /. Retorno inexperado, entre em contato com a Totvs.

* **Grupo B - Identificação da Nota Fiscal Eletrônica**

Na Tag Indicador de presença “indPres” (id: B25b) foi incluída a opção **5 - Operação Presencial, fora do estabelecimento**, utilizada no caso de venda ambulante.

Em relação ao indicador de presença, foi incluída a opção "Fora do Estabelecimento" conforme alteração da tag **indPres** do novo layout. Opção geralmente utilizada em operações efetuadas por ambulante.

* **Grupo BA - Documento Fiscal****Referenciado**

Inclusão do código modelo de documento 2-Nota Fiscal de Venda atendendo o preenchimento da tag **refNF**, quando se tratar de movimento referenciado.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| 29x.3 | BA03 | refNF | Informação da NF modelo 1/1A ou NF modelo 2 referenciada | CG | BA01 |  | 1-1 |  |  |
| 29x.7 | BA07 | mod | Modelo do Documento Fiscal | E | BA03 | N | 1-1 | 2 | 01=modelo 01  02=modelo 02 |

* **Grupo I80 - Rastreabilidade de produto**

Criação de novo grupo para permitir a rastreabilidade de qualquer produto sujeito a regulações sanitárias, casos de recolhimento/recall, além de defensivos agrícolas, produtos veterinários, odontológicos, medicamentos, bebidas, águas envasadas, embalagens, etc., a partir da indicação de informações de número de lote, data de fabricação/produção, data de validade, etc. Obrigatório o preenchimento deste grupo no caso de medicamentos e produtos farmacêuticos.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| 128q | I80 | rastro | Detalhamento de produto sujeito a rastreabilidade | G | I01 |  | 1-500 |  | Informar apenas quando se tratar de produto a ser rastreado posteriormente |
| 128r | I81 | nLote | Número do Lote do produto | E | I80 | C | 1-1 | 1-20 |  |
| 128s | I82 | qLote | Quantidade de produto no Lote | E | I80 | N | 1-1 | 8v3 |  |
| 128t | I83 | dFab | Data de fabricação/ Produção | E | I80 | D | 1-1 |  | Formato: “AAAA-MM-DD” |
| 128u | I84 | dVal | Data de validade | E | I80 | D | 1-1 |  | Formato: “AAAA-MM-DD”  Informar o último dia do mês caso a validade não especifique o dia. |
| 128v | I85 | cAgre | Código de Agregação | E | I80 | N | 0-1 | 1-20 |  |

As tags serão preenchidas de acordo com os dados informados no Lote do Produto criado em Anexos | Lotes do Produto no cadastro do produto.

Também é necessário marcar a flag abaixo para geração do grupo de rastreabilidade:

Cadastro do Produto | Anexos | Dados Fiscais do Produto | Aba Tributação

* **Grupo O - Imposto sobre Produtos Industrializados**

Excluído o campo Classe de enquadramento do IPI

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** |  | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| ~~247~~ | ~~O02~~ |  | ~~clEnq~~ | ~~Classe de enquadramento do IPI para Cigarros e Bebidas~~ | ~~E~~ | ~~O01~~ | ~~C~~ | ~~0-1~~ | ~~1-5~~ | ~~Exclusão do Campo clEnq (id:O02) “Classe de enquadramento do IPI para Cigarros e Bebidas”,~~ |

A tag "cEnq" Código de Enquadramento Legal do IPI atualmente é preenchida de acordo com valor preenchido na linha do tributo no item do movimento.

* **Grupo I - Produtos e Serviços da NF-e**

Criado novos campos para informar se o produto foi fabricado em escala relevante ou não, conforme [Cláusula 23 do Convênio ICMS 52/2017](https://www.confaz.fazenda.gov.br/legislacao/convenios/2017/CV052_17) e, em caso de produção em escala NÃO relevante, o campo CNPJ do Fabricante deve ser informado.

1. Tag **indEscala**

| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104e | I05d | indEscala | Indicador de Escala  Relevante | E | I05b | C | 0-1 | 1 | Indicador de Produção em escala relevante, conforme Cláusula 23 do Convenio ICMS 52/2017:  S -  Produzido em Escala Relevante;  N – Produzido em Escala NÃO Relevante.  Nota: preenchimento obrigatório para produtos com [NCM relacionado no Anexo XXVII do Convenio 52/2017](https://www.confaz.fazenda.gov.br/legislacao/convenios/2017/CV052_17) |

Para atender o preenchimento da tag indEscala - Indicador de Escala Relevante, foi criado o campo Indicador de Produção em escala relevante no cadastro do produto na aba Detalhes sub-aba Outros Dados.

2. Tag **CNPJFab**

| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104f | I05e | CNPJFab. | CNPJ do Fabricante da Mercadoria | E | I05b | N | 0-1 | 14 | CNPJ do Fabricante da Mercadoria, obrigatório para produto em escala NÃO relevante. |

Considerado o CNPJ informado no cadastro do fabricante vinculado ao cadastro do produto.

3. Tag **cBenef**

| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104g | I05f | cBenef | Código de Benefício Fiscal na UF aplicado ao item | E | I01 | C | 0-1 | 10 | Código de benefício Fiscal utilizado pela UF, aplicado ao item.  *Observação*: Deve ser utilizado o mesmo código adotado na EFD e Outras declarações, na UF que exigem |

Para emissão da tag cBenef, iremos considerar a seguinte sequencia de campos para buscar a informação:

1. Itens do Movimento - Campo Complementar - CODAJUSTESPED

         2. Gerado de acordo com o Código Fiscal informado nos Anexos do cadastro do produto em Dados Fiscais do Produto por UF | aba Identificação.

* **Grupo K - Detalhamento Específico de Medicamento e de matérias-primas farmacêuticas**

1. Tags excluídas do grupo K

| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ~~153~~ | ~~K02~~ | ~~nLote~~ | ~~Número do Lote de medicamentos ou~~ | ~~E~~ | ~~K01~~ | ~~C~~ | ~~1-1~~ | ~~1-20~~ |  |
| ~~154~~ | ~~K03~~ | ~~qLote~~ | ~~Quantidade de produto no Lote de medicamentos ou de matérias-primas farmacêuticas~~ | ~~E~~ | ~~K01~~ | ~~N~~ | ~~1-1~~ | ~~8v3~~ |  |
| ~~155~~ | ~~K04~~ | ~~dFab~~ | ~~Data de fabricação~~ | ~~E~~ | ~~K01~~ | ~~D~~ | ~~1-1~~ |  | ~~Formato: “AAAA-MM-DD”~~ |
| ~~156~~ | ~~K05~~ | ~~dVal~~ | ~~Data de validade~~ | ~~E~~ | ~~K01~~ | ~~D~~ | ~~1-1~~ |  | ~~Formato: “AAAA-MM-DD”~~ |

2. Tag **cProdANVISA**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| 152a | K01a | cProdANVISA | Código de Produto da ANVISA | E | K01 | C | 1-1 | 13 | Utilizar o número do registro do produto da Câmara de Regulação do Mercado de Medicamento – CMED |

Gerada de acordo com os dados do campo Registro da ANVISA informado no cadastro do produto em Anexos | Informações - TOTVS Saúde.

Nota

Tag obrigatória para todos os produtos farmacêuticos. Para o preenchimento será validado o código NCM dentro do grupo de medicamentos (3003 e 3004).

Caso não possuir integração com o RM Saúde , no envio da NF-e, a tag cProdANVISA poderá ser preenchida com os dados do campo Registro Anvisa informado

no produto (TPRODUTODEF) caso não estiver sido preenchido no Anexo do produto Informações - Totvs Saúde.

Observação: Necessário executar script do atualizador com o nome: NF-e 4.0 Anvisa e GLP

* **Grupo LA - Item / Combustível**

1. Exclusão da tag **pMixGN**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| ~~162b1~~ | ~~LA03~~ | ~~pMixGN~~ | ~~Percentual de Gás Natural para o produto GLP (cProdANP=210203001)~~ | ~~E~~ | ~~LA01~~ | ~~N~~ | ~~0-1~~ | ~~2v4~~ |  |

2. Criação de campo para os percentuais de mistura do **GLP.**

| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 162b1 | LA03 | descANP | Descrição do produto conforme ANP | E | LA01 | N | 1-1 | 2-95 | Utilizar a descrição de produtos do Sistema de Informações de Movimentação de Produtos - SIMP (<http://www.anp.gov.br/simp/>). |
| 162b2 | LA03a | pGLP | Percentual do GLP derivado do petróleo no produto GLP (cProdANP=210203001) | E | LA01 | N | 0-1 | 3v4 | Informar em número decimal o percentual do GLP derivado de petróleo no produto GLP. Valores de 0 a 100. |
| 162b3 | LA03b | pGNn | Percentual de Gás Natural Nacional – GLGNn para o produto GLP (cProdANP=210203001) | E | LA01 | N | 0-1 | 3v4 | Informar em número decimal o percentual do Gás Natural Nacional – GLGNn para o produto GLP. Valores de 0 a 100. |
| 162b4 | LA03c | pGNi | Percentual de Gás Natural Importado – GLGNi para o produto GLP (cProdANP=210203001) | E | LA01 | N | 0-1 | 3v4 | Informar em número decimal o percentual do Gás Natural Importado – GLGNi para o produto GLP. Valores de 0 a 100. |
| 162b5 | LA03d | vPart | Valor de partida (cProdANP=210203001) | E | LA01 | N | 0-1 | 13v2 | Deve ser informado neste campo o valor por quilograma sem ICMS. |

Para geração da tag "descANP"  é necessário o preenchimento do campo abaixo:

Foram implementadas as Tags do Grupo LA. Item / Combustível: pGLP, pGNn, pGNi e vPart conforme NT2016.002. Observação: Estas tags serão geradas no xml da NF-e apenas se código ANP

do produto for igual a "210203001".

* **Grupo N - ICMS Normal e ST**

Incluídas tags para identificar o valor devido em decorrência do percentual de ICMS relativo ao Fundo de Combate à Pobreza.

1. Grupo Tributação do **ICMS= 00**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| 171.1 | N17b | pFCP | Percentual do ICMS relativo ao Fundo de Combate à Pobreza (FCP) | E | N02 | N | 0-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP).  Nota: Percentual máximo de 2%, conforme a legislação. |
| 171.2 | N17c | vFCP | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) | E | N02 | N | 0-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP). |

2. Grupo Tributação do **ICMS= 10, 20, 51, 70 e 90**

| **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vBCFCP | Valor da Base de Cálculo do FCP | E | N09 | N | 0-1 | 13v2 | Valor da Base de Cálculo do FCP Retido |
| pFCP | Percentual do FCP | E | N03 | N | 0-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP)  Nota: Percentual máximo de 2%, conforme a legislação. |
| vFCP | Valor do FCP | E | N03 | N | 0-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) |

3. Grupo Tributação do **ICMS= 10, 30, 70 e 90**

| **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vBCFCPST | Valor da Base de Cálculo do FCP Retido Por Subtituição Tributária | E | N09 | N | 0-1 | 13v2 | Valor da Base de Cálculo do FCP Retido Por Subtituição Tributária |
| pFCPST | Percentual do FCP retido por Substituição Tributária | E | N03 | N | 0-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária.  Nota: Percentual máximo de 2%, conforme a legislação. |
| vFCPST | Valor do FCP retido por Substituição Tributária | E | N03 | N | 0-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária. |

4. Grupo Tributação do **ICMS= 60**

| **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vBCFCPST | Valor da Base de Cálculo do FCP retido anteriormente | E | N25.1 | N | 0-1 | 13v2 | Informar o valor da Base de Cálculo do FCP retido anteriormente por ST |
| pFCPSTRet | Percentual do FCP retido anteriormente por Substituição Tributária | E | N25.1 | N | 0-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária.  Nota: Percentual máximo de 2%, conforme a legislação. |
| vFCPSTRet | Valor do FCP retido por Substituição Tributária | E | N25.1 | N | 0-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária. |
| pST | Alíquota suportada pelo Consumidor Final | E | N25.1 | N | 0-1 | 3v2-4 | Deve ser informada a alíquota do cálculo do ICMS-ST, já incluso o FCP. Exemplo: alíquota da mercadoria na venda ao consumidor final = 18% e 2% de FCP. A alíquota a ser informada no campo pST deve ser 20%. |

Grupo opcional para informações do **ICMS Efetivo**:

| **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pRedBCEfet | Percentual de redução da base de cálculo efetiva | E | N33 | N | 1-1 | 3v2-4 | Percentual de redução, caso estivesse submetida ao regime comum de tributação, para obtenção da base de cálculo efetiva (vBCEfet).  Obs.: opcional a critério da UF. |
| vBCEfet | Valor da base de cálculo efetiva | E | N33 | N | 1-1 | 13v2 | Valor da base de cálculo que seria atribuída à operação própria do contribuinte substituído, caso estivesse submetida ao regime comum de tributação, obtida pelo produto do Vprod por (1- pRedBCEfet).  Obs.: opcional a critério da UF |
| pICMSEfet | Alíquota do ICMS efetiva | E | N33 | N | 1-1 | 3v2-4 | Alíquota do ICMS na operação a consumidor final, caso estivesse submetida ao regime comum de tributação.  Obs.: opcional a critério da UF |
| vICMSEfet | Valor do ICMS efetivo | E | N33 | N | 1-1 | 13v2 | Obtido pelo produto do valor do campo pICMSEfet pelo valor do campo vBCEfet, caso estivesse submetida ao regime comum de tributação. Obs.: opcional a critério da UF. |

O Grupo do opcional do **ICMS60** referente ao Valor efetivo do ICMS será gerado conforme abaixo:

**pRedBCEfet**: Será gerado com os dados do Anexo “Dados Fiscais por UF”, considerando a UF da Filial emitente.

2**. vBCEfet**: Calculado = **Vprod** - **pRedBCEfet**

3. **pICMSEfet**: Alíquota do ICMS informada nos “Dados Fiscais por UF”, considerando a UF da Filial emitente.

4. **vICMSEfet**: Calculado = **vBCEfet** \* **pICMSEfet**

* Grupo de Repasse do **ICMS ST**

Incluída nova opção para Tributação de ICMS 60\_Cobrado Anteriormente por Substituição Tributária

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| 245.19 | N12 | CST | Tributação do ICMS | E | N10b | N | 1-1 | 2 | 41=Não Tributado (v2.0)  60= cobrado anteriormente por substituição tributária |

1. Grupo **CRT = 1 e CSOSN 201, 202, 203 e 900**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| vBCFCPST | Valor da Base de Cálculo do FCP | E | N10e | N | 0-1 | 13v2 | Informar o valor da Base de Cálculo do FCP |
| pFCPST | Percentual do FCP retido por Substituição Tributária | E | N10e | N | 0-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária.  Nota: Percentual máximo de 2%, conforme a legislação. |
| vFCPST | Valor do FCP retido por Substituição Tributária | E | N10e | N | 0-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária. |

2. Grupo **CRT = 1 e CSOSN 500**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| 245.51w | N27a | vBCFCPSTRet | Valor da Base de Cálculo do FCP retido anteriormente por ST | E | N25.1 | N | 0-1 | 13v2 | Informar o valor da Base de Cálculo do FCP retido anteriormente por ST |
| 245.51x | N27b | pFCPSTRet | Percentual do FCP retido anteriormente por Substituição Tributária | E | N25.1 | N | 0-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP).  Nota: Percentual máximo de 2%, conforme a legislação. |
| 245.51y | N27d | vFCPSTRet | Valor do FCP retido anteriormente por Substituição Tributária | E | N25.1 | N | 0-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária. |
| 245.51z | N27e | pST | Alíquota suportada pelo Consumidor Final | E | N25.1 | N | 0-1 | 3v2-4 | Deve ser informada a alíquota do cálculo do ICMS-ST, já incluso o FCP. Exemplo: alíquota da mercadoria na venda ao consumidor final = 18% e 2% de FCP. A alíquota a ser informada no campo pST deve ser 20%. |

Foram criados dois novos campos na Regra de ICMS para identificar se a operação terá a incidência ou não do FCP, tanto para o ICMS como para o ICMS ST.

ICMS:

ICMS ST:

Na geração da NF-e foi alterado a geração das tags:

* vBCFCP - Valor da Base de Cálculo do FCP
* pFCP - Percentual do Fundo de Combate à Pobreza (FCP)
* vFCP - Valor do Fundo de Combate à Pobreza (FCP)
* vBCFCPST - Valor da Base de Cálculo do FCP retido por Substituição Tributária
* pFCPST - Percentual do FCP retido por Substituição Tributária
* vFCPST - Valor do FCP retido por Substituição Tributária

As tags acima só serão geradas se os respectivos campos estiverem marcados na Regra de ICMS.

Geração da Tag**vFCPST = (vBCFCPST \* (pFCPST/100)) - vFCP;**

**1 - Observação**: Neste caso a alíquota dos Tributos ICMS e ICMS ST foram majoradas em 2% referentes ao FCP na Natureza de Operação e as mesmas são reduzidas em 2% nos devidos campos no XML da NF-e

Então quando utilizar FCP ou FCP-ST a alíquota dos tributos ICMS e ICMS-ST devem ser majoradas conforme alíquota do FCP vigente e ainda será **OBRIGATÓRIO** informar a alíquota do FCP no Dados Fiscais por UF no cadastro do Produto.

Exemplo:

Movimento | Item de movimento | Tributos e Valores | Tributos

No exemplo acima, a alíquota de ICMS para o estado utilizado é de 12% e a do ICMS ST é de 18% sendo necessário majorar a alíquota adicionando 2% de FECP para ICMS e ICMS ST.

Na geração do XML o sistema irá subtrair o valor das alíquotas retirando o 2% do FECP:

<ICMS10>

<orig>0</orig>

<CST>10</CST>

<modBC>0</modBC>

<vBC>100.00</vBC>

**<pICMS>12.00</pICMS> → Alíquota gerada com 12% já subtraído o valor de 2% do FECP.**

<vICMS>12.00</vICMS>

<vBCFCP>100.00</vBCFCP>

<pFCP>2.00</pFCP>

<vFCP>2.00</vFCP>

<modBCST>0</modBCST>

<pRedBCST>0.00</pRedBCST>

<vBCST>100.00</vBCST>

**<pICMSST>18.00</pICMSST> → Alíquota gerada com 18% já subtraído o valor de 2% do FECP.**

<vICMSST>6.00</vICMSST>

<vBCFCPST>100.00</vBCFCPST>

<pFCPST>2.00</pFCPST>

<vFCPST>0.00</vFCPST>

</ICMS10>

Nota

Documentação das informações necessárias e parametrização para o cálculo do FECP disponível no caminho abaixo:

* [Fundo de Combate a Pobreza e Erradicação da Miséria de Minas Gerais](http://tdn.totvs.com/pages/viewpage.action?pageId=224113860)
* [FECP Incidente sobre ICMS ST](http://tdn.totvs.com/pages/viewpage.action?pageId=269432397)
* [Cálculo do Fundo de Erradicação da Miséria e Combate à Pobreza - MG](http://tdn.totvs.com/pages/viewpage.action?pageId=223905791)

* **Grupo NA - ICMS para a UF de destino**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| 245a.04 | NA04 | vBCFCPUFDest | Valor da BC FCP na UF de destino | E | NA01 | N | 0-1 | 13v2 | Valor da Base de Cálculo do FECP na UF de destino |

* **Grupo W - Total da NF-e**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| 329.02 | W04b | vFCP | Valor Total do FECP (Fundo de Combate à Pobreza) | E | W02 | N | 1-1 | 13v2 | Corresponde ao total da soma dos campos id: N17c |
| 331.01 | W06a | vFCPST | Valor Total do FECP (Fundo de Combate à Pobreza) retido por substituição tributária | E | W02 | N | 1-1 | 13v2 | Corresponde ao total da soma dos campos id:N23d |
| 331.02 | W06b | vFCPSTRet | Valor Total do FECP retido anteriormente por Substituição Tributária | E | W02 | N | 1-1 | 13v2 | Corresponde ao total da soma dos campos id:N27d |
| 337.01 | W12a | vIPIDevol | Valor Total do IPI devolvido | E | W02 | N | 1-1 | 13v2 | Deve ser informado quando preenchido o Grupo Tributos Devolvidos na emissão de nota finNFe=4 (devolução) nas operações com não contribuintes do IPI. Corresponde ao total da soma dos campos id:UA04. |

* **Grupo X. Informações do Transporte da NF-e**

As opções da tag modFrete foram alteradas.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| 357 | X02 | modFrete | Modalidade do frete | E | X01 | N | 1-1 | 1 | 0 = Contratação do Frete por conta do Remetente (CIF);  1 = Contratação do Frete por conta do Destinatário (FOB);  2 = Contratação do Frete por conta de Terceiros;  3 = Transporte Próprio por conta do Remetente;  4 = Transporte Próprio por conta do Destinatário;  9 = Sem Ocorrência de Transporte. |

Selecionado na aba Transportes | Identificação do movimento.

* **ZX. Informações Suplementares da Nota Fiscal**

Criação de novo campo com o objetivo de padronizar a URL de consulta por chave de acesso que aparece no DANFE NFC-e.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| 426 | ZX03 | urlChave | Texto  com  a  URL  de  consulta  por chave de acesso a ser impressa no DANFE NFC-e. | E | ZX01 | C | 1-1 | 21-85 | Informar a URL da “Consulta por chave de acesso da NFC-e”. A mesma URL que deve estar  informada  no  DANFE  NFC-e  para consulta por chave de acesso |

* **Grupo YA. Informação de Pagamento**

1. Foi realizado a inclusão da TAG **indPag** (id:YA01b) no **Grupo YA**conforme regra abaixo:  
   **Se** financeiro for gerado por condição de pagamentos **Ou**parcelamento

**então**

**Se** tem apenas uma parcela **E** a data de emissão **<=** (menor ou igual) a data vencimento

**então** 0 - Pagamento à Vista

**Senão** 1 - Pagamento à Prazo

**Se** financeiro for gerado por meio de pagamento

**então**

**Se** a data de emissão **<=**(menor ou igual) a data vencimento

**então** 0 - Pagamento à Vista

**Senão** 1 - Pagamento à Prazo

2. Foi modificado a geração da TAG **tPag**(id:YA02) no **Grupo YA**conforme regra abaixo:

**Se** NF-e foi emitida com tag **finNFe**= (3 - Ajuste ou 4 - Devolução)

 **então** 90 - Sem Pagamento

**Se** movimento**não** tem financeiro gerado

**então**90 - Sem Pagamento

**Se** financeiro for gerado por **condição de pagamentos** Ou **parcelamento**

**então**99 - Outros

**Se** financeiro for gerado por meio de pagamento

**então**Será gerado com o meio de pagamento informado por parcela.

Caso EXISTA Meio de Pagamento selecionado, o sistema irá considerar o Tipo Primitivo do mesmo;

De/Para da geração no XML:

|  |  |
| --- | --- |
| Tipo primitivo | Enumerado NF-e |
| Dinheiro | 01=Dinheiro |
| Cheque | 02=Cheque |
| Cartão | 03=Cartão de Crédito |
| Outros | 99=Outros |
| Cartão de débito | 04=Cartão de Débito |
| Parcelado | 99=Outros |
| Vale | 99=Outros |
| Vale Alimentação | 10=Vale Alimentação |
| Vale Refeição | 11=Vale Refeição |
| Vale Presente | 12=Vale Presente |
| Vale combustível | 13=Vale Combustível |
| Tipo Boleto bancário | 15=Boleto Bancário |
| Sem Pagamento | 90= Sem pagamento |
| Duplicata Mercantil | 99=Outros |

3. Foi implementado a geração dos grupos de cobrança 

Grupo Fatura

* **Número da Fatura (nFat):** Gerado pelo número do movimento.
* **Valor Original da Fatura (vOrig):**A soma do valor líquido dos lançamentos financeiros.
* **Valor de desconto (vDesc):** Será gerado sempre com o valor zero.
* **Valor Líquido da Fatura (vLiq):**A soma do valor líquido dos lançamentos financeiros.

Grupo Parcelas

* **Número da Parcela (ndup):** Passou a ser gerado com valor fixo, sequencial a partir do 001. Ex: 001, 002, 003
* **Data de vencimento (dVenc):** Data de vencimento do lançamento financeiro.
* **Valor da Parcela (vDup):** Valor líquido do lançamento financeiro.

Aviso

Pedimos para este processo a não utilização dos campos de valores opcionais na fórmula de Valor a Ratear , visto que a geração de valores opcionais que por sua natureza, podem ter inúmeras finalidades de acordo com a regra de negócio utilizada pelo cliente, sendo de difícil previsão a tratativa efetuada para geração destes valores.

É importante relembrar que o comportamento foi elaborado com base nas regras de validação da Sefaz, o que limita o nosso poder de atuação.

4. Tags que não são geradas pelo sistema.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| 398d | YA04 | card | Grupo de Cartões | G | YA01a |  | 0-1 |  |  |
| 398d.1 | YA04a | tpIntegra | Tipo de Integração para pagamento | E | YA04 | N | 1-1 | 1 | Tipo de Integração do processo de pagamento com o sistema de automação da empresa:  1=Pagamento integrado com o sistema de automação da empresa (Ex.: equipamento TEF, Comércio Eletrônico);  2= Pagamento não integrado com o sistema de automação da empresa (Ex.: equipamento POS); |
| 398e | YA05 | CNPJ | CNPJ da Credenciadora de cartão de crédito e/ou débito | E | YA04 | C | 0-1 | 14 | Informar o CNPJ da Credenciadora de cartão de crédito / débito |
| 398f | YA06 | tBand | Bandeira da operadora de cartão de crédito e/ou débito | E | YA04 | N | 0-1 | 2 | 01=Visa  02=Mastercard  03=American Express  04=Sorocred  05=Diners Club  06=Elo  07=Hipercard  08=Aura  09=Cabal  99=Outros |
| 398g | YA07 | cAut | Número de autorização da operação cartão de crédito e/ou débito | E | YA04 | C | 0-1 | 1-20 | Identifica o número da autorização da transação da operação com cartão de crédito e/ou débito |

5. Tag **vTroco** Valor do Troco.

| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 398i | YA09 | vTroco | Valor do troco | E | YA01 | N | 0-1 | 13V2 | Valor do Troco |

Até o momento a tag não é gerada.

* **Grupo I. Produtos e Serviços da NF-e**

Atualmente os ajustes [SINIEF 07/05](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/aj_007_05) e [SINIEF 19/16](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2016/aj_019_16),  obrigam o preenchimento dos campos **cEAN** e **cEANTrib** na **NF-e** e **NFC-e.** Quando o produto comercializado possuir código de barras será gerado o **GTIN.** Quando não houver código de barras informado, a tag será gerada como defaul com o texto: “**SEM GTIN**”. Destacamos que para as notas emitidas em homologação a NF-e gera a informação **"SEM GTIN"** conforme regras abaixo e em produção a alteração terá efeito somente a partir de 01/12/2018 conforme NT 2017.001 v 1.30 regra de validação I03-30 mensagem 883.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocor.** | **Tam.** | **Observação** |
| 102 | I03 | cEAN | GTIN (Global Trade Item Number) do produto, antigo código EAN ou código de barras | E | I01 | C | 1-1 | 0,8,12, 13, 14 | Preencher com o código GTIN-8, GTIN-12, GTIN-13 ou GTIN-14 (antigos códigos EAN, UPC e DUN-14).  **Para produtos que não possuem código de barras com GTIN, deve ser informado o literal “SEM GTIN”;**  Nos demais casos, preencher com GTIN contido na embalagem com código de barras ATENÇÃONo processo de geração da NF-e as TAG cEAN e cEANTrib serão preenchidas com a literal **"SEM GTIN"** automaticamente quando não for encontrado um código de barras cadastro no produto. **NÃO** é necessário cadastrar um código de barras com a literal **"SEM GTIN"**. |
| 111 | I12 | cEANTrib | GTIN (Global Trade Item Number) da unidade tributável, antigo código EAN ou código de barras | E | I01 | C | 1-1 | 0,8,12, 13, 14 | Preencher com o código GTIN-8, GTIN-12, GTIN-13 ou GTIN-14 (antigos códigos EAN, UPC e DUN-14) da unidade tributável do produto.  O GTIN Tributário deve corresponder ao GTIN da **menor unidade** comercializada no varejo identificável por código GTIN.  **Para produtos que não possuem código de barras com GTIN, deve ser informado o literal "SEM GTIN”;**  Nos demais casos, preencher com GTIN contido na embalagem com código de barras. ATENÇÃONo processo de geração da NF-e as TAG cEAN e cEANTrib serão preenchidas com a literal **"SEM GTIN"** automaticamente quando não for encontrado um código de barras cadastro no produto. **NÃO** é necessário cadastrar um código de barras com a literal **"SEM GTIN"**. |

Nota

Atualmente no sistema os campos cEAN e cEANTrib passaram a gerar a literal "SEM GTIN" quando o campo estiver vazio.

(em produção a alteração terá efeito somente a partir de 01/12/2018)

* **Demandas referentes as alterações das notas técnicas no sistema**  
    
  **[NT 2016.002 v1.50](http://tdn.totvs.com/pages/viewpage.action?pageId=371626643)**[NT 2016.002 v1.60 e NT2017.001 v1.30](http://tdn.totvs.com/pages/viewpage.action?pageId=382555011)

* **Demandas referente as implementações no TOTVS Gestão de Estoque, Compras e** **F****aturamento**

MATFATCMPCRM01-1206

MATFATCMPCRM01-2138 

MATFATCMPCRM01-2180

**- Observação:** Está parametrização é para ocorrência de FCP sem Diferencial de Alíquota.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
