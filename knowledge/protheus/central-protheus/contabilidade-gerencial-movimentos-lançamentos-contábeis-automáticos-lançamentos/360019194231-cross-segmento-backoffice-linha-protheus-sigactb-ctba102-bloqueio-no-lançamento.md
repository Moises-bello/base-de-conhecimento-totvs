---
article_id: 360019194231
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 9bf435fe8256b3a3563308e1f12ee1bfcc45844935647284eeb908856b06a261
fetched_at: '2026-06-28T22:40:32.434409+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Bloqueio no
  Lançamento Contábil
type: support-article
updated_at: '2023-03-30T12:07:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019194231-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Bloqueio-no-Lan%C3%A7amento-Cont%C3%A1bil
---

**Dúvida**Bloqueio no Lançamento Contábil

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

O  controle de bloqueio no Lançamento Contábil (Manual ou Automático) evita que dois ou mais usuários tentem alterar ou excluir o mesmo registro.

 

|  |
| --- |
| MV\_CT2SMLT |

Controle de alteração de lançamentos simultâneos: o padrão do sistema é F (false/falso), ou seja, com esta opção, o Sistema não fará o bloqueio.

 

Exemplo com a opção T (true/verdadeiro)

Controle de semáforo de alteração habilitado, caso ocorram tentativas de alterações simultâneas entre usuários, será apresentada uma janela de advertência.

**Importante**

O controle de bloqueio é opcional e servirá, apenas, em operações simples de alteração e exclusão, ele não interfere na exclusão por lote, ou seja, nos processos internos do Sistema.
