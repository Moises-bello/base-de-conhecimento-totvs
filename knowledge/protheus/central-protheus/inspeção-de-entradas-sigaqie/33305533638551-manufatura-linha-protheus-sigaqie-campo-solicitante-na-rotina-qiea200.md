---
article_id: 33305533638551
category: Inspeção de Entradas (SIGAQIE)
content_hash: 4623742920aab8cf6683bf6956cd22c27ad6f3ebf7f83a18f3debd0ba803a2ae
fetched_at: '2026-06-28T22:42:26.916576+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Campo Solicitante na rotina QIEA200
type: support-article
updated_at: '2025-07-07T20:12:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33305533638551-Manufatura-Linha-Protheus-SIGAQIE-Campo-Solicitante-na-rotina-QIEA200
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33305502521751) Tempo aproximado para leitura: **00:00:30 min**  
  
**Dúvida**  
Na rotina **QIEA200 - Entradas**, o campo **Solicitante** está bloqueado para preenchimento. Como habilitar?  
  
**Ambiente**  
Totvs Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Solução**  
Na rotina **QIEA200** o campo **Solicitante - QEK\_SOLIC** somente estará disponível para preenchimento quando a situação do fornecedor informada na rotina **MATA061 - Amarração Produto x Fornecedor** for igual a **C - Pré-Qualificada**. Para outras situações de fornecedor, não é possível preencher este campo.  
A documentação do campo **Solicitante** encontra-se em [Solicitante/Nome do Solicitante (QIEA200 - SIGAQIE)](https://tdn.totvs.com/pages/releaseview.action?pageId=306860210)  
  
**Observação**  
Caso não opte por não manter este comportamento do módulo, você poderá alterar via dicionário de dados, apagando o conteúdo **A200WhSo()** no campo **X3\_WHEN** do campo **QEK\_SOLIC**.
