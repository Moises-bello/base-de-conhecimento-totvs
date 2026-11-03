---
article_id: 360021146812
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 75875506067d7d76ac72245528d8106925abf52e489a6517f2ad789099620c25
fetched_at: '2026-06-28T22:42:02.430091+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Registro E200 -  PERÍODO DA APURAÇÃO DO ICMS - SUBSTITUIÇÃO TRIBUTÁRIA.
type: support-article
updated_at: '2025-02-11T21:31:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021146812-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Registro-E200-PER%C3%8DODO-DA-APURA%C3%87%C3%83O-DO-ICMS-SUBSTITUI%C3%87%C3%83O-TRIBUT%C3%81RIA
---

**Dúvida**Como gerar o registro E200 - PERÍODO DA APURAÇÃO DO ICMS - SUBSTITUIÇÃO TRIBUTÁRIA?  
   
 **Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80.  
   
**Solução**Este registro contém o período de apuração do ICMS - ST atual. Existindo um registro de apuração para cada UF onde o contribuinte foi substituto tributário. Para gerar o registro E200, verifique as configurações:

1. Verifique os parâmetros:  
**MV\_ESTADO** = SP (Deve ser o Estado que está sendo gerado na apuração)  
**MV\_USASPED** = T  
**MV\_P9SPED** = T  
**MV\_P9AUTO** = T  
**MV\_STUF**=AC/AL/AM/AP/BA/CE/DF/ES/GO/MA/MT/MS/MG/PA/PB/PR/PE/PI/RN/RS/RJ/RO/RR/SC/SP/SE/TO  
**MV\_STUFS**=AC/AL/AM/AP/BA/CE/DF/ES/GO/MA/MT/MS/MG/PA/PB/PR/PE/PI/RN/RS/RJ/RO/RR/SC/SP/SE/TO  
**MV\_SUBTRIB** = preenchido com estado + inscrição estadual (todos os estados que possuírem inscrição estadual para recolhimento do ICMS ST)

Exemplo: **MV\_SUBTRIB** = Preenchido com UF + Inscrição Estadual  
Exemplo: **MV\_SUBTRIB**=SP1234567/MG1234567

**MV\_STNIEUF** = Preencha com as unidades onde não é necessário ter inscrição estadual para recolhimento do ST. Preencher com UF concatenadas Exemplo: **MGPR/SPRJ** (de Minas Gerais para Paraná, de São Paulo para Rio de Janeiro).  
  
2. Verifique o arquivo **P9AUTOTEXT** na pasta system.  
O arquivo **P9AUTOTEXT** = De acordo com o Estado, deve estar na pasta system do Protheus. O arquivo fica disponível na central de downloads do portal do cliente.  
  
3. Gere a apuração do ICMS por meio da rotina MATA953 configurando os parâmetros da Wizard conforme abaixo:

Livro Selecionado = \* (Será gerada a apuração de todos os livros)  
Apuração = Mensal  (Apuração do mês)  
Período = 1º (Período Mensal)  
Gera guia de recolhimento = sim  
Imprime créditos de ST = Não  
Exclui GNR = Sim
