---
article_id: 1500011221322
category: Escrita Fiscal - Impostos - ICMS
content_hash: f1fb36f0a61742a79c9fc5fe7bfcf333a7738541f2bdde290d5be28d45167bfc
fetched_at: '2026-06-28T22:39:24.034399+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Escrituação e Relatórios
  Fiscais - Como Configurar ICMS diferido coluna Outros para RS ?
type: support-article
updated_at: '2024-10-08T21:24:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011221322-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Escritua%C3%A7%C3%A3o-e-Relat%C3%B3rios-Fiscais-Como-Configurar-ICMS-diferido-coluna-Outros-para-RS
---

**Dúvida**Como Configurar ICMS diferido coluna Outros para RS ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Para atender esta legislação foi necessário criar um novo campo no cadastro de TES, o **Col ICMS Dif(F4\_COLVDIF).**Este campo é específico para as situações onde a parcela diferida do ICMS precisa ser demonstrada nas colunas ***Outros***ou ***Isento***do Livro Fiscal. Para as operações com diferimento que deverão demonstrar na coluna Outros ou Isento, basta configurar no cadastro de TES este novo campo com uma das opções disponíveis (**1=Outros ou 2=Isento**), já para as demais operações de diferimento sem esta necessidade, não deverá preencher este novo campo.

De forma resumida, uma vez este novo campo preenchido na operação com cálculo de diferimento parcial de ICMS, a parcela diferida será gravada em Outros ou Isento, e a base de cálculo será reduzida, mantendo somente o valor da parcela tributada.

**Exemplo de cálculo de Diferimento parcial, demonstrando a parcela diferida na coluna Outros (campo F4\_COLVDIF com opção 1=Outros):**

* Valor de Mercadoria : 100,00
* Percentual de Diferimento: 30,00%
* Alíquota do ICMS: 17%
* Parcela tributada: 100,00 - 30,00% = 70,00
* Parcela diferida: 100,00 - 70,00 = 30,00
* Base de Cálculo do ICMS: 70,00
* Valor do ICMS tributado: 70,00 \* 17% = 11,90
* Valor do ICMS diferido: 30,00 \* 17% = 5,10
* Valor da coluna Outros: 30,00

Desta forma, a base de cálculo fica reduzida, e a parcela não tributada será demonstrada na coluna Outros, muito embora seja operação com diferimento do ICMS, e não operação com redução de base de cálculo.

https://tdn.totvs.com/display/public/PROT/1106564+DSERFIS2-1953+DT+Diferimento\_ICMS\_Coluna\_Outras\_Rio\_Grande\_do\_Sul
