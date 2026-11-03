---
content_hash: f7a9e7e0dbbb87e702685eaaff3b8973cc97eb9c577d5c0d0cef22ada8fb5803
fetched_at: '2026-06-29T00:11:26.197805+00:00'
page_id: '715830674'
product: rm
source: tdn-rm
title: R-2030 - Recursos Recebidos por Associação Desportiva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715830674
version: 31
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>#f5f5f5#363636noneR-2030

## **Conteúdo**



## **01. Regras****1**

### Regras Específicas

* A origem dessas informações é um serviço criado pelo Módulo de Materiais, uma vez que não há documento fiscal envolvido, considerado somente Movimento de Entrada.
* O Evento deve agrupar todos os lançamentos do período por cliente fornecedor.
* Para geração do Evento 2030 o período de apuração do Tributo INSS deve ser encerrado na Filial matriz e em todas as filiais que possuem o tributo INSS no período de geração do evento.

### Regras Gerais

**02. Parametrização2**

Segue abaixo parametrização necessária para geração dos eventos:

Passosslide

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
Obs: Campos de valores *TITMMOV.VALORBRUTOITEM, TTRBMOV.VALOR AS VALORINSS.*

ImagemLayout 2.01.02

A partir do layout 2.01.02 as seguintes tags serão geradas no xml para movimentações que possuem Cli\For do Exterior:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| recEmprExt | recursosRec | 0-1 | 001 | Informar se a empresa é domiciliada no exterior e não sujeita à inscrição no  CNPJ. Valores válidos: S. | Gerado com S quando o cli\for é do exterior |
| nmEmprExt | recursosRec | 0-1 | 070 | Informar o nome da empresa que repassou os recursos e que não é sujeita à  inscrição no CNPJ por ser domiciliada no exterior. Validação: Informação obrigatória e exclusiva se {recEmprExt} for  informado. Regra de validação: REGRA\_NOME\_VALIDO\_EXT | Gerado com o nome do cli\for do Exterior |

Para geração das tags é necessário que a versão informada nos parâmetros seja a 2.01.02 ou superior se houver:

Imagem

**03. Exemplo****3**

xmlExemplo R-2030


{...}

5
str1234
{...}
]]>ideContri

Utiliza um grupo **ideEstab** específico para este tipo

## **04. Origem dos Dados****4**

Origem-Dos-DadosevtAssocDespRec

| Elemento | Elemento Pai | Nível | Descrição | Ocorrência | Elemento Chave | Origem RM |
| --- | --- | --- | --- | --- | --- | --- |
|  | evtServPrest | 3 | Informações de Identificação do Evento | 1-1 |  |  |
|  |  | 3 | Informações de identificação do  contribuinte | 1-1 | tpInsc, nrInsc |  |
|  |  | 4 | Registro que identifica o estabelecimento  "prestador" de serviços mediante cessão  de mão de obra. | 1-1 | tpInscEstabPrest,  nrInscEstabPrest |  |
|  | ideEstab | 5 | Recursos recebidos por associação desportiva que mantenha equipe de futebol profissional | 1-N | cnpjOrigRecurso |  |
|  | recursosRec | 6 | Detalhamento dos recursos recebidos | 1-N | tpRepasse |  |
|  | recursosRec | 6 | Informações de Processsos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte | 0-50 |  |  |

ideEventoideEventoOrigem-dos-Dados-ideEventoideEstabideEstabOrigem-dos-Dados-ideEstabrecursosRecrecursosRec

Origem-dos-Dados-recursosRec

infoProcinfoProc

Origem-dos-Dados-infoProc

infoRecursoinfoRecurso

Origem-dos-Dados-infoRecurso

ideContriideContri

Origem-dos-Dados-ideContri
