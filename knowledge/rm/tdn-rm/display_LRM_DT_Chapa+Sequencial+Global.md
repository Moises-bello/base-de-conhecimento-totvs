---
content_hash: 2864e7d651ee451ca747a0f65fa3fefddba061e14e29bcc68a667b10c8c62a7c
fetched_at: '2026-06-29T00:08:17.152669+00:00'
page_id: '253987688'
product: rm
source: tdn-rm
title: DT_Chapa Sequencial Global
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Chapa+Sequencial+Global
version: 3
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Função:** | *Informe a função.* |
| **Situação/Requisito:** | *Informe a situação/requisito.* |
| **Solução/Implementação:** | *Informe a solução/implementação.* |
| **Conversores e Parâmetros:** | *Informe os conversores/parâmetros.* |
| **Chamados relacionados:** | *Informe o(s) chamado(s) relacionado(s).* |
| **Requisito (ISSUE):** | *Informe o requisito relacionado.* |

## Descrição

Esta inovação tem como objetivo evoluir o produto para permitir a inclusão de chapas de identificação dos funcionários sequenciais para multi coligadas. A chapa deverá seguir uma sequência única para todas coligadas (empresas).

## Procedimento para Utilização

### 1 - Parametrizador

Deverá marcar o parâmetro "Utiliza sequencia global" em Parametrizador | Funcionário | Configuração da Chapa para ativar o sequenciamento global de chapas.

Este parâmetro somente ficará disponível se estiver marcado o parâmetro "Cadastro automático de chapas sequenciais ".

Marcando este parâmetro em uma coligada, ele ficará desabilitado para as demais coligadas.

### 2 - Processos e Rotinas que serão evoluídas para receber a chapa sequencial global

**2.1 - Admissão**

Ao admitir um funcionário com  o parâmetro marcado o sistema irá utilizar a sequência de chapa global, ou seja, admitindo funcionário em qualquer coligada que utilizar "Cadastro Automático de Chapa Sequencial" a sequência será única para todas.

**2.2 – Transferência de funcionário (Rescisão Individual)**

O parâmetro "Utiliza Sequencia Global de Chapa" está pronto para ser utilizado nos processos abaixo:

- Transferência individual tipo 5 mesma coligada

- Transferência individual tipo 5 outra coligada

- Transferência individual tipo 6 mesma coligada

- Transferência individual tipo 6 outra coligada

O parâmetro "Incrementar 4 dígitos de controle no final da chapa dos demitidos", agora também funciona em transferências para outras coligadas, se utilizar o Sequenciamento Global. Maiores informações sobre a funcionalidade deste parâmetro, veja no link do TDN abaixo:

<http://tdn.totvs.com/display/LRM/DT_Transferencia_funcionario>

Ao transferir um funcionário para mesma ou outra coligada,  utilizando o recurso destacado acima, a chapa do registro “transferência saída“  (registro que ficará demitido) receberá  um incremento de 4 posições no fim da chapa.

Exemplo :

Máscara da chapa ##########

Tamanho 10

- Coligada 1 -  chapa 0000007500 - Ativo

- Transferência para Coligada 2

- A chapa na coligada 1  receberá o número  007500T001 – Demitido – Saída Transferência

- A chapa na coligada 2  receberá o número  0000007500 – Ativo – Entrada  Transferência

- Transferência para Coligada 1

- A chapa na coligada 2  receberá o número  007500T002 – Demitido – Saída Transferência

- A chapa na coligada 1  receberá o número  0000007500 – Ativo – Entrada Transferência

**2.3 – Transferência Coletiva (processo Rescisão Coletiva)**

Pronto para ser utilizado o parâmetro "Utiliza Sequencia Global de Chapa" nos processos referenciado no tópico 2.2

**2.5 -Importação**

Este parâmetro não terá efeito na importação. Hoje a importação considera a chapa informada no arquivo de importação.

**2.6 -Troca chapa**

Este parâmetro não terá efeito no processo de troca chapa. Quando se utiliza chapa sequencial o processo de troca chapa não fica disponível.
