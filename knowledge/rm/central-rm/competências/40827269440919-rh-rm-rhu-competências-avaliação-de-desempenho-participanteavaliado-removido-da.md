---
article_id: 40827269440919
category: Competências
content_hash: 969d4d3a2f283f0e73365c2c5d844f941591fd61d55bc6624e1c9ee9157a6bcf
fetched_at: '2026-06-28T22:47:20.164526+00:00'
product: rm
section_id: 1500000861322
source: central-rm
title: 'RH - RM - RHU - Competências - Avaliação de Desempenho: Participante/Avaliado
  removido da configuração'
type: support-article
updated_at: '2026-05-29T19:14:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40827269440919-RH-RM-RHU-Compet%C3%AAncias-Avalia%C3%A7%C3%A3o-de-Desempenho-Participante-Avaliado-removido-da-configura%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40827269405335) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
O que fazer quando ao configurar a Avaliação de Desempenho, o seguinte erro é disparado: "Os Avaliados abaixo foram removidos pois não possuíam itens a serem avaliados"  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - Todas as versões  
  
**Solução**  
Durante o processo de configuração da Avaliação de Desempenho o sistema validará os **Itens a Avaliar** e por quais meios ele serão considerados, como, por Função, Seção, Funcionário entre outros.  
  
Nesse sentido, os Avaliados costumam ser removidos quando de acordo com a configuração efetuada na Avaliação de Desempenho não há nenhum item a ser avaliado para o Funcionário.   
  
Por exemplo: foi configurado para avaliar Competências, e na Função do Funcionário não foi feita associação de nenhuma Competência (mapa de competências).  
  
**O que deve ser validado**

**1. Verifique a configuração da Avaliação de Desempenho**

Confirme quais critérios estão sendo utilizados na Avaliação.

**Exemplo:**

A Avaliação foi configurada para avaliar:

* Competências Técnicas
* Competências Comportamentais
* Itens vinculados à Função do Funcionário

Nesse cenário, o sistema somente permitirá incluir Funcionários que possuam competências relacionadas à sua Função.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40827269410711)

**2. Verifique se existe relacionamento entre Competência e Função**

Acesse: **Aba Acompanhamento | Mapa de Conhecimento | Definição por Competências**

Valide se foi realizado o vínculo entre:

* Competência
* Função do Funcionário

Caso o relacionamento não exista, o sistema não localizará itens para avaliação e removerá o Avaliado da configuração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40827275648663)

**Exemplo prático**

A Avaliação está configurada para considerar:

* Competências Técnicas
* Competências Comportamentais

Além disso, as competências devem estar vinculadas à **Função** do Avaliado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40827275653399)

Funcionário incluído na Avaliação exerce a Função **Diretor**. Na Definição por Competências, existe a Competência:

* Análise e Solução de Problemas

Essa competência:

* Está vinculada à Função **Diretor**
* É do tipo **Comportamental**

Como a Avaliação está configurada para considerar Competências Comportamentais, o item será identificado corretamente e o Funcionário permanecerá na Avaliação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40827275658263)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40827269419287)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40827269420311)

**Saiba Mais:**

[RH - RM - RHU - Parametrizar Avaliação de Desempenho por Competência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020245752)

[RH - RM - RHU -  Quais são os tipos de avaliação da Avaliação de desempenho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021217531)
