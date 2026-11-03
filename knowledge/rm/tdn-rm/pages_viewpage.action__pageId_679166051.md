---
content_hash: 6e6d7795e8bc5aed40d8415e06a503202662b29d49c71ee19fd2d1f7953b9059
fetched_at: '2026-06-29T00:11:17.352148+00:00'
page_id: '679166051'
product: rm
source: tdn-rm
title: Anexo - Cobrança fixa por Subunidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=679166051
version: 7
---

### Associação de Cobrança Fixa por Subunidade

---

Este anexo possibilita cadastrar Cobranças do tipo Valor Fixo para as Subunidades do Empreendimento/Bloco referente à Associação de Cobrança por Orçamento.

### Controle de Acesso e Permissões

---

Com as mudanças no comportamento do sistema, foram alteradas as permissões de acesso. Verifique com seu administrador se o seu perfil possui as seguintes permissões Em *Condomínios / Básicos / Cobrança por Orçamento*

| **Permissão** | **Descrição** |
| --- | --- |
| **Histórico de Valor: Processo de Atualização de Valor** | Permite iniciar o processo de atualização de valores da subunidade. |
| **Histórico de Valor: Excluir** | Permite apagar o último registro do histórico (conforme as regras acima). |

> **💡 Importante:** A separação dessas permissões garante que um usuário possa ter o direito de atualizar um valor, mas não necessariamente o de apagar um histórico já consolidado.

### Procedimento para utilização

---

Ao incluir é exibida uma tela com os seguintes campos:

* **Número da Subunidade:** Campo para seleção da subunidade desejada, dentro do filtro serão exibidas somente as subunidades do Empreendimento/Bloco respectivo.
* **Valor:** Valor definido para a cobrança de Valor Fixo.

### Alteração de valor fixo

---

Este processo permite ao usuário alterar um valor fixo previamente cadastrado, possibilitando uma flexibilidade no controle de cobranças quando uma ou várias subunidades necessitam de um reajuste ou um desconto em suas cobranças.

Para executar o processo, basta selecionar o registro da subunidade e ir em *Processos / Alterar Valor Fixo.*

Deverá ser inserida uma **nova data** para o novo valor fixo. Essa data deve ser **superior** a última data cadastrada.

O novo valor fixo pode ser menor ou maior que o valor fixo anterior. Como referência, na tela do processo o usuário poderá visualizar o último valor fixo cadastrado como base.

Após preencher a nova data e o novo valor, basta clicar em executar. Quaisquer fechamentos que sejam realizados em data igual ou superiores a data cadastrada do novo valor irão valer-se deste para seus devidos cálculos.

**Importante:**

* Os fechamentos em datas inferiores irão utilizar os valores antigos, de acordo com seus períodos baseados no histórico de alteração de valores.
* O processo de alteração de valor fixo não pode ser realizado em lote, devendo ser gerado para cada subunidade cadastrada na cobrança fixa.

#### Alteração de Valor Zero

O processo de atualização de valores foi flexibilizado para atender cenários de correção ou zeramento de taxas:

* **Permissão de Valor Zerado:** Agora é permitido informar o **valor 0,00 (zero)** durante o processo de alteração de valor.
* **Histórico Consolidado:** Mesmo valores zerados geram um registro no histórico, permitindo o rastreio de quando a subunidade deixou de ter um valor atribuído.

### Exclusão de Histórico de Valores de Subunidades

---

Esta atualização introduz melhorias no controle de alterações de valores e regras estritas para a exclusão de históricos, garantindo que não haja inconsistências na linha do tempo financeira da subunidade.

#### Regras de Exclusão de Histórico

Para manter a integridade dos intervalos de datas e valores, a exclusão de registros de histórico agora segue critérios específicos:

* **Regra do Último Registro:** Só é permitida a exclusão do **último registro** de histórico gerado.

  + *Exemplo:* Se uma subunidade possui 10 registros de histórico, você não pode excluir o registro de número 6. É necessário excluir do 10º em diante, em ordem decrescente.
* **Sincronização Automática:** Ao excluir o último registro do histórico, o sistema atualiza automaticamente a associação da subunidade com o valor presente no registro imediatamente anterior (o novo "último").
* **Mensagem de Validação:** Caso tente excluir um registro que não seja o mais recente, o sistema exibirá:

  > "Não é possível excluir o(s) registro(s) selecionado(s), pois existem registros com histórico superior ao(s) selecionado(s) para exclusão."
