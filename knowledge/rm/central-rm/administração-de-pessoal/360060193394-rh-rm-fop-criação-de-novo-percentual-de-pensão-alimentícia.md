---
article_id: 360060193394
category: Administração de Pessoal
content_hash: 30f3f3a93661801f84f4beb9f1ee924da9c386eb081d8443eb8487faee9744ad
fetched_at: '2026-06-28T22:47:02.211380+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Criação de novo percentual de Pensão Alimentícia
type: support-article
updated_at: '2025-03-13T11:07:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060193394-RH-RM-FOP-Cria%C3%A7%C3%A3o-de-novo-percentual-de-Pens%C3%A3o-Aliment%C3%ADcia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:50 min  
  
Dúvida**Como criar um novo percentual de Pensão Alimentícia?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Em Administração de Pessoal, vá até: Cadastros Globais | Tabelas Dinâmicas. Certifique-se de que o **Sistema** desta aba esteja identificado como **Folha de Pagamento**. Na tabela INT45, crie o registro com o nome que irá identificar o novo valor percentual em dependentes, conforme demonstrado na imagem abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/IgM83hui229DEk4oyfLNrtgLd/?name=inline-735349417.png)  
  
Após isso, em dependentes, conforme captura de tela abaixo:

1. Coloque o Percentual desejado;
2. Selecione o nome da criado em Tabelas Dinâmicas;
3. Se for baseado sobre o valor do Salário Mínimo, associar fórmula com [função SM](https://tdn.totvs.com/pages/releaseview.action?pageId=452719340) em Fórmulas de Cálculo. Caso a fórmula já traga o valor total do desconto, o campo Percentual terá de ser 100%.

![](https://totvssuporte.zendesk.com/attachments/token/TAR41U7uMdJTkrrt6N3XxnOYN/?name=inline1655771204.png)  
  
**Importante**- O suporte padrão não presta suporte para manutenção ou criação de formulas. Consulte o seu TI ou nos identifique no ticket que necessita de apoio da consultoria para tal demanda;  
- Para desconto com percentuais com valores, diferentes há de ser adequado por fórmulas também;  
- Caso ainda não esteja aparecendo a aba Dados da Pensão, na própria janela de dependentes, clique em incidências e marque a flag **Pensão**.  
**Saiba mais**[Parametrização para cálculo de Pensão Alimentícia no RM Labore](https://tdn.totvs.com/pages/viewpage.action?pageId=272420775)
