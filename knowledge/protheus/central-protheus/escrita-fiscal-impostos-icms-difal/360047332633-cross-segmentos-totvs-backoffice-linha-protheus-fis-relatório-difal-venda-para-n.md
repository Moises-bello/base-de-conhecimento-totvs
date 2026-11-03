---
article_id: 360047332633
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: a382e9500ff3ff1e8fe843c5f18aecc3e894e8ce88623e0e1a77851c0a0e6d7d
fetched_at: '2026-06-28T22:39:19.312381+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Relatório DIFAL -
  Venda para Não Contribuinte - FISR087
type: support-article
updated_at: '2021-09-27T20:24:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332633-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Relat%C3%B3rio-DIFAL-Venda-para-N%C3%A3o-Contribuinte-FISR087
---

**Dúvida**Qual relatório é possível gerar as notas fiscais com cálculo do Difal - Venda para Não contribuinte?  
   
 **Ambiente**Protheus a partir versão 11.8  
  
**Solução**

Relatório FISR087

Listagem de conferência dos documentos fiscais com cálculo do Difal/FECP, conforme alterações da EC 87/15.

**Configurações do Menu**

* No **Configurador (SIGACFG)** acesse **Ambiente/ Cadastros/ Menus**e inclua no *menu* **Livros Fiscais (SIGAFIS)**, a opção para execução do **Listagem NF EC 87/15**, conforme especificação a seguir:

| **Nome do Menu** | **Submenu** | **Nome da Rotina** | **Programa** | **Tabelas** |
| --- | --- | --- | --- | --- |
| Relatórios | List. Conferência | Listagem NF EC 87/15 | FISR087 | SF3 |

**Procedimentos para Utilização**

Acessar no módulo Livros Fiscais, Relatórios/List. Conferência/ Listagem NF EC 87/15 e preencha as seguintes informações:

Data inicial : Informe a data inicial da listagem

Data Final : informe a data final da listagem

Tipo de Listagem : Informe se deseja visualizar as notas ficais da seguinte maneira:

1- Todas UF: Irá listar documento fiscal com cálculo do Difal **independente** se o contribuinte tenha ou não Inscrição Estadual no Estado de destino

2- UF com IE: Irá listar somente documento fiscal com cálculo do Difal onde o Contribuinte **tenha** Inscrição Estadual no Estado de destino

3- UF sem IE : Irá listar somente documento fiscal com cálculo do Difal onde o Contribuinte **não** Inscrição Estadual no Estado de destino

 

O relatório irá listar documento fiscal gravado na tabela SF3 que tenha calculado DIFAL, seja de documento de saída ou de entrada. A listagem terá por padrão as seguintes colunas:

| Filial | Destino | NF | Série | Emissão | CFOP | Clie/For | Loja | Tipo | Valor Contábil | Base de ICMS | Difal do destino | Difal de Origem | FECP | N. Guia | N. Título | Prefixo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

 

 Exemplo de impressão:

 

![](https://tdn.totvs.com/download/attachments/224105637/image2016-1-28%2016%3A0%3A20.png?version=1&modificationDate=1453993236000&api=v2)

 

 

 

 

![](https://tdn.totvs.com/download/attachments/224105637/image2016-1-28%2016%3A0%3A43.png?version=1&modificationDate=1453993259000&api=v2)

 

 

![](https://tdn.totvs.com/download/attachments/223927604/image2016-10-20%2011%3A48%3A52.png?version=1&modificationDate=1476971335000&api=v2)

 

A listagem será agrupada por filial e estado de destino.

**IMPORTANTE**Caso o estado de destino estiver informado no parâmetro MV\_SUBTRIB, não será apresentado valores nas colunas "N.Guia" , "N.Título" e "Prefixo".

 

É possível personalizar o relatório, incluindo colunas e filtros que desejar:

![](https://tdn.totvs.com/download/attachments/224105637/image2016-1-28%2016%3A1%3A50.png?version=1&modificationDate=1453993326000&api=v2)

 

 

![](https://tdn.totvs.com/download/attachments/224105637/image2016-1-28%2016%3A2%3A8.png?version=1&modificationDate=1453993344000&api=v2)

 

 

Todos os campos da tabela SF3 estão disponíveis para serem incluídos no relatório.

 

Podemos também realizar filtros se necessário:

 

 

![](https://tdn.totvs.com/download/attachments/224105637/image2016-1-28%2016%3A2%3A33.png?version=1&modificationDate=1453993369000&api=v2)

 

 

Todos os campos da SF3 estão disponíveis para realização de filtros.

Ainda é possível exportar as informações para planilha eletrônica:

![](https://tdn.totvs.com/download/attachments/223927604/image2016-1-28%2016%3A22%3A3.png?version=1&modificationDate=1453994540000&api=v2)

![](https://tdn.totvs.com/download/attachments/223927604/image2016-1-28%2016%3A22%3A53.png?version=1&modificationDate=1453994590000&api=v2)
