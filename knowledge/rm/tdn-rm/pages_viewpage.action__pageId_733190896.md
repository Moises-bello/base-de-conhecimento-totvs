---
content_hash: aed783f8813ce862af21aff6d0401ece5845a8544a927c9100f3d844e82f3cde
fetched_at: '2026-06-29T00:11:28.733640+00:00'
page_id: '733190896'
product: rm
source: tdn-rm
title: R-4020 – Pagamentos/créditos a beneficiário pessoa jurídica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=733190896
version: 78
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>#f5f5f5#363636noneR-4020

## **Conteúdo**

**Conteúdo**

## **01. Introdução**

Neste evento deve ser declarado os pagamentos/créditos sobre os pagamentos de serviços de pessoas jurídicas.

## **02. Regras**

### Regras Específicas

* Necessário fazer o Cadastro do Parâmetros de Processos - **EFD REINF**. Para mis informações clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=490650588#1-5)
* É necessário parametrizar o Tributo e a Natureza de Rendimento -  Parâmetros de Processos - **EFD REINF** -Anexo - Filtro de Eventos - Para mais informações clique [aqui](https://tdn.totvs.com/display/LRM/Filtro+de+Eventos)
* **Centralizado**: No cadastro dos [Parâmetros de Processos](https://tdn.totvs.com/pages/viewpage.action?pageId=490650588), pode ser definido se a geração será Centralizada ou Descentralizada.  
  >> Quando estiver habilitado, todos os Lançamentos\Movimentações realizados a uma determinada Pessoa Física\Jurídica, serão gerados em um único arquivo XML a ser transmitido para a EFD-REINF.  
  >> Quando desabilitado, todos os Lançamentos\Movimentações realizados a uma determinada Pessoa Física\Jurídica, serão agrupados em um arquivo XML para cada Filial a ser transmitido para a EFD-REINF.

  Imagem
* Veja a regra para [Valores de Rendimentos Pagos a residentes ou Domiciliados no Exterior](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16960894085783).

### Regras Gerais

## **03. Módulo de Origem dos dados**

OrigemOrigem Gestão FinanceiraOrigem Gestão FinanceiraOrigem Gestão FinanceiraOrigemFinleftRetenção PJRetenção PJRetenção PJ

**Lançamentos e Rendimentos em que houve retenção do IRRF para Fornecedor Pessoa Jurídica:**

* Lançamentos cujo Cli/For seja pessoa jurídica;
* Somente serão selecionados os Lançamentos cujo Tipo de Documento seja “Gerador de IRRF” ou “Gerador de IRRF e INSS”;
* Lançamentos que tenham sido Baixados ou Baixados Parcialmente, no caso de lançamentos que tiveram retenção do imposto. No caso de lançamentos que possuam o Tributo e ainda não houve a retenção, os mesmos devem estar em aberto
* Lançamentos que não estejam cancelados.
* Os lançamentos serão selecionados para a geração do registro se sua Data estiver dentro do período definido no evento R-9015. Esta data é definida em Parâmetros de Processo na etapa "02.01.01.02.02 - IRRF - PJ".

* Imagem
Retenção das Contribuições, cumulatividade ou não retenção PJRetenção das Contribuições, cumulatividade ou não retenção PJRetenção das Contribuições, cumulatividade ou não retenção PJ

**Lançamentos em que houve retenção das Contribuições, cumulatividade do Imposto ou imposto não foi retido para Fornecedor Pessoal Jurídica.**

* Lançamentos cujo Cli/For seja pessoa jurídica;
* Lançamentos Baixados ou Baixados Parcialmente;
* Lançamentos que não estejam cancelados;
* Lançamentos que não foram Faturados (Somente quando o imposto não for retido)
* Lançamentos que não atingiram o valor mínimo parametrizado para geração da contribuição (Neste caso é apresentado na REINF apenas a base de cálculo na tag: vlrBaseAgreg).  
  Segue exemplo na imagem abaixo:

Parâmetro\_RetençãoParâmetro com valor "0"Parâmetro com valor diferente de "0"Origem Gestão FiscalOrigem Gestão FiscalOrigem Gestão FiscalOrigemFisleftLançamentos com retençãoLançamentos com retençãoLançamentos com retenção

**Lançamentos Fiscais**

* Lançamentos cujo Cli/For seja pessoa jurídica;
* Lançamentos referentes a notas Recebidas, ou seja Lançamentos de Entrada, cujo Fornecedor possua retenção do Tributo em pelo menos um dos meses do Ano de Retenção.
* Lançamentos que não estejam cancelados, extemporâneos ou estornados.
* Lançamentos em que o Fornecedor seja do tipo “Empresa” ou “Cliente”.
* Lançamentos que não sejam Notas Fiscais que acobertam Cupom Fiscal
* Deverá ser usado no lançamento e cadastrado nos Parâmetros de Processos o tributo **"IRRFPJ"**
* Lançamento de Entrada com o Tributo **"COSIRF"** considerando data de Entrada ou Data Previsão de Baixa informado na Pasta Integração Financeira.

      **Observação**: Para mais detalhes sobre apuração do Cosirf [click aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404876669975-Cross-Segmentos-Linha-RM-Gest%C3%A3o-Fiscal-Apura%C3%A7%C3%A3o-de-Tributos-COSIRF)

Residentes ou domiciliados no exteriorResidentes ou domiciliados no exteriorResidentes ou domiciliados no exterior

**Lançamentos de Rendimentos pagos a residentes ou domiciliados no exterior**

* Lançamentos cujo Cli/For seja pessoa jurídica;
* Lançamentos que não estejam\sejam cancelados, extemporâneos, estornados;
* Lançamentos em que o Fornecedor seja do tipo “Empresa” ou “Cliente”;
* Lançamentos que não tenham sejam Notas Fiscais que acobertam Cupom Fiscal;
* Lançamentos que possuam o Tributo IRRF Importação;
* Deverão estar informados os campos de “País” e “Estado” na aba de Endereço do Cadastro de Cliente/Fornecedor. Somente serão retornados Lançamentos em que o Estado do Cliente/Fornecedor não esteja com a opção “Nacional” marcada;
Fornecedor do Simples NacionalFornecedor do Simples NacionalFornecedor do Simples Nacional

**Lançamentos de Rendimentos pagos a Fornecedor do Simples Nacional**

* Lançamentos cujo Cli/For seja pessoa jurídica;
* Lançamentos referentes a notas Recebidas, ou seja Lançamentos de Entrada;
* Lançamentos que não estejam cancelados, extemporâneos ou estornados;
* Deverá ser cadastrado nos Parâmetros de Processos o tributo "**Simples Nacional**" e a “**Natureza de Rendimento**”;
* Deverá ser usado no lançamento o tributo "**Simples Nacional**" com a “**Natureza de Rendimento**” preenchida.

## **04. Exemplo****3**

xmlExemplo R-4020


{...}
{...}

{...}
]]>ideContri

