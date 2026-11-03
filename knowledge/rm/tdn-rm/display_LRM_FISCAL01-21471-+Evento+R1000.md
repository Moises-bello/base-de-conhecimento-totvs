---
content_hash: d58d200ac0dd9cbc7361fa494e8405910fb1bd0a6a098b08d6595aaa8252dd59
fetched_at: '2026-06-29T00:11:54.108995+00:00'
page_id: '853288768'
product: rm
source: tdn-rm
title: FISCAL01-21471- Evento R1000
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-21471-+Evento+R1000
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Fiscal |
| Processo | EFD REINF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-21471 |

## **02. SITUAÇÃO/REQUISITO**

Evento R-1000 - Alterar as tags **indUniao e nrInsc,** passando a ser gerada conforme a informação do Campo **"Natureza Jurídica"** informado no  Cadastro da Filial - Anexo Parâmetros da ECF - Escrituração Contábil Fiscal - Sub Pasta Tributação.

## **03. SOLUÇÃO**

Foi realizado ajuste na EFD REINF para preencher o campo indUniao como "1" sempre que a Natureza Jurídica da Filial for igual  
a uma destas opções: 1015,1040, 1074, 1104, 1139, 1163, 1210, 1228, 1252, 1260, 1287, 1317, 2011, 2038, se não recebe "0".

Quando PJ, o campo nrInsc passa a considerar a natureza jurídica da Filial para preenchimento. Caso a Natureza Juridica seja  
uma destas opções: 1015,1040, 1074, 1074, 1104, 1139, 1163, 1252,1287, 1341, o campo será preenchido com o CNPJ completo, se não  
será preenchido apenas com a raiz do CNPJ.

Registros afetados:  
Campo indUniao => Apenas R1000

Campo nrInsc => R1000, R1050, R1070, R2010, R2020, R2030, R2040, R2050, R2055, R2060, R2098, R2099, R-4010, R-4020 e R-4080, R4099, R9000

Disponível à partir da biblioteca 12.1.2306
