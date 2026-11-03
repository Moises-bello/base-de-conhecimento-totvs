---
content_hash: d995d251bf3f683e913e8eb5f8780cd8d2978ed1d3114e650a1f71f0a93819ce
fetched_at: '2026-06-29T00:06:26.642086+00:00'
page_id: '225952445'
product: rm
source: tdn-rm
title: ER_PCREQ-8869_Edição/Mostra campo Desconto integrado com o Solum
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=225952445
version: 123
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | 12.1.10 | **IRM1** | PCREQ-8868 |
| **Requisito1** | * [PCREQ-8869](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-8869 "PCREQ-8869") | **Subtarefa1** | N/A |
| **Chamado2** | N/A | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Identificar os movimentos gerados de contratos que contenham dedução e discriminação de valor de dedução e retenção do TOP,   
para que não seja permitido modificar o **Desconto** do movimento no Suprimento/Faturamento.

## Definição da Regra de Negócio

 Será realizado o tratamento do campo de Desconto na tela de movimentos e no serviço de alteração, para verificar se o movimento foi gerado através de um contrato com dedução e caso positivo bloquear a edição do campo Desconto.

O tratamento será realizado utilizando a função disponibilizada pelo TOP para verificar se o movimento foi gerado a partir de um  contrato com dedução conforme especificado neste documento: 

**Casos de Uso**

O serviço disponibilizado para verificar se o movimento foi gerado através de um contrato com dedução e bloquear o campo Desconto será chamado sempre que  campo INTEGRAAPLICACAO na tabela TMOV é igual a "M". 

No serviço de alteração do movimento a mesma consistência será realizada para evitar que outros processos/parâmetros realizem alterações no valor do desconto lançando uma exceção para o usuário.

No caso de faturamento parcial de um movimento gerado pelo TOP o sistema não fará a consistência do valor do Desconto, quando o mesmo for proporcionalizado

 

**Observação:**

 

Alguns parâmetros do TOTVS Gestão de Estoque, Compras e Faturamento podem afetar o desconto no movimento que será gerado pelo TOTVS Obras e Projetos. Um exemplo disso é o parâmetro **Afeta desconto do Movimento** nos parâmetros do item de movimento que faz sobrescrever o desconto do movimento com a soma dos descontos dos itens de movimento. Esse comportamento pode gerar inconsistências que não poderão ser alteradas após a geração do movimento. Consulte a documentação de Integração / Produto para obter mais informações. 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
