---
content_hash: 28b08675ebeca4e15a1e5775a485679a7151577d7c91cbf1f3e675297660fc23
fetched_at: '2026-06-29T00:08:46.185287+00:00'
page_id: '315904561'
product: rm
source: tdn-rm
title: CNT0003_Tipo_de_Movimento_Nao_e_Apresentado_no_Item_de_Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/CNT0003_Tipo_de_Movimento_Nao_e_Apresentado_no_Item_de_Contrato
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.82 e Superiores |
| **Ocorrência:** | Tipo de Movimento não é apresentado no Item de Contrato |
| **Ambiente:** | Contrato |
| **Passo a passo:** | Ao tentar informar um tipo de movimento dentro do item de contrato, este não é apresentado.     * **Causas**   1 - O usuário não tem permissão no tipo de movimento.  2 - O tipo de movimento **NÃO** esta parametrização com a edição de numeração, como **MOSTRA.**  3 - A Natureza do Contrato/item é incompatível com o tipo de movimento que deseja informar.     * **Solução**   1 - Acessar o cadastro de usuário e dar as devidas permissões do usuário ao tipo de movimento.  2 - Acessar o tipo de movimento que deseja informar e definir como **MOSTRA**no campo edição de numeração, na etapa de Mov – Identificação.  3 - Informar um tipo de movimento compatível com a natureza do contrato/Item de contrato, ou seja, se natureza “Compra” informar um tipo de movimento de Entrada, se natureza “Venda” informar um tipo de movimento de Saída. |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
