---
article_id: 10651821187863
category: RH - Arquivos Bancarios
content_hash: e5cdf3c7d22fad69c82c69ff7338cc174ae26320aefcb5dc0d867e2f58c7302e
fetched_at: '2026-06-28T22:43:38.327806+00:00'
product: protheus
section_id: 360004833673
source: central-protheus
title: RH - Linha Protheus - GPE - Identificadores de Lançamento Recibo Eletrônico
  Bradesco
type: support-article
updated_at: '2025-09-19T22:39:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10651821187863-RH-Linha-Protheus-GPE-Identificadores-de-Lan%C3%A7amento-Recibo-Eletr%C3%B4nico-Bradesco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Quais são os Identificadores de Lançamento do Recibo Eletrônico Bradesco?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Ao gerar o Arquivo de Recibo Eletrônico Bradesco, é apresentado na posição **38** o Identificador de Lançamento das verbas:  
  
1. Lançamentos de Proventos;  
2. Total de Vencimentos;  
3. Lançamentos de Descontos;  
4. Total de Descontos;  
5. Total Líquido;  
6. Total Líquido Negativo.

Veja abaixo, alguns exemplos de como o arquivo é apresentado:

**Exemplo 1** - Holerite de Pagamento do Adiantamento, onde o Funcionário tem verbas de Provento, Desconto e Líquido:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10651496991511)  
  
**Exemplo 2** - Holerite de Pagamento do Adiantamento, onde o Funcionário não tem verbas de Desconto. Veja que o Identificador 3 (Lançamentos de Desconto) não é apresentado, e o Identificador 4 (Total de Descontos) apresenta o valor zerado:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10651646393879)

**Saiba Mais:**  
Para mais informações sobre como gerar o arquivo de holerite eletrônico Bradesco [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038874694-RH-Linha-Protheus-GPE-Como-gerar-Holerite-Eletr%C3%B4nico-Bradesco).
