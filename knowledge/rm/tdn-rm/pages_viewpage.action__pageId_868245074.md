---
content_hash: 367db2f2e0b7536386a5ec74f097abcffc8c1038c95d100c99eae12d6f41d035
fetched_at: '2026-06-29T00:11:56.700313+00:00'
page_id: '868245074'
product: rm
source: tdn-rm
title: Regras geração nota 76/86 IPERGS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=868245074
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Regras da geração da nota 76**
3. **Exemplo Utilização nota 76**
4. **Regras da geração da nota 86**
5. **Exemplo Utilização nota 86**

itensVisão Geral

Conforme [publicação do IPERGS](https://admin.ipesaude.rs.gov.br/upload/arquivos/202211/28093358-instrucao-normativa-10-2022-dispoe-sobre-a-apresentacao-das-contas-hospitalares-e-revoga-a-os-05-2008.pdf), dispõe sobre a apresentação das contas hospitalares e ambulatoriais. Essa mudança foi expedida nos patchs de 27/09/2024 do RM Saúde.

## **01. VISÃO GERAL**

Regras para geração da taxa nota 76/86.

Regras da geração da nota 76

## **02. Regras da geração da nota 76**

A nota de débito TR 76 - Despesas Hospitalares, sendo que as referências devem ser apresentadas na seguinte ordem:

* Diárias;
* Taxas;
* Materiais e medicações;
* Órtese, próteses e Materiais Especiais.

**Art 2º - § 2º - II** – Especificamente para a taxa (60028327 - TAXA DE ARMAZENAMENTO, DISTRIBUIÇÃO, MANIPULAÇÃO, FRACIONAMENTO, UNITARIZAÇÃO DE MEDICAMENTO/DIA), a ordem do seu lançamento deve vir após o lançamento dos itens previstos na alínea “e” (materiais e medicações).

Essa taxa deve ter lançamento único, na data da alta, e deve ter os seus campos preenchidos da seguinte forma: “Ocorrências dias” = 01 e “Nº de dias” = ao número de dias em que se fez uso de medicamentos durante a internação. .

Exemplo:

|  |  |
| --- | --- |
| Data de lançamento | Lançamento |
| 23/09 | TAXA DE ARMAZENAMENTO |
| 24/09 | TAXA DE ARMAZENAMENTO |
| 25/09 | TAXA DE ARMAZENAMENTO |
| 26/09 |  |
| 27/09 | TAXA DE ARMAZENAMENTO |
| 28/09 | TAXA DE ARMAZENAMENTO |
| 29/09 | TAXA DE ARMAZENAMENTO |

## Data de saída/alta: Dia 30/09

Será lançado da seguinte forma, sempre somando todos os lançamento que tenham a mesma quantidade, e data será sempre a data da alta:

Ocorrências dias” = 01 e “Nº de dias 6(quantidade de lançamentos)   Data: 30 /09 ( data da alta)

Exemplo de utilização nota 76

## **03. Exemplo de utilização nota 76**

**Menu=> Cadastro Condições Contratuais=> selecionar  o convênio IPERGS**

Em eletrônico I-  preencher o código da taxa nota 76

**Menu=>Elaboração de contas na aba taxa, lançar a taxa cadastrada:**

Mesmo não sendo dias consecutivos o lançamento será único, considera que a quantidade será igual:

**Arquivo gerado:**

Regras da geração da nota 86

## **04.****Regras da geração da nota 86**

A nota de débito, é TR 86 - Despesas Ambulatoriais, sendo que as referências individuais devem ser apresentadas na nota de débito observando a seguinte ordem:

* Serviços;
* Materiais e Medicação;
* Órteses, Próteses e Materiais Especiais;
* Laudo dos exames, inclusive anatomopatológicos e exames de imagem.

**Art 2º - § 3º - II** – Especificamente para as taxas (60015381 – TAXA APLICAÇÃO QUIMIO/IMUNO SC/IM e 60000481 - TAXA COMPACTA DE SALA DE SESSÃO DE QUIMIO/IMUNO AMBULATORIAL EV), a ordem do seu lançamento deve vir após o lançamento dos itens previstos na alínea “b” (materiais e medicação).

Para o lançamento de cada uma dessas taxas deve-se respeitar o intervalo mínimo de 07 dias. A taxa deve ser informada para cada dia em que houver aplicação do medicamento correspondente, sempre respeitando o intervalo acima descrito. As duas taxas não podem ser cobradas no mesmo dia.

Exemplo de utilização nota 86

## **05. Exemplo de utilização nota 86**

**Menu=> Cadastro Condições Contratuais=> selecionar  o convênio IPERGS**

Em eletrônico I-  preencher o código da taxa nota 86

O sistema não valida o intervalo de lançamentos   e não verifica se os itens foram lanchados no mesmo dia. Ele apenas lança separados não concatenando estes itens.

**Menu=>Elaboração de contas na aba taxa, lançar a taxa cadastrada:**

Mesmo não sendo dias consecutivos o lançamento será único, considera que a quantidade será igual:

**Arquivo gerado:**
