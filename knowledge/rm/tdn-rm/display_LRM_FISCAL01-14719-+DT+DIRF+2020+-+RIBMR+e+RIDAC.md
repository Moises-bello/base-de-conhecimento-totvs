---
content_hash: 5c58a9b37e823b97e6d6531f1f7d2d618704ff59a6446770f729859ed1677455
fetched_at: '2026-06-29T00:10:56.713416+00:00'
page_id: '592750970'
product: rm
source: tdn-rm
title: FISCAL01-14719- DT DIRF 2020 - RIBMR e RIDAC
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-14719-+DT+DIRF+2020+-+RIBMR+e+RIDAC
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | DIRF |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14719 |

## **02. SITUAÇÃO/REQUISITO**

Passar a contemplar os registros RIDAC ( Rendimentos Isentos – Diária e Ajuda de Custo ) e RIBMR (Rendimentos Isentos – Bolsa de Estudo Recebida por Médico-residente ) na geração da DIRF

## **03. SOLUÇÃO**

Foram criados os registros RIDAC e RIBMR para o gerador de saídas da DIRF.

Para gerar os registros basta acessar o módulo Financeiro e selecionar o(s) Lançamento(s) Financeiro(s) que gerem DIRF e possui(em) Isenção. Neste(s) Lançamento(s), selecionar a opção Anexos | Dados Fiscais e escolher o Motivo de Isenção desejada. Ao gerar a DIRF com layout atualizado, o RM irá informar o valor da isenção no registro correto e no mês referente.
