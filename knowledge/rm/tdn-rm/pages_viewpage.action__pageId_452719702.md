---
content_hash: 54cbbd3cb4224d4540ae6d968be389da4e21577bfb5e3fed7c911f5696472a42
fetched_at: '2026-06-29T00:10:09.531660+00:00'
page_id: '452719702'
product: rm
source: tdn-rm
title: Definir Gestão Ativa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719702
version: 2
---

**Definir Gestão Ativa**

Este processo tem como objetivo ativar uma gestão de hierarquia.

**Observações:**

* Para gestões de hierarquia que utilizem a Proposta de Reestruturação de Seção, este processo não pode ser executado, sendo necessário "Executar Proposta" no Totvs Folha de Pagamento.
* O processo só pode ser acionado se uma única gestão estiver selecionada na visão de gestões, e apenas a partir de uma gestão que não esteja ativa.
* A execução do processo desativa a gestão vigente, se houver, e em seguida ativa a nova gestão.
* O campo "Motivo" é de preenchimento obrigatório.
* Ao executar o processo o sistema valida a gestão selecionada exibindo uma lista das possíveis inconsistências (alertas).

Se houver alertas impeditivos a gestão não pode ser ativada, até que os alertas impeditivos sejam acertados. São eles:

* Participante de um time está também alocado em posições;
* Time alocado em mais de uma posição;
* Líder direto em mais de uma posição;
* Participante alocado em mais de um time.

Se a parametrização vigente no sistema não for de Gestão por Posições, a Gestão que está prestes a ser ativada só será considerada pelas demais funcionalidades do sistema a partir do momento que a parametrização for realizada.

A parametrização está disponível no caminho: Configurações| Parametrizador| Preferências| Tipo de Gestão Hierárquica.

Ao final do processo, é gravado um histórico da operação, no anexo "Histórico de Ativação/Desativação" gerando um registro para a gestão desativada (se houver) e um registro para a gestão ativada.
