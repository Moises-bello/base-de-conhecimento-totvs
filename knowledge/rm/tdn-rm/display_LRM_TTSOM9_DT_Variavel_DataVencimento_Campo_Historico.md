---
content_hash: 1b460adebca819334d327f1a8d021bd5987a541a165becb3ea679f265e446305
fetched_at: '2026-06-29T00:06:19.529101+00:00'
page_id: '219698593'
product: rm
source: tdn-rm
title: TTSOM9_DT_Variavel_DataVencimento_Campo_Historico
type: documentation
url: https://tdn.totvs.com/display/LRM/TTSOM9_DT_Variavel_DataVencimento_Campo_Historico
version: 6
---

# VARIÁVEL DATA DE VENCIMENTO DO LANÇAMENTO PARA O CAMPO HISTÓRICO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de movimento por boleto* | *Geração de movimento por boleto* | | *Geração de movimento por competência* | *Geração de movimento por competência* | | *Geração de lançamentos* | *Geração de lançamentos* | | *Aproveitamento de valores em conta corrente* | *Aproveitamento de valores em conta corrente* | | *Repasse de Bolsas* | *Repasse de Bolsas* | |
| **Cadastros Iniciais:** | 1. *Cadastro da tag [LAN.DV] no campo histórico da parametrização da integração Fiscal do sistema.* 2. *Cadastro da tag [LAN.DV] no campo histórico da parametrização da integração Financeiro do sistema.* 3. **Cadastro da tag [LAN.DV] no campo histórico das funcionalidades citadas acima.** |
| **Parâmetro(s):** | *1) Educacional | Integração | Fiscal | Histórico . 2*) Educacional | Integração | Financeiro | Histórico .** |
| **Ponto de Entrada:** | *N/A.* |
| **Chamados relacionados** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **País(es):** | *Todos.* |
| **Banco(s) de Dados:** | *Todos.* |
| **Tabelas utilizadas:** | *N/A* |
| **Sistema(s) operacional(is):** | *Todos.* |
| **Versões/Release:** | *11.82.42* |

## Descrição

Foi realizada melhoria na formatação de histórico nas funcionalidades explicitadas acima de forma que essa formatação suporte a data de vencimento do lançamento financeiro.

A opção [LAN.DV] informada nos parâmetros de histórico, conterá os valores abaixo conforme o processo que está sendo executado.

1) Geração de movimentos por boleto: A opção [LAN.DV] será formatada com a data de vencimento do lançamento financeiro respectivo ao item de movimento.

2) Geração de movimentos por competência: A opção [LAN.DV] será formatada como string vazia (nulo) visto que o movimento gerado por competência não tem vínculo direto com o lançamento financeiro

3) Geração de lançamentos: A opção [LAN.DV] será formatada com a data de vencimento do lançamento financeiro.

4) Aproveitamento de valores em conta corrente: A opção [LAN.DV] será formatada com a data de vencimento do lançamento financeiro criado.

5) Repasse de Bolsas: A opção [LAN.DV] será formatada com a data de vencimento do lançamento financeiro criado.

OBSERVAÇÃO: O histórico formatado nos processos de gerações de movimentos são os históricos dos itens de movimento que poderão ser histórico curto ou histórico longo dependendo da parametrização informada no módulo Gestão de Compras (Nucleus)

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação da release *11.82.42* deste chamado.

## Procedimento para Configuração

N/A

## Procedimento para Utilização

**Exemplo:**

1. Geração de movimentos
   1. Acesse o Totvs Gestão de Estoque, Compras e Faturamento, parametrize o tipo de histórico a ser utilizado no item de movimento (Movimento -> Campos Livres) que poderá ser Histórico Longo ou Histórico Curto
   2. Nos parâmetros de integração com o Fiscal acesse Parâmetros / Integração / Fiscal /  e configure o parâmetro Histórico para que contenha a tag [LAN.DV]. Esse campo conterá o valor default com mnemônicos a serem convertidos para valores na geração de movimento
   3. Execute o processo de geração de movimentos (por boleto ou por competência), preencha os campos necessários.
   4. Após execução, verifique se o mnemônico [LAN.DV] foi formatado corretamente no caso de geração de movimentos por boleto ou se foi formatado como string nula no caso de geração de movimentos por competência (visto que não temos vínculo com lançamento financeiro nesse último caso)
2. Geração de lançamentos
   1. Nos parâmetros de integração com o Financeiro acesse Parâmetros / Integração / Financeiro /  e configure o parâmetro Histórico para que contenha a tag [LAN.DV]. Esse campo conterá o valor default com mnemônicos a serem convertidos para valores na geração de lançamentos
   2. Execute a geração de lançamentos (geração por parcela ou Wizard) e preencha os campos obrigatórios se necessário
   3. Após execução, verifique se o mnemônico [LAN.DV] foi formatado corretamente com a data de vencimento do lançamento.
3. Aproveitamento de Valores em Conta Corrente
   1. Parametrize os valores opcionais para pagamento a maior e/ou a menor em Parâmetros / Integração / Financeiro / Cobrança Retroativa
   2. Gere um lançamento para uma parcela qualquer
   3. Baixe esse lançamento preenchendo valor para o campo de pagamento a maior ou a menor
   4. Aproveite o crédito ou débito gerado na conta corrente do aluno através do anexo de conta corrente do aluno ou do Wizard de aproveitamento
   5. Verifique se o mnemônico [LAN.DV] foi formatado corretamente com a data de vencimento do lançamento no lançamento criado pelo aproveitamento.
4. Repasse de Bolsas
   1. Gere um lançamento para o aluno que contenha uma bolsa de crédito
   2. Inclua um repasse para a bolsa de crédito no contrato do aluno
   3. Execute o processo de Repasse de Bolsas
   4. Verifique se o mnemônico [LAN.DV] foi formatado corretamente com a data de vencimento do lançamento no lançamento criado pelo repasse