Utiliza um grupo **ideEstab** especifico para este tipo

## **05. Mapeamento de Campos**

1ideEventoideEventoideContriideContriEstabelecimentoEstabelecimento

**Informações de Identificação do Estabelecimento**

| Registro\Campo | Registro Pai | Descrção | Origem dos Dados RM |
| --- | --- | --- | --- |
| ideEstab | evtRetPF | Informações de identificação do estabelecimento. |  |
| tpInscEstab | ideEstab | Preencher com o código correspondente ao tipo de inscrição:   1 - CNPJ; 2 - CPF; 3 - CAEPF. Valores válidos: 1, 2, 3. | Gerando conforme informação do Campo CNPJ da Filial Matriz   Verificar o tamanho do campo CPF (11 carac.) e CNPJ(14 carac.)  GFILIAL.CGC |
| nrInscEstab | ideEstab | Informar o número de inscrição do estabelecimento de acordo com o tipo de inscrição indicado no campo {tpInscEstab}. Validação: A inscrição informada deve ser compatível com o {tpInscEstab}.   Se {tpInscEstab} = [1] e {classTrib} <> [85], deve ser um número de CNPJ pertencente ao contribuinte declarante (mesma raiz de {ideContri/nrInsc}). Se {tpInscEstab} = [2], deve ser igual a {ideContri/nrInsc}. | Gerando conforme informação do Campo CNPJ da Filial Matriz   GFILIAL.CGC |

