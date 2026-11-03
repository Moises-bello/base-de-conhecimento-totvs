---
content_hash: d24c54e7d119f57186134eeba3916302e007cc07e4885e359c69e23711d3410c
fetched_at: '2026-06-29T00:09:16.824519+00:00'
page_id: '421385571'
product: rm
source: tdn-rm
title: WebService de Exportação de Alocação Mão de Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385571
version: 2
---

---

O WebService no TBC (TOTVS Business Conector) é responsável por exportar os dados de Alocação de Mão de Obra para o coletor Móvel.  
 O Processo de exportação dos dados será iniciado pelo coletor móvel. Toda a comunicação com o coletor móvel será realizada pelo WebService a ser disponibilizado pela TOTVS, através de solicitação do coletor móvel.  
 O WebService de exportação será responsável por enviar os dados de alocação de Mão de Obra para o coletor móvel. Este WebService irá enviar ao coletor móvel as informações em formato XML. As informações de alocação serão enviadas juntamente com as informações de folha tarefa e itens de folha tarefa, assim como a relação da equipe com a tarefa e seus respectivos membros.  
 Após o envio dos dados ao coletor, o WebService irá gravar em tabelas de Logs os dados de identificação do equipamento, identificação do processo, Data e Hora. No caso de erro no envio dos dados, o WebService irá gravar esta informação nas tabelas de log do sistema e transmitirá ao coletor móvel a informação de erro na transmissão.
