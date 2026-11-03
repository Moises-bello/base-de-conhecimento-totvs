---
article_id: 18076512481175
category: CRM - Dúvidas Gerais
content_hash: 62640e86e908b5b4418edce8db4b69a40f00b73104bea8f0ecf7dabd02447641
fetched_at: '2026-06-28T22:40:27.407912+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGACRM - Transferência de
  Contas (CRMA020)
type: support-article
updated_at: '2025-03-12T17:29:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18076512481175-Cross-Segmentos-Backoffice-Linha-Protheus-SIGACRM-Transfer%C3%AAncia-de-Contas-CRMA020
---

**Tempo aproximado para leitura: **00:02:30 min******Dúvida:**

### Transferência de Contas (CRMA020)

**Ambiente:**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACRM - Todas as versões.  
  
**Solução:**

Esta funcionalidade possibilita ao vendedor transferir diretamente suas contas ou contas de vendedores subordinados a outros vendedores.

A transferência de contas pode efetuar-se pela área de trabalho do [SIGACRM](https://tdn.totvs.com/x/DYOpHg) de forma rápida e de fácil usabilidade ou pelo item **Gestão de Contas**do [Faturamento](https://tdn.totvs.com/x/ITmbEg).

```
![Help_button](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/help_button.zoom40.gif)Importante:  
  
Configure os conteúdos dos parâmetros conforme descrevemos: MV_FATPROP, conteúdo com P e MV_FATMNTP, conteúdo com 1.  
  
Configure o parâmetro MV_PAPEL com o conteúdo, uma lista de código de cargos utilizados como papel no time de vendas da oportunidade.
```

**Procedimentos:**

**Transferência de conta direta**

1. Acesse **Transferência de Contas**tendo posicionado em um usuário da árvore de negócios.
2. Selecione uma das contas disponíveis com duplo clique no campo **Mark,**para marcar a conta desejada.

```
![Help_button](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/help_button.zoom40.gif) Importante:  
  
Só podemos marcar a conta que tenha no campo Disponível o conteúdo SIM.
```

1. Clique em **Transferir**e visualize a tela de confirmação.
2. Confirme e veja mais uma vez uma nova tela.
3. Visualize os dados do vendedor proprietário da conta que estamos transferindo e os dados do vendedor que receberá as contas.
4. No **Grid Contas** visualize o vendedor selecionado na equipe de vendas. Preencha os dados, no campo **Código**selecionando o vendedor que receberá as contas.
5. No campo **Cod.Motivo**escolha o motivo da transferência.
6. Informe os campos **Obs.Motivo.**
7. Só preencha o campo **F.C.I.Oport.** quando for transferir uma conta e encerrar as oportunidades que esta tiver em aberto.  
     

   ---

**Transferência de conta por solicitação:**

1. No Cadastro do Vendedor o campo **Mod.Transf.** deve estar configurado com o valor **Transferência p/Solicitação.**
2. Acesse o sistema como usuário da árvore da **Estrutura de Negócio.**
3. Selecione uma das contas disponíveis com duplo clic no campo **Mark,** para marcar a conta desejada. Clique em **Transferir.**
4. Visualize a tela para confirmação. Clique em **SIM** e visualize a abertura de uma nova tela.
5. Visualize os dados do vendedor proprietário da conta que estamos transferindo e os dados do vendedor que receberá as contas.
6. No **Grid Contas** preencha os dados do vendedor selecionado.
7. No campo **Código**informe o vendedor que receberá as contas.
8. No campo **Cod.Motivo** preencha-o com o motivo da transferência e preencha o campo **Obs.Motiv.**
9. No**Grid Contas**preencha o fator de risco no campo**F.C.I.Oport,**apenas quando for transferir uma conta e encerrar as oportunidades em aberto que a ela pertençam.
10. Clique em**Confirmar.**

**Oportunidades:**

**As transferências realizadas encaminham as oportunidades para outro vendedor da seguinte maneira:**

1. A oportunidade aberta será enviada como "**aberta**" ou "**encerrada**".
2. As oportunidades já encerradas continuam com o cadastro do vendedor anterior, ou seja, o histórico das oportunidades encerradas não é transferido para o novo vendedor.
3. Para encaminhar uma oportunidade em aberto, você pode selecionar uma das opções abaixo:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30597116111127)
4. Enviar como "2 - Encerrar como perdida" para transferir a oportunidade que estava em aberto e foi fechada para o novo vendedor.

```
![Help_button](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/help_button.zoom40.gif) Importante:  
  
Esta opção de Transferência por Solicitação gera uma solicitação para o superior deste vendedor. A conta só será transferida quando o superior autorizar.
```

Saiba mais:

[CRM0021 - Transferência de permissões SIGACRM](https://tdn.totvs.com/pages/releaseview.action?pageId=271663440)

[Transferência de Contas (CRMA020 - SIGACRM)](https://tdn.totvs.com/pages/releaseview.action?pageId=345540679)
