---
article_id: 18493902627991
category: Escrita Fiscal - Impostos - IR
content_hash: d2fca933bd8d7e883dc3e9678b8d59567f62225828a1702919a0e892df34f8a4
fetched_at: '2026-06-28T22:39:31.860378+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Cálculo do IRRF pessoa
  física com deduções legais (Simplificado / INSS e Dependentes).
type: support-article
updated_at: '2025-10-28T11:40:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18493902627991-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-do-IRRF-pessoa-f%C3%ADsica-com-dedu%C3%A7%C3%B5es-legais-Simplificado-INSS-e-Dependentes
---

**Dúvida**Como configurar o Protheus para que ocorra o desconto simplificado na base de cálculo do IRRF, com posterior desconto da parcela dedutível para Pessoa Física utilizando a rotina Documento de Entrada?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Segue abaixo a configuração a ser utilizada:

Ajuste a tabela do progressiva do IRRF no Configurador (SIGACFG)**:**

Ambiente > Cadastros > Tabela IRRF:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31769571308311)

**CADASTROS:**

**NATUREZA (SED)**

Calcula IRRF (ED\_CALCIRF) = Sim

Porc. IRRF (ED\_PERCIRF) = 0,00

**FORNECEDOR (SA2)**

Cálculo IRRF (A2\_CALCIRF) = 1 - Normal

IRRF Prog (A2\_IRPROG) = Sim (Pessoa Física)

Vlr.Mín.IRRF (A2\_MINIRF) = 1 – Sim - O Sistema não considera o parâmetro MV\_VLRETIR

                                             2 – Não - O Sistema considera esse parâmetro.

**PRODUTOS (SB1)**

Impos Renda (B1\_IRRF) = Sim

Redução de IRRF (B1\_REDIRRF) - Caso haja redução

**PARÂMETROS**

**MV\_FMP1171 = .T.** (Indica se o IRRF de autônomos será calculado considerando o comparativo de dedução simplificada conforme a Medida Provisória 1.171/2023)

**MV\_FVL1171 = 607.20** (Valor da dedução simplificada do IRRF de autônomos conforme a MP 1.206/2024)

**MV\_VCTIRPF** - Indica se o título de IRRF (Pessoa Física) será gerado data de (E)missão, (V)encimento ou (C)ontabilização.

**MV\_ACMIRPF** - Indica se o título de IRRF (Pessoa Física) será gerado data de (E)missão, (V)encimento ou (C)ontabilização.

**MV\_AGLIMPJ** - Define forma de verificação da base do IRRF

                      1 = Apenas Filial Corrente (DEFAULT)

                      2 = Todas Filiais por CNPJ

                      3 = Todas Filias por raiz CNPJ (8 dígitos)

**MV\_VENCINS** – Parametrização do cálculo do vencimento dos títulos de INSS: 1 – Emissão, 2 – Vencimento Real;

**IMPORTANTE**

Caso seja necessário que o sistema realize a validação automática entre o valor do desconto simplificado do IRRF ou o valor do INSS na base do IRRF para pessoa física, realize os seguintes ajustes abaixo:

**NATUREZA (SED)**

Calcula INSS (ED\_CALCINS) = Sim

Porc. INSS (ED\_PERCINS) = 11% ou alíquota necessária

Ded. INSS (ED\_DEDINSS) = Sim

**FORNECEDOR (SA2)**

Calc. INSS (A2\_RECINSS) = Sim

Dependente (A2\_NUMDEP) = Quantidade de dependentes (informe o valor de dedução por dependente no parâmetro MV\_TMSVDEP). Este campo só pode ser acessado pelo Módulo Financeiro.

**PRODUTOS (SB1)**

Calcula INSS = Sim

**PARÂMETRO**

**MV\_INSIRF** - Define se o valor do INSS deve ser abatido da base de cálculo do IRRF no Financeiro.  
**1=Abate o valor**  
**2=Não abate**

**Documentação:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=784226438>

<https://tdn.totvs.com/pages/releaseview.action?pageId=531009057>

<https://www.totvs.com/blog/fiscal-clientes/nova-tabela-irpf-2025/>
