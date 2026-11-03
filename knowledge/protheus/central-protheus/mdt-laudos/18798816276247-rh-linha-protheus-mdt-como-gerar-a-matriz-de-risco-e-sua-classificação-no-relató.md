---
article_id: 18798816276247
category: MDT - Laudos
content_hash: fdc5fa19d80c2b658f679dc1123046bb224f88855b4720f07a39a82d0914f0b1
fetched_at: '2026-06-28T22:44:26.239103+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar a matriz de risco e sua classificação
  no relatório PGR
type: support-article
updated_at: '2024-11-06T12:14:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18798816276247-RH-Linha-Protheus-MDT-Como-gerar-a-matriz-de-risco-e-sua-classifica%C3%A7%C3%A3o-no-relat%C3%B3rio-PGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18798816211607) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como gerar a matriz de risco e sua classificação no relatório PGR?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Incluir um Laudo, através da rotina **Atualizações - Laudos - Laudos** *(MDTA210)* onde o campo de **Tipo Laudo (TO0\_TIPREL)** seja igual a **6-PGR** e deve incluir o atalho em questão na pasta de **Conteúdo**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18798857201559)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18798828502167)

Incluir um **Risco,** na rotina **Atualizações - PPRA - Riscos** (*MDTA180*) e preencher os campos obrigatórios e os demais campos:  
  
**Mapa risco diferente de 1-CIPA/CIPATR (TN0\_MAPRIS)****Dt. Avaliação (TN0\_DTAVAL)****Ambiente (TN0\_CODAMB)****Qtd. Agente (TN0\_QTAGEN)****Tipo Exposic. (TN0\_INDEXP)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18798840766999)**E também os campos:  
  
**MDTA180 - Severidade (TN0\_SEVERI)  
MDTA180 - Probab. (TN0\_PROBAB)  
MDTA180 - Classif. (TN0\_CLASSI)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18798832327959)**

Vincular o risco ao laudo, ainda na rotina de Riscos clique em Outras Ações -  **Relacionamentos** e na aba de **Laudo** vincular o código e preencher o campo de **Recomendação.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18798828508695)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18798816225047)**Caso queira incluir **Plano de Ação**, preenche a aba Planos de Ação:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18798857220119)

Realizado as parametrizações, para gerar o **Relatório PGR** acesse a rotina **Relatórios - PPRA - Rel. Geral PGR** *(**MDTR851).*Preencha as informações de acordo com a necessidade. Nos parâmetros, a pergunta "Imprimir matriz de risco?", ao selecionar "No final", serão impressas informações adicionais referentes matriz de risco.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18798816235287)  
  
Neste exemplo, estou utilizando a opção "Gráfico".  
Será apresentado neste formato:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18798857227927)  
  
Matriz de Risco:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18798828522519)

**Observação:** Será apresentado o campo de classificação no risco, nos modelos "Padrão" e "Gráfico".  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Consulte os atalhos disponíveis no relatório PGR](https://tdn.totvs.com/pages/viewpage.action?pageId=667375614)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
