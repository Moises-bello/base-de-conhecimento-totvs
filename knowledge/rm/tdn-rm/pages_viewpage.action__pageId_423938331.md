---
content_hash: f9809e6bd962f39048bc5f36eb572045808783a3dd1e1230a9e63bb7c0ef5eb3
fetched_at: '2026-06-29T00:09:26.607164+00:00'
page_id: '423938331'
product: rm
source: tdn-rm
title: Cálculo de Depreciação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938331
version: 6
---

Fracionamento de Job

A partir da 12.1.2310 o processo de Cálculo da Depreciação permite o [Fracionamento de Jobs](https://tdn.totvs.com/display/LRM/Fracionamento+de+Jobs). Na parametrização da Segurança de Jobs fracionáveis, utilize o ID "**PatExecutaCalculoCenarioProc**".

O processo de cálculo de depreciação permite que seja realizado o cálculo de um ou mais patrimônios de forma a definir informações como os valores base, corrigido e de correção além do saldo residual. Permite também que sejam definidos os valores referentes ao índice associado a moeda que está vinculada ao patrimônio. Valores estes como o base, o saldo residual e a depreciação.

**Observação**

Os campos usuário e data de criação serão preenchidos automaticamente bem como o usuário e a data de alteração. Para isto será respeitado os dados referentes ao usuário logado no sistema.

Antes de executar o processo de cálculo deve-se conferir se os valores por moedas/índices e os cálculos por cenário estão preenchidos corretamente. Caso não haja informações nestas opções pode-se incluir manualmente os valores ou executar o processo que permite criar a moeda e o cenário do cálculo.

Importante: o sistema utilizará a taxa de depreciação com a data de início de vigência mais recente, correspondente ao cenário de cálculo selecionado.

**Log**

Ao executar o processo de calculo o sistema gera um arquivo contendo todos os procedimentos realizados. Desta forma pode-se acompanhar quais cálculos foram realizados e os patrimônios contemplados pelo mesmo. Para conferir o arquivo de log deve-se acessar a tela referente ao progresso de execução do(s) processo(s).

Para verificar os cálculos existem as seguintes opções:

* Cálculo Razão: permite visualizar todas as informações referentes a valores de forma geral.
* Razão por moeda/índice: permite visualizar todas as informações referentes a valores filtrando pelas moedas associadas ao patrimônio.
* Razão por tipo de cálculo: permite visualizar todas as informações referentes a valores filtrando pelos cálculos associados ao patrimônio.
* Razão por cenário: permite visualizar todas as informações referentes a valores filtrando pelos cenários associados ao patrimônio.

**Observação**

Esta opção está disponível apenas para uma versão especial cuja a liberação será controlada. Para maiores informações, favor entrar em contato com o suporte técnico.
