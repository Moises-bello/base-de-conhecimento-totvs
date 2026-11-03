---
content_hash: e2bb0c73bd28c7ec9b3165525f46e7186edfdf25b3b4db77105d6fee129489d7
fetched_at: '2026-06-29T00:10:52.465747+00:00'
page_id: '572749691'
product: rm
source: tdn-rm
title: 9495209 FISCAL01-14090 DT Erro cálculo NF - Regra ICMS Natureza
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572749691
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Gestão Fiscal - Calculo ICMS-ST Próprio |
| Ticket: | 9495209 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14090 |

## **02. SITUAÇÃO/REQUISITO**

O cliente informou que o Cálculo do ICMS ST de Produtos de Cesta Básica é diferente.

O sujeito à substituição tributária na operação interestadual e beneficiados com a base de cálculo reduzida, nas operações internas, de forma que a carga tributária resulte no percentual de 7%, conforme  artigo 3º, inciso XXIII do Anexo I do RICMS/SP, o remetente deverá reduzir a base de cálculo da substituição tributária, de forma que a carga tributária corresponda ao percentual de 7%, deduzindo  o valor do ICMS da operação própria de 7%, embora para o destaque do ICMS da operação própria do   
remetente na Nota Fiscal deverá ser considerada a alíquota de 12%.

## **03. SOLUÇÃO**

Ajuste no Cálculo do ICMSST Próprio quando Parâmetro "ICMSST considera redução no cálculo do ICMS Próprio" estiver marcado.

Foi criado um novo campo no cadastro da Regra de ICMS - "Alíquota Redução ICMS Próprio", o intuito do campo é informar a Alíquota a ser utilizada no Cálculo do ICMSST - Próprio.

Obs.: Este campo estará disponível a partir da versão 12.1.27 após a atualização da Base com o Script LI.2020.11\_02.
