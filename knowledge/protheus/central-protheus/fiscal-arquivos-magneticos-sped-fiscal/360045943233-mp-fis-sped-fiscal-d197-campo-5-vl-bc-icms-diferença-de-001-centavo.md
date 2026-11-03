---
article_id: 360045943233
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 3a6476d43912b3fca0e3632035f436ce9934f453c8cd2317aa224bd3a31f3c0f
fetched_at: '2026-06-28T22:42:03.841164+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS - SPED FISCAL - D197 -Campo 5 VL_BC_ICMS - DIFERENÇA DE 0,01 CENTAVO
type: support-article
updated_at: '2021-04-28T14:25:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045943233-MP-FIS-SPED-FISCAL-D197-Campo-5-VL-BC-ICMS-DIFEREN%C3%87A-DE-0-01-CENTAVO
---

**Dúvida**

Ao gerar o arquivo do SPED FISCAL o campo 5 - VL\_BC\_ICMS do registro D197 é gravado com diferença de 0,01 centavo a menor.

**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Para a gravação do campo 5 - VL\_BC\_ICMS do registro D197, são utilizados os valores gravados no campo CDA\_BASE em conjunto com o campo CDA\_VALOR.

Analisando o print abaixo referente a tabela CDA, se somarmos os valores do campo CDA\_BASE chegaremos no total de R$ 4,30.

Para o item 002 no campo CDA\_SEQ, o valor do campo CDA\_BASE é de 0,01 e o valor do campo CDA\_VALOR é igual a 0.

No fonte do SPEDFISCAL, para geração do registro D197, a Query que busca informações da CDA, somente "traz" informações da CDA que tenham valor maior que zero.

No exemplo abaixo para o item 002 o campo CDA\_BASE foi gravado o valor de 0,01 e no campo CDA\_VALOR igual 0.  
  
![](https://totvssuporte.zendesk.com/attachments/token/2bAQHV0qcmYoeqC6YGeFJQlAR/?name=CDA_SPED.PNG)Por esse motivo, ao gerar o arquivo do SPEDFISCAL o valor de R$ 0,01 do item 002 foi desconsiderado gerando assim a diferença de 0,01 centavo no registro D197 conforme abaixo:

"|D197|SC10000070|não deu tempo.||4,29|20,00|0,87|0|"

Avaliando o Guia Pratico do SPED FISCAL o campo 5 do registro D197 não é de preenchimento obrigatório, logo não será apresentado erros na validação do arquivo. ​
