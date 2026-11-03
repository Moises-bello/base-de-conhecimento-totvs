---
article_id: 360027701492
category: Escrita Fiscal - Impostos - IPI
content_hash: 4bed0e6c4d00bd6d03a2bd76723c0ef5296f1fd59e2bbecf97fb81f1b266e26f
fetched_at: '2026-06-28T22:39:29.032315+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Cadastro da Tabela
  IBPT - P12
type: support-article
updated_at: '2026-06-11T17:56:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027701492-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Cadastro-da-Tabela-IBPT-P12
---

**Dúvida**Inconsistência no momento da Carga da Tabela IBPT. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027829932/mceclip0.png)  
  
   
 **Ambiente**Protheus - Livros Fiscais -  A partir da versão 11.80  
  
**Solução**

Verifique se a nomenclatura do arquivo refere-se a TabelaIBPTax+UF+Versão da tabela. Ex: TabelaIBPTaxAM14.2.a.csv.

Caso o nome não esteja com esta nomenclatura, o arquivo não será importado.

# Cadastro da Tabela IBPT

Implementada a rotina de **Cadastro da Tabela IBPT (FISA092)**, que importa da tabela fornecida pelo IBPT (Instituto Brasileiro de Planejamento Tributário) por ente Tributário,  a partir da versão 14.2.a. Nesta rotina é possível realizar a manutenção dos códigos cadastrados.

## Procedimentos para Utilização

1)       No módulo **Livros Fiscais (SIGAFIS)** acesse **Atualizações/ Cadastros/****Tabela IBPT****(FISA092)**. Proceda conforme segue abaixo:

2)       Selecione a opção **Importar**.

3)       Informe a pasta e o arquivo (CSV) disponibilizado pelo IBPT cuja versão seja igual ou superior a 14.2.a, Instituto Brasileiro de Planejamento Tributário para a Importação.

4)       Os campos serão preenchidos conforme a tabela informada. Clique em **Ok**.

**Importante**

Além da importação da tabela IBPT por ente tributário, o sistema permite Inclusão, Alteração, Exclusão do cadastro através das opções **Incluir, Alterar, Excluir e Visualizar**.

Para que o sistema busque informações da tabela CLK é necessário configurar o parâmetro MV\_ENTETRB, que se os percentuais da Lei 12.741 serão apresentados por ente de tributação (Federal / Estadual ou Municipal).

|  |  |
| --- | --- |
| Nome | MV\_ENTETRB |
| Tipo | Lógico |
| Conteúdo | .F. |
| Descrição | Indica se os percentuais da Lei 12.741 serão apresentados por ente de tributação (Federal / Estadual ou Municipal). T= Sim; F= Não |

**Importante**

Para importação das tabelas IBPT cuja versão seja inferior a 14.2.a será necessário seguir os procedimentos disponibilizados nos boletins **[Carga Tributaria](http://tdn.totvs.com.br/pages/viewpage.action?pageId=185750463)** e **[Cadastro da Tabela IBPT LC116](http://tdn.totvs.com.br/pages/viewpage.action?pageId=185750471)**.

5)       No **Configurador (SIGACFG)** acesse **Ambientes/ Cadastro/ Menu (CFGX013)**. Informe a nova opção de menu do **Livros Fiscais (SIGAFIS)** conforme instruções a seguir:

|  |  |
| --- | --- |
| Menu | Atualizações |
| Submenu | Cadastros |
| Nome da Rotina | Cadastro IBPT |
| Programa | FISA092 |
| Módulo | 09 |
| Tipo | 01 |
| Tabelas | CLK |

## Informações Técnicas

|  |  |
| --- | --- |
| Tabelas Utilizadas | CLK – Cadastro IBPT |
| Funções Envolvidas | FISA092 – Cadastro da Tabela IBPT |
| Sistemas Operacionais | Windows®/Linux® |

<http://tdn.totvs.com/display/public/PROT/Cadastro+da+Tabela+IBPT+-+P12>
