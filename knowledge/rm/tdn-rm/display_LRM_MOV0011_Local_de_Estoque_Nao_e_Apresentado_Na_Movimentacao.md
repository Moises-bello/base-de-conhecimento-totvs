---
content_hash: 8d74a0e6eef7035771e9779e2c0396ce346d92ebb3072560a03cba3b7da240fc
fetched_at: '2026-06-29T00:08:46.175212+00:00'
page_id: '315904019'
product: rm
source: tdn-rm
title: MOV0011_Local_de_Estoque_Nao_e_Apresentado_Na_Movimentacao
type: documentation
url: https://tdn.totvs.com/display/LRM/MOV0011_Local_de_Estoque_Nao_e_Apresentado_Na_Movimentacao
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.82 e Superiores |
| **Ocorrência:** | Local de Estoque não é apresentado na Movimentação |
| **Ambiente:** | Inclusão de Movimento |
| **Passo a passo:** | Durante a inclusão de um movimento, o Local de Estoque não é apresentado.     * **Causas**   1 - O local de estoque informado não é de último nível, ou seja, não esta compatível com a máscara do local de estoque.  2 - O local de estoque não esta cadastrado para a filial da movimentação.  3 - O parâmetro “Usar local único” esta marcado e não existe pelo menos um local de estoque para a filial do movimento.  4 - O campo local (TMOV.CODLOC)não é apresentado na movimento.     * **Solução**   1 - Verificar e corrigir, se for o caso, para que o local de estoque seja de último nível e compatível com a máscara do local de estoque.  2 - Cadastrar o local de estoque correspondente para a filial utilizada no movimento.  2.1- Se parâmetro “Usar local único” marcado, cadastrar um local para cada filial.  3 - Quando o parâmetro “Usar local único” o campo local (TMOV.CODLOC) não será apresentado.  4 - O tipo de movimento esta parametrizado para ser do tipo serviço e o campo local (TMOV.CODLOC) não será apresentado.  4.1- O tipo dos itens na edição do movimento é “Serviço ”, sendo assim o campo local (TMOV.CODLOC) não será apresentado. |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
