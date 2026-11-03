---
content_hash: 0902e56e70f18abcae8173137c79bdbf41d964f39c11a9ff18573ce846f62166
fetched_at: '2026-06-29T00:10:00.481465+00:00'
page_id: '452718572'
product: rm
source: tdn-rm
title: Rateio de Centros de Custos
type: documentation
url: https://tdn.totvs.com/display/LRM/Rateio+de+Centros+de+Custos
version: 5
---

**Rateio de Centros de Custos**

Quando o parâmetro (Habilitar o rateio de centros de custos em requisições) estiver ativo será habilitada uma aba nas requisições de aumento de quadro, substituição, alteração de dados funcionais, transferência, transferência com alteração de dados funcionais e transferência em lote.

Para saber mais sobre o parâmetro clique no link : Parâmetros de Requisições

**Aba - Rateio de Centros de custos**

Nesta aba será permitido ao solicitante/aprovador propor um rateio de centros de custos para o funcionário/vaga relacionado às requisições citadas anteriormente.  
   
**Cadastro de Centros de Custos nas Requisições**

Na aba Rateio de centros de custos poderá ser cadastrado os centros de custos das requisições, ao clicar em incluir deverá ser escolhido o/os centros de custos e o valor da porcentagem de cada um. O rateio sempre deverá totalizar 100%.

Nas requisições criadas através do MDI, o comportamento se dará da seguinte forma:

* Alteração de Dados Funcionais, Transferência e Transferência com Alteração de Dados Funcionais
  + O sistema carregará automaticamente o rateio atual do funcionário (se houver) no momento em que o funcionário for informado na requisição.

Nas requisições criadas através do Portal RM, o comportamento se dará da seguinte forma:

* Aumento de Quadro e Transferência em Lote:
  + Caso o rateio não seja informado, será exibida a mensagem de erro: *"O rateio deve totalizar 100%. Favor verificar."*
* Alteração de Dados Funcionais, Transferência e Transferência com Alteração de Dados Funcionais:
  + Se for informado o rateio, este será aplicado na requisição.
  + Na ausência de rateio informado, o sistema utilizará automaticamente o rateio padrão definido na chapa do colaborador. Se não houver um rateio padrão definido para o colaborador, será exibida a mensagem de erro: *"O rateio deve totalizar 100%. Favor verificar."*

Após criar uma requisição, somente enquanto a mesma estiver com status "Pendente" será possível editar o rateio.

Quando a requisição estiver  "Em andamento", a edição poderá ser feita pela inclusão de pareceres, e um log da alteração será gravado acrescido ao parecer.

**Efetivação**

Ao efetivar as requisições supracitadas, exceto requisição de aumento de quadro e requisição de transferência em lote, o rateio de centros de custos deverá ser aplicado  ao cadastro do funcionário. Para a requisição de aumento de quadro, o rateio será aplicado ao funcionário que assumir a vaga criada.
