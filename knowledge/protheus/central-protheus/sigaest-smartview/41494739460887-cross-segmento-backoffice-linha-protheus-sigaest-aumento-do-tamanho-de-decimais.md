---
article_id: 41494739460887
category: SIGAEST - SMARTVIEW
content_hash: 3fc95ece0f912febe7ee7bf6030e0d7f168385441a6a1df4cdd48a7d49010e24
fetched_at: '2026-06-28T22:38:47.039938+00:00'
product: protheus
section_id: 16108365627287
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Aumento do tamanho
  de decimais nos relatorios Smart View
type: support-article
updated_at: '2026-06-25T20:10:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41494739460887-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Aumento-do-tamanho-de-decimais-nos-relatorios-Smart-View
---

Os relatórios nativos do Smart View exibem apenas 2 casas decimais, ignorando o tamanho definido no dicionário de dados (SX3). Para aumentar decimais ou tamanho de campos, é necessário copiar e personalizar o relatório via Smart View, tornando-o customizado. Ajustes técnicos devem ser feitos com a equipe de suporte de Framework.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41494739443479) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como aumentar o tamanho de decimais dos relatórios no Smart View, visto que no dicionário de dados (SX3) existe um tamanho configurado, mas o relatório não reflete essa definição?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.2310

**Solução**

Os relatórios nativos do Smart View têm como objetivo a validação baseada no objeto de negócio. Dessa forma, eles **não validam o tamanho do campo estipulado no dicionário de dados (SX3)**, assumindo o padrão nativo do sistema de exibir apenas 2 (duas) casas decimais.

Caso deseje aumentar o tamanho dos campos ou o número de decimais, **você deverá copiar o relatório desejado através do próprio Smart View e importá-lo para realizar a personalização**, adequando a visualização às características necessárias da sua operação. É importante ressaltar que esse processo torna o relatório customizado.

**Exemplo Kardex Padrão:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41495196560919)

**Após Customizar:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41495237047575)

**E como fazer esse tipo de personalização?**

Detalhes e apoio técnico sobre como ajustar, aumentar, configurar campos e customizar os relatórios na ferramenta **devem ser tratados diretamente com a equipe de suporte de Framework**, independentemente do módulo de origem ao qual o relatório pertence.

**Mais detalhes:**

[Formatação de campos](https://tdn.totvs.com/pages/releaseview.action?pageId=684018378#Vis%C3%A3odeDados-Formata%C3%A7%C3%A3odecampos)

[Formatação de sumários](https://tdn.totvs.com/pages/releaseview.action?pageId=684018378#Vis%C3%A3odeDados-Formata%C3%A7%C3%A3odesum%C3%A1rios)

**Saiba mais:**

[Como configurar o SmartView](https://tdn.totvs.com/x/8WTCMQ)

[Clique aqui e veja mais artigos sobre Relatórios SmartView do Estoque Custos](https://tdn.totvs.com/x/pwKQLg)
