---
content_hash: a236342c3f22efaf25f6dd515b13d769128652a5ec5d4dddf938730b66254cdb
fetched_at: '2026-06-29T00:06:25.451430+00:00'
page_id: '224397434'
product: rm
source: tdn-rm
title: DT_Transferencia_funcionario
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Transferencia_funcionario
version: 1
---

# Transferência de Funcionário - Novo controle na criação de chapas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Ambiente / Parâmetros* | *Transferência* | |
| **Versão/Release:** | *12.1.4* |

## Descrição

No Parametrizador  “Funcionário / Configuração da Chapa” o flag “**Incrementar 4 dígitos de controle no final da chapa dos demitidos**” tem como objetivo auto incrementar a sequência das transferências (Txxx) ao final da chapa, ou seja, marcando este parâmetro, no processo de transferência a chapa do registro ativo será mantida e a chapa do registro demitido será preenchida conforme regra acima.   
Obs¹: Deve existir uma reserva de no mínimo 4 dígitos do tamanho máximo da chapa (16 dígitos).   
Obs²: O parâmetro “Sequenciamento de Chapa e Registro na Transferência Individual” deve estar desmarcado. 2. Também foi implementado no Parametrizador em “Rescisão / transferência” um parâmetro para não exibir os funcionários com saída por transferência (código demissão 5 e 6) na visão de funcionário, exceto quando a transferência for dentro da competência atual.

## Procedimento para Utilização

Para que o usuário tenha acesso aos flags é preciso seguir o seguinte caminho. **Acesse Folha de Pagamento / Ambiente / Parâmeros / Folha de pagamento.**

Selecione Funcionário e em seguida clique em “Avançar\_>

Em seguida selecione Configuração da Chapa e o flag estará disponível.

Em Configurações / Parametrizado, selecione Rescisão e em seguida clique em Avançar >

Em seguida selecione Configuração da Chapa e o flag estará disponível.
