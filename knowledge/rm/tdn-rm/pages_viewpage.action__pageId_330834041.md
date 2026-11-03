---
content_hash: 803264b42becb9caae6329b468868700036ac1794045b3d3fccf6f15f6041c97
fetched_at: '2026-06-29T00:08:49.464751+00:00'
page_id: '330834041'
product: rm
source: tdn-rm
title: DT Aviso Prévio - Melhorias Em Telas de Aviso Prévio e Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330834041
version: 4
---

# Melhorias Em Telas de Aviso Prévio e Rescisão

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Folha de Pagamento |
| **Módulo:** | Rescisão/Aviso Prévio |
| **Solução/Implementação:** | Pedido de melhoria em validações da tela, preenchimento automático de campos, adição de funcionalidades por fórmulas. |
| **Tickets relacionados:** | [FOPCALCULO01-2339](http://jiraproducao.totvs.com.br/browse/FOPCALCULO01-2339) |

**AVISO PRÉVIO TRABALHADO INDIVIDUAL**

1)      Data de Demissão Prevista: Após digitar/alterar a “Data de Início do Aviso” e dar um TAB ou salvar, a “Data de Demissão Prevista” receberá 30 dias por default. Caso o usuário altere a “Data de Demissão Prevista” o produto permitirá.

2)      Botão “Executa Fórmula Aviso Sindicato”: Após salvar o aviso prévio é permitido executar a fórmula para calcular a “Data de Demissão Prevista”. Após a execução da fórmula a data de demissão será atualizada e será mostrado o total de dias de aviso. Essa fórmula se encontra dentro do cadastro de sindicato.

3)      Opção Default”: Após salvar o aviso prévio é possível definir o valor “Default” para os campos presentes na tela.

**AVISO PRÉVIO TRABALHADO COLETIVO**

1)      Data de Demissão Prevista: Após digitar/alterar a “Data de Início do Aviso” e dar um TAB ou salvar, a “Data de Demissão Prevista” receberá 30 dias por default. Caso o usuário altere a “Data de Demissão Prevista” o produto permitirá.

2)      Parâmetro “Executa Fórmula Aviso Sindicato”: Ao marcar o parâmetro, a fórmula de aviso prévio, que se encontra no sindicato, será utilizada durante a execução do processo para calcular a “Data de Demissão Prevista”. Consequentemente o campo “Data de Demissão Prevista” será desabilitado na tela.

**RESCISÃO**

1)      Alteração da “Data de Demissão” com parâmetro “Tem Aviso Prévio Indenizado” marcado:

1. Após digitar/alterar a “Data de Demissão”, a “Data de Início do Aviso Prévio” será alterada de acordo com as seguintes regras:

                                                               i.      Caso a data anterior do aviso indenizado era a data da demissão mais um dia, a nova data de aviso indenizado será a data de demissão mais um dia;

                                                             ii.      Caso a data anterior do aviso indenizado era a data da demissão, a nova data de aviso indenizado será a data de demissão.

1. Caso a “Data de Início do Aviso Prévio” seja diferente da “Data de Demissão” ou “Data de Demissão” mais um, não será permitido salvar a rescisão.
2. Se ao salvar os “Dias de Aviso Indenizado” estiver zerado será mostrado uma mensagem para o usuário e permitirá salvar.
3. Ao salvar a rescisão após alteração da “Data de Demissão”, aparecerá uma mensagem para o usuário solicitando-o verificar se o campo “Dias de Aviso Indenizado” permanecerá com o mesmo valor.

2)      “Data de Demissão” anterior e posterior a competência atual:

1. É possível cadastrar rescisão somente se a “Data de Demissão” estiver na competência anterior, atual ou posterior.
2. Ao cadastrar em mais de duas competências posteriores, o usuário será informado e a rescisão não será salva.
3. Ao cadastrar em competência anterior a atual, o usuário será informado e a rescisão será salva. Porém não será possível calculá-la.

3)      Rescisão com Aviso Prévio Misto:

1. Quando o parâmetro “Aviso Prévio Misto” for marcado, o sistema preenche o campo “Data de Início Aviso Prévio Indenizado” com a “Data de Demissão” mais um dia.
