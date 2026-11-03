---
article_id: 4412150057495
category: RH - Integração de Titulo
content_hash: 99e0e026a21a432dbeb767bcdd3f54c494ab5871551d938f958b0421dae07db2
fetched_at: '2026-06-28T22:43:36.437592+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Quais verbas devo considerar para conferir os títulos
  de INSS definidos por padrão
type: support-article
updated_at: '2025-07-17T12:51:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412150057495-RH-Linha-Protheus-GPE-Quais-verbas-devo-considerar-para-conferir-os-t%C3%ADtulos-de-INSS-definidos-por-padr%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22190583773847) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Quais verbas devo considerar para conferir os títulos de INSS definidos por padrão  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412135107479)**

Se os títulos foram definidos por INSS - Folha de Pagamento (padrão), conforme imagem acima, devemos considerar as seguintes verbas para compor o valor do título:

**ID. 0064 INSS Folha**

**ID.0065 INSS Férias**

**ID.0070 INSS 13º**

**ID.0148 INSS % Empresa**

**ID. 0149 % Terceiros**

**ID.0150 % Acidente de trabalho**

Para as deduções considerar:

**ID.0034 Salário família**

**ID.0040 Auxílio maternidade**

**Observações:**1) Os valores gerados no financeiro devem ser os mesmos apresentados na Guia de GPS ( Relatórios - Mensais - GPS)

2) Caso na conferência , verifique que existe uma verba específica , apresentando o valor também como dedução de INSS , verifique no cadastro da verba o campo  "Ded. G. INSS"= SIM e realize a alteração.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412157194775)

**IMPORTANTE:**Quando os valores de outras entidades forem desmembrados na folha de pagamento, eles não serão gerados no título padrão, uma vez que ao desmembrar os valores , entende-se que o pagamento será realizado em guias separadas e distribuídas a cada uma das entidades individualmente.   
Para estas situações criar um título **DEFINIDO por USUÁRIO**e definir como será gerado (título único ou 1 título para cada entidade).   
  
**Saiba Mais:**

[Página Centralizadora da Definição, Geração , Manutenção e Integração dos títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
