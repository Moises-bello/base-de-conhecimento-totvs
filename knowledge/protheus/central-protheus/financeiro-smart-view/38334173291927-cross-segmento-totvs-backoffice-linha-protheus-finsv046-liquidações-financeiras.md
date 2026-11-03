---
article_id: 38334173291927
category: Financeiro - Smart View
content_hash: 235620f127864c03d3895d04d3e7366643769f7ada24867c350953b1704700f4
fetched_at: '2026-06-28T22:37:44.673613+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - FINSV046 - Liquidações financeiras
type: support-article
updated_at: '2026-02-11T21:45:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38334173291927-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FINSV046-Liquida%C3%A7%C3%B5es-financeiras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38334156762775) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Qual relatório do Smart View permite visualizar as liquidações?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Versão 12.1.2210.  
  
**Solução**  
A visualização das liquidações financeiras deve ser realizada através da **Visão de Dados e Tabela Dinâmica de Liquidações Financeiras** no Smart View. Esta ferramenta visa demonstrar as liquidações efetuadas, apresentando detalhadamente os títulos baixados (originais) e os títulos gerados após o processo de liquidação.

A funcionalidade oferece:

* **Agrupamento Flexível:** Possibilidade de agrupar os dados por qualquer campo disponível na visão, adaptando-se à necessidade de análise.
* **Filtros Avançados:** Demonstração de dados filtrados por processo de liquidação, número da liquidação, status dos títulos (Baixados ou Gerados) e seleção por carteira (Pagar, Receber ou Ambas).
* **Rastreabilidade:** Permite visualizar em cada liquidação todos os itens que a compuseram, mantendo o vínculo entre o título gerado e a liquidação de origem, inclusive em casos de reliquidação de parcelas.

1. Acesse o módulo **Financeiro (SIGAFIN)**;
2. Vá em **Consultas > Smart View > Tesouraria >** **Liquidações (FINSV046)**
3. Localize o objeto de negócio relacionado a **liquidações financeiras (visão de dados) > Em tela e clique em imprimir.**
4. Ao executar a visão de dados, preencha os parâmetros de tela conforme o período e carteira desejados e clique em enviar;
5. O relatório será apresentado em tela, permitindo a aplicação de filtros por **nome da filial, processo, número da liquidação e status (gerado ou baixado – título pai).**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38334173277591)

Exemplo de Status:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38334156764183)

Por meio do seletor de colunas, é possível incluir novas colunas no relatório, conforme a necessidade de visualização das informações.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38334156764439)

Na opção **Exportar todos os dados**, é possível realizar a exportação completa do relatório para o formato Excel, facilitando a análise e o tratamento das informações.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38334156764567)

Ao acessar a rotina, também é possível selecionar a opção **Visão de Dados**, que apresenta as mesmas informações em formato de tabela dinâmica, proporcionando melhor visualização e análise das liquidações. Nessa visão, é possível focar apenas nos dados relevantes, com campos como valor do título, juros, descontos, valores acessórios e valor liquidado.

A tabela retorna, ainda, uma grade com os totais consolidados dos campos mencionados. A ordenação segue os critérios definidos na Visão de Dados, com filtros por Processo, Número da Liquidação e Número do Título.

O relatório permite a visualização dos dados de Contas a Pagar e de Contas a Receber, podendo ser consultados de forma separada ou ambos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38335585845527)

**Saiba mais**

[Smart View - Liquidações Financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=814527875)

[Financeiro - Smart View](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32632656432151-Financeiro-Smart-View)
