---
article_id: 19368148908439
category: RH - Folha de Pagamento
content_hash: 26598290e5322b762d4257f46a053bc3e66cf8d9ebe95fd869964df55b1ad2bc
fetched_at: '2026-06-28T22:44:12.124218+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo do roteiro RTF - Folha Retificadora é finalizado
  com a  fórmula S_VLDPDRTF
type: support-article
updated_at: '2025-09-15T19:41:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19368148908439-RH-Linha-Protheus-GPE-C%C3%A1lculo-do-roteiro-RTF-Folha-Retificadora-%C3%A9-finalizado-com-a-f%C3%B3rmula-S-VLDPDRTF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19368148870935) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao calcular roteiro RTF, sistema finaliza o cálculo com o log:  
Calculo Finalizado Pela FinalCalc() ou Pela EndCalc() - S\_VLDPDRTF  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19368135296023)  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**O erro é apresentado quando não existe verbas relacionada a um ou mais dos IDs **1658, 1659** e **1660.**  
  
**Solução**Crie verbas conforme orientação abaixo e relacione aos IDs **1658, 1659 e 1660** na rotina de **Verbas** pelo caminho **>Atualizações >Definições cálculos >Verbas:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19368119244439)

**Saiba mais**  
[Manual do Roteiro RTF - Retificação da folha de pagamento](https://tdn.totvs.com/pages/viewpage.action?pageId=829317568)
