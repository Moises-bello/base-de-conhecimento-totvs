---
article_id: 360048616894
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: c672a0dd29f065b19ff0c6af4cae5e2c3fc9d5b7f5cadfc8a1e1620a1ee4e9ea
fetched_at: '2026-06-28T22:38:33.020041+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Cliente inativo no Cadastro
  do Cliente permitindo faturamento
type: support-article
updated_at: '2025-06-05T18:58:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048616894-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cliente-inativo-no-Cadastro-do-Cliente-permitindo-faturamento
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32617818618135) Tempo aproximado para leitura: **00:01:00 min******

**Dúvida**Cliente inativo no Cadastro do Cliente permitindo faturamento.

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

O bloqueio de clientes no Protheus é realizado por meio do campo **A1\_MSBLQL** da tabela de clientes (SA1).

A validação para impedir que seja criado pedido de venda para clientes inativos somente é feita na rotina Pedido de Vendas (**MATA410**). Ou seja, a funcionalidade padrão do sistema impede apenas a inclusão de novos pedidos vinculados a clientes bloqueados.

No entanto, os dados já existentes no sistema não são invalidados ou desconsiderados após o bloqueio. Todos os registros previamente gerados para o cliente (como orçamentos, pedidos já incluídos, entre outros) permanece inalterados e podem ser manipulados normalmente — por exemplo, faturar um pedido existente que contenha esse cliente.

Assim, o bloqueio terá efeito somente para novos registros que venham a tentar referenciar o cadastro do cliente após o seu bloqueio.

Caso o comportamento padrão não atenda à necessidade (como bloquear o faturamento de pedidos antigos, impedir alterações ou devoluções), recomenda-se implementar validações adicionais por Ponto de Entrada:

[MTA410T - Para todos os itens do pedido](https://tdn.totvs.com/x/iIVn)  
[M410STTS - Executado após todas as alterações no arquivo de pedidos (alteração, inclusão, exclusão e devolução)](https://tdn.totvs.com/x/m4Rn)  
[MT410INC - Localizado na rotina de alteração do pedido, A410INCLUI(). É executado após a gravação das informações](https://tdn.totvs.com/x/XoVn)  
[MT410ALT - Executado após a gravação das alterações](https://tdn.totvs.com/x/W4Vn)  
[MA410VLD - Tratamento de não confirmação de inclusão ou alteração](https://tdn.totvs.com/x/EIVn)

**Saiba Mais: [Bloqueio de Registro / Cadastro](https://tdn.totvs.com/x/p4WFDg)**
