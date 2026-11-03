---
content_hash: f15294184b77c02da7f97cabb9a845a976e54aef59dbfd7d9a9ba880cc34ce9c
fetched_at: '2026-06-29T00:08:40.946593+00:00'
page_id: '286518328'
product: rm
source: tdn-rm
title: DT Parâmetro Incluir Competência Atual na Atualização do Saldo de FGTS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286518328
version: 105
---

# ATUALIZAÇÃO DO SALDO DE FGTS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Atualização do Saldo FGTS* | *Atualização do Saldo FGTS* | |  |  | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FOPROTINAS01-836 |
| **País(es):** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |

# Interpretação da demanda

Criação de um novo parâmetro para incluir a competência atual no processo de Atualização do Saldo de FGTS.

# Analise da demanda

### Criação do Parâmetro

Foi criado um novo parâmetro na Wizard do processo Atualização do Saldo FGTS, que pode ser acessado em 'RH' -> 'Folha de Pagamento' ->aba  'Administração de Pessoal' -> grupo 'Alterações Globais' -> menu 'Alterações Cadastrais' -> botão 'Atualização do Saldo FGTS'. O parâmetro criado é um checkbox que deve ser marcado (por padrão ele fica desmarcado para manter o comportamento atual do sistema) para que a competência atual seja incluída na atualização, conforme mostrado na imagem a seguir:

Repare que quando o parâmetro é marcado, a mensagem de aviso é alterada também de modo a refletir o comportamento esperado:

**Importante:** O comportamento antigo, onde o FGTS era atualizado apenas até a competência anterior, foi projetado para evitar inconsistências nos valores de FGTS devido à ausência de alguma informação que deveria ter sido cadastrada. Ao marcar este parâmetro para executar o processo deve-se ter certeza que todas as informações necessárias ao cálculo do FGTS já foram preenchidas, pois o saldo de FGTS de cada funcionário pode ser atualizado apenas uma vez por competência.

divs
