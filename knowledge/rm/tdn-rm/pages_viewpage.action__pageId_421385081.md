---
content_hash: ef4f9c8061bd0d7b263672dd6fd8d9586ce1d3e07a85cb5166abf4a8ac15786a
fetched_at: '2026-06-29T00:09:13.656434+00:00'
page_id: '421385081'
product: rm
source: tdn-rm
title: Associação de Coletores a Usuários 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385081
version: 6
---

Na visão de cadastro de usuários de coletores, o usuário poderá fazer o vínculo e visualizar quais coletores estão associados ao usuário. Para vincular um coletor, o usuário deve selecioná-lo na lista de coletores disponíveis e clicar no botão "Vincular". Os coletores vinculados serão exibidos em uma lista separada, permitindo ao usuário visualizar rapidamente quais dispositivos ele tem acesso.

**Funcionalidades:**

* **Vínculo individual:** Por padrão, cada usuário ativo de coletor móvel pode estar associado a apenas um coletor.
* **Vínculo múltiplo:** A opção de vincular vários coletores a um único usuário está disponível, mas requer a ativação do parâmetro "Utiliza mais de um coletor móvel por usuário" em **Opções | Parâmetros | TOTVS Obras e Projetos | Gerais | aba Mobilidade**.
* **Coletores ativos:** Apenas coletores ativos podem ser vinculados a usuários.

O sistema monitora as vinculações de coletores para garantir que nenhum usuário exceda o limite permitido. Caso o parâmetro "**Utiliza mais de um coletor móvel por usuário**" não esteja habilitado, a vinculação de mais de um coletor a um único usuário será bloqueada.

**Atenção:**  
Somente os coletores ativos poderão ser vinculados ao usuário. Serão exibidos apenas coletores ativos, não sendo possível associação de coletores desativados.

**Etapas:**

1. Acesse o **Menu Controle > Minha Obra > Usuários de Coletores Móveis > Anexos > Associação de Coletor a Usuário(s).**

   Selecione o usuário ao qual deseja vincular um coletor.

   Na seção "**Associação de Coletor a Usuário(s)**", clique em "**+**" para adicionar e localize os coletores que deseja vincular.

   Clique em "**OK**" para confirmar.

* Coletores Associados a Folha Tarefa

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folhas Tarefa \ Anexos \ Coletores Associados a Folha Tarefa;
* Neste anexo o usuário deverá associar os coletores que a folha tarefa poderá ser sincronizada.
* Não será possível incluir novos coletores caso a folha tarefa esteja com status de cancelada ou Encerrada.
* Não será possível excluir coletores que já possuem status de ‘associado ao coletor’.

* Processo de Associar coletor a Folha Tarefa

Permite a associação de coletores à folha tarefa selecionada:

* Para sua execução é necessário que o status da folha seja "Em Processamento", "Gerada" ou "Associada ao Coletor";
* São exibidos apenas os coletores que tem o projeto corrente associado;
* São exibidos apenas os coletores que tem usuários associados;
