---
content_hash: 5a9e15a25df2edd5145eca730bc3e1bd1681a799b29d1e144428fd9e47f8be91
fetched_at: '2026-06-29T00:09:42.585672+00:00'
page_id: '431678780'
product: rm
source: tdn-rm
title: DT Envio de Ordem de Compra Automático Paradigma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=431678780
version: 14
---

# PARADIGMA - ORDEM DE COMPRA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Tipos de Movimento. | RMSParamsWizardAction. | |
| **Cadastros Iniciais:** | Não se aplica. |
| **Parâmetro(s):** | Código do Tipo de Movimento = Pedido de Compra (1.1)  Tipo do Movimento de Compras = Pedido de Compras (Etapa - Compra/Venda - Outros Dados)  Envio Automático para Portal de Compras Paradigma = Marcado |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATESTCNTFTOF01-3516. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | TTMVEXT - Tipos de Movimento. |
| **Sistema(s) Operacional(is):** | Windows 10. |

## Descrição

Permitir que o usuário possa integrar automaticamente a Ordem de Compras do BackOffice RM com o Portal de Compras Paradigma ao realizar o processo de Retorno de Cotações Orçadas.

### Configurar Tipo de Movimento de Ordem de Compra

Para que a ordem de compra seja enviada automaticamente ao Portal Paradigma para o Aceite do Fornecedor, será necessário configurar o tipo de movimento de ordem de compra para o envio automático.

**Configuração de Tipo de Movimento**

* Tipo de movimento deve ser configurado como Envio Automático para Portal de Compras Paradigma (vide item Configurações e Parâmetros);

**Premissas para utilização do novo parâmetro**

* Parâmetro global de integração com Paradigma ativo (***Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.03 –Integrações | 04.03.05***)
* Tipo de movimento parametrizado como **Pedido**(***Parâmetros do Tipo de Movimento | Etapa 49 –Compras/Vendas Outros***)

### Retorno de Cotações Orçadas no Portal de Compras Paradigma

Quando executado via MDI, pela visão de Cotações, é apresentada a opção **Geração de Ordem Automática** no formulário de execução do processo de Retorno. Caso esta flag seja marcada, deve gerar automaticamente as Ordens de Compra para os itens encerrados no Portal de Compras Paradigma e apresentá-los na grid do tipo de movimento parametrizado.

Este processo também pode ser agendado para execução recorrente (ex.: de 30 em 30 minutos). Caso deseje que este processo seja sempre executado com a geração automática de ordem de compra, salve um agendamento recorrente com o parâmetro acima marcado.

### Envio de Ordem de Compra Automático ao Portal Paradigma

Quando o tipo de movimento de Ordem de Compra estiver configurado como **Envio Automático para Portal de Compras Paradigma,** ao executar o processo de **Retorno de Cotações Orçadas no Portal de Compras Paradigma**  para os movimentos de ordem de compra configurados como envio automático, após salvar o movimento no Backoffice RM será consumido o serviço de **[Integrar Pedido com Portal de Compras Paradigma](http://tdn.totvs.com/display/LRM/CMP_BT_Paradigma+-+Pedido+de+Compras_BRA_PCREQ-4539).**

### **Retorno de Cotações orçadas no Portal Paradigma**

A classe de parâmetros deste processo contém um novo campo que indicará se a ordem de compra será gerada automaticamente para o fornecedor vencedor da cotação, nome do parâmetro **GeraOrdemCompraAutomatico.**

Quando informado que é para gerar a ordem de compra, será consumido o serviço de Gerar Ordem de Compra da Cotação. Caso ocorra alguma validação que impede a criação da Ordem de Compra, o log do processo será atualizado com as informações e o Status do Processo ficará como aviso.

Este  novo parâmetro ficará disponível somente para utilização via webservice e para obter o xml esperado para utilização faça uma requisição via GetSchema ([http://servidor.com:8051/wsProcess/IwsProcess](http://bhn050102754.bh01.local:8051/wsProcess/IwsProcess)) utilizando o nome do processo **CmpRetornoCotacaoProc.**

### Inclusão de Ordem de Compra sem Cotação.

É possível incluir um movimento de Ordem de Compra vinculado ao Paradigma, mesmo que essa Ordem de Compra não seja gerada a partir de uma cotação. Para isso, esse tipo de movimento de Ordem de Compra deve estar com o Parâmetro **Envio Automático para Portal de Compras Paradigma**marcado. Assim, esse vinculo será realizado nos seguintes casos:

* Inclusão Manual direto da tela do Movimento de Ordem de Compra;
* Cópia de Movimento na mesma tela.
* Inclusão de Movimento de Ordem de Compra via Faturamento direto da Solicitação de Compra.
* Inclusão de Movimento de Ordem de Compra via Faturamento de Contrato.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações Biblioteca RM versão 12.1.23.

A opção de **Geração de Ordem Automática** está disponível após a aplicação do pacote de atualizações Biblioteca RM Patch versão 12.1.23.107 ou superior.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Gestão de Estoque, Compras e Faturamento**, acesse **Ambientes/Parâmetros/Gestão de Estoque, Compras e Faturamento/04.06 - Gestão de Compras/04.06.04 - Ordem de Compra**. Selecione um tipo de movimento e clique em **Parametrizar**. Na **Etapa Compra/Venda - Outros Dados**configure o(s) parâmetro(s) a seguir:

   |  |  |  |
   | --- | --- | --- |
   | **Parâmetro** | **Valor** | **Observação** |
   | **Tipo do Movimento de Compra:** | Pedido de Compras |  |
2. Na **Etapa Integração Paradigma**configure o(s) parâmetro(s) a seguir:

   |  |  |  |
   | --- | --- | --- |
   | **Parâmetro** | **Valor** | **Observação** |
   | **Envio Automático para Portal de Compras Paradigma:** | Marcado | Este parâmetro ficará disponível somente quando existir integração com Paradigma habilitada para a coligada logada. |
