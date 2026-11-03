---
content_hash: 61b36bc27b936e571dce346f556d85f38022df3bf33cea14e45ea6d5cbad8984
fetched_at: '2026-06-29T00:08:37.802979+00:00'
page_id: '284884144'
product: rm
source: tdn-rm
title: MOV0010_Buscar_aliquota_do_Pedido
type: documentation
url: https://tdn.totvs.com/display/LRM/MOV0010_Buscar_aliquota_do_Pedido
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.52 e superiores |
| **Ocorrência:** | Faturamento/Recebimento |
| **Ambiente:** | Parâmetros do Tipo de Movimento |
| **Passo a passo:** | Este documento tem por finalidade auxiliar na configuração do sistema para que no Faturamento/Recebido a alíquota do movimento de Pedido seja levado para o movimento de Nota Fiscal. Passo a Passo Para começarmos a configurar é necessário entendermos quais são as regras que o sistema segue para preenchimento do campo de Alíquota.  O primeiro local onde o sistema verifica de onde deve buscar alíquota é no cadastro do **Tributo.** Dentro deste cadastro, na aba Outros Dados, existe o campo **Procurar Alíquota no** conforme destaque do print abaixo:    O sistema sempre respeitará primeiro a configuração deste campo, por tanto, a prioridade de onde deverá buscar a alíquota é sempre definida no cadastro do Tributo.  Desta forma, caso queira que o sistema busque a alíquota do Pedido, terá que configurar seu Tributo para buscar alíquota no Tipo de Movimento, e este por sua vez, ser configurado para buscar alíquota no Pedido.    Com esta configuração aplicada, durante a inclusão do movimento via faturamento o sistema verificará no cadastro do Tributo de onde deverá buscar a alíquota. Como está configurado com Tipo de Movimento, o sistema verificará a configuração do movimento, e como este está parametrizado para buscar do Pedido, o sistema carregará a alíquota corretamente. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
