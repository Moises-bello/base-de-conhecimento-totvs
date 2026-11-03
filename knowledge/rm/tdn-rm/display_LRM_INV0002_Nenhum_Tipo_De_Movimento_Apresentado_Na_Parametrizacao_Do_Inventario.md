---
content_hash: afdcf342bdee67f9db9eb4b7060848e45b98d24f9328e4d4077f28b76bdfe58b
fetched_at: '2026-06-29T00:08:14.752686+00:00'
page_id: '244715080'
product: rm
source: tdn-rm
title: INV0002_Nenhum_Tipo_De_Movimento_Apresentado_Na_Parametrizacao_Do_Inventario
type: documentation
url: https://tdn.totvs.com/display/LRM/INV0002_Nenhum_Tipo_De_Movimento_Apresentado_Na_Parametrizacao_Do_Inventario
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.82 e superiores |
| **Ocorrência:** | Nenhum movimento apresentado nos parâmetros de inventário |
| **Ambiente:** | Parâmetros de Inventário |
| **Passo a passo:** | Ao tentar parametrizar as etapas de Inventário, nenhum tipo de movimento é apresentado para acerto de Entrada e/ou Saída.   ParâmetrosDefinições de Inventário 1/3  Pesquisa de movimento  CAUSA 1- O Tipo de movimento não é do Tipo 4.1.  2- A numeração do movimento não esta como mostra.  3- O usuário não tem permissão ao tipo de movimento.  4- A unidade de medida definido no tipo de movimento esta diferente de unidade “controle”.  5- O saldo e o efeito sobre o saldo parametrizado no tipo de movimento estão incompatíveis com campo onde o tipo de movimento de inventario é definido. SOLUÇÃO  1- Criar um tipo de movimento do tipo 4.1.  2- Definir a numeração do movimento como mostra.  3- Liberar acesso ao usuário ao tipo de movimento criado para inventario.  4- Definir no tipo de movimento que a unidade de medida será unidade de “controle”.  5- Definir o saldo e o efeito de saldo compatível com o campo ao qual deseja informar o tipo de movimento. Exemplo: Se inventario sobre o saldo 2. Definir um tipo de movimento que o efeito sobre o saldo será aumenta e outro que será diminui. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
