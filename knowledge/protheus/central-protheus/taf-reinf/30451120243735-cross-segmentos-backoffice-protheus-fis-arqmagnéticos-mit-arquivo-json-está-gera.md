---
article_id: 30451120243735
category: TAF - REINF
content_hash: a19da9de1733488975c897fa6cd994ed96701c45d84a7c056ef958058d24dfcd
fetched_at: '2026-06-28T22:41:33.459567+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - MIT - arquivo
  Json está gerando com a tag "SemMovimento"= true
type: support-article
updated_at: '2025-03-17T21:47:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30451120243735-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-MIT-arquivo-Json-est%C3%A1-gerando-com-a-tag-SemMovimento-true
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30451120229783) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**MIT - Arquivo Json está gerando com a tag **"SemMovimento"= true.**  
**Ambiente**TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - A partir da versão 12.1.2310  
  
**Causa**Esse incidente ocorre quando é utilizado um tributo diferente dos tributos permitidos para geração do MIT.

**Solução**Para solucionar essa ocorrência, altere o campo **Cód.Tributo (T1A\_IDTRIB)** para um dos códigos permitidos e faça um novo teste:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30451089490327)

Segue os códigos permitidos para preencher a tag corretamente:

**000005** - 05 - IPI (IMPOSTO SOBRE PRODUTOS INDUSTRIALIZADOS)                                                                                                                                                                                                                   
**000006** - 06 - PIS/PASEP (PROGRAMA DE INTEGRACAO SOCIAL - PROGRAMA DE FORMACAO DO PATRIMONIO DO SERVIDOR PUBLICO)                                                                                                                                                              
**000007** - 07 - COFINS (CONTRIBUICAO PARA O FINANCIAMENTO DA SEGURIDADE SOCIAL)                                                                                                                                                                                                 
**000012** - 12 - IR (IMPOSTO DE RENDA EMISSÃO)                                                                                                                                                                                                                                   
**000018** - 18 - CSLL (CONTRIBUICAO SOCIAL SOBRE O LUCRO LIQUIDO)                                                                                                                                                                                                                
**000019** - 19 - IRPJ (IMPOSTO SOBRE A RENDA DE PESSOA JURIDICA)                                                                                                                                                                                                                 
**000027 -** 27 - CSLL RETENCAO (CONTRIBUICAO SOCIAL SOBRE O LUCRO LIQUIDO - RETENCAO)                                                                                                                                                                                          
**000028 -** 28 - IR (IMPOSTO DE RENDA PAGAMENTO)                                                                                                                                                                                                                                 
**000035 -** 34 - IOF (IMPOSTO SOBRE OPERAÇÕES FINANCEIRAS)                                                                                                                                                                                                                       
**000036 -** 35 - RET (RET UNIFICADO)                                                                                                                                    -                                                                                                          
**000037 -** 36 - CPSS (CONTRIBUIÇÃO DO PLANO DE SEGURIDADE SOCIAL)                                                                                                                                                                                                               
**000038 -** 37 - CONTRIBUIÇÕES DIVERSAS

Importante: Mesmo que no movimento o tributo seja por exemplo Pis ou Cofins Importação, deve ser utilizado obrigatoriamente os códigos 06(Pis) ou 07(Cofins) pois o que a Receita Federal irá considerar será o tributo x Código de Receita que está sendo encaminhado no arquivo.
