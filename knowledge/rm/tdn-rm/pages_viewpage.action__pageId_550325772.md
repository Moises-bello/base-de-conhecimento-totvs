---
content_hash: 2eab3d10b18f7dd33a9800c60aaf3318e3ad6e512b52385ea8451698b6ebcf87
fetched_at: '2026-06-29T00:10:43.684483+00:00'
page_id: '550325772'
product: rm
source: tdn-rm
title: Processo para Alterar a Forma de Inscrição do Candidato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550325772
version: 5
---

Este processo é executado a partir da tela de “inscrição dos candidatos”. Toda inscrição possui uma forma de inscrição e um lançamento gerado através de serviços do Módulo Gestão Financeira

Uma vez que uma inscrição foi realizada, é possível alterar sua forma de inscrição através deste processo. Abaixo segue a figura ilustrando os campos que deverão ser preenchidos para a execução do processo.

**Forma de inscrição** - Deve ser informada a nova forma de inscrição, nesta seleção não aparece a forma de inscrição atual.

**Motivo** - Deve ser informado para fins de histórico, o motivo pelo qual a inscrição teve sua forma de inscrição alterada.

Se a inscrição tiver um lançamento gerado no Módulo Gestão Financeira e ele não tiver sido cancelado, o processo tentará realizar o cancelamento do mesmo. Se não for possível cancelá-lo, consequentemente, não será permitido alterar a forma de inscrição. Assim que este processo for executado, a inscrição do candidato estará com a nova forma de inscrição.

Se a nova forma de inscrição escolhida possuir 100% de desconto, então o status da inscrição passará a ser “Candidato (inscrição confirmada)”. Caso contrário, se a nova forma de inscrição gerar um novo lançamento com valor maior que zero, o status da inscrição passará a ser “*Inscrito (pendente de confirmação)*”.

**O processo descrito apresenta pré-requisitos, tais como:**

* ***O Processo Seletivo para o qual o processo é executado deve estar no período de inscrição;***
* ***O Processo Seletivo para o qual a inscrição foi realizada deve ter mais de uma forma de inscrição;***
* ***As formas de inscrição disponíveis devem estar no período de inscrição;***
* ***A inscrição não pode estar com o status “Inscrição Cancelada”.***
