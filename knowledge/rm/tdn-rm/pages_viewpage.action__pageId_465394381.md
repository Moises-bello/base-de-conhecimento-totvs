---
content_hash: c2f85b9e914848611d1d8da568397bd15469d420f0658f2ab73d5623218ac474
fetched_at: '2026-06-29T00:10:15.967482+00:00'
page_id: '465394381'
product: rm
source: tdn-rm
title: PORTALMOBILE01-6820 DT Integração TOTVS Captação Sustentável
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465394381
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | Processo Seletivo |
| Função: | Inscrição de candidato |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | PORTALMOBILE01-6820 |

## **02. SITUAÇÃO/REQUISITO**

Os dados de um possível candidato do TOTVS Processo Seletivo não era persistido durante o processo de inscrição online, além disso não existia um canal de captação e relacionamento com os possível candidatos.

## **03. SOLUÇÃO**

A cada avanço de etapa do Processo Seletivo os dados do interessado são atualizados no TOTVS Captação Sustentável. Assim que o interessado finaliza a inscrição com sucesso é atualizado no cadastro do TOTVS Captação Sustentável o novo código de usuário do Processo Seletivo.

O pré-requisito desta integração é a visibilidade do campo e-mail. Este campo será a chave temporária do interessado.

São 6 eventos passíveis de atualização:

1. Primeiro formulário de inscrição (mini-formulário);
2. Primeira etapa do formulário principal de inscrição;
3. Segunda etapa do formulário principal de inscrição;
4. Terceira etapa do formulário principal de inscrição ( finalização da inscrição );
5. Nova inscrição;
6. Tentativa de inscrição em um novo processo seletivo.

Assim que realizado a seleção da atividade ofertada será atualizado o TOTVS Captação Sustentável.

Parametrização, Simulaçãopasso1,passo2yespasso1

Durante a implantação do TOTVS Captação Sustentável, favor realizar a parametrização da Integração.

Os dados de acesso são gerados exclusivamente no TOTVS Captação Sustentável.

Os campos de Tipos de Eventos representam os códigos chave do cadastro de Tipo de Evento do TOTVS Captação Sustentável.

A parametrização é realizada por Processo Seletivo.

nopasso2

Simulação do envio dos dados ao TOTVS Captação Sustentável ao avançar a primeira etapa do formulário principal do TOTVS Processo Seletivo.
