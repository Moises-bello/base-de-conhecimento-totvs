---
content_hash: de0f2415ba45202aa747b94d534870bd583be8f61bdc3a7f2c880231362aa1c3
fetched_at: '2026-06-29T00:11:03.578065+00:00'
page_id: '624592057'
product: rm
source: tdn-rm
title: FISCAL01-14900 - DT Apuração ICMS considerar Lanc. Ajuste Débito e Crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=624592057
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Encerramento do período de apuração do tributo ICMS |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14900 |

## **02. SITUAÇÃO/REQUISITO**

Alterar a apuração de ICMS para considerar o valor do código de ajustes.

## **03. SOLUÇÃO**

Na apuração do ICMS os lançamentos de ajuste de débito e crédito do período serão considerados na Apuração.

São considerados lançamentos de Ajuste C197\D197 do Item e Lançamento fiscal.  
Somente lançamentos Fiscais com Modelo de Documento 01,1B,04,55,65,07,08,8B,09,10,11,26,27,57,63 ou 67.

Deve ser considerado como Ajuste de Debito (Considerar como débito) os Códigos de Ajuste cujo o Terceiro caractere for igual a 3,4 ou 5 e o Quarto caractere for igual a 0,3,4,5,6,7 ou 8.

Exemplo de código: UF03xxxxxx, UF04xxxxxx

Deve ser considerado como Ajuste de Credito (Considerar como crédito) os Códigos de Ajuste cujo o Terceiro caractere for igual a 0,1 ou 2 e o Quarto caractere for igual a 0,3,4,5,6,7 ou 8.

Exemplo de código: UF00xxxxxx, UF02xxxxxx.

Relatório de Apuração .Net não sofreu impacto visto que só demonstra os valores totais de outros débito e crédito.  
Relatório de Apuração Delphi não discrimina os lançamentos de ajustes. mas demonstra os valores totais de outros débito e crédito.

.
