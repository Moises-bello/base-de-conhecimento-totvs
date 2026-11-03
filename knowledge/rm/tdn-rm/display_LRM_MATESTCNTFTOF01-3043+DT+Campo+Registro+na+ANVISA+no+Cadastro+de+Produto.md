---
content_hash: e45651bea9fb332875ddf24335370707826b9ad0d0ae7fd66e1f548f240dd8cf
fetched_at: '2026-06-29T00:09:08.393167+00:00'
page_id: '387296911'
product: rm
source: tdn-rm
title: MATESTCNTFTOF01-3043 DT Campo Registro na ANVISA no Cadastro de Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/MATESTCNTFTOF01-3043+DT+Campo+Registro+na+ANVISA+no+Cadastro+de+Produto
version: 5
---

# REGISTRO NA ANVISA NO CADASTRO DE PRODUTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Cadastro de Produto. |
| **Situação/Requisito:** | Em atendimento a NF-e 4.0 se torna necessário informar o código de produto da ANVISA (tag cProdANVISA) para produtos do ramo de medicamentos.  Na Linha RM é necessário informar esse número nos Anexos do Produto | Informações - TOTVS Saúde. Entretanto, esse anexo somente está disponível se a Empresa possui a integração RM NUCLEUS x RM SAUDE ativa (Disponível em Ambiente | Parâmetros | Integrações de Sistemas) e possui licença para o módulo do RM SAUDE. |
| **Solução/Implementação:** | Visando a atender todos os clientes que utilizam o nosso produto, inclusive aqueles que possuem e não possuem licença no módulo do RM SAUDE foi criado um novo campo no cadastro de produto para que seja informado o número de registro do produto na ANVISA.  Este novo campo está disponível na aba Integração do Cadastro de Produto. |
| **Conversores e Parâmetros:** | Ambiente | Parâmetros | Integrações de Sistemas.  Cadastros | Produtos | Edição do Produto | Aba Integração. |
| **Tickets relacionados:** | Não se aplica. |
| **Requisito:** | MATESTCNTFTOF01-3043. |
| **Documento de Referência:** | [Cadastro de Produto](http://wikihelp.totvs.com.br/WikiHelp/EST/EST.Produto.aspx). |

## Descrição

Após a execução do script necessário para a criação do campo. Siga os passos abaixo para informar o número de registro na ANVISA no cadastro de produto:

1. Acesse o Cadastro de Produto | Edição do Produto | Aba Integração | Preencha a informação no novo campo criado, conforme figura abaixo:

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 12.1.18.341 e posteriores deste chamado.

## Dicionário de Dados

**Arquivo ou Código do Script:**/\*$Versao=NU.2018.08\_01\*/

|  |  |
| --- | --- |
| **Tabela** | TPRODUTODEF |
| **Campo** | REGISTROANVISA |
| **Tipo** | varchar. |
| **Tamanho** | 15. |
| **Valor Inicial** | Não se aplica. |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Número de Registro do Produto na ANVISA. |
| **Título** | Registro na ANVISA. |
