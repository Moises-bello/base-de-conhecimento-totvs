---
content_hash: 27a63afd9ffd31b0e96182a06fa0d32718f8c429d753aa3cb8564611fdf5b743
fetched_at: '2026-06-29T00:09:33.282094+00:00'
page_id: '425458952'
product: rm
source: tdn-rm
title: Consulta Status Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Consulta+Status+Folha+de+Pagamento
version: 3
---

**Consulta Status Folha de Pagamento**

---

A Integração Consulta Status do TOTVS Folha de Pagamento x Gestor AVB (TOOLS) tem como objetivo buscar (através de um XML) informações sobre o status da folha para uma determinada competência. O Gestor AVB (TOOLS) envia a consulta (em forma de XML) para o TOTVS Folha, que por sua vez, verifica se a competência está maior ou menor que o informado na consulta. Para o status da folha ser considerado como ABERTO o período indicado para consulta deverá ser maior que do TOTVS Folha, caso contrário o status da folha será FECHADO. Quando o status da folha está ABERTO, ela continuará aceitando inclusão de lançamentos enviados diretamente pelo TOOLS, como por exemplo a inclusão de um novo empréstimo para um determinado funcionário. Já quando esse status encontra-se FECHADO o sistema não irá mais aceitar a inclusão de lançamentos.  
    
 O sistema busca as informações do mês e ano de competência na tabela PPARAM, as informações que chegam para a consulta do status folha estão descritas na tabela abaixo:  
  

|  |  |
| --- | --- |
| **CAMPO** | **OBRIGATÓRIO** |
| CNPJ (coligada) | SIM |
| Mês/Ano | SIM |
| Usuário | SIM |
| Senha | SIM |
