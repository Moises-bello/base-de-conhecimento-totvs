---
article_id: 39762111114007
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 62ea921904e314532424acd717f48ff7274734b92ea55f8bab79cc799f65f17c
fetched_at: '2026-06-28T22:39:51.274754+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Ponto de Entrada
  para os ítens da DUIMP (EICLP500).
type: support-article
updated_at: '2026-04-20T13:36:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39762111114007-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-Entrada-para-os-%C3%ADtens-da-DUIMP-EICLP500
---

O SIGAEIC possui Ponto de Entrada para a rotina de Itens da DUIMP (EICLP500) no padrão MVC. Para implementar, deve-se criar um arquivo fonte, declarar a User Function "eiclp500" e receber o vetor de informações "PARAMIXB". As três primeiras posições do vetor indicam o objeto, o local de execução e o formulário, permitindo validar e aplicar customizações nos itens da DUIMP.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39762111103895) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
O SIGAEIC possui Ponto de Entrada para a rotina de ítens da DUIMP (EICLP500)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - a partir da versão 12  
  
**Solução**  
A rotina de Itens DUIMP (EICLP500) possibilita somente a utilização de Pontos de Entrada no Padrão MVC.

Para realizar a implementação, é necessário criar um único fonte (por exemplo, "**EICLP500\_RDM.prw**"), onde deverá ser declarada a User Function "**eiclp500**". Durante a execução, o Ponto de Entrada recebe um vetor com as informações da aplicação através do parâmetro "**PARAMIXB**".

Os três primeiros elementos deste vetor são padrão para todas as situações de chamada do MVC:  
Posição 1: Objeto do formulário ou do modelo, conforme o caso;

Posição 2: ID do local de execução do ponto de entrada no padrão MVC;

Posição 3: ID do formulário (models de dados utilizados na View da DUIMP, como SWDDEFAULT, SWEDETAIL, etc.).  
  
**Passos:**  
Crie um novo arquivo fonte em seu projeto (exemplo sugerido: "**EICLP500\_RDM.prw**").

Declare a Função de Usuário com o nome padrão exigido pela rotina: "**User Function eiclp500()"**.

Identifique o recebimento do parâmetro com a variável local que receberá o array padrão "**PARAMIXB"**.

Realize a validação das posições do array (posições 1, 2 e 3) para identificar qual ação, objeto ou formulário está acionando o Ponto de Entrada (ex: validando o ID do local de execução).

Aplique as regras de customização desejadas para os itens da DUIMP e compile o fonte no ambiente.  
  
  
  
**Saiba mais:**  
[**PE EICLP500 Ponto de Entrada Itens DUIMP – Padrão MVC**](https://tdn.totvs.com/pages/releaseview.action?pageId=889115248)  
[**Desembaraço**](https://tdn.totvs.com/pages/releaseview.action?pageId=312158532)
