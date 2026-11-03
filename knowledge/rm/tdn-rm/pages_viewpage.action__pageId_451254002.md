---
content_hash: 89807466a2e8b9bab921d1893504f7c4517ea35156b8637ebdc12ea074d70339
fetched_at: '2026-06-29T00:09:58.107978+00:00'
page_id: '451254002'
product: rm
source: tdn-rm
title: DT Produção Conjunta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=451254002
version: 16
---

# PRODUÇÃO CONJUNTA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Produção Conjunta. | Produção Conjunta. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Produto Composto. | Expandir Produto Composto. | | Processo Produtivo Simples. | Processo Produtivo Simples. | |
| **Cadastros Iniciais:** | Realizar o cadastro do Produto Composto. |
| **Parâmetro(s):** | Parâmetros Gerais | Tabelas | Produtos | Definições Gerais | Definições de Produto 3/3 | Produto Composto marcado.  Parâmetros do Tipo de Movimento | Etapa Item - Identificação 2/2 | Utilizar Produto Composto marcado.  Parâmetros do Tipo de Movimento | Etapa Mov - Outros Dados | Usar Cópia de Movimentos por referência marcado | Motivo de Referência: 9 - Produção. |
| **Tickets relacionados** | **Informe o(s) chamado(s) relacionado(s).** |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Sistema(s) Operacional(is):** | Windows 7 ou superior. |

## Descrição

Utilizando o processo produtivo simples no TOTVS Gestão de Estoque, Compras e Faturamento é possível também realizar Produção Conjunta, para isso é necessário algumas configurações adicionais.

O produto deve ser definido como um produto composto com as respectivas quantidades dos produtos que o compõe e a estrutura que representa esse produto deve estar com o parâmetro produção conjunta marcado.

Esses produtos que fazem parte do produto composto serão movimentados ao realizar a expansão do item (produto da ordem) no movimento de Entrada de Produção Simples que é gerado via cópia por referência a partir do Movimento de Ordem de Produção incluído com o produto composto.

Utilizando o processo de produção conjunta é possível gerar dados para os blocos fiscais K290, K291 e K292.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações ***(Patch)*** deste chamado.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS****(Parâmetros Gerais)**

1. Na nova MDI acesse Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01 - Parâmetros Gerais | 04.01.04 - Tabelas | 04.01.04.07 - Produtos | 04.01.04.07.01 - Definições Gerais | Definições de Produto 3/3 | Produto Composto marcado:  
     
     
   **(Parâmetros do movimento - Entrada de Produto Acabado - Produção Conjunta)**
2. Na nova MDI acesse Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros do Tipo de Movimento | Etapa Item - Identificação 2/2 | Utilizar Produto Composto marcado:
3. Na nova MDI acesse Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros do Tipo de Movimento | Etapa Mov - Outros Dados | Usar Cópia de Movimentos por referência marcado | Motivo de Referência: 9 - Produção:

## Procedimento para Utilização

**CADASTRAR PRODUTO COMPOSTO**

Após realizar a parametrização para utilizar o Produto Composto, acesse o cadastro de Produto e selecione o produto que será utilizado como composto. Vá em Anexos | Produtos Compostos:

Cadastre todos os subprodutos que compõem o Produto Composto selecionado.

Defina a estrutura do produto como sendo produção conjunta:

Informação 

O campo **Produção****Conjunta**do cadastro de **Estruturas** ficará disponível após aplicar o patch da **Biblioteca RM 12.1.29.254 ou superior** e executar o Atualizador de base de dados.

**PRODUÇÃO CONJUNTA**

1. Realizar a Entrada do Produto Acabado utilizando o Motivo de Referência de 9 - Produção e referenciando a Ordem de Produção do Produto Composto.
2. No movimento de Entrada de Produto Acabado, selecionar o Produto Composto e clicar em Expandir Itens Compostos:
3. Será apresentada uma mensagem em relação a expansão completa do Produto Composto. Ao marcar "Sim", o sistema irá expandir os itens e os subitens do produto composto, se existir, e se optar por não expandir os itens vai produzir o item indicador no movimento que representa a ordem de produção.:
4. Após definir os produtos e a quantidade gerada na produção, salve o movimento de Entrada de Produto Acabado. Ao realizar a expansão do Produto Composto, o sistema **somente irá criar relacionamento entre os movimentos**, não havendo relacionamento entre os itens.

**Bloco K**:

A Produção Conjunta é reportada no SPED Fiscal através dos Bloco K290 (Ordem de Produção), K292 (Baixa/Consumo realizado) e K291 (Produção Gerada).

A geração desse Bloco é feita quando existe a movimentação de Baixa/Consumo e/ou Produção Gerada, então, se afetou estoque vai gerar registro no mês.

Se tiver apenas movimento de baixa vai gerar K290 e K292, se tiver apenas movimento de entrada vai gerar K290 e K2921, se ocorreu baixa e entrada no mês então gera K290, K291, K292.

O sistema permite e consegue gerar dados mesmo quando os movimentos ocorrem em meses diferentes, em cada mês reportando o que ocorreu em relação a produção.

**Observação**:

A baixa da matéria-prima consumida no processo produtivo simples deve ser realizada antes da geração do produto acabado através da cópia por referência, após a cópia por referência não é possível faturar o movimento "Ordem de Produção" para realização da baixa.

## Documentos de Referência

* [Produtos Compostos](https://tdn.totvs.com/display/public/LRM/Produtos+Compostos)
* [Processo Produtivo Simples](http://tdn.totvs.com/display/LRM/MOV0001_Bloco_K_Processo_Produtivo_Simples)
