---
content_hash: 5583f792ab2aaeeb20773a47a48facfdd28135161f16da92464438ef29a895b1
fetched_at: '2026-06-29T00:10:57.811018+00:00'
page_id: '599858153'
product: rm
source: tdn-rm
title: DT- Folha de pagamento - Atestado médico do parecer SEI Nº 16120/2020
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=599858153
version: 1
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Folha de pagamento - Parecer SEI nº 16120/2020/ME |
| **Situação/Requisito:** | O usuário precisa gerar a folha de pagamento do colaborador que teve atestado médico do parecer SEI Nº 16120/2020 - 15 dias, e ao substituir o cc 145 no envelope do colaborador e executar recálculo o evento cc 145 retorna para o envelope. |
| **Solução/Implementação:** | Não será lançado o código de cálculo 145 existente no parametrizador via lançamento de grupo de eventos caso exista o código de cálculo 445 no envelope do funcionário. Os dois códigos de cálculo deverão ser lançados manualmente caso haja necessidade de lançamento simultâneo. Por exemplo: Atestado de 15 dias por acidente de trabalho no início do mês e lançamento de atestado por doença, Previdência, maior que 15 dias no final do mês.  A entrada de dados, a inclusão de evento no envelope e o lançamento de grupo de eventos com o parâmetro "Lança o evento de atestado médico via grupo de eventos" marcado são tratados como controle manual do usuário e com isso o evento com código de cálculo 145 será lançado no movimento mesmo que exista o código de cálculo 445 já lançado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-12994](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-12994) e [FOPCALCULO01-13001](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-13001) |
| **Documento de Referência:** | [Código de Cálculo 445 - ATESTADO MÉDICO COM INCIDÊNCIA SOMENTE SEGURADO](https://tdn.totvs.com/pages/viewpage.action?pageId=589761956)  [Folha de Pagamento - Atestado médico com incidência somente segurado (CC445)](https://tdn.totvs.com/pages/viewpage.action?pageId=590618716) |
| **Pacote:** | N/A |
