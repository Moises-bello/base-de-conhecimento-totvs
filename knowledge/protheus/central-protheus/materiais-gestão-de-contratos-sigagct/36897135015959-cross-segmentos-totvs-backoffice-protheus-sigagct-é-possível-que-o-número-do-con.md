---
article_id: 36897135015959
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: c171ef4a6a35d00cc6035aca54cddcfd00808344bd1258b4d1b47c40a8a4a3f6
fetched_at: '2026-06-28T22:37:22.695654+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - É Possível que o número
  do contrato / medição Seja gravado na nota fiscal do Pedido gerado na Medição ?
type: support-article
updated_at: '2025-12-09T20:53:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36897135015959-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-%C3%89-Poss%C3%ADvel-que-o-n%C3%BAmero-do-contrato-medi%C3%A7%C3%A3o-Seja-gravado-na-nota-fiscal-do-Pedido-gerado-na-Medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36897135002775) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

É possível que o número do contrato e medição sejam gravados na nota fiscal que feita para o Pedido gerado na Medição ?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Por padrão o módulo de Gestão de Contratos, ele possui a funcionalidade de gravação do número do contrato apenas no documento que é gerado diretamente pelo módulo SIGAGCT, neste caso, o Pedido de Vendas ou Pedido de Compras conforme o tipo de contrato cadastrado.

E no caso o Processo posterior de geração da NF (que já não faz parte do módulo SIGAGCT), este é realizado já pelos módulos de Faturamento (Documento de Saída) ou Compras (Documento de Entrada) e o Gestão de Contratos não possui mais interferência.

Neste caso, se se deseja possuir gravações nos processos posteriores, o que podemos sugerir é a realização customização no processo realizado geração da NF no módulo de Faturamento ou Compras, para que possa ter essa informação nesses processos posteriores aos do Gestão de Contratos.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pontos de entrada do Documento de Entrada - MATA103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006469332-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-entrada-do-Documento-de-Entrada-MATA103)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Documentação Gestão de Contratos do TDN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441027145623)

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[FAQs - Gestão de Contratos](https://tdn.totvs.com/x/O_tgDQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
