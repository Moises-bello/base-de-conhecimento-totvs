---
content_hash: b9bbb4146cea553ce22546cb0d2e5d901d489abf3d69559a25ad92b1f85994e4
fetched_at: '2026-06-29T00:09:16.367894+00:00'
page_id: '421385522'
product: rm
source: tdn-rm
title: Sincronização de Bens e Transferência de Filial e Centro de Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385522
version: 2
---

---

A sincronização de equipamentos (bens) entre o módulo Manutenção de Ativos do Protheus e o TOP (Módulo Gestão de Patrimônio do Corpore) permite que os equipamentos cadastrados no Protheus sejam utilizados no TOP. A funcionalidade também mantém o sincronismo nas transferências entre filias e centros de custo dos equipamentos, as mesmas são realizadas no Protheus e replicadas para o Corpore.

Quando a integração estiver ativa e devidamente configurada, existirão gatilhos no Manutenção de Ativos (Protheus) que irão enviar mensagens ao Corpore RM assim que alguma inclusão, alteração, inativação ou transferência for realizada em algum equipamento. O Corpore RM por sua vez vai atualizar os seus registros de equipamentos, refletindo as mudanças feitas no lado Protheus da integração para o lado RM.

A capacidade do bem é um campo do equipamento necessário para o projeto mobilidade e que irá constar na integração. No cadastro de patrimônio do TOTVS Gestão Patrimonial (Corpore RM) não existe campo fixo equivalente para manter este valor então nos valeremos da criação de um campo complementar e neste é que será atribuída a capacidade do bem.

Com relação à transferência de equipamentos de filial ou centro de custo no Protheus, também haverá sincronismo com o Corpore RM. Sendo assim, são refletidas as ações realizadas no Protheus para o Corpore RM, de modo a manter os registros históricos devidamente sincronizados em ambos os sistemas.

**Importante:**

Para realizar essa integração os cadastros de centros de custo deverão estar compatibilizados nos dois sistemas, deverão ser cadastrados os "DE-PARA" das coligadas, das filiais e da integração da "família" do Protheus para o grupo de patrimônio do Corpore.

**Passos para a Sincronização de Bens e Transferência de Filial e Centro de Custo:**

1. Acessar o módulo Manutenção de Ativos do Protheus

2. Acessar o cadastro de equipamentos

3. Inserir/Alterar/Inativar/Transferir equipamento

4. Salvar.

---
