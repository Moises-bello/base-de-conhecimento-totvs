---
article_id: 360040818134
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: deac30e0adfd3a6e6468908df99cdb9859dfbf6e34b6d3e59d8afbd6eeb649ee
fetched_at: '2026-06-28T22:42:00.783773+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: ' MP - FIS - Processo para geração do registro C176 - RESSARCIMENTO DE ICMS
  EM OPERAÇÕES COM SUBSTITUIÇÃO TRIBUTÁRIA (CÓDIGO 01, 55).'
type: support-article
updated_at: '2021-04-28T14:25:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040818134--MP-FIS-Processo-para-gera%C3%A7%C3%A3o-do-registro-C176-RESSARCIMENTO-DE-ICMS-EM-OPERA%C3%87%C3%95ES-COM-SUBSTITUI%C3%87%C3%83O-TRIBUT%C3%81RIA-C%C3%93DIGO-01-55
---

**Dúvida**Qual o processo para geração do registro C176 - RESSARCIMENTO DE ICMS EM OPERAÇÕES COM SUBSTITUIÇÃO TRIBUTÁRIA (CÓDIGO 01, 55)?

**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**Registro C176 - RESSARCIMENTO DE ICMS EM OPERAÇÕES COM SUBSTITUIÇÃO TRIBUTÁRIA (CÓDIGO 01, 55).

 Este registro deve ser informado quando da emissão de documento fiscal, destinado a outra unidade federada (UF deve ser diferente do MV\_ESTADO), que ensejará futuro pedido de ressarcimento de ICMS, em operações com produtos submetidos à substituição tributária na operação anterior. Aplica-se somente aos contribuintes domiciliados nos estados, cuja legislação obriga a emissão de nota fiscal para documentar processo de pedido de ressarcimento de ICMS/ST.

Para geração deste Registro, Segue configurações e passo a passo :

I. Ter primeiramente na base de dados a Nota de Compra onde foi calculado os impostos ICMS e ICMS - ST.

II. Realizar a venda (Mesmo produto da NF de entrada) que calcularam os impostos citados.

III - Alimentar a tabela CD0 para preencher os dados das notas fiscais de entrada em que houve o pagamento da Substituição Tributária. Esta tabela pode ser alimentada de 3 formas:

1 - Utilizando a rotina de Ressarcimento de ICMS ST (FISA132) para que o sistema preencha de forma automática a tabela CD0.

2 - Através do ponto de entrada MATUCOM. O ponto de entrada será executado no momento da gravação do documento de saída e deve ser configurado para buscar os dados da NF de entrada para que assim a CD0 seja alimentada com as informações corretas.

3 - Caso não utilize o ponto de entrada MATUCOMP, acessar a rotina NF Manual Saída (MATA920) e realizar o complemento realcionado a NF de Saída escriturada --> Ações Relacionadas --> Complementos -- > Complementos --> Compl. Ressarc. - > Preencher utilizando a NF de entrada.

**Observação:** se o processo foi realizado dentro da própria Unidade de federação o registro C176 não será gerado, como diz o guia prático: "...Este registro deve ser informado quando da emissão de documento fiscal, destinado a outra unidade federada".

Informações adicionais:

<https://tdn.totvs.com/display/public/PROT/ARQ0005_Gerar_Registro_C176_Do_SPED_FISCAL>

<https://tdn.totvs.com/display/public/PROT/FIS0005_SPED_FISCAL>
