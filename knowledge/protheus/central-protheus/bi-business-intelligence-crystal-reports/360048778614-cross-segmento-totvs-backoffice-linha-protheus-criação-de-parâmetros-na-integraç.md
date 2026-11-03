---
article_id: 360048778614
category: BI - Business Intelligence - Crystal-Reports
content_hash: 58686a49b48aae38c10ac5ed624d1cd6ff076ee12285f63554e2e5aededf8783
fetched_at: '2026-06-28T22:40:29.047975+00:00'
product: protheus
section_id: 1500001548282
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - Criação de Parâmetros na
  Integração com o Crystal Reports
type: support-article
updated_at: '2022-07-27T18:28:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048778614-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Cria%C3%A7%C3%A3o-de-Par%C3%A2metros-na-Integra%C3%A7%C3%A3o-com-o-Crystal-Reports
---

![](https://jiratdncdncontent.blob.core.windows.net/tdn/icons/time.png) Tempo aproximado para leitura: **2****minuto****Dúvida**Quais as principais regras para criação de parâmetros na Integração com**Crystal Reports?****Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – BI – A partir da versão 11.8  
  
**Solução**Para utilizar parâmetros no relatório do **Crystal Reports** da mesma maneira que no **Microsiga Protheus®** através do cadastro de perguntas, siga os seguintes passos:

* O nome do relatório criado no **Crystal Reports** deve ter no máximo 6 caracteres.
* Crie no seu relatório **Crystal Reports** os parâmetros desejados, associando a eles uma condição de filtro ou uma fórmula;
* No cadastro de perguntas do **Microsiga Protheus®** deve ser criada uma pergunta para cada parâmetro do relatório, respeitando as seguintes regras:
  + O grupo de perguntas deve ser o nome do relatório sem a extensão.
  + As perguntas devem ser criadas na mesma ordem de criação dos parâmetros do relatório. Ou seja, as únicas ligações entre as perguntas do **Microsiga Protheus®** e os parâmetros do relatório são a **ORDEM** e o **GRUPO** definidos no cadastro de perguntas do Sistema. Desta forma, o primeiro parâmetro criado no relatório será preenchido pelo conteúdo informado para a pergunta de ordem 01 e assim sucessivamente.

**Observações**Recomendamos que o nome do relatório seja colocado em caixa alta, bem como a pergunta criada no **Microsiga Protheus®**
