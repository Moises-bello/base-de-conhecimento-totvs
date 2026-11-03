---
content_hash: 5ba1d5e00712f37843d671b41ec184f493af77a979d52ceccfeaa2be14e5bfe2
fetched_at: '2026-06-29T00:09:34.792606+00:00'
page_id: '425459248'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Cadastro de Ativos (Patrimônio)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459248
version: 3
---

**Linha** **RM x Protheus SigaMNT - Cadastro de Ativos (Patrimônio)**

---

A inclusão, alteração e deleção dos cadastros de Ativo são feitos no RM e replicados no Protheus.

1.   A inclusão é feita no RM acessando: BackOffice > Gestão patrimonial.

2.   Pra visualização dos ativos cadastrados no Protheus, acesse: SIGAMNT > Atualizações > Cadastros básicos > Ativos

* Dados sincronizados:
* Código da empresa
* Código da filial
* InternalId da empresa
* Código
* Código de propriedade
* Data de aquisição
* Descrição
* Quantidade
* Código do ativo
* Status do ativo
* Data de inicio de depreciação

**Observações :**

1.   Serão integrados somente ativos do tipo "Patrimônio". Assim sendo, qualquer ativo dos tipos "Título" ou "Terceiros" será desconsiderado e não disparará o gatilho de integração.

2.   A alteração e a exclusão de ativos são executadas via processo, assim sendo, caso haja algum erro na integração a operação executada **não será desfeita**, sendo necessário seguir o seguinte processo:

* Analisar a mensagem de erro obtida
* Corrigir a origem do problema
* Reencaminhar a mensagem de integração
* Caso o erro não seja sanado deve-se fazer os ajustes de forma manual

3.   Para integrar esta entidade, o PROTHEUS exige que sejam cadastrados valores defaults para Plano de Contas em sua base (para cada filial), com os seguintes parâmetros:

* Código: 001
* Descrição: "Default Integração"
* Classe de conta: Analítica
* Condição normal: Credora

4.   No processo de Transferência de Controle (filial e centro de custo) é necessário cadastrar no PROTHEUS cotação de moeda para a moeda utilizada na data de transferência. Caso não exista cotação de moeda na data de transferência, podem ser apresentadas as seguintes mensagens de erro: "HELP: AF010JABAI" ou "HELP: AF060NOTXA".

5.   O campo "N1\_CHAPA" da tabela de Ativos do PROTHEUS deve ter seu tamanho alterado para 30 caracteres para ficar compatível com o RM.

---

Para mais detalhes sobre o cadastro de Ativos, acesse o boletim técnico:

**Recursos Adicionais**

TDN - Boletim Técnico : [Patrimônio](http://tdn.totvs.com/download/attachments/76251248/CONNECTOR_BT_CADASTRAR+ATIVOS%28PATRIMONIO%29_BR_CON000158.pdf?version=1&modificationDate=1380044708000)
