---
content_hash: bd33a6db936cf5ff2f7838c99bb04b637975d99094db597ac2f46603aecf2bd1
fetched_at: '2026-06-29T00:12:13.981092+00:00'
page_id: '962613044'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Atendimento > Alta > Processo de alta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=962613044
version: 14
---

## **ÍNDICE**

1. **Visão Geral**
2. **Permissão de acesso**
3. **Início do Fluxo**
4. **Processo**
5. **Log**
6. **Parâmetros**

sumarioVisão Geral

Processo de realização de alta de pacientes internados no RM Saúde, esse processo cria um fluxo onde é necessário liberação médica, da enfermagem, da tesouraria e da portaria para que a alta seja concluída.

Esse processo contempla apenas pacientes internados, ou seja, registro de atendimento com o tipo paciente igual a interno.

Permissão de acesso

Para que o processo funcione devidamente, é necessário habilitar as seguintes permissões para que as liberações ocorram.

1. Avança tesouraria
2. Avança enfermagem
3. Avança portaria

Início do fluxo

O fluxo atualmente é iniciado pelo registro de alta no RM.

1. Ao realizar o processo de alta, caso o RM esteja configurado para utilizar o fluxo de processo de alta, é criado um registro automático no processo para que o fluxo seja executado.
2. O PEP ainda não possui integração com esse processo, a solicitação é realizada no PEP e o início é manual no RM.

Processo

1. Após início do fluxo é exibido no menu Atendimento > Alta > Processo de alta o registro do fluxo de processo de alta.

2 Ao clicar em editar, o RM exibe o fluxo e um indicador visual dos status as etapas.

* O fluxo deve seguir a ordem, enquanto a etapa atual não for executada, a etapa seguinte seguinte não é habilitada.
* O usuário responsável pela liberação pode informar uma observação que é registrada no log.
* A alta médica e liberação da enfermagem são realizadas em processos específicos dentro de seus respectivos fluxos e alteram automaticamente o fluxo de processo de alta.
  + A alta médica ainda será integrada com o PEP.
  + A liberação da enfermagem é realizada no processo de alta documentado [nesse link](https://tdn.totvs.com/pages/viewpage.action?pageId=962608217), se refere a alta administrativa.
* A liberação da tesouraria e portaria são realizadas no fluxo de processo de alta.
* A liberação da tesouraria é realizada após o paciente ter realizado a quitação de seus débitos junto a instituição.
* Por último a liberação da portaria que é realizada quando o paciente de fato deixa a instituição.
  + Apenas após essa última etapa que o leito é desocupado e disponibilizado para higienização

Log1. Todas as ações são registradas e podem ser consultadas no formulário do fluxo de alta ou em seu anexo Log do fluxo do processo de alta

* O log registra as informações de liberação de todas as etapas:

  + O usuário responsável pela liberação
  + Data/hora da liberação
  + Observação, caso tenha sido preenchida
  + Etapa

Parâmetros

### 1. Utilizar workflow de processo de alta

* Caso o parâmetro **Utiliza workflow de processo de alta**esteja habilitado, o RM inicia o fluxo de processo de alta ao realizar a alta administrativa.
* [Processo de alta administrativa](https://tdn.totvs.com/pages/viewpage.action?pageId=962608217)
