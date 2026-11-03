---
article_id: 32580547517591
category: eConsignado (Crédito do Trabalhador)
content_hash: 999b319f0acc6e072b6d250aa610796db950645fbfa8c537da5776183e90833d
fetched_at: '2026-06-28T22:43:07.179778+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Ao importar o arquivo Crédito do Trabalhador gera
  mensagem "A competência do arquivo não é igual a competência do parâmetro" Econsignado
  (MP1.292/2025)
type: support-article
updated_at: '2025-07-10T14:06:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32580547517591-RH-Linha-Protheus-GPE-Ao-importar-o-arquivo-Cr%C3%A9dito-do-Trabalhador-gera-mensagem-A-compet%C3%AAncia-do-arquivo-n%C3%A3o-%C3%A9-igual-a-compet%C3%AAncia-do-par%C3%A2metro-Econsignado-MP1-292-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32580576606871) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**  
Ao importar o arquivo Crédito do Trabalhador gera mensagem "A competência do arquivo não é igual a competência do parâmetro"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32580547477911)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Esse incidente pode ocorrer por dois motivos;

1° nos parâmetros foi selecionado competência diferente do arquivo do Crédito do Trabalhador baixado no portal Emprega Brasil.

2° o ambiente está desatualizado   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Atualizar o ambiente com o ultimo acumulado do portal - <https://suporte.totvs.com/portal/p/10098/download#000006>  
  
2**.** Verifique a competência no arquivo baixado do Portal Emprega Brasil;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32580576622615)  
  
3**.** Acesse a rotina de Importação do arquivo em **Miscelânea > Importação > Crédito do Trabalhador (GPEM944)** e **Altere** os parâmetros preenchendo a **competência conforme o arquivo**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33375437295511)

4**.** Selecione novamente o arquivo baixado no Portal Emprega Brasil e clique em **Importar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32580576635799)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32580576641047)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32580576643351)

**Saiba mais:**

[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)
