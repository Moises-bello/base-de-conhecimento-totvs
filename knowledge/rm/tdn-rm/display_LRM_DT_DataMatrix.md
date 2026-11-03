---
content_hash: 830615f0b3d3ab83d4247bfbc77de7d84c192efd62888c4f295478fddc9d7d40
fetched_at: '2026-06-29T00:06:07.854543+00:00'
page_id: '201739210'
product: rm
source: tdn-rm
title: DT_DataMatrix
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_DataMatrix
version: 1
---

# DataMatrix

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Inserir item de movimento pelo código DataMatrix | MovInsereProdutoCodigoEANForm |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Movimento | *Informe o nome técnico da(s) rotina(s) envolvidas.* | |  |  | |
| **Cadastros Iniciais:** | Produto, Código de Barras do Produto |
| **Parâmetro(s):** | Código do Produto : Código Datamatrix” |
| **Requisito (ISSUE):** | PCREQ-6374 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas utilizadas:** | TPRDCODIGO – Código de Barras  TITMMOV – Item de movimento |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superior. |
| **Versões/Release:** | 12.1.8 |

## 

## Descrição

O código DataMatrix é um código de barras bidimensional que permite a codificação grande quantidade de informações em um espaço muito compacto que se fez necessário na produção de alguns tipos de produtos como por exemplo a produção de medicamentos. Com a finalidade de rastreamento de medicamentos e com a cooperação de órgãos reguladores e através da RDC59 foram criadas normas para o seu uso e implementação.

A rastreabilidade surgiu devido à necessidade de saber a localização de determinado produto na cadeia logística. Este conceito representa a capacidade de recuperação do histórico, da aplicação ou da localização de um produto, através da impressão de números de identificação. Ou seja, a habilidade de se poder saber através de um código de barras qual a identidade de uma mercadoria e as suas origens.

Os benefícios mais significativos da rastreabilidade de produtos no setor da saúde são:

• Garantia da segurança de pacientes e de profissionais de saúde;

• Controle dos custos de produção, operação, compras e de logística;

• Conformidade com as normas em vigor.

A implementação será realizada no módulo de Movimentos para lançamento e consulta de produtos no item de movimento.

Será implementado apenas os seguintes Identificadores de Aplicação (AI’s):

* AI (01): Numeração Global de Item Comercial – GTIN;
* AI (17): Data de Validade;
* AI (10): Numero do Lote;

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Nos parâmetros do Tipo de Movimento será a acrescentada na opção Código do Produto o valor “Código Datamatrix” (Etapa 26 – Item – Identificação) para utilizar Código do Produto igual a “Código Datamatrix”

## Procedimento para Utilização

 Estará disponível duas possíveis formas de inclusão do código Datamatrix:

* Item de Movimento. Pela tela de edição do Item de Movimento, semelhante ao código EAN, ao clicar no botão 'Código DataMatrix'.

* Movimento. Pela guia do Item de Movimento, ao clicar no botão 'Inserir pelo código DataMatrix'

Ao informar todo o código Datamatrix na inclusão de Item de Movimento será incluído o Lote, caso o mesmo não exista, com a quantidade informada pelo usuário na tela. Se o Lote estiver parametrizado para utilizar numero do lote seqüencial  **(Parâmetros Gerais – Tabelas – Produto – Lote)** , será apenas acrescido o valor anterior mais um, caso contrario, será utilizado o numero do lote do fabricante contido no código Datamatrix bem como a sua data de validade.

Ao incluir um Lote existente será verificado na parametrizaçãopara o Item de Movimento se o mesmo possui o Status do Lote conforme a configuração no parametrizador **(Etapa 30 – Item – Lote / Grade Numerada/ Numero de serie)**. Se for incluir um Lote novo conforme regra supracitada será incluído o Lote com o 1º primeiro Status parametrizado.

Ao informar o Produto através do código Datamatrix e o mesmo não for controlado por Lote será emitida uma mensagem de erro: “O produto X não é controlado por lote.”

Ao incluir um Lote no momento de informar o Código e o mesmo não possuir o Status conforme a parametrização do Tipo de Movimento será emitida a mensagem: “Status do Lote não permitido para o Tipo de Movimento X”.
