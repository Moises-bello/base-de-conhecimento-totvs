---
content_hash: f7e217ea04db94f4b86e363b322648c60617cb3f6c0734168a271c7348f7d6da
fetched_at: '2026-06-29T00:10:58.752010+00:00'
page_id: '606424147'
product: rm
source: tdn-rm
title: Transferência de Pacientes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=606424147
version: 21
---

## **CONTEÚDO**

CONTEÚDO

sumarioVisão Geral

## **01. Visão Geral**

Essa rotina é utilizada para realizar a transferência de pacientes de **Interno para Externo** ou **Externo para Interno.**

Transferência Paciente

## **02.** **Transferência Paciente**

A rotina pode ser executada através de dois locais distintos no menu:

Opção 1: Atendimento > Registro de Atendimento > Transferência Paciente

Opção 2: Registro de Atendimento > Selecione o atendimento desejado > Anexo > Transferência Paciente

1) selecionar o atendimento desejado e ao abrir o mesmo através da rotina de transferência de paciente, o mesmo já será preenchido automaticamente como **Interno/Externo****.**

2) Ao clicar em Salvar, todo processo de transferência é realizado e assim o atendimento passa para **Interno/Externo**.

3) Para ambos os tipos de transferência será criada uma nova parcial para o atendimento.

Regras para Transferência

## **03. Regras para T****ransferência**

As seguintes regras abaixo serão executas durante o processo de transferência de atendimentos interno/externo, sendo elas:

* 1. Para a transferência de Externo → Interno ou Interno → Externo o paciente deve obrigatoriamente ter um atendimento em **aberto**.
  2. Para a transferência de Externo → Interno ou Interno → Externo a parcial do atendimento deve estar obrigatoriamente com status em **Elaboração**.
  3. Para a transferência de Externo → Interno ou Interno → Externo a parcial do atendimento deve estar sem **remessa vinculado**.
  4. O paciente não pode ter um registro de Internação **aberto**. (Regra exclusiva na transferência de atendimento de **Externo** para **Interno).**
  5. Não pode ser selecionado um paciente que já possua um leito **vinculado ao seu atendimento**. (Regra exclusiva na transferência de atendimento de **Interno** para **Externo**)
Transferência com Remessa Vinculada

## **04. T****ransferência** **com Remessa Vinculada**

Caso uma parcial já tenha sido incluída em uma remessa, será necessário primeiro remove-la da remessa, para depois realizar o processo de transferência. Para isso, execute os seguintes passos:

1) Identifique qual o **número da remessa** a parcial está vinculada.

2) Acesse a rotina **Faturamento para Convênios**, faça um filtro localizando a remessa do convênio onde será removido o vínculo.

3) Executar o processo **Faturamento de Convênio** e selecionar a opção **Reprocessamento** e em seguida avançar.

4) Selecionar a opção “**Remover conta da fatura”.**

5) Selecionar a parcial que será removida o vínculo e executar o processo.

6) Após a conclusão do processo, a parcial será desvinculada da fatura, retornando seus status para **Liberada**, ficando disponível para inclusão na mesma fatura posteriormente ou em uma outra fatura futura.

7) A próxima etapa será retornar a Parcial para o status em **Elaboração**, para isso acesse a rotina de **Elaboração de Contas**, faça um filtro localizando a parcial e execute a rotina de **Retornar Parcial para Elaboração**

**8) A partir desse momento, a o atendimento já pode ser transferido de Externo/Interno, para mais detalhes, proceder conforme orientações no tópico 2 deste manual.**

## **05.** **Parâmetro Cancelamento Parcial**

No processo padrão, ao realizar a transferência de atendimento de Externo para Interno, a Parcial 1 permanecerá em aberto e deverá ser encerrada manualmente por meio da rotina ***Encerramento de Parciais Sem Débitos*.**

Caso deseje que a Parcial 1 seja **cancelada automaticamente** nesse tipo de transferência, é necessário ativar o parâmetro: **Registro e Controle > Cancela Primeira Parcial ao Mudar o Tipo de Atendimento.**
