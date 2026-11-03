---
content_hash: 1cb259a8b865e90bcdb6689386ac839bbbf49c21bae32d389bf1badefe8ccb02
fetched_at: '2026-06-29T00:11:49.446666+00:00'
page_id: '833934288'
product: rm
source: tdn-rm
title: Portal de Imóveis - Backend - Usuários - Grupos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=833934288
version: 8
---

### Permissões: Prospect / Lead

* **Criar:** Permite ao usuário deste grupo acessar a tela de visualização de prospects e inserir um novo registro. Também possibilita inserir este registro diretamente através da tela de proposta;
* **Alterar:** Habilita o usuário deste grupo a editar um prospect já cadastrado. Esta ação depende da combinação dos demais parâmetros descritos abaixo;
* **Excluir:** Permite ao usuário deste grupo excluir o registro de um prospect, de acordo com a combinação dos demais parâmetros descritos abaixo;
* **Visualizar banco de prospects:** Permite ao usuário visualizar e manipular, conforme a combinação de outros parâmetros, os registros de prospects que estão no "banco de compradores" e "banco de não compradores";
* **Visualizar todos os prospects:** Permite aos usuários deste grupo visualizar todos os prospects, independentemente da hierarquia, conforme combinação dos demais parâmetros abaixo. Geralmente indicada para administradores e gestores da incorporadora;
* **Pode visualizar prospects dos subordinados:** Permite aos usuários deste grupo visualizar os prospects de seus subordinados, com base na sua posição hierárquica. Geralmente indicada para administradores de imobiliárias, chefes dos corretores, entre outros;
* **Editar prospects de outros usuários:** Permite aos usuários deste grupo editar prospects de outros usuários. Para que essa permissão funcione corretamente, é necessário que o usuário também tenha ativada ao menos uma permissão de visualização (todos os prospects ou dos subordinados). Geralmente indicada para gestores da incorporadora e analistas financeiros;
* **Vincular prospect ao corretor (ao criar):** Ao cadastrar um novo prospect, o mesmo será associado ao usuário que está realizando esta ação. Depois, outro usuário com permissão adequada poderá associar este registro a um outro corretor;
* **Vincular prospect ao corretor (ao editar):** Ao editar um prospect, o mesmo será associado ao usuário que está realizando esta ação. Essa opção tem dependência direta com a parametrização do Papel Exercido de Corretor;
* **Acessa apenas a aba de cadastro básico:** Permite acesso apenas ao cadastro de dados básicos dos prospects, aba Dados Básicos. Indicada para controle mais rigoroso em relação às demais informações e ao acesso aos dados dos prospects;
* **Permite editar SDR:** Permite que os usuários deste grupo possam editar o SDR associando-o ou alterando-o, ao cadastrar ou editar um prospect. Esta opção é mais voltada para administradores;
* **Vincular prospect ao SDR ao salvar:** Ao editar um Prospect, o usuário que tenha o Papel Exercido de SDR será associado automaticamente a ele.
* **Pode visualizar prospect sem corretor:** Ao ativar este parâmetro, o usuário pertencente a este grupo poderá visualizar, na tela de pessoas, os registros que não possuem corretores associados. OBS: Para este parâmetro funcionar, será necessário estar com parâmetro: **Visualizar todos os prospects:** (desmarcado)

Importante

**Visão Leads:**   
As configurações da visão de leads seguirá as permissões do agrupador prospect em grupo associado aos usuários, caso o grupo permita a visão de funil de leads.  
  
Os Leads que não tiver um usuário como responsável por eles, serão exibidos somente para quem pode ver todos.

### Permissões:  Proposta

* **Autorizar proposta reprovada:**
* **Imprimir proposta:**
* **Ver qualquer proposta:** Define se o grupo de usuários pode ver as propostas de qualquer hierarquia que não seja a sua. Com esta opção marcada, os usuários deste grupo podem visualizar as propostas de outros corretores, mas não pode editá-las, caso não seja o superior do corretor da proposta editada. Os superiores hierárquicos dos corretores sempre podem visualizar e editar as propostas dos seus subordinados.
* **Ver propostas dos subordinados e seus subordinados:** Esta opção define se os usuários deste grupo poderão ver e editar somente as propostas dos seus subordinados ou de todos os demais usuários. Os superiores hierárquicos dos corretores sempre podem visualizar e editar as propostas dos seus subordinados.
* **Ver o debug do VPL:** .
* **Escolher usuário da proposta:**
* **Alterar situação da proposta:**
* **Pode alterar CPF/CNPJ de propostas salvas:**
* **Transformar proposta em contrato:**
* **Enviar proposta para o backoffice:**
* **Anexar documentos à proposta:**
* **Avaliar documentos da proposta:**
* **Excluir anexos da proposta:**
* **Excluir proposta:**
* **Pode simular proposta:**
* **Mostrar tabela padrão:**
* **Carregar tabela padrão:**
* **Zerar proposta:**
* **À Vista:**
* **Acessar Relatório Comparação VPL:**
* **Pode avançar etapa da proposta:**
* **Pode imprimir plano pagamento:**
* **Visualizar e enviar mensagens de grupos autorizados:**
* **Visualizar e enviar imagens de grupos autorizados:**
* **Pode visualizar mensagem de proposta reprovada na impressão da proposta:**
* **Visualizar Situação Financeira Backoffice:**
* **Trocar corretor da proposta:**
* **Cria proposta com reserva de qualquer corretor:**
* **Mostrar menu Documentos da Pessoa:**
* **Pode alterar correspondente bancário da proposta:**
* **Pode salvar proposta c/ prospect de outro corretor:**
