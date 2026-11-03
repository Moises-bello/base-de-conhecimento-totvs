---
content_hash: 68094bc054a34bfdb10ecf5cec948379975e480e098e4846fc7f8df7c82de196
fetched_at: '2026-06-29T00:09:16.178655+00:00'
page_id: '421385482'
product: rm
source: tdn-rm
title: Histórico de Aditivo 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385482
version: 4
---

---

Para o Aditivo contratual foram criados controle de status que é habilitado quando o parâmetro "Utiliza Status do Contrato" é marcado. A alteração dos status do aditivo é realizada através do Anexo da edição do Aditivo "Histórico do Contrato". Os status são: Em andamento, Paralisado, Concluído, Em Negociação, Cancelado e Sem status definido, e cada um possui um controle.  
   
**Em negociação:** Todas as funções de aditivo estão liberadas, exceto as relacionadas à medição. Ou seja, um aditivo em negociação não deve impactar de nenhuma forma na medição. Não será permitido para o mesmo contrato ter mais de um aditivo em negociação.  
**Em andamento:** Somente as funções relacionadas à medição estarão liberadas. Não deve ser possível editar o aditivo e seus anexos, incluir itens, somente visualizar.   
**Paralisados, Encerrados e Cancelados:** Nenhuma funcionalidade deve estar liberada. A edição de aditivo, itens de aditivo e anexo de alteração em Itens de Contrato não devem ser modificados neste status. Somente visualizar os aditivos, os dados do anexo de alteração em Itens de Contrato e as medições dos aditivos.  
Da mesma forma que ao terminar o cadastro do aditivo o usuário realiza o cadastro dos itens de aditivo, haverá um processo para o usuário indicar as modificações nos itens de contrato que atualmente estão vigorando, o processo é  

**Observações:** Não é permitido mais de um aditivo "Em Negociação" para o mesmo contrato.   
A partir do status "Em andamento" é possível retornar para o status "Em negociação" somente se ainda não existir medições. A partir deste status também é possível ser modificado para os Status Cancelado, Encerrado e Paralisado. Esta modificação pode ser feita a qualquer momento.  
O aditivo contratual somente será apresentado para contratos com status "Em Andamento" e que tenham medição  no período que compreenda sua data de utilização.  
A utilização do status do aditivo sem a definição do parâmetro "Utiliza status do contrato", possibilita a realização de medições, associações, cadastros em ambos os status "Em Negociação" e "Em Andamento". Nos outros status (Paralisado, Concluído, Encerrados e Sem status definido) o aditivo é bloqueado para edição.
