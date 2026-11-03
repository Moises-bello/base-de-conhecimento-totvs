---
content_hash: a4dfbe0484af6bcb2e3b795c0a8ddabb62f5245c09b915875a453a59e7b999cc
fetched_at: '2026-06-29T00:10:23.229351+00:00'
page_id: '500286424'
product: rm
source: tdn-rm
title: Parâmetro "Resc.Compl.recalcula fórmulas quando aumento salarial for posterior
  a demissão, durante a projeção do aviso".
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=500286424
version: 12
---

Como padrão, na Rescisão Complementar não são recalculados os eventos que contenham fórmula, se o aumento salarial ocorrer em data posterior à demissão, ou seja, durante o período da projeção do Aviso Prévio Indenizado.   
Este parâmetro foi criado para forçar o cálculo da diferença desses eventos com fórmula existentes na rescisão original, nessa situação de aumento salarial.

**Atenção:**

Eventos com fórmula que contenham os códigos de cálculos (1-Horas Normais,2-Dias Trabalhados,145-Atestado Médico (Previdência),8-Faltas,12-Contribuição Sindical,352-Salário Maternidade Complementar e 353-Salário Paternidade) não serão recalculados no caso de aumento salarial posterior à demissão, mesmo que o parâmetro esteja marcado.

**Exemplo :**

Calculada rescisão para o colaborador com projeção de Aviso prévio indenizado.

Demissão : 30/04/2019 .

Data de Início do Aviso Prévio indenizado : 01/05/2019 (30 dias)

* Na Rescisão foi lançado no envelope o evento 1111-Produtividade calculado por fórmula.

       Na competência Maio/2019 teve aumento salarial na data  01/05/2019.

       Com o parâmetro marcado, o sistema realizará o cálculo para os eventos com fórmula , caso contrário , serão desconsiderados.
