---
content_hash: 4ab0f7bf57b2a9daee1e8b0ea7ca3e7127eafbec7460240d66f5580623b49c2c
fetched_at: '2026-06-29T00:10:30.518143+00:00'
page_id: '520102601'
product: rm
source: tdn-rm
title: FISCAL01-11189 DT Layout TAF - Alteração T003
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520102601
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | TAF |
| Ticket: | FISCAL01-11189 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11189 |

## **02. SITUAÇÃO/REQUISITO**

Atualizar a estrutura do Registro T003 para contemplar os novos campos:

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem da Informação |
| 46 | INDOPCCP | Indicativo da opção pelo produtor rural pela forma de tributação da contribuição previdenciária | Incluir este campo no Layout mais sem ligação. Especifico para o eSocial |
| 47 | ISENCAO\_IMUNIDADE | Informações sobre isenção e imunidade | Gerar fixo “1”. De acordo com o layout da Reinf, as opções 2 e 3 são muito específicas e não serão tratadas neste momento. |
| 48 | ESTADO\_EXT | Nome da província / estado - Exterior | Gerado com o Campo Cidade do Cadastro do Cli\For – **FCFO\CIDADE** |
| 49 | TELEFONE\_EXT | Número de telefone - Exterior | Gerado com o Campo Telefone do Cadastro do Cli\For – **FCFO\TELEFONE** |
| 50 | INDICATIVO\_NIF | Indicativo do Número de Identificação Fiscal: 1 - Beneficiário com NIF; 2 - Beneficiário dispensado do NIF; 3 - País não exige NIF. | Gerado com o Campo Situação do NIF do Cadastro do Cli\For – Sub Pasta Tributos – **FCFO\SITUACAONIF** |
| 51 | NIF | Número de Identificação Fiscal - NIF | Gerado com o Campo Numero Identificação Fiscal do Cadastro do Cli\For – Sub Pasta Tributos – **FCFO\NIF** |
| 52 | FORMA\_TRIBUTACAO | Forma de tributação para residentes no exterior. | Gerado com o Campo Forma Tributação do Cadastro do Cli\For – Sub Pasta Tributos – **FCFO\FORMATRIBUTACAO** |
| 53 | CNPJ\_PLS | CNPJ da operadora de plano de saúde privado coletivo empresarial. | Não aderência. |

## **03. SOLUÇÃO**

Foi realizado a inclusão dos campos no Layout do TAF referente ao Registro T003.

* INDOPCCP
* ISENCAO\_IMUNIDADE
* ESTADO\_EXT
* TELEFONE\_EXT
* INDICATIVO\_NIF
* NIF
* FORMA\_TRIBUTACAO

**Obs:** O campo de telefone não será ligado ao contexto, pois o formato de telefone é tratado como nacional e o  
padrão internacional é diferente do brasileiro. Por exemplo, o formato americano o DDD possui 3 dígitos.  
O campo 53 - CNPJ\_PLS não existe no layout do TAF e por isso não foi incluído.
