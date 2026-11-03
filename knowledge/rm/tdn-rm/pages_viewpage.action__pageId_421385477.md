---
content_hash: cdeb9ecc08b5d122f0156af1aea4b6de83afdd0b35c4df044a5b7211106cd185
fetched_at: '2026-06-29T00:09:16.170469+00:00'
page_id: '421385477'
product: rm
source: tdn-rm
title: Histórico do Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385477
version: 4
---

O histórico do Contrato, localizado em Anexos da visão de contratos é possível inserir/visualizar novos status para o contrato, assim como os funcionários responsáveis pelo mesmo.

**Passos:**

No campo Chapa do responsável , é possível vincular o responsável

No campo Data da Mudança , define -se a data que será realizada a mudança do histórico.

No campo Status atual(posição) é possível definir a posição do contrato: Em andamento, Em negociação, Paralisado, Concluído,  Cancelado e Sem status definido, para atribuir ao contrato.

**Definindo parâmetro:**

As restrições para cada contrato variam de acordo com cada status:  
 Alguns controles podem ser utilizados quando for definido o status do contrato, para isso é necessário que seja marcado o parâmetro "Utiliza Controle de Status" em   .  Com esta opção marcada os status do contrato irão se comportar da seguinte forma:  
 Em Negociação: todas as funções estão liberadas como associação de itens, exceto às relacionadas à medição. Não é possível realizar liberação, criar aditivos ou gerar períodos do contrato.  
 Em andamento:  estarão liberadas as funções relacionadas à medição, aditivo e liberação para Suprimento/Faturamento. Não é possível realizar, por exemplo, edição das informações do contrato.  
 Sem status, Paralisados, Encerrados e Cancelados: nenhuma funcionalidade deve estar liberada. A edição de aditivo, itens de contrato e o próprio contrato não estão liberadas pra modificações. Somente para visualização de dados como aditivos, itens e medições.  
 Depois de salvar o status não será possível realizar nenhuma alteração. Para isso é necessário incluir um novo Histórico no Contrato com a posição desejada.

Informações

O status com que o contrato é criado pode ser definido em Parâmetros do projeto -> Contrato -> Status inicial do contrato. O ideal ao utilizar a opção "Utilizar status do contrato" é criar o contrato com status "Em Negociação", devido a associação de itens ser realizada apenas neste status.  
  
A mudança do status do contrato será livre a qualquer momento. Para controlar o acesso a esta funcionalidade deve-se usar o controle de segurança do Totvs Obras e Projetos, autorizando somente os usuários que estejam habilitados para tal.  
  
A forma da validação da apresentação das informações do contrato de acordo com o status, será evidenciada no momento da alteração dos dados através da ferramenta. O sistema consistirá e não permitirá as alterações quando estas não puderem ser feitas.   
  
Haverá um processo para o usuário indicar modificações nos itens de contrato que atualmente estão vigorando, o processo é  , que possibilita aumentar ou diminuir a quantidade do item.
