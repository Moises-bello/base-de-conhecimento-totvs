---
content_hash: 0178884242c802a1e2158437d796604f522d388da119f3b9845c98404cf75c3d
fetched_at: '2026-06-29T00:11:17.056402+00:00'
page_id: '676050165'
product: rm
source: tdn-rm
title: FISCAL01-17686 - DT - Correção para erro no código de variação para Tributo
  IRRFPJ - DCTF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=676050165
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotinas Fiscais - Federais - DCTF |
| País: | Brasil |
| Ticket: | 13776688 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17686 |

## **02. SITUAÇÃO/REQUISITO**

**INTERPRETAÇÃO DE DEMANDA**

Ao gerar o registro R10 da DCTF, tributo IRRF PJ, o campo 7 (Código da Receita), é gerado com a variação incorreta = 170800. No cadastro do Código de Receita | Anexos | Codificação do Código de Receita, a variação está preenchida como 06.

**TESTES REALIZADOS**

Foi gerado o arquivo da rotina e confirmado o comportamento. Foi usado um código de variação 99 e no arquivo gerado o código foi preenchido como "08" conforme o​ cadastro no tributo associado ao período de apuração.

Imagem

**BENEFÍCIOS ALCANÇADOS**

Correção do sistema para que o comportamento seja adequado com a regra de geração deste registro.

## **03. SOLUÇÃO**

Alteração feita na rotina de geração do arquivo DCTF. Com essa alteração a geração do arquivo para o tributo IRRFPJ obterá o código de variação a partir do cadastro de código de receita, semelhante aos tributos PIS, PISIMPORT, COFINS, COFINSIMPORT, RET, CONTRIBSOCIALRF, IRRF e COSIRF.

Disponível a partir da versão 12.1.34
