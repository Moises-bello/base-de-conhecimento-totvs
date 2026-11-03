---
article_id: 38128626539799
category: RH – DIRF
content_hash: 23b9ed8c1399f586b35cd05dc791ae9ae01100a34913fc7cc5d723e5a4577abe
fetched_at: '2026-06-28T22:44:07.056902+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Melhoria na Ficha Financeira para DIRF x eSocial
type: support-article
updated_at: '2026-02-03T16:44:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38128626539799-RH-Linha-Protheus-GPE-Melhoria-na-Ficha-Financeira-para-DIRF-x-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38128651381399) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual foi a Melhoria implementada na Ficha Financeira para a Conferência da DIRF x eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2310  
  
**Solução**  
Incluídos os Códigos de Incidência IRRF e FGTS utilizados no eSocial na Ficha Financeira, para facilitar nas conferências dos valores do Informe de Rendimento.

Para esta implementação, é necessário aplicar o pacote RH Expedição Contínua abaixo:

12.1.2310: <https://suporte.totvs.com/portal/p/10098/download#detail/1123885>  
**Importante:** **O pacote para o release 12.1.2310 deve ser aplicado SOMENTE para clientes com Garantia Estendida.**

12.1.2410: <https://suporte.totvs.com/portal/p/10098/download#detail/1170810>

12.1.2510:  <https://suporte.totvs.com/portal/p/10098/download#detail/1221795>

Na impressão da Ficha Financeira (tanto no modelo padrão quanto no SmartView) serão impressas as colunas:

5- Cd. Inc. IRRF (campo RV\_INCIRF)

6- Cd. Inc. Fgts (campo RV\_INCFGTS)

Para emitir o Relatório de Ficha Financeira, acesse:

1. Acesse: Relatórios > Lançamentos > Ficha Financeira (GPER270 ou GPERSV270 para emissão via Smart View), clique em Outras Ações e Parâmetros, e Preencha as perguntas para emissão da Ficha Financeira.
2. Caso a pergunta "Impr. Incidências?" seja preenchida com Sim,  selecione as Incidências conforme a sua demanda:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38128626526103)
3. Será gerada a Ficha Financeira, com as colunas 5 e 6, com o Código de Incidência IRRF (RV\_INCIRF) e FGTS (RV\_INCFGTS):  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38128626527255)

**Saiba mais**  
✔️ <https://tdn.totvs.com/display/public/PROT/DT+Ficha+Financeira>    
✔️[RH - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
