---
article_id: 1500011502862
category: PMS - Projetos
content_hash: b1aff2412c4dc7c26ce1c2165f64937c404f66e02530427344ba458a16ae748e
fetched_at: '2026-06-28T22:37:14.890455+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Custo Realizado, Custo Previsto
  e Saldo Realizado
type: support-article
updated_at: '2026-04-10T20:22:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011502862-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Custo-Realizado-Custo-Previsto-e-Saldo-Realizado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39665941232535)** **Tempo aproximado para leitura:****00:02:00 min**

**Dúvida**  
Quando visualizo os custos no modelo Planilha, qual o calculo que o sistema faz para chegar no Custo Realizado, Custo Previsto e Saldo realizado?  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice - SIGAPMS- Todas as versões  
  
**Solução**

Segue exemplos de como são realizados estes custos:

**Saldo Realizado**

É o Custo Orçado Previsto (**COTP**) menos o Custo Real do Trabalho Executado (**CRTE**).

Exemplo: Se tenho um Saldo Realizado na inclusão do Projeto de 20.000 e Incluo um Contas a Pagar com valor de R$500,00 - O valor do meu Saldo Realizado passa a ser 19.500,00.

**COTP - Custo Orçado do Trabalho Previsto**

Os custos previstos cadastrados nas abas Produtos, Recursos e Despesas serão somados para calcular quanto que, de acordo com a data-base do sistema, aquela tarefa/EDT custará.

![custo_previsto.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018807041)

**CRTE - Custo Real do Trabalho Executado**

Os custos desta coluna serão referentes aos apontamentos amarrados ao projeto como documentos de entrada, remessas, requisições, apontamentos de recursos, títulos a pagar, movimentos internos, observando a data base do sistema. Seguindo o mesmo exemplo citado em Saldo Realizado, um titulo no Contas a Pagar com o valor de R$ 500,00 - este valor é referente ao Custo Realizado.

**Saiba mais :**

* [Custos do projeto na visualização em planilha do projeto](https://tdn.totvs.com/x/yr0IHw)
* [Como visualizar os Custos no Projetos](https://tdn.totvs.com/x/xN-SGQ)
