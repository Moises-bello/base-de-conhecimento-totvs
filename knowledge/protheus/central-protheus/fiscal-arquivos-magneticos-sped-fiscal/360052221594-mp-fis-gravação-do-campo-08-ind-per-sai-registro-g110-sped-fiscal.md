---
article_id: 360052221594
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: cc7d7945002b819cf68677315875bf68f7aa4483fb41015e40fef2e600009bb2
fetched_at: '2026-06-28T22:42:03.785840+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'MP - FIS - Gravação do Campo 08 - IND_PER_SAI - Registro G110 - SPED FISCAL '
type: support-article
updated_at: '2021-04-28T14:24:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052221594-MP-FIS-Grava%C3%A7%C3%A3o-do-Campo-08-IND-PER-SAI-Registro-G110-SPED-FISCAL
---

**Dúvida**Como é composta a gravação do campo 08 - IND\_PER\_SAI no registro G110 do arquivo SPED FISCAL?   
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
O campo 08 - IND\_PER\_SAI do registro G110 é gravado com base no fator de conversão gravado no campo FA\_FATPRO da tabela SFA.

O campo FA\_FATPRO é gravado com base no fator de conversão preenchido no campo "Fator da lc 102/2000" na Wizzard de apropriação na rotina MATA906 - Estorno do Ciap
