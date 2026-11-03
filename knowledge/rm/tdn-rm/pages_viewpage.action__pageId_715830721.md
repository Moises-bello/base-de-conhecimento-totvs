---
content_hash: 6b5a247adcb0acff4b061c3772133e1ab3e51e36a7b1cc32c77f6f8c87af1b34
fetched_at: '2026-06-29T00:11:26.238633+00:00'
page_id: '715830721'
product: rm
source: tdn-rm
title: R-2055 - Comercialização da Produção por Produtor Rural PJ/Agroindústria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715830721
version: 20
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>#f5f5f5#363636noneR-2055

## **Conteúdo**



## **01. Regras****1**

### Regras Específicas

* Para geração desse evento devem ser selecionados os lançamentos fiscais de entrada que possuem o Tributo Funrural informado.
* O Evento deve agrupar todos os lançamentos do período por filial.
* Este evento vai ser agrupado por Cliente\Fornecedor
* Para lançamento fiscal com Tipo Emitente igual a Filial Será considerado o Cliente\Fornecedor Origem\Destino parametrizado
* Não será considerado no evento lançamento fiscal com Cliente\Fornecedor **sem** a informação de **CPF\CNPJ** obrigatório para autorização do evento REINF
* O campo "Produtor Rural" dentro de *Filial | Dados Adicionais* deve ser selecionado.
* O campo "Forma de tributação da Contribuição previdenciária sobre a folha de pagamento" dentro de *Filial | Anexos | Dados Fiscais* deve ser selecionado.

### Regras Gerais

## **02. Parametrização2**

Segue abaixo passo a passo para geração do Evento R-2055.

Passos para geração do evento R-2055

**1 -** Versão parametrizada ser 1.5.01 ou superior se houver:

Imagem

**2 -** Cliente Fornecedor parametrizado como Produtor Rural, no cadastro do Cliente Fornecedor na pasta *Outros* acesse *Tributos* e marque a opção *Produtor Rural* . Caso seja Pessoa Jurídica (CNPJ), a flag "Entidade executora do Programa de Aquisição de Alimentos" deve estar marcada.

Imagem

**3 -** No item do lançamento de Entrada em Outros Tributos deve ser informado o tributo Funrural:

Imagem

**4 -** A tag *<indAquis>* será gerada de acordo com o parâmetros *Entidade executora do Programa de Aquisição de Alimentos - PAA* localizado no cadastro do Cliente\Fornecedor pasta *Tributos*, o código gerado na tag *<indAquis>* gera de acordo com a marcação ou não desse parâmetro, para verificar as regras de geração o manual pode ser consultado.

ImagemImagem

**5 -** Caso o Lançamento de Entrada possua tributo discutido informado na Situação Tributária será gerado o grupo <infoProcJud>

Imagem

**6 -** A geração de evento R2055 passa a verificar este novo campo “Forma de tributação da Contribuição previdenciária sobre a folha de pagamento”. Se o Campo estiver desabilitado, o Campo 22 – indOpcCP- ideProdutor do Registro não será gerado no xml. Se mesmo estiver habilitado, o Campo 22 – indOpcCP- ideProdutor do Registro será gerado com a Letra “S” no xml.

Se o campo "Produtor Rural" for selecionado e salvo conforme a imagem abaixo:

*Filial | Dados Adicionais*

Imagem

E também o campo "Forma de tributação da Contribuição previdenciária sobre a folha de pagamento" for selecionado:

*Filial | Anexos | Dados Fiscais*

Imagem

 Então será gerado uma nova tag no Xml de Envio:

**`<``indOpcCP``>S</``indOpcCP``>`**

Caso contrário a tag não será gerada.

**NOTA**

Conforme Legislação CAT 45 21/08/2008, os Produtores Rurais do Estado de SP podem ter o CNPJ para a Emissão da NFe e para a REINF pode ser utilizado o CPF.

Será utilizado o campo **CPF** criado para o **eSocial** - No cadastro do Cliente\Fornecedor – Anexo – eSocial – CPF

Este campo somente é habilitado para o Estado SP – Categoria igual a Pessoa Física – CNPJ e Produtor Rural.

ImagemImagem

Se o Cliente\Fornecedor for Pessoa Física, com CNPJ e Produtor Rural, a Tag **tpInscAdq** , deve ser gerada igual a **‘2 – CPF’**

A Tag **tpInscProd** deve ser gerada com o **CPF** informado no cadastro do Cliente\Fornecedor – Anexo – eSocial – CFP **(PESOCIALCLIFOR.CPF)**

