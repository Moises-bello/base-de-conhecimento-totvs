---
content_hash: 32313b00e351a4aa1410bacfd68419998d61f3abf563c597996594764d914337
fetched_at: '2026-06-29T00:11:25.613935+00:00'
page_id: '714212979'
product: rm
source: tdn-rm
title: FISCAL01-18379 - DT - Registro C185
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-18379+-+DT+-+Registro+C185
version: 2
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18379 |

## **02. SITUAÇÃO/REQUISITO**

Alteração da regra de validação do campo 06 do registro C185.

**Atenção! Regra do Aplicativo**

Se o terceiro caractere do código preenchido no campo “COD\_MOT\_REST\_COMPL” for:

1. a)  igual a 0, os campos 10 a 18 não devem ser preenchidos. **Necessário alterar.**
2. b) igual a 1, os campos 10, 12, 13, 14, 15 e 16 devem ser preenchidos e os campos 11, 17 e 18 não devem ser preenchidos. Está OK, não tem atuação.
3. c) igual a 2, os campos 12, 13, 14, 15 e 16 devem ser preenchidos e os campos 10, 17 e 18 não devem ser preenchidos. O campo 11 pode ser preenchido de acordo com a legislação de cada UF. Está Ok, não tem atuação.
4. d) igual a 3, os campos 10, 12, 13, 14, 17 e 18 devem ser preenchidos e os campos 11, 15 e 16 não devem ser preenchidos. Está Ok, não tem atuação.

## **03. SOLUÇÃO**

Alterada a regra de validação do campo 06 do registro C185, onde se o terceiro caractere do código preenchido no campo “COD\_MOT\_REST\_COMPL” for igual a 0, os campos 12, 13 e 14 devem ser preenchidos e os campos 10, 11 e 15 a 18 não devem ser preenchidos. 

Disponível a partir da biblioteca 12.1.34
