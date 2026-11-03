---
article_id: 360020113692
category: Cálculo
content_hash: 98b9bfb3b2b2198f9fa8f9982515ee6b6e3c2ac271192b980cd587f5988594e8
fetched_at: '2026-06-28T22:46:29.241732+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Considerar jornada noturna nas férias
type: support-article
updated_at: '2025-01-27T17:21:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020113692-RH-RM-PTO-Considerar-jornada-noturna-nas-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16780587894295) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**  
Como considerar a jornada trabalho noturna nas férias do funcionário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) -  Automação de Ponto - A partir da versão 11.80  
  
**Solução**Para considerar a jornada noturna do funcionário nas férias, siga os passos abaixo.

1. Acesse o espelho do funcionário e vá em **Processos**e selecione a opção **Parametrizar Sindicato**.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29533107350423)
2. Ao abrir o assistente, avance até a etapa **Solução de Conflitos** e na seção **Solução de Conflito de Férias** marque a opção **Substitui jornada planejada que iniciou nas férias.**  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29533107354391)
3. Recalcule o espelho do funcionário e verifique que a jornada noturna do funcionário que faz interseção com as férias vai considerada integralmente.  
   No caso abaixo as férias inicia no dia 07/01/2025, com o parâmetro **Substitui jornada planejada que iniciou nas férias marcado,** as horas trabalhadas serão calculadas ate o fim da jornada.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29533121896599)
4. Caso marque a opção **Considera apenas as férias,** e o cálculo da jornada trabalhada será realizado até 00:00hr.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29533107358871)  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29533121906071)  
    **Saiba Mais:**[Solução de Conflito de Férias, Afastamentos, Admissão e Demissão](https://tdn.totvs.com/pages/releaseview.action?pageId=452718985)