## **03. Exemplo****3**

xmlExemplo R-2055


{...}
{...}


...
S
...
]]>ideContri

Utiliza um grupo **ideEstabAdquir** especifico para este tipo

## **04. Origem dos Dados****4**

Dados1evtAqProdevtAqProd

| Elemento | Elemento Pai | Ele | Nível | Descrição | Ocorrência | Elemento Chave | Origem RM |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ideEvento** | **evtAqProd** | **G** | **3** | **Informações de identificação do evento** | **1-1** |  |  |
| **ideContri** | **evtAqProd** | **G** | **3** | **Informações de identificação do contribuinte** | **1-1** | **tpInsc, nrInsc** |  |
| **infoAquisProd** | **evtAqProd** | **G** | **3** | **Informações da aquisição de produção** | **1-1** |  |  |
| **ideEstabAdquir** | **infoAquisProd** | **G** | **4** | **Identificação do estabelecimento adquirente da** **produção** | **1-1** | **tpInscAdq, nrInscAdq** |  |
| **ideProdutor** | **ideEstabAdquir** | **G** | **5** | **Identificação do produtor rural** | **1-1** | **tpInscProd, nrInscProd** |  |
| **detAquis** | **ideProdutor** | **G** | **6** | **Detalhamento da aquisição de produção rural** | **1-6** | **indAquis** |  |

evtAqProddetAquis

| Elemento | Elemento Pai | Ele | Descrição | Ocorrência | Origem RM |
| --- | --- | --- | --- | --- | --- |
| **detAquis** | **ideProdutor** | **G** | **Detalhamento da aquisição de produção rural** | **1-6** |  |
| vlrBruto | detAquis | E | Informação de processo judicial do produtor rural | 1-1 | Valor Bruto do Item do Lançamento Fiscal (DITEM.VALORMERC) |
| **infoProcJud** | **detAquis** | **G** | **Informação de processo judicial do produtor rural** | **0-50** |  |

ideEventoideEventoideContriideContriideEstabAdquir

| Elemento do XML | Origem |
| --- | --- |
| indAquis | Será gerado de acordo com os parâmetros *Entidade executora do Programa de Aquisição de Alimentos - PAA* localizado no cadastro do Cliente\Fornecedor pasta *Tributos*, o código gerado na tag *<indAquis>* gera de acordo com a marcação ou não desse parâmetro, para verificar as regras de geração o manual pode ser consultado. |
| vlrBruto | Valor bruto do tributo Funrural informado em Outros Tributos no item do Lançamento de Entrada. |
| vlrCPDescPR | Se indOpcCP **for** "S": Campo estará com valor fixo 0; Se indOpcCP **não** for gerado: Campo conterá o valor Lançamento Fiscal – Outros Tributos do Item – Funrural \**Valor Retenção**. |
| vlrRatDescPR | Se indOpcCP **for** "S": Campo estará com valor fixo 0; Se indOpcCP **não** for gerado: Campo conterá o valor Lançamento Fiscal – Outros Tributos do Item – Funrural \**Campo Giralt**. |
| VlrSenarDesc | Se indOpcCP **for** "S": Lançamento Fiscal – Outros Tributos do Item; Se indOpcCP **não** for gerado: Campo conterá o valor Lançamento Fiscal – Outros Tributos do Item – Funrural \**Campo Senar**. |
| indOpcCP | A geração de evento R2055 verifica este novo campo Cadastro do Cli\For - Anexo eSocial   “**Indicativo da Opção pelo produtor rural pela forma de tributação da contribuição previdenciária**”.  **1 - Sobre a Comercialização da sua produção.**  Informar [S] caso a opção do produtor rural em relação à forma de tributação da contribuição previdenciária seja sobre a folha de pagamento.  Então a Tag **<indOpcCP>** **não deve** ser gerada.            {vlrBruto} com o valor bruto do Lançamento Fiscal;            {vlrCPDescPR} com o valor real informado no Lançamento Fiscal;            {vlrRatDescPR} com o valor real informado no Lançamento Fiscal;           {vlrSenarDesc} com o valor real informado no Lançamento Fiscal.    **2 - Sobre a Folha de Pagamento.**  Então a Tag **<indOpcCP> S</indOpcCP> deve** ser gerada**.**            {vlrBruto} com o valor bruto do Lançamento Fiscal;            {vlrCPDescPR} com valor zero;            {vlrRatDescPR} com valor zero;            {vlrSenarDesc} com o valor real informado no Item do Lançamento Fiscal\Outros Tributos. |