ideBenefideBenef

**Identificação do Beneficiário do Rendimento**

| Registro\Campo | Registro Pai | Descrição | Origem dados RM |
| --- | --- | --- | --- |
| ideBenef | ideEstab | Identificação do beneficiário do rendimento. |  |
| cnpjBenef | ideBenef | Informar o CNPJ do beneficiário do crédito ou pagamento. Validação: Informação obrigatória se houver ao menos um registro {idePgto} cujo campo {paisResidExt} não tenha sido informado. Não pode haver mais de um registro {ideBenef} com um mesmo número de CNPJ para o mesmo estabelecimento no mesmo período de apuração. Não pode ser igual ao CNPJ do declarante, exceto nas seguintes situações: a) se {natRend} =  [11001, 11002, 11003], [12017 a 12028] ou [15012 a 15034]; b) se  {nrInscFciScp} for informado com um fundo/clube de investimento ou com um CNPJ de sociedade em conta de participação. Se informado, deve ser um número de inscrição no CNPJ válido. | Gerar com o CNPJ do Cliente\Fornecedor associado ao Lançamento Fiscal de Entrada ou ao Lançamento Financeiro |
| nmBenef | ideBenef | Nome do beneficiário. Validação: Informação obrigatória e exclusiva se {cnpjBenef} não for informado. | Gerar com o Nome do Cliente\Fornecedor associado ao Lançamento Fiscal ou Lançamento Financeiro |
| isenImun | ideBenef | Informações sobre isenção e imunidade: 1 - Entidade não isenta/não imune - Tributação normal; 2- Instituição de educação e de assistência social sem fins lucrativos, a que se refere o art. 12 da Lei nº 9.532, de 10 de dezembro de 1997; 3- Instituição de caráter filantrópico, recreativo, cultural, científico e às associações civis, a que se refere o art. 15 da Lei nº 9.532, de 1997. Os valores [2, 3] são permitidos apenas para órgãos da administração pública federal direta, autarquias e fundações da administração pública federal, empresas públicas, sociedades de economia mista, ou demais entidades em que a que União detenha maioria do capital social sujeito a voto, recebe recursos do Tesouro Nacional e está obrigada a registrar a execução orçamentária no Siafi. Validação: Só é permitido valor igual a [2, 3] se {indUniao} do R-1000 for igual a [1]. | Gerar Fixo com valor 1.  Não é gerado a partir da versão 2.1.2 |

idePgtoidePgto

**Informações relativas ao pagamento efetuado.**

