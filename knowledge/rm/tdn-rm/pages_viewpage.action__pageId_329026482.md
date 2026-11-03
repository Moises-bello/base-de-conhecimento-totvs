---
content_hash: 6933fdfc60b1ce59f05d9781f5b345d5917b496453a2be1aae630fb20dff441f
fetched_at: '2026-06-29T00:08:48.863585+00:00'
page_id: '329026482'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-1130 DT Ajuste de Pagamento a Maior e a Menor em Valor de Integração
  do Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=329026482
version: 7
---

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão Financeira* |
| **Cadastros Iniciais:** | *O comportamento do Retorno Bancário está condicionado à parametrização de Valores de Integração no Educacional, devidamente estabelecidos os valores de integração para pagamento a maior e a menor.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FIN000169 |
| **País(es):** | *Brasil* |
| **Tabelas Utilizadas:** | *FLANBAIXAINTEGRACAO* |

## Descrição

O retorno bancário do Financeiro disponibiliza opção de tratamento de pagamento a maior e a menor, através de valores de integração, caso o Educacional esteja configurado para utilização de valores de integração para esta finalidade.

## Procedimento para Implantação

Não é necessário nenhum procedimento específico para implantação no Financeiro.

## Atualizações do Compatibilizador

Não é necessário nenhuma conversão de base de dados no Financeiro.

## Procedimento para Configuração

Os valores de integração devem ser configurados diretamente no Educacional. Caso existam valores de integração associados a pagamento a maior, e pagamento a menor, as respectivas opções de ajuste na interface do Retorno Bancário serão disponibilizadas para uso.

## Procedimento para Utilização

* Cadastre os Valores de integração no Educacional >> Financeiro / Contábil >> Financeiro >> Valores de Integração Financeira conforme imagem abaixo.

* Após criar os valores de integração do Financeiro na base de dados, acesse o parametrizador do módulo Educacional conforme imagem abaixo e selecione as opções.

* Desta forma o retorno de cobrança utilizado no TOTVS Gestão Financeira terá como default para os lançamentos do Educacional, os valores de integração para serem utilizados em situações de pagamento a maior e pagamento a menor.
* Ao executar o processo de retorno bancário no Financeiro, caso seja informado algum campo para o recebimento dos valores de Pagamento a Maior e/ou Pagamento a Menor, se o lançamento tiver sido criado pelo Educacional e estiver configurado para utilizar valores de integração para esta finalidade, o sistema irá se comportar conforme indicado pelo Educacional.
* Por outro lado, se ao executar o processo de retorno bancário no Financeiro, e esteja informado para "Não Baixar" em caso de recebimento de valores de Pagamento a Maior e/ou Pagamento a Menor, o sistema NÃO procederá a baixa, mesmo que esteja configurado no Educacional a indicação de valores de integração para este fim.

**Tratamento de exceções:**

1. O Campo configurado na tela de processamento do retorno de cobrança, valores opcionais, irá afetar apenas lançamentos gerados pelo Educacional em data anterior à data de configuração do valor de integração.
2. Para lançamentos do Educacional que foram gerados após a data de configuração do valor de integração, o sistema irá utilizar os valores de integração parametrizados no Educacional >> Integração >> Financeiro >> Educacional >> Fin - Vlrs. Opcionais/Integração.
