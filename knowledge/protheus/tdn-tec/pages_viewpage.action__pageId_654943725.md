---
content_hash: 306752ebd1078a051d19c4fc20e698d3aedc6570dfd36d5c62afb31d7563b9af
fetched_at: '2026-07-02T19:24:26.793607+00:00'
page_id: '654943725'
product: protheus
source: tdn-tec
title: Correção  - AutoUpdate com LoadBalance é feito apenas no servidor Master -
  20
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=654943725
version: 2
---

Update automático com LoadBalance não é feito no servidor Slave

|  |  |
| --- | --- |
| Situação | Em ambiente com Load Balance, o AutoUpdate não reconhece as configurações feitas no(s) Slave(s) |
| Ocorrência | Em ambiente com Load Balance, o Auto Update reconhece apenas informações do servidor Master e não o Slave o qual a conexão foi direcionada |
| Correção | Após a primeira conexão no servidor Master, ela retorna as informações de IP e Porta do Slave o qual o SmartClient deve se conectar, porém internamente essa informação não era atualizada para no processo que faz a atualização automática,  fazendo com que esse processo sempre se conecta-se no servidor Master |
| Informações adicionais | * Referente ao chamado: [12263213](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%2212263213%22 "12263213") * Referente à ocorrência: [DTCLIENT01-3131](https://jiraproducao.totvs.com.br/browse/DTCLIENT01-3131) * Disponível em builds superiores a 19.3.8.1 e 20.3.0.1 |
