---
content_hash: 876e6d5e1009060ef21b4c37f0298148f347ee6adb189a6b19c8e01cbd6c8ecc
fetched_at: '2026-06-29T00:10:51.484880+00:00'
page_id: '568924136'
product: rm
source: tdn-rm
title: Inscrição utilizando Responsável Legal (Responsável Acadêmico)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=568924136
version: 8
---

Importante

Esta funcionalidade está liberada a partir das versões 12.1.27.283, 12.1.28.198, 12.1.29.121 e superiores mediante a execução do script **CN.2020.10\_02,** disponível nos patchs. 

Este parâmetro obriga candidatos menores de idade do ensino superior, a informarem um responsável legal, este responsável será representado pelo responsável acadêmico da inscrição. Para que isso ocorra corretamente, logo ao marcar o parâmetro, será habilitado na aba "Visibilidade/obrigatoriedade de campos" os campos abaixo:

* Campo do candidato:
  + Data de nascimento (Visível e obrigatório) - Este campo deve ser de obrigatório preenchimento do candidato, para que a idade seja informada.
* Campos do responsável - Somente visível (Para não interferir na parametrização de campos obrigatório para outros responsáveis, os campos serão marcados como somente visível, porem os que estão em negrito serão de obrigatório preenchimento para a regra de responsável legal):
  + **Nome**
  + **Data de nascimento**
  + **Estado Natal**
  + **Naturalidade**
  + **CPF**
  + Telefone
  + E-mail

OBS.: Os campos citados acima, não podem ser desmarcados, enquanto o parâmetro estiver marcado.

Caso nenhum dos responsáveis esteja visível para inscrição, ao acessar o formulário de inscrições, não será exibido o passo de Responsáveis, porem, assim que o candidato informar sua data de nascimento e o mesmo for menor de idade, será incluído o passo de responsáveis com o preenchimento obrigatório do responsável acadêmico.
