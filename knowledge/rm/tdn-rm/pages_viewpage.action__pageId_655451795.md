---
content_hash: b82f77d6c1739fa6da116d253f5ee569552d8507b14f551e88ad2778704705a9
fetched_at: '2026-06-29T00:11:12.594117+00:00'
page_id: '655451795'
product: rm
source: tdn-rm
title: Hierarquia (Cadastro)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=655451795
version: 12
---

**Disponível a partir da versão 12.1.34**

Representa a **Hierarquia** a qual o funcionário está alocado/faz parte.

**Detalhamento de Campos**

**Hierarquia:**Campo gerado automaticamente pelo produto de forma sequencial.

**Estrutura:**Campo gerado automaticamente pelo produto. A estrutura apresentada é construída  baseada no nível da hierarquia + hierarquia superior (ou superiores) + valor sequencial

**Descrição:**Campo texto de preenchimento obrigatório. Aqui pode ser informado o título ou descrição da Hierarquia por exemplo.

**Status:**Define se a Hierarquia está ativa ou inativa.

**Nível de Hierarquia:** Neste campo deverá ser informado o . Serão exibidos níveis previamente cadastrados e que estão ativos.

**Hierarquia Superior: Neste campo são apresentadas para seleção as Hierarquia que estão ativas.**

**Observação:**As hierarquias associadas ao nível múltiplo não serão apresentadas por serem o último nível na estrutura organizacional.

**Cód.Calendário:** Deverá ser selecionado o calendário a ser utilizado. Este campo deverá ser preenchido ou não de acordo com a definição realizada através dos .

**Id. Externo:**Campo texto de preenchimento opcional. Direcionado para clientes que possuem um outro sistema de controle hierarquia e necessitada de uma forma de ligar os códigos do sistema externo com a Hierarquia do Gestão de Pessoas.

**Anexos da Hierarquia**

**Histórico da Hierarquia:**Através deste cadastro é possível visualizar todas as alterações sofridas na Hierarquia. As regras são as mesmas do cadastro da hierarquia, incluindo o campo Data da Mudança, onde é exibido a data e hora em que houve a alteração do dado.

**Definir Substituto:** Através deste anexo você poderá definir um substituto para a Hierarquia editada, definindo um período de duração para a substituição.

Esta definição poderá ser feita das seguintes formas:

**Hierarquia Substituta:**Selecionando este campo, será definido que o substituto da Hierarquia manipulada será uma outra Hierarquia. Serão apresentadas para seleção somente Hierarquias que possuam funcionário associados (posição).

**Substituto Externo:** Selecionando este campo, será definido que o substituto da Hierarquia manipulada será um . Serão exibidos apenas externos que possuam o código de usuário informado em seu cadastro.

**Coligada/Funcionário:**Selecionando este campo, será definido que o substituto da Hierarquia manipulada será um funcionário. Poderá ser da coligada de origem do cadastro ou outra coligada.

**Pessoa/Coligada Externa:**Através deste cadastro poderá ser definido que o responsável pela hierarquia será um Externo ou um funcionário de outra coligada.

**Observação:** A definição da pessoa que ocupa a hierarquia (coligada atual) é feita diretamente no cadastro de **Posição**.

Repasses de Aprovações

Caso uma hierarquia esteja vazia ou sem um substituto definido, repasses de aprovação serão automaticamente **encaminhados** ao próximo aprovador no fluxo.

**Links Importantes e Complementares:**
