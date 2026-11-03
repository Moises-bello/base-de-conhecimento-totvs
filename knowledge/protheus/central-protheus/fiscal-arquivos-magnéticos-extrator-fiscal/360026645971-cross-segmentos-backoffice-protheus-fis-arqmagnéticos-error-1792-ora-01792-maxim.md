---
article_id: 360026645971
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: f23f72dec7c24e869e103ed4a57bdce613b325e40fbce99fb3dc2d6b4acae56d
fetched_at: '2026-06-28T22:42:07.737696+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Error : 1792
  - ORA-01792: Maximum Number of Columns in a Table or View is 1000'
type: support-article
updated_at: '2022-08-18T17:24:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026645971-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Error-1792-ORA-01792-Maximum-Number-of-Columns-in-a-Table-or-View-is-1000
---

**Ocorrência**

Ao tentar executar a geração de algum arquivo magnético ou algum processamento que possibilite a criação de uma consulta (View) com combinação de colunas de uma (auto-junção) ou mais tabelas (Join) é apresentado error.log mencionando o trecho abaixo:

**Error : 1792 - ORA-01792: maximum number of columns in a table or view is 1000**.

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 12.1.17

**Causa**O erro ORA-01792 é especifico da versão utilizada no banco de dados Oracle e é um Bug do Oracle 12, onde uma das situações é que: **SELECT e JOINs** executando (recursiva de **rm\_story**, por exemplo), mesmo quando o número de colunas na tarefa não excedesse 1000 nem o número de colunas definido para saída.

Este erro pode ocorrer no Oracle database nas versões 10.2.0.4 até a 12.1.0.2.

Uma das recomendações da Oracle é a não utilização de tabelas com mais de 1000 colunas.

Uma observação importante é que se estivermos criando uma view e fazendo join entre tabelas, a quantidade de colunas a ser contabilizada é a da view e não necessariamente da tabela original.

**Solução**Para correção (Recomendado pelo próprio Fabricante) deve ser aplicado o *PATH* 19509982.

Este patch está incluso na atualização de produto Oracle 12c (database) a partir de Abril/2016 (19-04-16). 

Em alguns casos mesmo com o Path aplicado a mensagem continuou aparecendo, por isso é recomendo que seja avaliado por um DBA.

Outro ponto que pode executar é a alteração do parâmetro "**\_fix\_control**".

**SQL> alter system set "\_fix\_control"='17376322:OFF'**;

**Referencia:**

Bug Fix path correção 19509982 <https://support.oracle.com/epmos/faces/DocumentDisplay?id=19509982.8>

Declaração erro ORA-01792 <https://support.oracle.com/epmos/faces/DocumentDisplay?id=1951689.1>

<https://community.oracle.com/thread/3691573?start=0&tstart=0>
