---
article_id: 37100272710039
category: Contabilidade gerencial - Reforma Tributária
content_hash: f77dd4b99d221118f66318bfb2c72df0eac115fd411ed95a990a9a9530c76585
fetched_at: '2026-06-28T22:40:29.714601+00:00'
product: protheus
section_id: 37095816599831
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Contabilização com Base
  na Sigla do Tributo
type: support-article
updated_at: '2025-12-17T20:44:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37100272710039-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Contabiliza%C3%A7%C3%A3o-com-Base-na-Sigla-do-Tributo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37100237052183) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como realizar a contabilização de tributos utilizando a sigla definida no Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade gerencial - Todas as versões  
  
**Solução**  
A contabilização baseada na sigla do tributo utiliza a tabela **F2D (Tributos Genéricos Calculados)**. Esta estrutura armazena os valores calculados tanto para Documentos de Entrada (SD1) quanto de Saída (SD2).

A normalização desta tabela permite maior *performance* e organização, utilizando campos de relacionamento para vincular os itens das notas fiscais aos seus respectivos tributos.

**Principais Campos para Integração:**

* **F2D\_IDREL**: ID de relacionamento que liga a F2D às tabelas SD1/SD2 através dos campos **D1\_IDTRIB** ou **D2\_IDTRIB**.
* **F2D\_TRIB**: Sigla ou "apelido" do tributo definido na Regra de Cálculo.
* **F2D\_VALOR**: Valor do tributo calculado.

**Passos para a contabilização**

1. **Identificar a Sigla do Tributo**:

   * Acesse: **Configurador de Tributos** → **Regras Fiscais** → **Regra de Cálculo - Documentos Fiscais**.
   * Verifique o conteúdo do campo **Código Regra** (ex: "ATF001"), que será utilizado como a sigla de busca.  
       
     ![image-2025-4-30_9-45-38.png](https://tdn.totvs.com/download/attachments/977835583/image-2025-4-30_9-45-38.png?version=1&modificationDate=1755536996063&api=v2)  
       
     ![image-2025-4-30_9-43-49.png](https://tdn.totvs.com/download/attachments/977835583/image-2025-4-30_9-43-49.png?version=1&modificationDate=1755536996287&api=v2)
2. **Configurar o Lançamento Padrão**:

   * No campo de valor do Lançamento Padrão (ex: Vlr Moeda 1), utilize a função POSICIONE para buscar o valor na tabela F2D.
   * Utilize o **índice 6** da tabela F2D para realizar a busca por ID de relacionamento + Sigla.

**Exemplo de Sintaxe para Documento de Entrada:**

POSICIONE("F2D", 6, SD1->D1\_IDTRIB + "ATF001", "F2D\_VALOR")  
  
![](https://tdn.totvs.com/download/attachments/977835583/image-2025-8-29_14-43-33.png?version=1&modificationDate=1756489414717&api=v2)

Saiba mais sobre a função:

https://tdn.totvs.com/display/public/framework/Posicione

**Detalhamento do Comando:**

* **"F2D"**: Tabela de origem dos dados tributários.
* **6**: Índice de busca composto.
* **SD1->D1\_IDTRIB + "ATF001"**: Chave de busca que concatena o ID do item da nota com a sigla do tributo desejado.
* **"F2D\_VALOR"**: Campo que contém o valor a ser contabilizado.  
    
  ![](https://tdn.totvs.com/download/attachments/977835583/image-2025-8-29_15-25-54.png?version=1&modificationDate=1756491956220&api=v2)

**Saiba Mais**

[Contabilização com Base na Sigla do Tributo](https://tdn.totvs.com/pages/viewpage.action?pageId=977835583)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Reforma tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35707320972439-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Reforma-tribut%C3%A1ria)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como Contabilizar IBS, CBS e IS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36639180648983-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-Contabilizar-IBS-CBS-e-IS)
