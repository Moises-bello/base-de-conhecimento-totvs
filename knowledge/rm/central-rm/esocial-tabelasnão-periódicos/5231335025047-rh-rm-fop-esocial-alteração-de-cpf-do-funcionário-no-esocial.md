---
article_id: 5231335025047
category: eSocial - Tabelas/Não Periódicos
content_hash: 0b92fc116c6909026bacd3ced0c386295e82a7836853ef3fa2e5153a9979512f
fetched_at: '2026-06-28T22:47:10.241885+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Alteração de CPF do funcionário no eSocial
type: support-article
updated_at: '2024-06-27T16:32:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5231335025047-RH-RM-FOP-eSocial-Altera%C3%A7%C3%A3o-de-CPF-do-funcion%C3%A1rio-no-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24396334350231) Tempo aproximado para leitura: **00:03:30 min****Dúvida**Como fazer alteração de CPF do funcionário no eSocial e quando realizar tal alteração?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**

O **CPF** é um documento utilizado no eSocial como o **principal identificador do trabalhador**. O CPF é fundamental para a vinculação e aplicação de regras e validações do eSocial.

Em algumas situações, **o CPF pode ser alterado pela Receita Federal do Brasil**, impactando, assim, os cadastros desses trabalhadores no eSocial. Por isso, o Comitê Gestor do eSocial orientou, por meio de Nota, quais os procedimentos necessários em casos de alteração de CPF do trabalhador no que tange o projeto.

O procedimento consiste no envio de um evento **S-2299/S-2399** com o motivo com o motivo **36 – Mudança de CPF** seguido do envio de um novo **S-2200/S-2300** com o tipo de admissão **6 – Mudança de CPF**.

Abaixo, segue o passo a passo de como realizar o processo no sistema:

1. No TOTVS Folha de Pagamento, acesse o menu **Administração de Pessoal | Funcionários**;  
2. Selecione o funcionário que deseja realizar a alteração do CPF e acesse **Processos | Alteração de CPF eSocial**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24477543162135)

3. Cadastre o **novo CPF** e a **data de alteração** (essa data representa o **início da validade do novo CPF**) e clique em **Executar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24477543165591)

4. O sistema irá apresentar uma mensagem informando que a alteração ocorrerá em todas as chapas relacionadas ao CPF informado, isso para o caso do funcionário possuir múltiplos vínculos, mesmo que em outra coligada. Para concluir a alteração clique em **Sim**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24477543168663)

5.Após execução, serão gerados os gatilhos **S-2299/S-2399** e **S-2200/S-2300** com o tipo de operação **Alteração de CPF** para geração do XML e envio ao eSocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24477549909271)

**S-2299**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24477512473367)

**S-2200**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24477543184919)

**Importante**

- Esse processo afeta **todas as coligadas**. Ao executa-lo serão alterados os campos CPF e matrícula eSocial. Caso o CPF que está sendo processado seja encontrado em outras chapas e coligadas, a alteração também será aplicada a esses funcionários.

- Caso possua algum evento não periódico com status **Gerado** na fila de eventos, o mesmo terá seu status retornado para **Pendente** para que seja gerado novamente com o **CPF** e **Matricula eSocial** atualizados.

- Caso possua algum **evento periódico** na fila de eventos, será necessário **regerá-los**, pois este evento **não terá seu status alterado automaticamente**.

- **Não** é possível a inclusão manual desses gatilhos com o tipo de operação **Alteração CPF**.

- O detalhamento da **REGRA\_MUDANCA\_CPF** pode ser encontrado no **Anexo II dos leiautes do eSocial - Regras de validação**.

**Saiba mais**  
Para visualização de prints e de todo detalhamento do processo, acesse a documentação abaixo:  
     - [Alteração de CPF para o eSocial](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=550306792#1-3)
