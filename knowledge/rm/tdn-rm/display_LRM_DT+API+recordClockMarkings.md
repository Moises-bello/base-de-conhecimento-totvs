---
content_hash: bda29f01f3c9eed1fe5af769d67a7c47988bc52d0897d599fe19e2c61792fc8f
fetched_at: '2026-06-29T00:11:27.471560+00:00'
page_id: '725741835'
product: rm
source: tdn-rm
title: DT API recordClockMarkings
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+API+recordClockMarkings
version: 30
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Automação de Ponto (CHRONUS) |
| Função: | Alterar a API para atender a portaria 671/2021 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHJORNRM-3514  DRHJORNRM-2755 |

## **02. SITUAÇÃO/REQUISITO**

Para atender a portaria 671/2021 foram criados nas tabelas AINTEGRACAOBATIDAS e MSA\_CONTROL\_MARCAC os campos (CODFUSO, CODCPFFUNC, NUMVERSLAYOUTAFD e CODINSCREMP)  e serão utilizadas na integração com o Suricato, sendo necessário atualizar a API de integração de marcações para preencher os novos campos.

## **03. SOLUÇÃO**

Alterada a API *recordClockMarkings,*para receber, validar e salvar os dados nos novos campos. Se as marcações a serem integradas forem referentes a portaria 671, antes de consumir a API será necessário validar se os novos campos já foram criados no RM, para isso siga a documentação a seguir: .

Após a criação dos novos campos a API estará preparada para receber as marcações, conforme o exemplo abaixo:

bashConfluenceMétodo POST - BodyImportante

A API aceita apenas um registro por requisição. Ela não foi projetada para processar marcações em lote, sendo necessário enviar uma requisição individual para cada marcação.

## **04. Retornos da API**

A API irá retornar a lista com o indicativo individual de sucesso ou erro na gravação. Os retornos possíveis estão na lista abaixo:

|  |  |  |
| --- | --- | --- |
| **Status** | **errorCode** | **message** |
| 200 |  | "Gravação efetuada com sucesso." |
| 400 | "00001" | "PIS em formato inválido ou inexistente no cadastro." |
| 400 | "00002" | "NSR duplicado. Número já foi importado na tabela" |
| 400 | "00002" | "NSR duplicado. Número já foi importado na InscrEmp informada." |
| 400 | "00003" | "NSR não foi informado e é obrigatório" |
| 400 | "00006" | "Não foi informado o campo obrigatório: CodRelogioExtChave" |
| 400 | "00006" | "Não foi informado o campo obrigatório: codFuncMsa" |
| 400 | "00006" | "Não foi informado o campo obrigatório: numHorarMarcacAces" |
| 400 | "00006" | "Código do REP é obrigatório" |
| 400 | "00006" | "Não foi informado o campo obrigatório: codUnidExtChave" |
| 400 | "00006" | "Não foi informado o campo obrigatório: codUsuarExtChave" |
| 400 | "00006" | "Data da marcação é obrigatória" |
| 400 | "00006" | "Campo 'datMarcacAces' no formato incorreto. Deve ser preenchido como data." |
| 400 | "00006" | "Tamanho do campo InscrEmp inválido. O campo permite a quantia de caracteres 11 ou 14 apenas." |
| 400 | "00006" | "Campo codRelogioExtChave no formato inválido. Deve ser preenchido para o Suricato: Coligada;Código do Terminal de Coleta ou para Ahgora: PONTOWEB." |
| 400 | "00007" | "Terminal de coleta não está cadastrado no ERP." |
| 400 | "99999" | "Erro interno na tabela. Registro não foi gravado." |
| 400 | "00001" | "CPF em formato inválido ou inexistente no cadastro." |

## **05. ASSUNTOS RELACIONADOS**

* [Importação de batidas integrada via API](https://tdn.totvs.com/pages/releaseview.action?pageId=682054374)
