---
content_hash: c6268136a12e8d51e53097e9c9479dba3bbc66d140fb06a74a62acc6307321b3
fetched_at: '2026-06-29T00:08:54.764706+00:00'
page_id: '346491403'
product: rm
source: tdn-rm
title: S-2230 - Porque a Quantidade de dias(Obrigatório) é gerada com valor zerado?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=346491403
version: 4
---

|  |  |
| --- | --- |
| **Produto:** | TOTVS Folha de Pagamento |
| **Dúvida:** | Na geração do XML o valor da tag qtdDiasAfast é gerada com valor zero: |
| **Resposta:** | Dentro do Layout do eSocial, relacionado ao **evento S-2230**, o layout apresenta o seguinte resumo de registro:    Isto significa que a tag **infoAtestado** (Informações complementares - Atestado Médico) é **obrigatória** se o motivo de afastamento for 01 (Acidente/Doença do Trabalho) ou 03 (Acidente/Doença não relacionado ao trabalho) - vide tabela abaixo.      Dentro da tag agrupadora infoAtestado é exigido a "quantidade de dias de afastamento concedidos pelo médico" através da tag **qtdDiasAfast**.    O número 1-1 significa que deve ser informado no mínimo 1 e no máximo 1 registro.    Desta forma, torna-se obrigatório o preenchimento da quantidade de dias de afastamento. Lembrando que no sistema este campo possui relação com o campo "Data Final Afastamento", assim, quando a quantidade de dias é informada o sistema automaticamente preenche a data final.  Caso o afastamento não possua data final preenchida, o sistema levará o valor 0, pois o campo nesse caso será de preenchimento obrigatório, porém ainda não existe previsão de retorno do afastamento.    *Obs.: Em casos de afastamentos pela previdência, se não houve uma data final preenchida e o usuário desejar enviar a quantidade de dias de afastamento, sugere-se preencher a data final com a data da próxima vistoria médica.* |