| Registro\Campo | Registro Pai | Descrição | Origem Dados RM |
| --- | --- | --- | --- |
| infoPgto | idePgto | Informações relativas ao pagamento efetuado |  |
| natRend | idePgto | Código da natureza do rendimento, conforme Tabela 01.  Validação: Deve ser um código válido, existente na Tabela 01. | Gerado conforme código associado ao Lançamento Fiscal\Lançamento Financeiro O Cadastro deve ser feito no Aplicativo Gestão Fiscal\Cadatro\Mais\Natureza de Rendimento  DNATUREZARENDIMENTO.CODNATRENDIMENTO |
| dtFG | infoPgto | Informar a data do fato gerador, ou, em caso de fato não tributável mas de informação obrigatória conforme legislação vigente, a data do pagamento ou crédito, no formato AAAA-MM-DD. Validação: A data informada deve estar compreendida no período de apuração ao qual se refere o arquivo, conforme informado em (perApur}, no formato AAAA-MM-DD. | Para lançamentos de Entrada com o Tributo "COSIRF" é considerado a Data Previsão de Baixa informado na Pasta Integração Financeira. Caso a Data Previsão de Baixa não esteja preenchida é considerada a data do documento. |
| vlrBruto | infoPgto | Informar o valor bruto. Validação: Deve ser igual ou maior que 0 (zero). | Gerado com o Valor Contábil do Lançamento Fiscal ou Valor Liquido do Lançamento Financeiro, seguindo o que foi configurado nos Parâmetros de Processo da Reinf - "Valor Rendimentos Financeiros" |
| indFciScp | infoPgto | Indicativo da origem do rendimento, de acordo com as seguintes opções: 1 - FCI - Fundo ou Clube de Investimento; 2 - SCP - Sociedade em Conta de Participação. Se o rendimento não se refere a nenhuma das opções acima, não deve ser informado. Valores válidos: 1, 2. | Será gerado apenas se a filial do lançamento for **SCP**, com valor fixo igual a 2. |
| nrInscFciScp | infoPgto | Número de inscrição no CNPJ, de acordo com o conteúdo do campo {indFciScp}:  a) do Fundo ou Clube de Investimento (FCI) do qual o beneficiário faça parte e seja administrado pelo declarante; b) da Sociedade em Conta de Participação (SCP) da qual o beneficiário faça parte e o declarante seja sócio ostensivo. Validação: Informação exclusiva e obrigatória se {indFciScp} = [1,2]. Se informado, deve ser um CNPJ válido e diferente do CNPJ do declarante (se este for PJ). Se {indFciScp} = [1], o CNPJ do FCI deve ter o número de ordem 0001, observadas as regras de preenchimento estabelecidas na Tabela 01. | Campo gerado com o CNPJ da Filial **SCP** informada no lançamento, por isso, será exibido **somente**se a filial do lançamento for **SCP**. |
| percSCP | infoPgto | Percentual que o beneficiário possui na Sociedade em Conta de Participação. Validação: Informação obrigatória e exclusiva se {indFciScp} = [2]. Não pode ser maior que 100. | Gerado somente para lançamentos que possuam o **CNPJ** do Cliente/Fornecedor cadastrado como sócio da Filial e natureza de rendimento igual a **12001** (Lucro e Dividendo). É necessário o preenchimento do campo DSOCIOECF. PERCAPTOT (% Participação no Capital Total) no cadastro do Sócio.  Para realizar o cadastro do sócio acesse: Cadastros | Filial | Selecione a filial | Anexos | Parâmetros – Escrituração Contábil Fiscal | Edite o Parâmetro | Anexos | Sócio |
| indJud | infoPgto | Indicativo de rendimento oriundo de decisão judicial: S - Sim; N - Não. Validação: Informação obrigatória se {natRend} = [11001], [11002], [11003]). Valores válidos: S, N. | Não gerado |
| paisResidExt | infoPgto | Informar o código do país de residência para fins fiscais, quando no exterior, conforme Tabela 07. Somente informar este campo caso o país de residência para fins fiscais seja diferente de Brasil. Se não informado, implica que o país de residência fiscal é Brasil. Validação: Observar as regras estabelecidas na Tabela 01. | Gerado o código do País conforme a tabela informado na tela de geração da Rotina ou Parametrização |

retencoes retencoes 

**Informações relativas a retenções na fonte e respectivas bases de cálculo**

Informações Não Geradas

Ao gerar o Evento **R-4020**, com o Tributo **IRRFPJ** e o Tipo de Recolhimento igual a **"IRRF Devido pelo Prestador"** estes dados relativos as **retenções** não são gerados.

