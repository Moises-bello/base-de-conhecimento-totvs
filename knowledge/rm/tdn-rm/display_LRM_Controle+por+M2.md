---
content_hash: 8ed29c221cd57f1332c24868e5ad99b06c043df4ede7ae933ea164d823400d26
fetched_at: '2026-06-29T00:08:57.058592+00:00'
page_id: '353272947'
product: rm
source: tdn-rm
title: Controle por M2
type: documentation
url: https://tdn.totvs.com/display/LRM/Controle+por+M2
version: 5
---

Além do Controle de M2 já desenvolvido  devem ser feitas as seguintes evoluções:

**Cadastro do Imóvel**

* No cadastro de Áreas do imóvel, não obrigar a informar valor do M2 e permitir informar o valor sugerido para os "Tipo de Locação"  = "Áreas unificadas" e "Imóvel".

**Contrato de Locação**

* O Reajuste deve ser aplicado no Item no contrato de Locação e não nas ocupações, para isso deve ser criado parâmetro por coligada, modelo de contrato (default) e contrato de Locação, afim de permitir os dois comportamentos (reajuste por ocupação e reajuste por item) mantendo compatibilidade com demais clientes.
* Habilitar para edição o campo "Valor do Item do Contrato";
  + Quando o usuário alterar este valor automaticamente o campo "Valor Médio do M2" deve ser atualizado e vice versa.
  + Os valores devem ser trazidos na tela do item do contrato de locação ao sair do campo de imóvel e não apenas ao clicar no botão salvar.

**Considerações:**

Embora o cliente tenha alguns imóveis que possui locação por área, todo o controle de valor é negociado por imóvel e por área, diferente de cliente que trabalham exclusivamente com imóveis com locação por M2. Diante desta situação é necessário compatibilizar o comportamento permitindo o comportamento de calculo por m2 ou por imóvel.
