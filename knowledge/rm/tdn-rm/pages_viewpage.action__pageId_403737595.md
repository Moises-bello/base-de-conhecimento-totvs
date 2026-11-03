---
content_hash: 1681ed5a29396c4342d0b90db484b7524413f8efe5657604d23a716320f066b0
fetched_at: '2026-06-29T00:09:10.957716+00:00'
page_id: '403737595'
product: rm
source: tdn-rm
title: 3332009 ESOCIALFOP01-7235 Transferência de Funcioinário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403737595
version: 1
---

# Transferência de Funcionário

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Funcionários | Movimento | Rescisão |
| **Situação/Requisito:** | Ao transferir funcionário para outra coligada ocorre o seguinte erro: ORA-02291: restrição de integridade (RM.FKPFVERBASDIS\_PDADOSDIS) violada - chave mãe não localizada" O erro está relacionado a Verbas de Dissidio que ficam armazenadas na aba de Verbas Geradas por Dissidio na ficha financeira e que estes dados estão relacionado ao eSocial > Dissidio/Acordo Coletivo Cadastrado. |
| **Solução/Implementação:** | Retirado auto incremento do campo ID pela GAutoInc, deixando livre para o usuário informar o valor do identificador e validando caso já exista. |
| **Tickets relacionados:** | 3332009 |
