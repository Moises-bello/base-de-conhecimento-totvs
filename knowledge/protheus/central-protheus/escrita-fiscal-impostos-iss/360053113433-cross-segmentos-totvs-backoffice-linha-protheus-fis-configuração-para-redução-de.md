---
article_id: 360053113433
category: Escrita Fiscal - Impostos - ISS
content_hash: a0e4d200ab5045e453df59f6289ff3333b1ddefbf39f7a413a44bfb53cb80cb3
fetched_at: '2026-06-28T22:39:35.225115+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Configuração para
  Redução de Base de cálculo do ISS
type: support-article
updated_at: '2021-06-15T13:24:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053113433-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-para-Redu%C3%A7%C3%A3o-de-Base-de-c%C3%A1lculo-do-ISS
---

**Dúvida**Qual a configuração para a correta redução da Base de ISS ?  
  
**Ambiente**  
Microsiga Protheus– Livros Fiscais– A partir da versão 11.80  
  
**Solução**

Configurar o parâmetro abaixo:

**MV\_DBRDIF** = .F.  
Indica se o valor do ICMS/ISS a ser deduzido, quando o campo F4\_AGREG = D ou R , deverá ser sobre o  
valor da base reduzida ou valor de redução da base.

Preencher os campos abaixo no Cadastro de Produtos:

**Aliq. ISS (B1\_ALIQISS)** = preencher com a alíquota do imposto.

**Cod. Serv. ISS (B1\_CODISS)** = preencher com o código de Serviço.

Preencher os campos no Cadastro do Fornecedor

**Recolhe ISS (A2\_RECISS)** = N - Não

Preencher os campos abaixo no Cadastro do TES

**Calculo ISS (F4\_ISS)** = S - Sim

**L. Fiscal ISS (F4\_LFISS)** = T - Tributado

**Agrega Valor (F4\_AGREG)** = D - Ded IC V.Ct

**%Red. do ISS (F4\_BASEISS)** = Define o percentual da base de ISS para o caso de existir base reduzida.

 Configurar Natureza para reter ISS 

**Calcula ISS**(ED\_CALCISS) = **Sim**

Informações Adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=6076798>

<https://tdn.totvs.com/pages/releaseview.action?pageId=235571086>
