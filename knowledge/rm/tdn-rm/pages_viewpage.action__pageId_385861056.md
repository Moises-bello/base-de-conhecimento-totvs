---
content_hash: bfbf65472416a64c2b30f1deb7ab56095a5b227f485f08179554f6ab38a50f0c
fetched_at: '2026-06-29T00:09:08.265801+00:00'
page_id: '385861056'
product: rm
source: tdn-rm
title: 1962105 FISCAL01-3045 DT EFD-CONTRIBUIÇÕES - "COD_CTA" - "Dispensa de ECD -
  IN RFB nº 1.774/2017"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385861056
version: 6
---

# EFD-CONTRIBUIÇÕES - "COD\_CTA" - "Dispensa de ECD - IN RFB nº 1.774/2017"

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | EFD-CONTRIBUIÇÕES - "COD\_CTA" - "Dispensa de ECD - IN RFB nº 1.774/2017" |
| **Situação/Requisito:** | As pessoas jurídicas tributadas com base no lucro presumido não sujeitas à obrigatoriedade da ECD, nos termos da IN RFB nº 1.774/2017, poderão, opcionalmente, informar nos campos "COD\_CTA" dos registros da EFDContribuições, para os fatos geradores a partir de novembro/2017, inclusive, a informação "Dispensa de ECD - IN RFB nº 1.774/2017" |
| **Solução/Implementação:** | Foi modificado a geração do arquivo magnético da EFD Contribuições para gerar a informação "Dispensa de ECD - IN RFB nº 1.774/2017" sempre que no cadastro da Filial, Anexo Dados Fiscais, o campo "**Empresa obrigada - ECD**" estiver **desmarcado** e o campo "Lucro Presumido", na tela de geração da rotina, estiver com opção **diferente** de "Não se aplica".  Neste caso será criado um registro 0500 fictício e o campo COD\_CTA dos registros abaixo serão afetados.   1. Dados do registro 0500 fictício     1. Campo 02 DT\_ALT: Data de Inclusão fixo 01/11/2017    2. Campo 03 COD\_ NAT\_CC: Código da Natureza da Conta igual a 09- outras    3. Campo 04 IND\_CTA : Indicador do Tipo da Conta fixo S - Sintética    4. Campo 05 NÍVEL: Nível igual a "0"    5. Campos 06 COD\_CTA e 07 NOME\_CTA: Código Conta e Descrição fixo "**Dispensa de ECD - IN RFB nº 1.774/2017**" 2. Registros Afetados (Conforme Guia Pratico EFD Contribuicoes Versao 1.27)    1. A170 campo 17    2. C170 campo 37    3. C175 campo 17    4. C381 campo 10    5. C385 campo 10    6. C396 campo 14    7. C481 campo 10    8. C485 campo 10    9. C501 campo 8    10. C505 campo 8    11. C601 campo 7    12. C605 campo 7    13. C870 campo 14    14. C880 campo 14    15. D100 campo 23    16. D101 campo 9    17. D105 campo 9    18. D201 campo 7    19. D205 campo 7    20. D300 campo 19    21. D350 campo 23    22. D501 campo 8    23. D505 campo 8    24. D601 campo 9    25. D605 campo 9    26. F100 campo 17    27. F120 campo 16    28. F130 campo 19    29. F500 campo 15    30. F510 campo 15    31. F525 campo 11    32. F550 campo 15    33. M400 campo 04    34. M410 campo 04    35. M800 campo 04    36. M810 campo 04    37. 1900 campo 13    38. P100 campo 11    39. 1101 campo 18 |
