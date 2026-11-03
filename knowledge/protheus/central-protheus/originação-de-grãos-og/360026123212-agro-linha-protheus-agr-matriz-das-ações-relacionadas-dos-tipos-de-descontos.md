---
article_id: 360026123212
category: Originação de Grãos (OG)
content_hash: a54ce0fe47aa8a9a234f89fe23cf8e193f8550cba3b537124bc997fbb1e8cfe7
fetched_at: '2026-06-28T22:45:40.988633+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Matriz das ações relacionadas dos tipos de descontos
type: support-article
updated_at: '2025-04-10T14:00:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026123212-Agro-Linha-Protheus-AGR-Matriz-das-a%C3%A7%C3%B5es-relacionadas-dos-tipos-de-descontos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20415036770199)** Tempo aproximado para leitura: **00:01:50 min****Ocorrência**Na rotina **Tabelas de Classificação -** **AGRA035** são cadastrados os itens de **Desconto** **Análise** para as respectivas tabelas, e nas ações relacionadas dos **Itens de Desconto** há uma opção chamada **Matriz**. Como utilizá-la e para quê serve essa opção?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O objetivo dessa função é o de obter um resultado combinado de outras análises existentes.   
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Cadastrar um **Item de** **Desconto/Análise X** com a matriz do tipo **Linha**;

![MATRI.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7940883427991)

**2.** Cadastrar um segundo **Item de** **Desconto Análise** **Y** com a matriz do tipo **Coluna**;

![MATRI1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7940885140759)

**3.** Cadastrar um terceiro **Item de Desconto Análise** **Z** com a matriz do tipo **Resultado**. Esse **terceiro item** será uma combinação do item **X** e do item **Y**, concluindo em um **terceiro resultado combinado**;

![MATRI2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7940878324759)

**4.** Após cadastrar os **3 Itens de Desconto Análise** é necessário selecionar o item de **Resultado** e acionar a ação relacionada **Matriz**;

![MATRI3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7940888218135)

**5.** Conforme determinado nos **cadastros dos itens X e Y**, a **Acidez será definida pela Linha e a Umidade será definida pela Coluna**. O item **Resultado** será o valor informado na linha selecionada.  
Isso significa que sempre que o item correspondente à **Acidez X** estiver entre os valores de **1 a 5**, e o item de **Umidade** **Y** estiver entre os valores de **2 a 6**, o resultado combinado destes dois itens será **4**.

![MATRI4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7940889700119)
