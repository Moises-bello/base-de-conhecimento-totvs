---
content_hash: 9c4a4533d2cd376d10330b8c25b1ceaf302d8b3d9545c902b90f400404fe7646
fetched_at: '2026-06-29T00:08:55.861586+00:00'
page_id: '351019497'
product: rm
source: tdn-rm
title: DT Trabalhador Cedido
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Trabalhador+Cedido
version: 7
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Eventos S-2230 e S-2300 |
| **Situação/Requisito:** | Adequação do produto para atender ao layout, para funcionário cedido temporariamente para outra empresa. |
| **Solução/Implementação:** | **Na empresa CEDENTE**  Foi criado um novo tipo de afastamento “K-Cessão / Requisição“, para permitir o cadastro da transferência temporária, na aba Situação.    Após o cadastro do afastamento, na aba Históricos / Histórico de afastamentos / eSocial  Sistema irá habilitar os dados do trabalhador cedido    Ao gerar o XML na fila de eventos, sistema irá trazer as seguintes tags no evento S-2230.      **Na empresa CESSIONÁRIA**  Ao admitir o funcionário com o código de categoria eSocial "410-Trabalhador cedido - informação prestada pelo Cessionário", sistema irá habitar uma nova aba com os dados da Cessão.    Essa aba será cadastrado os dados da empresa cedente.    Ao gerar o XML na fila de eventos, sistema irá trazer as seguintes tags no evento S-2300.    Para o desligamento dessa tranferência temporaria, foi criado um novo tipo de desligamento "W- Término da Cessão/Requisição". |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
| **Documento de Referência:** |  |
