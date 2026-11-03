---
content_hash: 0c302f96636a2bc566a98f8fb9f904eec2b2668394680e020f5255598b3ca99c
fetched_at: '2026-06-29T00:09:16.842766+00:00'
page_id: '421385575'
product: rm
source: tdn-rm
title: WebService de Importação de Apontamento Mão de Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385575
version: 2
---

---

O Processo de importação dos dados será iniciado pelo coletor móvel. Toda a comunicação com o coletor móvel será realizada pelo WebService a ser disponibilizado pela TOTVS, sendo este acessado pelo coletor móvel.  
 O WebService de importação será responsável por receber os dados de apontamento de Mão de Obra e incluí-los no sistema TOTVS Obras e Projetos para posterior validação e, após validação dos dados, Apropriação dos apontamentos. Após o recebimento dos dados do coletor, o WebService irá gravar, em tabelas de Logs, os dados de identificação do equipamento, identificação do processo, Data e Hora da execução. No caso de sucesso no recebimento dos dados ou aconteça algum erro na transmissão, o WebService transmitirá ao coletor móvel a informação de sucesso ou erro na transmissão. Se alguma inconsistência for encontrada no registro importado, o mesmo receberá o status de "Inconsistente", caso contrário o mesmo será definido como "Pendente".  
 O valor do campo Horas Apontadas será calculado durante a importação (Hora Final – Hora Inicial). O cálculo das Horas Apontadas do tipo improdutiva depende do campo Improdutivo vir com o valor "verdadeiro".