| Registro\Campo | Registro Pai | Descrição | Origem de Dados RM |
| --- | --- | --- | --- |
| retencoes | infoPgto | Informações relativas a retenções na fonte e respectivas bases de cálculo. |  |
| vlrBaseIR | retencoes | Valor da base de retenção do IR, efetivamente realizada. Validação: Informação permitida apenas se, para a natureza do rendimento informada em {natRend}, houver "IR" na coluna "Tributo" da Tabela 01. Se informado, deve ser maior que 0 (zero). | Gerado conforme o Campo Base de Calculo do Tributo IRRF PJ informado no outros Tributos do Lançamento Fiscal ou Conforme informação do Lançamento Financeiro,  seguindo o que foi configurado nos Parâmetros de Processo da Reinf - "Valor Rendimentos Financeiros"   Também será gerado para o tributo que tenha seu tipo cadastrado como COSIRF (DTRIBUTO.TRIFISC igual a “26”) e  possua Código de Receita igual a **6256**    Se no cadastro de Natureza de Rendimento estiver marcada a opção "Sem IR" a tag vlrBaseIR não será gerada: Imagem |
| vlrIR | retencoes | Valor do Imposto de Renda Retido na Fonte. Validação: Informação obrigatória se {vlrBaseIR} for informado. Se informado, deve ser maior que zero. | Gerado conforme o Campo Valor do Tributo IRRF PJ informado no outros Tributos do Lançamento Fiscal ou Conforme informação do Lançamento Financeiro   Também será gerado para o tributo que tenha seu tipo cadastrado como COSIRF (DTRIBUTO.TRIFISC igual a “26”) e  possua Código de Receita igual a **6256**  Se no cadastro de Natureza de Rendimento estiver marcada a opção "Sem IR" a tag  vlrIR não será gerada: Imagem |
| vlrBaseAgreg | retencoes | Valor da base de retenção de tributos de forma agregada, efetivamente realizada. Este campo deve ser utilizado nos casos em que a retenção for realizada em valor agregado e informada no campo {vlrAgreg}. Validação: Informação permitida apenas se, para a natureza do rendimento informada em {natRend}, houver "Agreg" na coluna "Tributo" da Tabela 01. Se informado, deve ser maior que 0 (zero). | Gerado com a Base de calculo dos Lançamentos Fiscais que possuam:  Tributo que tenha seu tipo cadastrado como COSIRF (DTRIBUTO.TRIFISC igual a “26”) e  possua Código de Receita **diferente** de **6256,** **6228****,** **4387,** **6243****,** **4407,** **6230,** **4409 ou não preenchido.**  Ou Lançamentos Fiscal/Financeiro para o  tributo que tenha seu tipo cadastrado como CSRF - PIS\COFINS e CSLL (DTRIBUTO.TRIFISC igual a “21”) Código de Receita 5952 |
| vlrAgreg | retencoes | Valor da retenção em valor agregado de tributos (IR, CSLL, Cofins e PIS/Pasep). Validação: Informação obrigatória se {vlrBaseAgreg} for informado. Se informado, deve ser maior que zero. | Tributo que tenha seu tipo cadastrado como **COSIRF** (DTRIBUTO.TRIFISC igual a “26”) e  possua Código de Receita **diferente** de **6256,** **6228****,** **4387,** **6243****,** **4407,** **6230,** **4409 ou não preenchido.**  Ou tributo que tenha seu tipo cadastrado como **CSRF -** **PIS\COFINS e CSLL** (DTRIBUTO.TRIFISC igual a “21”) Código de Receita 5952 |
| vlrBaseCSLL | retencoes | Valor da base de cálculo da Contribuição Social sobre Lucro Líquido - CSLL, relativa à retenção efetivamente realizada. Validação: Informação permitida apenas se, para a natureza do rendimento informada em {natRend}, houver "CSLL" na coluna "Tributo" da Tabela 01. Não pode ser informado se {vlrBaseAgreg} for informado. Se informado, deve ser maior que zero. | Gerado com a Base de cálculo dos Lançamentos Financeiro ou Fiscal que tem o Tributo CSLL- RF (DTRIBUTO.TRIFISC igual a “18”)  Também será gerado para o tributo que tenha seu tipo cadastrado como COSIRF (DTRIBUTO.TRIFISC igual a “26”) e possua o Código de Receita igual a **6228** ou **4387** |
| vlrCSLL | retencoes | Valor da retenção da Contribuição Social sobre Lucro Líquido - CSLL. Validação: Informação obrigatória se {vlrBaseCSLL} for informado. Se informado, deve ser maior que zero. | Gerado com o valor do Imposto dos Lançamentos Financeiro ou Fiscal que tem o Tributo CSLL- RF (DTRIBUTO.TRIFISC igual a “18”)  Também será gerado para o tributo que tenha seu tipo cadastrado como COSIRF (DTRIBUTO.TRIFISC igual a “26”) e possua o Código de Receita igual a **6228** ou **4387** |
| vlrBaseCofins | retencoes | Valor da base de cálculo da Cofins, relativa à retenção efetivamente realizada. Validação: Informação permitida apenas se, para a natureza do rendimento informada em {natRend}, houver "Cofins" na coluna "Tributo" da Tabela 01. Não pode ser informado se {vlrBaseAgreg} for informado. Se informado, deve ser maior que zero. | Gerado com a Base de cálculo dos Lançamentos Financeiro ou Fiscal que tem o Tributo COFINS - RF (DTRIBUTO.TRIFISC igual a “20”)  Também será gerado para o tributo que tenha seu tipo cadastrado como COSIRF (DTRIBUTO.TRIFISC igual a “26”) e possua Código de Receita igual a **6243** ou **4407** |
| vlrCofins | retencoes | Valor da retenção relativa a Cofins. Validação: Informação obrigatória se {vlrBaseCofins} for informado. Se informado, deve ser maior que zero. | Gerado com o valor do Imposto dos Lançamentos Financeiro ou Fiscal que tem o Tributo COFINS - RF (DTRIBUTO.TRIFISC igual a “20”)  Também será gerado para o tributo que tenha seu tipo cadastrado como COSIRF (DTRIBUTO.TRIFISC igual a “26”) e possua Código de Receita igual a **6243** ou **4407** |
| vlrBasePP | retencoes | Valor da base do PIS/PASEP, relativa à retenção efetivamente realizada. Validação: Informação permitida apenas se, para a natureza do rendimento informada em {natRend}, houver "PP" na coluna "Tributo" da Tabela 01. Não pode ser informado se {vlrBaseAgreg} for informado. Se informado, deve ser maior que zero. | Gerado com a Base de cálculo dos Lançamentos Financeiro ou Fiscal que tem o Tributo PIS - RF (DTRIBUTO.TRIFISC igual a “19”)  Também será gerado para o tributo que tenha seu tipo cadastrado como COSIRF (DTRIBUTO.TRIFISC igual a “26”) e possua Código de Receita igual a **6230** ou **4409** |
| vlrPP | retencoes | Valor da retenção do PIS/PASEP. Validação: Informação obrigatória se {vlrBasePP} for informado. Se informado, deve ser maior que zero. | Gerado com o valor do Imposto dos Lançamentos Financeiro ou Fiscal que tem o Tributo PIS – RF (DTRIBUTO.TRIFISC igual a “19”)  Também será gerado para o tributo que tenha seu tipo cadastrado como COSIRF (DTRIBUTO.TRIFISC igual a “26”) e possua Código de Receita for igual a **6230** ou **4409** |

