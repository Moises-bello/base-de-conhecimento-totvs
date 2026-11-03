---
article_id: 360018997531
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 48d04366753fcaa1af125bf1a15f9fea728dad37356c190a4d3278ecc193e80c
fetched_at: '2026-06-28T22:39:20.439847+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Complemento de ICMS
  ST para Venda
type: support-article
updated_at: '2023-03-17T14:10:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018997531-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Complemento-de-ICMS-ST-para-Venda
---

**Dúvida**Como realizar complemento de ICMS- ST para venda?  
   
 **Ambiente**

Protheus - Fiscal - Todas as versões.

**Solução**

Incluir um pedido de venda, informado que trata-se de um Complemento de ICMS.

No pedido de venda informe o código do produto da 1º nota e o valor do ICMS complementar nos campos valor unitário, valor total e ICMS Retido (C6\_ICMSRET).

**IMPORTANTE: NÃO deverá ser informado o valor da ST no campo ICM Retido (C6\_PICMRET). O correto é que seja informado o valor da ST no campo C6\_ICMSRET.**

É necessário amarrar a nota fiscal de origem através do campo N.F Original **(C6\_NFORI).**

**Configuração da TES:**

Credita ICMS **(F4\_CREDICM)** = Não  
Calcula ICMS **(F4\_ICM)** = Não  
Agrega Solidário **(F4\_INCSOL)** =  Não

Agrega Valor = Sim

L. Fiscal ICMS **(F4\_LFIMC)** = ICMS Zerado  
Sit.trib.ICMS **(F4\_SITTRIB)** = 10, 30, 70 e 90

Fórmula**(F4\_FORMULA)** = Amarrar uma fórmula com conteúdo texto = "Complemento" para que o sistema não destaca o ICMS normal nos livros, apenas o ICMS retido

Verificar a existência do campo **C6\_ICMSRET**.

Caso não exista, deve-se criar o mesmo utilizando o módulo configurador.

O campo deve ser criado com a seguinte característica:  
Nome: **C6\_ICMSRET**;  
Texto:**ICMS Retido**;   
Tipo: **Númerico**;   
Tamanho: **14**;   
Decimal: **4;**   
Formato:**99,999,999.99;**  
Validação: **MaFisGet("IT\_VALSOL")**

 Caso seja necessário destacar o valor da base de cálculo do ICMS ST na nota complementar deverá seguir o procedimento conforme orientado abaixo:

<http://tdn.totvs.com/display/public/PROT/576086+DSERFIS2-123+DT+BASE+DE+CALCULO+EM+NF+DE+COMPLEMENTO+DE+ICMS>
