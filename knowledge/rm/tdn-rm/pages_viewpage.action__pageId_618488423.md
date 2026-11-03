---
content_hash: 55733ba5b2cdcb75328e4999d12d6fe7139515586004bfd6d8e7ad33206181a6
fetched_at: '2026-06-29T00:11:02.485820+00:00'
page_id: '618488423'
product: rm
source: tdn-rm
title: FISCAL01-15278 - DT ECF - Inclusão de Campos - Registro 0000
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=618488423
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | ECF Layout 0007 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15278 |

## **02. SITUAÇÃO/REQUISITO**

Alterar a geração da ECF 2021 para incluir os campos abaixo a partir de 2021:

**Registro 0000:** Abertura do Arquivo Digital e Identificação da Pessoa Jurídica

**Campo 3** - COD\_VER “**Código da versão do leiaute”**

De acordo com o layout 7, para o ano-calendário 2020 e situações especiais de 2021, o leiaute a ser informado deverá ser = 0007.

**Campo 6** - IND\_SIT\_INI\_PER - Indicador do Início do Período:

Incluído mais uma Opção: 3 – Resultante de Mudança de Qualificação da Pessoa Jurídica.

**Observação:** Este campo é gerado conforme a parametrização do Cadastro da Filial – Parâmetros ECF – Pasta Identificação Campo **“Indicador do Início do Período”** criar a Opção.

**Campo 7** - SIT\_ESPECIAL - Indicador de Situação Especial e Outros Eventos:

Incluído mais uma Opção: 7 – Mudança de Qualificação da Pessoa Jurídica

**Observação:** Campo gerado conforme parametrização do Cadastro da Filial – Parâmetros ECF – Pasta Identificação Campo “**Indicador de Situação Especial**”

## **03. SOLUÇÃO**

Adicionado validação no fonte onde, ao tentar gerar a rotina para os anos de 2020 e 2021 com layouts diferentes do 0007, uma mensagem de erro será exibida.

Acrescentado enumerado no campo **“Indicador do Início do Período”** e no Campo “**Indicador de Situação Especial**”.

Alterado layout da ECF para adequar os Campos 6 (IND\_SIT\_INI\_PER) e Campo 7 (SIT\_ESPECIAL) aos novos enumerados criados.

Disponível a partir da biblioteca 12.1.29
