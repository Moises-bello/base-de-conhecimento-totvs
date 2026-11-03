---
content_hash: 52fcfa8e8c8c3eed6529a4b7290a7f8ae86809d49e012ed88e2f1a491f2c2f3c
fetched_at: '2026-06-29T00:05:56.420389+00:00'
page_id: '149882529'
product: rm
source: tdn-rm
title: RMPES00001_Como Fazer - Inclusão de Atestados que geram Afastamento no RM Labore.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149882529
version: 3
---

|  |
| --- |
| **Produto:** *TOTVS Gestão de Pessoas***Versão:***11.5 X ou   superior* |
| **Processo:** *Atestados* |
| **Subprocesso:** *Inclusão de Atestados que geram Afastamento no RM Labore* |
| ***Introdução*** |
| Este roteiro tem como objetivo instruir quanto ao processo de cadastro de atestados médicos pelo Vitae que irão gerar afastamento no RM Labore.  Obs.: Pelas regras do SEFIP, todo atestado maior ou igual a 1 dia deve ser informado como afastamento no RM Labore com o intuito de realizar o controle do pagamento dos quinze primeiros dias de atestado por parte da empresa. |

**Passo 1 – Tipo de Atestado**

- Via RM Vitae.exe:

Acessar o menu Cadastros |Tabelas Auxiliares| Tipos de Atestado e criar um tipo de atestado vinculado a um tipo de afastamento do Labore.

- Via nova MDI:

Acessar Produto Gestão de Pessoas e na guia Gestão Organizacional | Tabelas Auxiliares| Tipos de Atestado e criar um tipo de atestado vinculado a um tipo de afastamento do Labore.

Exemplo:  
  
Código: 0002  
Descrição: Afastamento Acid. Trabalho  
Cód. Afastamento: T – Af.Ac.Trabalho

**Passo 2 – Inclusão do Atestado**

- Via RM Vitae.exe:

Acessar Cadastro| Funcionário, selecionar o funcionário, clicar em Anexos | Segurança e Medicina| Atestados, informe os dados do atestado. Não esqueça de vincular o tipo de atestado cadastrado no 1º Passo. Após salvar o sistema irá habilitar a guia Chapas Envolvidas, informe a chapa do funcionário e o motivo do afastamento.

- Via nova MDI:

Acessar o produto Gestão de Pessoas e na guia Acompanhamento | Funcionários, marque funcionário desejado e em seguida clique em Anexos | Segurança e Medicina| Atestados, informe os dados do atestado. Não esqueça de vincular o tipo de atestado cadastrado no 1º Passo.  Após salvar o sistema irá habilitar a guia Chapas Envolvidas, informe a chapa do funcionário e o motivo do afastamento.

Exemplo:  
Tipo Atestado: 06 - Afastamento Acid.Trabalho.

Data Início: 01/01/2014

Data final:  30/01/2014

Obs.: Se no momento da inclusão do atestado você não souber a data de retorno basta não informar, quando tiver esta informação em mão volte e informe o retorno do funcionário ao trabalho.

 CID: XXXX

Após salvar os dados da pasta Chapas envolvidas onde a "Data Final " do atestado tenha sido cadastrada, será exibida mensagem para lançamento do retorno automático do funcionário no RM Labore; se for confirmado o lançamento do retorno automático, o funcionário terá o registro do histórico do afastamento lançado no RM Labore porém permanecerá com status "Ativo" ; se não for confirmado o lançamento do retorno automático, o histórico do afastamento será registrado da mesma forma porém, neste caso, o status da situação do funcionário será modificado para "Afastado", sendo necessária a alteração manual da situação diretamente pelo RM Labore.  
  
**Dicas:**  
Para excluir um atestado, primeiro deverá ser excluído a Chapa Envolvida depois será permitido excluir o atestado, desde que, esteja ainda na mesma competência do RM Labore.  
  
Caso deseje cadastrar um atestado sem integração com os demais aplicativos RH, basta não cadastrar a chapa envolvida.
