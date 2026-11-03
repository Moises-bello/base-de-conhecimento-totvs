---
content_hash: 30d6e8f35cede177ef497a63017b7bab5ba5366a4d878c6c1c4360afded5867e
fetched_at: '2026-06-29T00:06:06.204267+00:00'
page_id: '201729248'
product: rm
source: tdn-rm
title: DT_Defaults_de_Relatorios_para_Novo_Gerador_.Net
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Defaults_de_Relatorios_para_Novo_Gerador_.Net
version: 3
---

# DEFAULTS DE RELAÓRIOS PARA O NOVO GERADOR .NET

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e projetos |
| **Módulo:** | Estoque, Compras e Faturamento |
| **Requisito (ISSUE):** | PCREQ-5386 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle/SQL |
| **Tabelas utilizadas:** | TCPARAMETROS – Parâmetros da Cotação  TTMVEXT – Tipos de Movimento |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superiores. |
| **Versões/Release:** | 12.1.7 |

## Descrição

Permitir que o usuário, parametrize os relatórios Padrão para Pedido Orçamento, Padrão para Pedido Orçamento (E-mail), Padrão para Pedido Orçamento (Web) e Quadro Comparativo Default que tenham sido criados pelo novo gerador .NET. Também será possível parametrizar os relatórios do Movimento, do Tipo Fatura e do Tipo Duplicata que estejam neste mesmo formato.

**Desenvolvimento/Procedimento**

**Parametrização dos Defauts de Relatórios .Net**

Nos parâmetros do TOTVS Gestão de Estoque, Compras e Faturamento foram disponibilizados novos parâmetros que serão utilizados para informar os layouts defaults no Novo Gerador .Net.

Os processos que possuem relatórios defaults são os seguintes:

*Comunicar Fornecedores*

O processo de Comunicar Fornecedores, que está disponível na tela de edição da Cotação, irá utilizar como relatório default o layout que estiver parametrizado nos parâmetros “Relatório Padrão para Pedido Orçamento .NET”, “Relatório Padrão para Pedido Orçamento .NET (E-mail)” ou “Relatório Padrão para Pedido Orçamento .NET (Web)” de acordo com o Tipo de Comunicação correspondente que tenha sido selecionado no assistente.

 

 

  

 

*Imprimir Quadro Comparativo de Preços e Envio do Quadro Comparativo via email*

      O processo de Imprimir Quadro Comparativo de Preços e o Envio do Quadro Comparativo via email, que estão disponível na tela de edição da Cotação, irão utilizar como relatório default o layout que estiver parametrizado no parâmetro “Relatório Quadro Comparativo Default .NET”.

 

*Imprimir Movimentos*

O processo de Imprimir Movimentos irá verificar o tipo de relatório selecionado pelo usuário e irá utilizar como relatório default o layout que estiver parametrizado nos parâmetros “Formato do Relatório do Movimento”, “Formato do Relatório do Tipo Fatura” ou “Formato do Relatório do Tipo Duplicata” de acordo com o tipo de relatório selecionado.

 

 

 **Seleção do Tipo de Relatório**

 Nas telas de impressão serão apresentados dois campos, um campo para o usuário marcar se será utilizado o Gerador Dot.Net ou não e um campo de Lookup que será carregado com o Formato do Relatório default que estiver parametrizado.

 

 Informações Adicionais

 A regra que irá definir qual relatório default (.NET ou Delphi) será carregado para o lookup será a seguinte:

 1 - Se existir relatório .NET parametrizado, o mesmo será carregado para o lookup e será marcado o campo Gerador  Dot.Net.

 2 - Caso contrário, se não existir relatório .NET e existir relatório Delphi, o relatório Delphi será carregado para o lookup e o campo de Gerador Dot.Net será desmarcado.

 3 -  Caso tenha informado default para os dois tipos de relatório valerá a regra 1 e desconsiderará a regra 2.
