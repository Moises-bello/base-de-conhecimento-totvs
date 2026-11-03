---
content_hash: 6e4c4c92a85a9132b4d2689cabcad3466fb9a8233bdc7b640b62120696156047
fetched_at: '2026-06-29T00:08:45.297111+00:00'
page_id: '311065074'
product: rm
source: tdn-rm
title: Geração GRRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=311065074
version: 3
---

**Assunto**

|  |  |
| --- | --- |
| **Produto:** | RM |
| **Versões:** |  |
| **Ocorrência:** | Art. 484-A. O contrato de trabalho poderá ser extinto por acordo entre empregado e empregador, caso em que serão devidas as seguintes verbas trabalhistas: I – por metade: a) o aviso prévio, se indenizado; e b) a indenização sobre o saldo do Fundo de Garantia do Tempo de Serviço, prevista no § 1º do art. 18 da Lei nº 8.036, de 11 de maio de 1990; II – na integralidade, as demais verbas trabalhistas. § 1º A extinção do contrato prevista no caput deste artigo permite a movimentação da conta vinculada do trabalhador no Fundo de Garantia do Tempo de Serviço na forma do inciso I-A do art. 20 da Lei nº 8.036, de 11 de maio de 1990, limitada até 80% (oitenta por cento) do valor dos depósitos. § 2º A extinção do contrato por acordo prevista no caput deste artigo não autoriza o ingresso no Programa de Seguro-Desemprego.” |
| **Ambiente:** | GRRF WinForms |
| **Passo a passo:** | Para habilitar as alterações da reforma trabalhista; Acesse  MDI  > RH > Folha de pagamento > Configurações > Parametrizador > Folha Normal > Geral  Marque o parâmetro: Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº 13.467 de 13 de Julho de 2017    Criado novo tipo de rescisão – V – Comum acordo  Siga os passos abaixo:  1. Cadastrar rescisão do tipo "V - Comum Acordo" com aviso prévio indenizado, informando o valor "Aviso Prévio indenizado ou não exigível" no campo de indicador de cumprimento de aviso prévio, e com código de saque diferente de "02 - Rescisão por culpa recíproca ou força maior". Calcular rescisão.    2. Gerar GRRF para o funcionário gerando lançamentos financeiros informando a parametrização de total da GRFC e marcando o parâmetro para gerar lançamentos individuais.        3. O código da movimentação deverá ser 'I5', que representa 'Outros', o tipo do aviso prévio deverá ser '2', e o código de saque do FGTS deverá ser '07'' o que significa indenizado e a soma dos valores das verbas indenizatórias deve ser levada no campo 'Aviso Prévio Indenizado'    4. Cadastrar rescisão do tipo "V - Comum Acordo" sem aviso prévio indenizado, informando o valor "Cumprimento total" no campo de indicador de cumprimento de aviso prévio, e com código de saque diferente de "02 - Rescisão por culpa recíproca ou força maior". Calcular rescisão.    5. Gerar GRRF para o funcionário gerando lançamentos financeiros informando a parametrização de total da GRFC e marcando o parâmetro para gerar lançamentos individuais.    6. O código da movimentação deverá ser 'I5', que representa 'Outros', o tipo do aviso prévio deverá ser '1'  e o código de saque do FGTS deverá ser '07'', que significa trabalhado e o campo 'Aviso Prévio Indenizado' deverá estar zerado    7. Cadastrar rescisão do tipo "V - Comum Acordo" com aviso prévio indenizado, informando o valor "Cumprimento total" no campo de indicador de cumprimento de aviso prévio, 15 dias de aviso trabalhado, e aviso misto e com código de saque diferente de "02 - Rescisão por culpa recíproca ou força maior". Calcular rescisão.    8. Gerar GRRF para o funcionário gerando lançamentos financeiros informando a parametrização de total da GRFC e marcando o parâmetro para gerar lançamentos individuais.    9. O código da movimentação deverá ser 'I5', que representa 'Outros', o tipo do aviso prévio deverá ser '2', e o código de saque do FGTS deverá ser '07'' que significa indenizado e a soma dos valores das verbas indenizatórias (que são proporcionais aos dias indenizados) deve ser levada no campo 'Aviso Prévio Indenizado' |
| **Observações:** |  |
