---
article_id: 4412681997335
category: RH - Ambiente
content_hash: f515c261c6dd3f7e60ac0d8c3d9be352a6495954f3a3446ed9d5c0c3e1a73cd0
fetched_at: '2026-06-28T22:43:09.559415+00:00'
product: protheus
section_id: 20669342808471
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada da rotina Controle Dias de Direito
  - GPEA050
type: support-article
updated_at: '2026-06-24T17:24:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412681997335-RH-Linha-Protheus-GPE-Ponto-de-Entrada-da-rotina-Controle-Dias-de-Direito-GPEA050
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32880346290455) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ponto de Entrada da rotina **Controle Dias de Direito - GPEA050.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A rotina **GPEA050** foi desenvolvida em **MVC**, portanto, possui um **ponto de entrada único**, que pode ser chamado em vários momentos de acordo com a necessidade, e faz com que a customização desta forma se torne mais segura.  
  
Para os **fontes em MVC**, o ponto de entrada deve ser uma ***User Function*** **e ter como nome o ID do Modelo de Dados (*Model*) do fonte**, e por padrão, o nome do modelo é o mesmo do arquivo.  
  
O ponto de entrada criado recebe via parâmetro **PARAMIXB** um vetor com informações referentes a rotina. Estes parâmetros variam para cada situação, em comum todos eles tem os três primeiros elementos.  
Abaixo, temos as posições do array de parâmetros **comuns a todos os IDs:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32880367643927)  
  
Os **IDs do local de execução** do ponto de entrada padrão do MVC (2ª posição), podem ser verificados na documentação **[Pontos de Entrada para fontes Advpl desenvolvidos utilizando o conceito MVC](https://tdn.totvs.com/display/public/framework/Pontos+de+Entrada+para+fontes+Advpl+desenvolvidos+utilizando+o+conceito+MVC).**Os **IDs dos formulários** (3ª posição) dos modelos de dados do MVC para a rotina Controle Dias de Direito, são:  
**> GPEA050\_SRA** (dados do funcionário)  
**> GPEA050\_SRF** (dados dos períodos aquisitivos e dias de direito)  
**> GPEA050\_RHI** (manutenção de dados na tabela RHI que é utilizada pelo Mercado Internacional)  
  
  
**Saiba Mais:**  
[ADVPL - Fontes em MVC](https://tdn.totvs.com/display/public/PROT/Fontes+em+MVC#Modulos-RH)
