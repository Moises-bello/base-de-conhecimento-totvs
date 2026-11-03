---
article_id: 360018604191
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1cf96a6607d5a1dc3e44f580abd3fe65b94c0e9582136a0e2f55726dfef4a543
fetched_at: '2026-06-28T22:38:39.793558+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Funcionalidade do campo "Status
  (C5_MSBLQL)" no Pedido de Vendas
type: support-article
updated_at: '2025-10-30T18:34:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018604191-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Funcionalidade-do-campo-Status-C5-MSBLQL-no-Pedido-de-Vendas
---

**Dúvida**

Qual a funcionalidade do campo **"Status (C5\_MSBLQL)"** no Pedido de Vendas?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**

O campo **"Status (C5\_MSBLQL)"** não possui funcionalidade, ele foi incluído no dicionário de dados da versão 12 inconsistentemente e sem efeito.  
  
Ocorre que o Pedido de Vendas incluso no sistema **não será bloqueado por este campo**. Os critérios de bloqueio atendem à outros requisitos do Protheus como (Bloqueio de Regra de Negócio, Verba de Venda, Credito e Estoque).  
  
Se desejar poderá inserir um campo de usuário (com nome diferente) caso deseje validar alguma regra customizada de sua organização. Porém, o campo **\_MSBLQL** do Protheus no ambiente Faturamento é utilizado apenas para cadastros pois visa não permitir incluir este cadastro em novos registros  **([MSBLQL - Bloqueio de Registro Cadastro](https://tdn.totvs.com/x/p4WFDg))**, conceito este que não se adéqua ao Pedido.  
  
Como se trata de uma tabela de processo, não é permitido o uso deste campo, por isso o desenvolvimento do produto retirou o mesmo de uso no processo, e vai acabar ocorrendo de você colocá-lo manual e ele não permanecer ativo.

O campo reservado **\_MSBLQL** é apenas para tratamento de tabelas de cadastros, se há a necessidade de um bloqueio de pedido, você pode utilizar a Regra de Negócio para efetuar um tipo de bloqueio, conforme indicado pela documentação ou tratar via ponto de entrada, segue algumas sugestões:

* **[M410RLIB - Refaz liberações de estoque](https://tdn.totvs.com/x/h-kpJw)**
* **[MA410VLD - Tratamento de não confirmação de inclusão ou alteração](https://tdn.totvs.com/x/EIVn)**
* **[MT410BRW - Chamado antes da apresentação da mbrowse](https://tdn.totvs.com/x/XIVn)**
* **[MT410TOK - Validar confirmação da operação](https://tdn.totvs.com/x/YYVn)**

Existe um tratamento de dicionário efetuado para este campo, onde terá sua função habilitada para uso a partir da release 12.1.20, conforme documentação técnica: **[Ajustes dos campos C5\_MSBLQL e C5\_TPFRETE no dicionário SX3](http://tdn.totvs.com/pages/viewpage.action?pageId=334335537)** .

Desta forma, quando a próxima release após a release 12.1.17 estiver disponível para uso, já conterá o tratamento informado acima.
