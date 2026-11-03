---
article_id: 360016083291
category: Financeiro - Contas a Pagar
content_hash: b400a1ca2884b178a3eb30f716c488f591bec59c73c63669063c3db3aa3afb33
fetched_at: '2026-06-28T22:38:08.469540+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  FINA870 - Não exibe
  os impostos na aglutinação
type: support-article
updated_at: '2024-08-26T13:36:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016083291-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA870-N%C3%A3o-exibe-os-impostos-na-aglutina%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25908980508823)**Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**No módulo **FINANCEIRO** selecione a rotina **FINA870 (Emissão GPS)**, ao realizar **aglutinação dos títulos gerados de INSS** o sistema não exibe nenhum lançamento.  
   
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**

**1)** Verifique se no cadastro da natureza está conforme a imagem abaixo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25908980515223)

**2)** Verifique se no cadastro do fornecedor está conforme a imagem abaixo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25908934149783)

**3)** Verifique se o tipo do título é:  
**'INS','INA', 'INP',** pois somente esses tipos que serão considerados na rotina **FINA870 - Emissão de****GPS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25908980522391)

**4)** O título PAI (gerador do imposto) do tipo NF / BOL e etc..., e verifique se o campo **E2\_RETINS** possui conteúdo referente ao código de retenção. Pois é obrigatório essa informação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25908934154263)

**5)** Se a origem do título tipo NF (titulo pai) tem que ser **diferente** da rotina FINA870

E2\_ORIGEM<> FINA870

**6)** Títulos de impostos (do tipo  **'INS','INA', 'INP'**) inclusos manualmente sem ter sido gerado através de uma NF/BOL ou etc...., não serão aglutinados, pois é necessário ter um título pai.
