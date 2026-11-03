---
content_hash: 84dc33730d6a240228fd4788642c4ed8d3008bcbb485b9ff08e61bb2c82320f9
fetched_at: '2026-06-29T00:11:28.211158+00:00'
page_id: '730541397'
product: rm
source: tdn-rm
title: Condições Contratuais - Parâmetros 1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=730541397
version: 4
---

## **01.** **Código Dependente Obrigatório**

Indica se o campo será de preenchimento obrigatório durante o registro do atendimento.

## **02.** **Externos/Internos: exigir preenchimento CPF**

Indica se o campo será de preenchimento obrigatório durante o cadastro de um novo responsável financeiro durante o registro do atendimento.

## **03. Número e data da GUIA / NOTA / COMPROVANTE sempre obrigatórios**

Indica se os campos Núm. Guia / Comprovante e Data da Guia serão de preenchimento obrigatório durante o cadastra de uma nova Guia / Autorização.

## **04. Número da AUTORIZAÇÃO / SENHA e procedimentos autorizados sempre obrigatórios**

Indica se o campo Número Autorização / Senha será de preenchimento obrigatórios durante o cadastro de uma nova Guia / Autorização.

**Observação**, Desativado o parâmetro Número da AUTORIZAÇÃO / SENHA e procedimentos autorizados sempre obrigatórios, caso o campo abaixo seja incluido.

## **05. Validade cartão obrigatório para paciente Interno**

Indica se o campo será de preenchimento obrigatório durante o registro do atendimento.

## **06. Externo/Internos: exigir preenchimento EMAIL do paciente**

Indica se o campo será de preenchimento obrigatório durante o registro do atendimento.

## **07. Lança procedimentos das guias de autorização na conta do paciente,  se dentro da faixa de codificação**

Indica se o item da autorização informado na Guia / Autorização será lançado na parcial do paciente. O item será lançado no grupo de gastos de acordo com a sua da faixa de codificação.

## **08. Obriga o preenchimento de guias no pré-registro**

Indica se as Guias / Autorização devem ser preenchidas no ato do pré-registro do atendimento.

## **09. Regra de Retorno de Eletivo**

| Opção | Regra |
| --- | --- |
| Não se aplica | Nenhuma regra de retorno será aplicada no atendimento do Paciente. |
| Considerar contagem de retorno a partir de atendimento não classificados como retorno |  |
| Considerar como retorno apenas o primeiro atendimento dentro do prazo |  |

## **10. Informações obrigatórias para paciente Externo**

Indica se os campos serão de preenchimento obrigatórios para pacientes externos.

## **11. Código do Beneficiário**

Nesse campo deverá ser informada a rotina para cálculo do dígito verificador do código do beneficiário. Se informado, o sistema fara a consistência do código do Beneficiário no momento da digitação na tela de registro de atendimento interno e externo.

## **12. Diárias obrigatoriamente incluídas nas Guias / Autorizações de Internação**

Indica se o registro do atendimento deverá ter obrigatoriamente uma diária na Guia / Autorização quando o atendimento for do tipo internação.

## **13. Cálculo da diferença de diárias e honorários para gastos particulares**

Se informadas, ao transferir gastos ou houver cobrança em coparticipação, o sistema irá recalcular o preço baseada na tabela informada ou utilizar um valor fixo para a diferença da diária

Exemplo: Se o paciente é internado pelo convênio em um plano de Enfermaria, porém o paciente opta por ficar internado em um Apartamento, ao realizar a mudança de categoria, utilizando como convênio Particular, os lançamentos então as diferenças de valores serão calculadas com base nesta tabela ou qual o valor que deverá ser cobrado na diferença da diária.
