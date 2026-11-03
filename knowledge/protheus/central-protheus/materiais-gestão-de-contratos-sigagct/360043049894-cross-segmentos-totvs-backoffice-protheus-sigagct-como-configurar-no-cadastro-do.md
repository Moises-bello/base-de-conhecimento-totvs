---
article_id: 360043049894
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: bc866c5e7e7d315306059acf0846863e22523c0b3ca0a733f31f1ab888fb7442
fetched_at: '2026-06-28T22:37:21.470423+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como configurar no
  Cadastro do Contrato (CNTA300) Naturezas distintas por planilhas do contrato ?
type: support-article
updated_at: '2022-02-07T19:49:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043049894-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-configurar-no-Cadastro-do-Contrato-CNTA300-Naturezas-distintas-por-planilhas-do-contrato
---

**Dúvida**

Como configurar no Cadastro do Contrato (CNTA300) Naturezas distintas por planilhas do contrato ?  
  
**Ambiente**Protheus – Gestão de Contratos – A partir da versão 12.1.27  
  
**Solução**

Permitir que o usuário escolha naturezas diferentes para cada planilha do contrato.

O sistema foi ajustado para permitir que o usuário informe a natureza na planilha através do campo Natureza (**CNA\_NATURE**), ao invés de obter sempre do cabeçalho do contrato (**CN9\_NATURE**).

A natureza é buscada inicialmente na planilha, não sendo informada na planilha, será obtida do contrato. Essa regra vale para geração de qualquer título e para pedidos de venda.

**Importante**

O novo campo Natureza **(CNA\_NATURE)** será disponibilizado oficialmente apenas no release **12.1.33.**

Para utilização desta melhoria antecipadamente, o usuário deverá criar o campo através do configurador. O campo **CNA\_NATURE** deve ter as mesmas propriedades (tipo, tamanho, consulta padrão e validação) do **CN9\_NATURE.**

***Saiba Mais:***

[8193373 DMANMAT02-25768 DT Naturezas distintas por planilhas de um contrato](https://tdn.totvs.com/display/PROT/8193373+DMANMAT02-25768+DT+Naturezas+distintas+por+planilhas+de+um+contrato)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
