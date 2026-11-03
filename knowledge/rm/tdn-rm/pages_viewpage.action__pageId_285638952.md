---
content_hash: fef5e3023416752c819e645cd4a72c8906392d7d274bf44ddeada9e5b0b349db
fetched_at: '2026-06-29T00:08:38.184249+00:00'
page_id: '285638952'
product: rm
source: tdn-rm
title: Visibilidade / Obrigatoriedade de campos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285638952
version: 10
---

Nesta guia é possível configurar os campos de usuário nos serviços de candidato. Através destes parâmetros será possível determinar se um campo será visível e/ou obrigatório no formulário de inscrição e também no formulário de matrícula.

A partir da versão 12.1.2406

As opções de visibilidade e obrigatoriedade de campos para a matrícula do candidato foram adicionadas no TOTVS Processo Seletivo a partir da versão **12.1.2406:**

* Visível candidato matrícula
* Obrigatório candidato matrícula
* Visível responsável matrícula
* Obrigatório responsável matrícula

Estas opções podem ser selecionadas independentemente das opções de visibilidade e obrigatoriedade das inscrições, já existentes nas versões anteriores.

Dependendo da configuração do sistema ou das opções selecionadas no processo seletivo, pode não ser possível desmarcar a visibilidade ou a obrigatoriedade do campo. Para facilitar, quando isso acontecer, será exibida uma caixa de texto informando o motivo pelo qual a opção não pode ser desmarcada.

A partir da versão 12.1.2506

Quando a instituição configurar a **Visibilidade/Obrigatoriedade dos campos** e definir o campo **CPF** como **obrigatório** para o candidato, o sistema passará a aplicar a seguinte regra de validação no ato da inscrição:

1. **Verificação de Inscrição Existente:** O sistema irá validar, em todo o processo seletivo (independente do número maximo de inscrições por candidato permitido), se já existe uma inscrição vinculada ao CPF informado.
2. **Impedimento de Duplicidade:** Caso o CPF já tenha sido utilizado por outro usuário dentro do mesmo processo seletivo, o candidato **não poderá concluir a inscrição**.
3. **Critério de Acionamento:** Esta validação de bloqueio é disparada **exclusivamente** quando o campo CPF está marcado como **obrigatório para o candidato** nos parâmetros de visibilidade do formulário.
