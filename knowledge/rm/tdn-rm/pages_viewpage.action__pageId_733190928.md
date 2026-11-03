---
content_hash: 1b3044f19cbcd968b13f147baba51bb60c0cc3d1d202c9771dafbb8c10806532
fetched_at: '2026-06-29T00:11:28.746571+00:00'
page_id: '733190928'
product: rm
source: tdn-rm
title: R-4080 – Retenção no Recebimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=733190928
version: 21
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>#f5f5f5#363636noneR-4080

## **Conteúdo**



## **01. Introdução1**

Neste evento são enviadas informações de rendimentos cuja retenção e recolhimento do imposto de renda são feitos pela própria empresa prestadora dos serviços, procedimento mais conhecida como auto retenção.

## **02. Regras****2**

### Regras Específicas

* Necessário fazer o Cadastro do Parâmetros de Processos - **EFD REINF**. Para mis informações clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=490650588#1-5)
* É necessário parametrizar o Tributo e a Natureza de Rendimento -  Parâmetros de Processos - **EFD REINF** -Anexo - Filtro de Eventos - Para mais informações clique [aqui](https://tdn.totvs.com/display/LRM/Filtro+de+Eventos)

### **Origem de Dados Aplicativo Gestão Fiscal\RM Liber**

* Serão selecionados os lançamentos fiscais de saída com o tributo IRRF-PJ no período e tipo de recolhimento "Devido Prestador" conforme parâmetro financeiro "Geração do IRRF para fornecedores Pessoa Jurídica" o campo "Data Base para Geração".

  **Se o parâmetro "Data Base para Geração" for diferente de Emissão (DLAF.DATAEMISSAO) ou Vencimento (DLAF.VENCIMENTO) os lançamentos fiscais serão carregados pela Data Documento(DLAF.DATALF).**

Imagem

Regras Gerais

## **03. Exemplo****3**

xmlExemplo R-4080


{...}
{...}

{...}
]]>ideContri

Utiliza um grupo **ideEstab** especifico para este tipo

## **04. Origem dos Dados****4**

1ideEventoideEventoideContriideContriEstabelecimentoEstabelecimento

## Informações de Identificação do Estabelecimento

| Registro\Campo | Registro Pai | Descrção | Origem dos Dados RM |
| --- | --- | --- | --- |
| ideEstab | evtRetPF | Informações de identificação do estabelecimento. |  |
| tpInscEstab | ideEstab | Preencher com o código correspondente ao tipo de inscrição:   1 - CNPJ; 2 - CPF; 3 - CAEPF. Valores válidos: 1, 2, 3. | Gerando conforme informação do Campo CNPJ da Filial Matriz   Verificar o tamanho do campo CPF (11 carac.) e CNPJ(14 carac.)  GFILIAL.CGC |
| nrInscEstab | ideEstab | Informar o número de inscrição do estabelecimento de acordo com o tipo de inscrição indicado no campo {tpInscEstab}. Validação: A inscrição informada deve ser compatível com o {tpInscEstab}.   Se {tpInscEstab} = [1] e {classTrib} <> [85], deve ser um número de CNPJ pertencente ao contribuinte declarante (mesma raiz de {ideContri/nrInsc}). Se {tpInscEstab} = [2], deve ser igual a {ideContri/nrInsc}. | Gerando conforme informação do Campo CNPJ da Filial Matriz   GFILIAL.CGC |

ideFontideFont

## Identificação da fonte pagadora do rendimento

| Registro\Campo | Registro Pai | Descrição | Origem dados RM |
| --- | --- | --- | --- |
| ideFont | ideEstab | Identificação da fonte pagadora do rendimento. |  |
| cnpjFont | ideFont | Informar o CNPJ da fonte pagadora do rendimento. Validação: Não pode haver mais de um registro {ideFont} com um mesmo número de CNPJ para o mesmo estabelecimento no mesmo período de apuração. Não pode ser igual ao CNPJ do declarante. Deve ser um número de inscrição no CNPJ válido. |  |

infoRecinfoRec

## Informações relativas ao recebimento do rendimento.

| Registro\Campo | Registro Pai | Descrição | Origem Dados RM |
| --- | --- | --- | --- |
| natRend | ideRend | Código da natureza do rendimento, conforme Tabela 01. Validação: Informação permitida apenas para natureza de rendimento cujo código seja do grupo 20 da Tabela 01. |  |
| observ | ideRend | Observações. | Campo não gerado. Gerado sob Demanda como o Evento é agrupado por Natureza do Rendimento e Beneficiário não faz sentido considerar a Observação do Lançamento Fiscal. |
| dtFG | infoRec | Informar a data do recebimento do rendimento no formato AAAA-MM-DD. Validação: A data informada deve estar compreendida no período de apuração ao qual se refere o arquivo, conforme informado em (perApur}, no formato AAAA-MM-DD. |  |
| vlrBruto | infoRec | Informar o valor bruto. Validação: Deve ser maior que 0 (zero). | Gerado como Valor Contábil do Lançamento Fiscal. |
| vlrBaseIR | infoRec | Valor da base do IR, conforme previsto na legislação vigente. Validação: Deve ser maior que 0 (zero). | Gerado com a Base do IRRF PJ do Lançamento Fiscal |
| vlrIR | infoRec | Valor do Imposto de Renda Retido na Fonte, conforme previsto na legislação. | Gerado com o Valor do Imposto do IRRF PJ do Lançamento Fiscal |

Informações Não Geradas

infoComplContri - Informações complementares do contribuinte.

infoProcRet - Informações de processos relacionados a não retenção de tributos ou a depósitos judiciais.
