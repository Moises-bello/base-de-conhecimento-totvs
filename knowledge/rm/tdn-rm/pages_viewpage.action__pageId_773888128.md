---
content_hash: 339fb169f0cc6c6f973fc6be39711c01ff3bb562dee08b71b45343f88a7891bc
fetched_at: '2026-06-29T00:11:36.940949+00:00'
page_id: '773888128'
product: rm
source: tdn-rm
title: S-2299 - Como retificar a data de demissão quando há um processo judicial retroagindo
  a data de demissão?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773888128
version: 11
---

false

**A partir das Versões:**

* 12.1.2209.243
* 12.1.2302.167
* 12.1.2306.111

# Objetivo:

---

Este documento tem como objetivo fornecer informações de como realizar o processo de retificação de desligamento judicial.

---

Foram realizadas as seguintes atualizações no produto, a partir dos patches mencionados acima:

* Um novo parâmetro chamado "Indicativo Remuneração Após o Desligamento" foi adicionado no cadastro de rescisão, na aba "Rescisão".
* O campo "Data Fim Quarentena" será desabilitado quando o campo "Indicativo Remuneração Após o Desligamento" estiver preenchido com o valor 2.
* Um novo campo chamado "Data Desligamento Judicial" foi adicionado.
* Este campo deve ser preenchido com uma data de desligamento determinada pelo juiz.

Após preencher a "Data Desligamento Judicial", será gerado um gatilho na fila de eventos com o status de "Retificação" contendo as seguintes informações:

* `<dtDeslig>`: data informada no novo campo "Data Desligamento Judicial";
* `<indRemun>`: indicativo de situação de remuneração após o desligamento igual a 2;
* `<dtFimRemun>`: data informada no campo "Data de Desligamento" da rescisão.

Exemplo de preenchimento dos campos:

ATENÇÃO:

Para realizar a tratativa mencionada acima, é imprescindível executar o script por meio da versão correta do sistema RM.Atualizador.exe.
