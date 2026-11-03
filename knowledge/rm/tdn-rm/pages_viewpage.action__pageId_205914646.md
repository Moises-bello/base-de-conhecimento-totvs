---
content_hash: 058db2208c1fa953da5f79278c4b7a27c50f56cb90d9e91fa4f0d2421f99ee8b
fetched_at: '2026-06-29T00:06:12.214107+00:00'
page_id: '205914646'
product: rm
source: tdn-rm
title: TSTE01_DT_Variável_Bolsa_Campo_Histórico_Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=205914646
version: 4
---

# VARIÁVEIS DE BOLSA PARA O CAMPO HISTÓRICO DO MOVIMENTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de movimento por competência* | *Geração de movimento por competência* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Geração de movimento por boleto* | *Geração de movimento por boleto* | |
| **Cadastros Iniciais:** | *1. Cadastro das tags de bolsa no campo histórico da parametrização da integração Fiscal do sistema.* |
| **Parâmetro(s):** | *1) Educacional | Integração | Fiscal | Histórico .* |
| **Ponto de Entrada:** | *N/A.* |
| **Chamados relacionados** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **País(es):** | *Todos.* |
| **Banco(s) de Dados:** | *Todos.* |
| **Tabelas utilizadas:** | *N/A* |
| **Sistema(s) operacional(is):** | *Todos.* |
| **Versões/Release:** | *11.82.42* |

## Descrição

Foi realizada melhoria no processo de geração de movimento, de forma que o campo histórico da parametrização do sistema, suporte a tradução de variáveis referentes as bolsas que compõe o desconto incondicional do movimento.

Com o novo modelo, o sistema passa a suportar novas variáveis referentes as bolsas. São elas:

- [BOL.CX] – Máscara de histórco para o código da bolsa;

- [BOL.DX] – Máscara de histórco para a descrição da bolsa;

- [BOL.VX] – Máscara de histórco para o valor da bolsa;

Para essas variáveis em específico, A letra “C” é referente ao código da Bolsa, a letra “D” é referente a descrição da Bolsa e a letra “V” é referente ao valor da bolsa. O caractere curinga “X” deve ser substituído por uma número inteiro acima de zero, para representar a bolsa pela qual serão obtidas as informações. Assim, ao formatar o histórico, devem ser criadas tantas variáveis quanto a quantidade máxima de bolsas incondicionais que se espera que uma parcela possua.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação da release *11.82.42* deste chamado.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Configurador Educacional**, acesse **Educacional/Fiscal/**. Configure o(s) parâmetro(s) a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Histórico:** | *Histórico para a geração de movimento.* |
| **Tipo:** | *Texto.* |
| **Cont. Por.:** | *Falso* |
| **Descrição:** | *Texto que será levado para o campo histórico longo dos items de movimento.* |

## Procedimento para Utilização

**Exemplo:**

1.            No sistema TOTVS Educacional, acesse Parâmetros / Integração / Fiscal /  e configure o parâmetro Histórico para que contenha uma das tags criadas.

2.            Acesse a visão de contratos financeiros.

       3.            Selecione um contrato que possua bolsa.

       4.            Execute o processo Gerar Movimento por Competência.

       Obs: Acessando o sistema TOTVS Gestão de Estoque, Compras e Faturamento, é possível visualizar o campo histórico longo do item de movimento criado para confirmar a tradução da variável parametrizada no sistema TOTVS Educacional.
