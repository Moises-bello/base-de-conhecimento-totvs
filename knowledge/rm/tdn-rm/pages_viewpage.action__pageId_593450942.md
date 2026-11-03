---
content_hash: 7c481948f41f449b9f4fab74690b34b0c46f294b9132237fe2fb8deab762b044
fetched_at: '2026-06-29T00:10:56.921115+00:00'
page_id: '593450942'
product: rm
source: tdn-rm
title: DT- Parametrizador - Resc.Compl. com aumento salarial posterior a demissão
  paga férias e 13º somente sobre dias após reajuste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593450942
version: 1
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Rescisão complementar |
| **Situação/Requisito:** | Funcionário foi demitido no mês 3/2020 e teve aumento para a categoria dele no mês 5/2020, como ele tem aviso indenizado a projeção do aviso cai dia 05/05 então o sistema deve calcular a diferença apenas dos 5 dias de aviso e caso estes 5 dias tenham resultado em um avo indenizado de férias ou 13º, destes eventos.  Ao calcular a diferença salarial o sistema está trazendo todas as diferenças independente se sofrem impacto do aviso. |
| **Solução/Implementação:** | Criado parâmetro “Resc.Compl. com aumento salarial posterior a demissão paga férias e 13º somente sobre dias após reajuste” para quando a alteração salarial ocorrer durante a projeção do aviso prévio e posterior ao mês da rescisão, ao calcular a rescisão complementar será pago diferença de férias e diferença de 13º salário proporcionalizado a partir do dia da alteração salarial.  Atualmente o padrão é proporcionalizar somente a diferença do aviso prévio indenizado, sendo que Férias e 13º salário tem os valores de diferença calculados integralmente, considerando o valor do salário no último dia da projeção. Esse procedimento continua quando o parâmetro estiver desmarcado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-12115](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-12115) |
| **Documento de Referência:** | [Parametrizador / Aviso Prévio](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719173) |
| **Pacote:** | N/A |
