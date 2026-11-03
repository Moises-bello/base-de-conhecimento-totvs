---
content_hash: 1d03ff04f2f41993871f1f55d38c403bcd28d86a1a30dc9e89bc4337eef2be4a
fetched_at: '2026-06-29T00:11:26.210384+00:00'
page_id: '715830693'
product: rm
source: tdn-rm
title: R-2040 - Recursos Repassados para Associação Desportiva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715830693
version: 20
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>#f5f5f5#363636noneR-2040

## **Conteúdo**

2. [Parametrização](http://tdn.totvs.com)

## **01. Regras****1**

### Regras Específicas

* A origem dessas informações é um serviço criado pelo Módulo de Materiais uma vez que não há documento fiscal envolvido, considerado somente Movimento de Saída.
* O Evento deve agrupar todos os lançamentos do período por cliente fornecedor.

### Regras Gerais

## **02. Parametrização****2**

Segue abaixo parametrização necessária para geração dos eventos:

Passos para geração dos eventos R-2030\R-2040:Passosslide

**1 -** Nos parâmetros do movimento acesse a etapa *Fis-Dados* e coloque o parâmetro *Movimento de Repasse EDF Reinf* como Edita. 

Imagem

**2 -** Na etapa *Item - Campos Livres 1/2* habilite a opção *Editar Campo Livre*

Imagem

**3 -** Na etapa *Fis - Tributação Item* informe o tributo INSS com Tributo Base INSS e Tipo de Recolhimento INSS

ImagemImagem

**4 -** No item do Movimento, acesse Integrações|Fiscal preencha o campo *Tipo Repasse EDF Reinf* com a opção desejada.  
Obs: campo na base de dados *TITMMOVFISCAL.TIPOREPASSEREINF.*

Imagem

**5 -** No item do Movimento, acesse Informações Adicionais|Observações e preencha o Campo livre com a Descrição do Recurso conforme desejado.  
Obs: O preenchimento deste campo é obrigatório para transmissão do evento, campo na base de dados *TITMMOV.CAMPOLIVRE*.

Imagem

**6 -** No item do Movimento, *Tributos e Valores* > *Tributos*, o tributo INSS deve ter Base, Alíquota e Valor.  
Obs: Campos de valores *TITMMOV.VALORBRUTOITEM, TTRBMOV.VALOR AS VALORINSS.*

Imagem

**7 -** É necessário encerrar o *Período de Apuração* do INSS para que o evento seja gerado, no *Totvs Gestão Fiscal* acesse *Obrigações Principais|Período de Apuração*.  
Selecione o período de apuração de INSS que corresponde ao mesmo período de inclusão do Movimento e faça o Encerramento.

Imagem

## **02. Exemplo****3**

xmlExemplo R-2040


{...}

5
str12340
{...}
]]>ideContri

Utiliza um grupo **ideEstab** específico para este tipo

## **03. Origem dos Dados****4**

DadosevtAssocDespRepevtAssocDespRep

| Elemento | Elemento Pai | Nível | Descrição | Ocorrência | Elemento Chave | Origem RM |
| --- | --- | --- | --- | --- | --- | --- |
|  | evtAssocDespRep | 3 | Informações de identificação do evento | 1-1 |  |  |
|  | evtAssocDespRep | 3 | Informações de identificação do contribuinte | 1-1 | tpInsc, nrInsc |  |
|  | IdeContri | 4 | Identificação do estabelecimento que repassou recursos. | 1-1 | tpInscEstab,  nrInscEstab |  |
|  | ideEstab | 5 | Recursos repassados para associação desportiva. | 1-1 | cnpjPrestador |  |
|  | ideEstab | 6 | Detalhamento dos recursos repassados | 1-N | serie, numDocto |  |
|  | recursosRep | 6 | Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte |  |  |  |

ideEventoideEventoOrigem-dos-Dados-ideEventoideContriideContri

Origem-dos-Dados-ideContri

ideEstabideEstab

Origem-dos-Dados-ideEstab

recursosReprecursosRep

Origem-dos-Dados-recursosRep

infoRecursoinfoRecurso

Origem-dos-Dados-infoRecurso

infoProcinfoProc

Origem-dos-Dados-infoProc
