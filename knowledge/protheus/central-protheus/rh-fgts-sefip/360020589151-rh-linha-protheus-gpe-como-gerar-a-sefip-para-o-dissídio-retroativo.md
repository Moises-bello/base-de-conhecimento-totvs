---
article_id: 360020589151
category: RH - FGTS / SEFIP
content_hash: f1009b097556f49799d1f5c28bf152b0e3a2ba1960261aedf47f529e71722d63
fetched_at: '2026-06-28T22:43:41.374656+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar a Sefip para o dissídio retroativo
type: support-article
updated_at: '2025-08-07T13:38:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020589151-RH-Linha-Protheus-GPE-Como-gerar-a-Sefip-para-o-diss%C3%ADdio-retroativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34012871243415) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como gerar a SEFIP referente ao dissídio retroativo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**  
Os valores de dissídio são levados exclusivamente para **SEFIP código 650**, ou seja, é necessário gerar uma SEFIP padrão da folha de pagamento (recolhimento: 115, 150,155, etc) e outra **SEFIP apenas com os valores de dissidio** seguindo as orientações abaixo:  
![image2016-2-10_10_37_59.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016476712)  
  
Além do grupo de perguntas, é importante verificar se há **valores gerados de dissídio na folha** **de** **pagamento** e para isso segue quais os **identificadores de cálculo** o sistema irá consultar:

\* Coluna "Remun. sem 13o" (FGTS):  considerar o valor da verba do **ID 0337**.  
\* Coluna "Remun. sobre 13o" (FGTS):  considerar o valor da verba do **ID 0398**.   
\* Coluna "Base INSS Fol" (INSS):  considerar o valor da verba do **ID 0338.**   
\* Coluna "Base INSS 13o" (INSS): considerar o valor da verba do **ID 0399**.   
\* Coluna "Desc. INSS" (INSS): considerar o valor da verba do **ID 0340**.  
  
Ao confirmar os parâmetros para geração da SEFIP o sistema irá gerar o **log de ocorrências**, nele é possível confirmar os dados informados no grupo de perguntas, verificar o conteúdo do parâmetro **MV\_SOMAVIS**, conferir a **regra para conferência** da sefip, **funcionários sem pis** e **valores** gerados por funcionário.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406033330199)  
  
Mantenha o **ambiente sempre atualizado**, segue *link* para *download* da expedição continua do RH:<https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO>.

**Saiba Mais:**[RH - FGTS /SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