infoPgtoExtinfoPgtoExt

**Informações complementares relativas a pagamentos a residente fiscal no exterior**

| Registro\Campos | Registro Pai | Descrição | Origem de Dados RM |
| --- | --- | --- | --- |
| infoPgtoExt | infoPgto | Informações complementares relativas a pagamentos a residente fiscal no Exterior. | Gerado quando o Cliente\Fornecedor for do Exterior e Pessoal Jurídica |
| indNIF | infoPgtoExt | Indicativo do Número de Identificação Fiscal: 1 - Beneficiário com NIF; 2 - Beneficiário dispensado do NIF; 3 - País não exige NIF. Valores válidos: 1, 2, 3. | Campo Gerado conforme o Cadastro do Cliente\Fornecedor – Sub Pasta Tributo   FCFO.SITUACAONIF |
| nifBenef | infoPgtoExt | Número de Identificação Fiscal - NIF. Validação: Obrigatório se {indNIF} = [1]. | Campo Gerado conforme o Cadastro do Cliente\Fornecedor – Sub Pasta Tributo   FCFO.NIF |
| relFontPg | infoPgtoExt | Relação da fonte pagadora com o beneficiário, conforme Tabela 03. Validação: O código informado deve existir na Tabela 03. | Tipos de Relacionamentos de Participantes (CRELACIONAMENTO.CODIGO) 00 == 900 01 == 500 02 == 510 03 == 520 04 == 530 05 == 540 06 == 550 07 == 570 09 == 560 |
| frmTribut | infoPgtoExt | Forma de tributação, conforme opções disponíveis na Tabela 02. Validação: Deve ser um código existente na Tabela 02. | Gerado com a informação do Lançamento, campo Forma de Tributação Localizado na pasta Outro Tributos da Situação Tributária.  **Importante:** O campo fica disponível apenas para o tributo IRRF IMPORTAÇÃO  (no cadastro do tributo o Tipo Tributo deve ser IRRF Importação). Vídeo  DTRBLAF.FORMATRIBUTACAO  Caso o campo não esteja preenchido no Lançamento será considerado  o campo Forma de Tributação do cadastro do Cliente Fornecedor Sub Pasta Tributos. Vídeo   FCFO.FORMATRIBUTACAO  Gerado com a informação do Lançamento, campo Forma de Tributação Localizado na pasta Outro Tributos da Situação Tributária.  **Importante:** O campo fica disponível apenas para o tributo IRRF IMPORTAÇÃO  (no cadastro do tributo o Tipo Tributo deve ser IRRF Importação). Vídeo  DTRBLAF.FORMATRIBUTACAO  Caso o campo não esteja preenchido no Lançamento será considerado  o campo Forma de Tributação do cadastro do Cliente Fornecedor Sub Pasta Tributos. Vídeo   FCFO.FORMATRIBUTACAO    **OBSERVAÇÃO:**Caso seja usado no mesmo período Formas de Tributação diferentes para o mesmo Cliente Fornecedor podem ocorrer inconsistências, nesse caso devem ser verificadas as regras da EFD-REINF. |
| dscLograd | endExt | Descrição do logradouro. | Campo Gerado com o Cadastro do Cliente\Fornecedor – Sub Pasta Endereço  FCFO.RUA |
| nrLograd | endExt | Número do logradouro. | Campo Gerado com o Cadastro do Cliente\Fornecedor – Sub Pasta Endereço  FCFO.NUMERO  Se houver caracteres não numéricos no cadastro o campo não será gerado. |
| complem | endExt | Complemento do logradouro. | Campo Gerado com o Cadastro do Cliente\Fornecedor – Sub Pasta Endereço  FCFO.COMPLEMENTO |
| bairro | endExt | Nome do bairro/distrito. | Campo Gerado com o Cadastro do Cliente\Fornecedor – Sub Pasta Endereço  FCFO.BAIRRO |
| cidade | endExt | Nome da cidade. | Campo Gerado com o Cadastro do Cliente\Fornecedor – Sub Pasta Endereço  FCFO.CIDADE |
| estado | endExt | Nome da província/estado. | Campo Gerado com o Cadastro do Cliente\Fornecedor – Sub Pasta Endereço  FCFO.CODETD |
| codPostal | endExt | Código de Endereçamento Postal. | Campo Gerado com o Cadastro do Cliente\Fornecedor – Sub Pasta Endereço  FCFO.CAIXAPOSTAL |
| telef | endExt | Número do telefone. | Campo Gerado com o Cadastro do Cliente\Fornecedor – Sub Pasta Endereço  FCFO.TELEFONE |

Informações Não Geradas

infoComplContri - Informações complementares do contribuinte.

infoProcRet - Informações de processos relacionados a não retenção de tributos ou a depósitos judiciais.

infoProcJud - Informações complementares relativas a rendimentos decorrentes de decisão judicial.

despProcJud - Detalhamento das despesas com processo judicial.

ideAdv - Identificação do advogado.
