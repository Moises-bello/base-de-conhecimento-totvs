---
content_hash: 62970ce6162863ae500576e57f740477cf96339f29756cbd322e9c574f087573
fetched_at: '2026-06-29T00:10:47.961948+00:00'
page_id: '561628654'
product: rm
source: tdn-rm
title: DT- Cadastro de Funcionários - Parâmetro 'Não calcula Recibo de Férias'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=561628654
version: 6
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Parâmetro 'Não calcula Recibo de Férias' |
| **Situação/Requisito:** | O cliente solicitava a criação de um parâmetro para permitir pagar 30 dias para funcionários com férias cadastradas no mês. A empresa é Órgão Público e não paga adiantamento de férias e o 1/3 de férias é pago na folha normal do funcionário, conforme determina um Lei Estadual dos funcionários públicos da Paraíba. |
| **Solução/Implementação:** | Foi criado em **RH | Administração de Pessoal | Funcionários | Informações para o Cálculo | Parâmetros**, o parâmetro '**Não calcula Recibo de Férias**'.  Ao ser marcado o parâmetro, o sistema não irá calcular o recibo de férias para o funcionário.  Não serão exibidos no cadastro de férias o campo '**Data Pagamento**' e os botões de '**Calcular**' e '**Visualizar Recibo**' de férias.  A mudança da situação do funcionário para 'Férias', continuará sendo feito pelo processo 'Lançar' férias'.  O processo 'Finalizar' férias vai mudar a situação do funcionário de 'Férias' para 'Ativo' e atualizar os dados cadastrais do período aquisitivo de férias.  O sistema não irá consistir na Liberação de Competência se constam no envelope do funcionário os códigos de cálculo específicos de férias para funcionários com o parâmetro marcado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-9461](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-9461) |
| **Documento de Referência:** |  |
| **Pacote:** | N/A |
