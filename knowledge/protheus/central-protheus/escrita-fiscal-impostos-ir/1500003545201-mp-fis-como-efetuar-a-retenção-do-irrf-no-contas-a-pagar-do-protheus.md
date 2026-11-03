---
article_id: 1500003545201
category: Escrita Fiscal - Impostos - IR
content_hash: ec58ecf98e3549828ade3c3b832029f0d997a43b38104037d50605b1e857f64a
fetched_at: '2026-06-28T22:39:31.935462+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: MP - FIS - Como efetuar a retenção do IRRF  no Contas a Pagar do Protheus?
type: support-article
updated_at: '2021-04-28T13:48:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003545201-MP-FIS-Como-efetuar-a-reten%C3%A7%C3%A3o-do-IRRF-no-Contas-a-Pagar-do-Protheus
---

**Dúvida**Quais as configurações necessárias para que a retenção do IR seja feita no Contas a Pagar do Protheus?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Veremos baixo as configurações necessárias para que a retenção do IR seja feita no Contas a Pagar do Protheus.

### Cadastro do Fornecedor (MATA020)

Preencher os campos abaixo da seguinte forma:

**Cálculo IRRF (A2\_CALCIRF)** = Normal  
**IRRF Prog (A2\_IRPROG)** = SIM (Pessoa Física)  
**Vlr. Mín. IRRF (A2\_MINIRF)** = 1 – SIM- O Sistema não considera o parâmetro MV\_VLRETIR ou 2 – NÃO – O Sistema considera esse parâmetro.

![](http://anadi.com.br/wp-content/uploads/RETENCAO-IRRF-FORNECEDOR.jpg "Retenção IRRF fornecedor")

### 

### Cadastro do Produto (MATA010)

Preencher os campos abaixo da seguinte forma:

**Impos Renda (B1\_IRRF)** = SIM  
**Redução de IRRF (B1\_REDIRRF)** – \*Caso haja redução

![](http://anadi.com.br/wp-content/uploads/RETENCAO-IRRF-PRODUTO.jpg "Rentenção IRRF produto")

### 

### Cadastro de Natureza (FINA010)

Preencher os campos abaixo da seguinte forma:

**Calcula IRRF (ED\_CALCIRF) =** SIM  
**Percentual de cálculo de IRRF (ED\_PERCIRF)** = 1,0 / 1,5 por exemplo

![](http://anadi.com.br/wp-content/uploads/RETENCAO-IRRF-NATUREZA.jpg "Retenção IRRF natureza")

Se o fornecedor for Pessoa Física, o Sistema busca a alíquota da tabela de IRRF (CFX011) do configurador

**Assuntos relacionados:**

# Cálculo de IRRF - Tabela Progressiva

<https://tdn.totvs.com/pages/releaseview.action?pageId=6076801>
