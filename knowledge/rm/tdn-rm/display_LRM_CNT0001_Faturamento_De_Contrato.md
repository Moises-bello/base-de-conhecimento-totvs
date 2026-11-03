---
content_hash: 0977263151875f9b20bd36c469e84dcfd00b73affa66a5dff7ff9b89902c94c3
fetched_at: '2026-06-29T00:08:34.242324+00:00'
page_id: '274654514'
product: rm
source: tdn-rm
title: CNT0001_Faturamento_De_Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/CNT0001_Faturamento_De_Contrato
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.80 e superiores |
| **Ocorrência:** | Faturamento de Contrato |
| **Ambiente:** | Manutenção de Contrato |
| **Passo a passo:** | Ao tentar realizar o processo de faturamento de contrato, nenhum movimento é gerado. CAUSA 1- Status do Item de Contrato não permite faturamento.   2 - Item totalmente Faturado.   3 - O período de faturamento é menor que períodos já faturados.   4 - O item de contrato não permite o faturamento com lançamentos em aberto para movimentos gerados para aquele item.  5 - Campo “Preço de Faturamento” incorreto.  6 - Consistência do campo “N.F. Acompanha Boleto”.  7 - Tipo de Movimento informado incorretamente.  8 - Faturamento de item no período de carência.  9 - Tipo de item incorreto entre lote e item de contrato.  10 - Filtros obrigatórios e opcionais no lote de faturamento.  11- Mensagens de consistências no(s) movimento (s) a ser(em) criado(s).    SOLUÇÃO 1 – Verificar se o status do item permite faturamento, para isso você deve editá-lo no Menu Cadastro / Tabelas de Contratos / Status do Contrato, e verificar o campo “Faturar”.  2 - Se o status de faturamento for “Faturado” indica que o item já foi totalmente faturado e que não há mais o que faturar;  3 - Se o “Status de faturamento” estiver como “Parc. Faturado” deve-se verificar se já existem movimentos já faturados para o mesmo item em períodos posteriores ao período de faturamento.  4 – Verifique se o item de contrato já gerou movimentos anteriormente e se os lançamentos desses movimentos estão em aberto. Caso exista a necessidade de se faturar nessa situação a opção “Fatura Com Notas em Atraso” deve ser marcada no item do contrato.  5 - O campo “preço de Faturamento” deve ser maior que 0,00 (zero).  6 - Se o campo “N.F. Acompanha Boleto”. estiver marcado no item, ele deverá ser marcado também no lote de faturamento do contrato.  7 - Verifique se o tipo de movimento parametrizado no item de contrato é o mesmo informado durante a tentativa de faturamento, seja pela Grid. ou pelo lote de faturamento do contrato.  8 - Verificar no item de contrato na pasta datas os campos “Dias de carência” e “carência temporária”.  9 - Verificar se o tipo de item para faturamento (medição, periódico, não periódico) está consistente entre item e lote de faturamento.  10 - Verificar se os itens que se deseja faturar se adéquam aos filtros informados no lote de faturamento, todas as informações devem estar consistentes.  11 - Verificar as possíveis mensagens de erro no log de faturamento do lote. |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
