---
content_hash: b09e65eeb98018731c1b2d955878affb8d0d44153b4654d28a2c7ba50d213e3c
fetched_at: '2026-06-29T00:11:28.639274+00:00'
page_id: '732687383'
product: rm
source: tdn-rm
title: DT - eSocial - Eventos S-2200 e S-2206 - Geração da tag <treiCap>
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=732687383
version: 13
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Geração da tag <treiCap> nos eventos S-2200 e S-2206 |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHROTRM-3936 |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.34.236
* 12.1.2205.183
* 12.1.2209.125
* e Superiores.

## **03. SITUAÇÃO/REQUISITO**

Tratar a geração da tag <treiCap> nos eventos abaixo, para ser enviado somente uma vez o treinamento, quando a avaliação for finalizada.

* S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador
* S-2206 - Alteração de Contrato de Trabalho/ Relação Estatutária

## **04. SOLUÇÃO**

Implementado a tratativa na geração da tag <treiCap> nos eventos S-2200 e S-2206, passando a considerar somente os treinamentos executados conforme regra:

* S-2200: serão considerados os treinamentos até a data de admissão ou data transferência, verificando o campo "DTFECHAMENTO" preenchido na tabela VTUAVCONH, esse campo encontra-se no menu RH | Gestão de Pessoas | Desenvolvimento | Turmas | Anexos | Avaliação de conhecimento campo "Data de Encerramento"
* S-2206: serão considerados os treinamentos com data de fechamento (campo  VTUAVCONH.DTFECHAMENTO) igual a data de alteração do evento, esse campo encontra-se no menu RH | Gestão de Pessoas | Desenvolvimento | Turmas | Anexos | Avaliação de conhecimento campo "Data de Encerramento". Caso seja inserido o evento manual na fila será considerado a data do evento.

## **05. DEMAIS INFORMAÇÕES**

* [S-2206 – Alteração de Contrato de Trabalho](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719585)
* [S-2200 – Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719244)
