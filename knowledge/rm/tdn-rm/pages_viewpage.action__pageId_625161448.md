---
content_hash: 7ceee582b8d1a08ea5cd7bc5931e8737a9b04f8e6accf5b12af963890c0c608e
fetched_at: '2026-06-29T00:11:04.101074+00:00'
page_id: '625161448'
product: rm
source: tdn-rm
title: FISCAL01-15860 - DT EFD ICMS\IPI - Ajuste de Crédito e Débito sempre ser Gerado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=625161448
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração do Arquivo EFD ICMS\IPI |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15860 |

## **02. SITUAÇÃO/REQUISITO**

No sped fiscal os registros C197 e D197 são gerados de forma opcional conforme definido na parametrização da rotina. Os ajustes de débito e crédito serão sempre considerados na Apuração do ICMS e consequentemente quando informado no lançamento fiscal os mesmos deverão ser gerados na rotina de forma obrigatória.

Somente ajustes que se encaixam como débito e crédito que sempre serão gerados, os demais tipos de ajuste como por exemplo Diferencial de Alíquota continuam sendo gerados de forma opcional definido na parametrização do Sped Fiscal.

## **03. SOLUÇÃO**

Implementação nos registros C197\D197 da EFD ICMS\IPI para que os lançamentos de Ajuste de Débito e Crédito sejam sempre exibidos independente da parametrização onde os registros C197 e D197 são considerados opcionais.

Regra para os códigos de ajuste de Débito e Crédito que sempre serão exibidos:

Deve ser considerado como Ajuste de Débito (Considerar como débito) os Códigos de Ajuste cujo o Terceiro caractere for igual a ‘3’, ‘4’ ou ‘5’ e o Quarto caractere for igual a “0”, “3”, “4”, “5”, “6”, “7” ou “8”.

Exemplo de código: UF30xxxxxx, UF04xxxxxx

Deve ser considerado como Ajuste de Crédito (Considerar como crédito) os Códigos de Ajuste cujo o Terceiro caractere for igual a ‘0’, ‘1’ ou ‘2’ e o Quarto caractere for igual a ‘0’, “3”, “4”, “5”, “6”, “7” ou “8”.

Exemplo de código: UF00xxxxxx, UF03xxxxxx.
