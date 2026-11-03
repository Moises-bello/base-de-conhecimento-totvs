---
article_id: 360027460512
category: UBS - Unidade de Beneficiamento de Sementes
content_hash: 4b9b021d17ee564d19752add700ec7048ffef3ac202f23bf9f5a0dddd1ba61ed
fetched_at: '2026-06-28T22:45:34.806888+00:00'
product: protheus
section_id: 360005696194
source: central-protheus
title: Agro - Linha Protheus - UBS - Importação de resultado laboratorial do UBS
type: support-article
updated_at: '2025-06-20T15:38:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027460512-Agro-Linha-Protheus-UBS-Importa%C3%A7%C3%A3o-de-resultado-laboratorial-do-UBS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22238984548631) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como efetuo a **Importação de Resultado Laboratorial** no módulo de **UBS - Unidade de Beneficiamento de Sementes**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBS - Unidade de Beneficiamento de Sementes - A partir da versão 12  
  
**Solução**Após cadastrar um **Lote de Sementes** é necessário aprovar o **Resultado Laboratorial**, para que o Lote fique disponível para a continuidade dos demais processos.  
  
Existem duas formas mais utilizadas de efetuar a aprovação do**Resultado Laboratorial** do lote.  
  
A **aprovação manual** é efetuada por intermédio da rotina **AGRA960 - Resultado****Laboratorial** e conforme o *layout* utilizado, são lançados os resultados. Após efetuados os lançamentos deve ser efetivada a aprovação, e dessa forma o lote já assumirá o status **disponível**.

![UBS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6932269325719)

A outra forma de aprovação de **Resultado Laboratorial** é efetuada por meio da rotina **AGRA930 - Importação Análises do Lote** e conforme definido no *layout* utilizado, a aprovação é realizada por meio da importação dos resultados, que são registrados em um documento no formato .csv para excel.

![UBS1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6932290263191)

Desta maneira, a partir do momento que for efetuada a importação dos resultados registrados no documento de excel, e a germinação estiver acima de **50,00** - **valor determinado no tipo de análise**, o lote será automaticamente aprovado.

![image2018-8-31_17-27-55.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360027339211)

![UBS2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6932292136983)

**Importante**  
É importante que o documento com os resultados seja salvo no formato .csv e que seja retirada a linha de cabeçalho com o nome das colunas, para que a importação ocorra corretamente sem erros no Sistema.
