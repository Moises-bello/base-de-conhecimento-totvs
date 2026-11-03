---
article_id: 360021322392
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 0f041f46212f8f284fe5569d6d61d684884fc81b9475adecc27b4a165dc1104f
fetched_at: '2026-06-28T22:39:30.522423+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Cálculo FASE MT
type: support-article
updated_at: '2021-07-29T14:38:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021322392-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-FASE-MT
---

**Dúvida**

Configuração para gerar o calculo do FASE MT  
   
**Ambiente**

Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**

Para que o calculo seja efetuado corretamente se atentar a configuração abaixo:

Parâmetro:MV\_INDUPF -  Informe o campo que deve ser utilizado da tabela SM2 para informar o indexador  UPF/MT. Ex: M2\_MOEDA5  
  
Em seguida cadastrar a moeda na tabela SM2  
  
Cadastro de Produto: deverá produto preencher os campos: B1\_AFASEMT  = Alíquota, B1\_UM ou B1\_SEGUM = KG  
  
Cadastro cliente/fornecedor: A2\_RFASEMT ou A1\_RFASEMT  
  
Cadastro de TES  
F4\_CFASE = 1 (SIM)
