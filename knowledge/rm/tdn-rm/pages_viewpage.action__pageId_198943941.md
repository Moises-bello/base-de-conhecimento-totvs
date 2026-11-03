---
content_hash: c1e524e3604c2bd2b692b7d0b1298dfcfd1a25319a286c3ed818bbc29bee59b6
fetched_at: '2026-06-29T00:06:02.148568+00:00'
page_id: '198943941'
product: rm
source: tdn-rm
title: Defaults de Relatórios (Novo Gerador.Net )
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198943941
version: 8
---

## Visão Geral

Os defaults de relatórios existem para possibilitar ao usuário parametrizar determinados relatórios padrão de forma que nos seus respectivos processos possam ser impressos diretamente sem que haja necessidade de serem selecionados em cada impressão.   
Nos parâmetros do TOTVS Gestão de Estoque, Compras e Faturamento foram criadas novas opções que permitem a configuração dos relatórios Padrão para Pedido Orçamento, Pedido Orçamento (E-mail), Pedido Orçamento (Web) e Quadro Comparativo Default que tenham sido criados pelo novo gerador .NET.   
Também será possível parametrizar os relatórios do Movimento, do Tipo Fatura e do Tipo Duplicata que estejam neste mesmo formato.

**Parametrização dos Defaults de Relatórios .Net**

**Comunicar Fornecedores:**O processo de Comunicar Fornecedores, que está disponível na tela de edição da Cotação, irá utilizar como relatório default o layout que estiver parametrizado nos parâmetros da Cotação | E-mail| “Relatório Padrão para Pedido Orçamento .NET (E-mail)” ou “Relatório Padrão para Pedido Orçamento .NET (Web)”. Para imprimir orçamento, deve ser configurado na etapa Relatório do parametrizador da cotação o "“Relatório Padrão para Pedido Orçamento .NET”".

**Imprimir Quadro Comparativo de Preços e Envio do Quadro Comparativo via e-mail:**O processo de Imprimir Quadro Comparativo de Preços e o Envio do Quadro Comparativo via e-mail, que estão disponíveis na tela de edição da Cotação, irão utilizar como relatório default o layout que estiver parametrizado nos parâmetros da Cotação | Relatório |“Relatório Quadro Comparativo Default .NET”

**Imprimir Movimentos:**O processo de Imprimir Movimentos irá utilizar como relatório default o layout que estiver parametrizado nos parâmetros do Tipo de Movimento | etapa - Mov - Impressão | “Formato do Relatório do Movimento”, “Formato do Relatório do Tipo Fatura” ou “Formato do Relatório do Tipo Duplicata” de acordo com o tipo de relatório selecionado.

****Seleção do tipo de relatório:****Nas telas de impressão serão apresentados dois campos, um campo para o usuário marcar se será utilizado o Gerador Dot.Net ou não e um campo de Lookup que será carregado com o Formato do Relatório default que estiver parametrizado.

*****Observações*:****A regra que irá definir qual relatório default (.NET ou Delphi) será carregado para o lookup será a seguinte:

1. Se existir relatório .NET parametrizado, o mesmo será carregado para o lookup e será marcado o campo Gerador  Dot.Net.
2. Caso contrário, se não existir relatório .NET e existir relatório Delphi, o relatório Delphi será carregado para o lookup e o campo de Gerador Dot.Net será desmarcado.
3. Caso tenha informado default para os dois tipos de relatório valerá a regra 1 e desconsiderará a regra 2.

**Tabelas**

|  |  |
| --- | --- |
| *TCPARAMETROS* | *Parâmetros da Cotação* |
| *TTMVEXT* | *Tipos de movimentos* |
