---
article_id: 360015653632
category: Rescisão
content_hash: b0fcd17680ca90c18ec8fc0ec144138865ff40fbc0773017e7a79d24bb3e2ba0
fetched_at: '2026-06-28T22:46:55.396791+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - TRCT: Preenchimento do campo 21 do relatório'
type: support-article
updated_at: '2026-05-28T15:06:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015653632-RH-RM-FOP-TRCT-Preenchimento-do-campo-21-do-relat%C3%B3rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**Como preencher o campo 21 do relatório TRCT?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento  - Todas as versões  
  
**Solução**Para o preenchimento do campo 21 do relatório Termo de Rescisão de Contrato (TRCT), **Pelo Vínculo da RAIS**, o sistema irá fazer a seguinte validação:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8865615272599/mceclip1.png)

Será considerado o campo **Vínculo da RAIS** disponível na aba **RAIS** no cadastro dos funcionários em **Administração de Pessoal | Funcionários.**Seo campoestiver preenchido com  4, 5, 9 ou 0, será levado o tipo de contrato 3 - Contrato de Trabalho por prazo determinado sem cláusula assecuratória de direito recíproco.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8865617135255/mceclip2.png)

Os demais **Vínculos da RAIS** (1, 2, 3, 6, 7, 8 e 10) correspondem ao **Contrato de trabalho por prazo indeterminado**.  
  
Parametrizando o TRCT para considerar o Vínculo da RAIS, o sistema não levará o Tipo de Contrato 2, somente o 1 e o 3.  
  
Para que seja levado o Tipo de Contrato 2 - Contrato de trabalho por prazo determinado com cláusula assecuratória de direito recíproco de rescisão antecipada, deverá utilizar a parametrização por fórmula.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8865652407319/mceclip3.png)  
  
**Saiba Mais**  
[Parametrização TRCT](https://tdn.totvs.com/pages/releaseview.action?pageId=42042615)
