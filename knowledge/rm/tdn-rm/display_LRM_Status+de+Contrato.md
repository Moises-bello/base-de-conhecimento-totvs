---
content_hash: ff5769db974b3797c4aceea19a8cec40a23360217376ec21ccd93ec7e0dcde57
fetched_at: '2026-06-29T00:09:28.689262+00:00'
page_id: '423938753'
product: rm
source: tdn-rm
title: Status de Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Status+de+Contrato
version: 5
---

Por esta opção são cadastrados os status do contrato, utilizados pela empresa durante a inclusão / manutenção de contratos.   
 Vencido, suspenso, cancelado, Carência, Normal, Especial, Cancelado reversível, Cancelado irreversível, etc. Ao cadastrar / editar um Status será possível visualizar as seguintes opções:

**Status do Contrato**: Por esta opção serão cadastrados os status do contrato(Este código não poderá ser editado após a gravação do registro).  
**Código**: Informe o código do status a ser incluído.  
**Descrição**: Informe a descrição para o status.  
**Faturar**: Ao marcar esse parâmetro, os contratos incluídos com este status poderão ser faturados normalmente. Do contrário o usuário não poderá fatura-lo.  
**Cancelamento**: Similar ao parâmetro anterior, ao marcar esse parâmetro o sistema considera o mesmo como um status de cancelamento, ou seja, quando um contrato é cancelado, um status de cancelamento deverá ser informado e nesta etapa são apresentados apenas os status que têm esse parâmetro marcado.  
**Considerar nas análises do agente gestor de contratos:**Flag que permite que o agente gestor de contratos considere contratos deste tipo de status para ser avaliado na tool que verifica quais contratos estão vencendo.

***Observação***: O sistema não permite a exclusão de um status que estiver sendo referenciado em algum contrato.

---
