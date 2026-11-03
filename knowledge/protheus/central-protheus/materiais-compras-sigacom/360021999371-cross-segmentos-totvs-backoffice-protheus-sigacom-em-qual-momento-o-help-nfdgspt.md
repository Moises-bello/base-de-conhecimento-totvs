---
article_id: 360021999371
category: Materiais - Compras (SIGACOM)
content_hash: 86c011384f5b987268cc42f0153116540ba47729f05e24c5e105f4d47b546a83
fetched_at: '2026-06-28T22:41:08.839809+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Em qual momento o help 
  NFDGSPTZ  é apresentado, no retorno da nota fiscal.
type: support-article
updated_at: '2022-05-12T21:13:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021999371-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Em-qual-momento-o-help-NFDGSPTZ-%C3%A9-apresentado-no-retorno-da-nota-fiscal
---

**Dúvida** Em qual momento o help  NFDGSPTZ  é apresentado, no retorno da nota fiscal.  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
  
**Solução**O Help em questão (NFDGSPTZ), só é apresentado  quando sua nota de origem já foi totalmente Devolvida.

![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018724831/Sem_t_tulo.png)

A verificação quanto a devolução total da nota pode ser realizada da seguinte forma:  
• Localizar na SD2 a nota original (remessa), e verificar o valor do campo D2\_IDENTB6, este Campo é utilizado quando a nota controla poder de terceiros e relaciona o registro da SD2 com os Registros na SB6.  
• Na SB6, utilizar o valor encontrado para D2\_IDENTB6 e filtrar pelo campo B6\_IDENT.  
• Após o filtro serão apresentados os registros do controle de poder de terceiros, de remessa e de devolução. Destes registros filtrados, identificar o registro de remessa (ele tera B6\_DOC+B6\_SERIE+B6\_CLIFOR+B6\_LOJA iguais ao da nota de remessa e o campo B6\_`PODER3=R).  
• Neste registro o campo B6\_SALDO estará zerado por este motivo o help é apresentado, pois a Nota já foi retornada.  
• A partir deste filtro é possível identificar as notas de retorno. Todos os registros onde B6\_PODER3=D são notas de devolução de poder de terceiros.  
  
  
Saiba Mais:   
[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM)
