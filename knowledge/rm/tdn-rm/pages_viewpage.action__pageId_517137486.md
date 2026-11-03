---
content_hash: 8a93df10e4b9431105ca7e82306b2822f68427b8fc973d87b8ca5f56ca45d3bd
fetched_at: '2026-06-29T00:10:27.960447+00:00'
page_id: '517137486'
product: rm
source: tdn-rm
title: Código de cálculo 419-Desconto do Arredondamento de Líquido Insuficiente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=517137486
version: 8
---

Evento do tipo Desconto, valor.

Este evento deverá ser utilizado quando o parâmetro **"Lança Líquido insuficiente separado do arredondamento"**  existente em **Configurações | Parâmetros | Parametrizador | 06.01 - Folha de Pagamento | 06.01.03 - Folha Normal | Geral**estiver marcado.

Foi inserida uma melhoria no Log de Cálculo, para que passe a exibir a origem dos valores e o período considerado nos códigos de cálculo 21, 314 e 419. Mais informações: [DT - Códigos de Cálculo 21/314/419 - Melhoria do Log de Cálculo](https://tdn.totvs.com/pages/viewpage.action?pageId=917132275)

*Exemplo da melhoria no Código de Cálculo 419*                                                       

**Atenção:**

* A criação deste código de calculo foi necessária para atender ao eSocial .
* Sempre que existir Insuficiência de saldo no envelope , o sistema lançará, automaticamente, o [Código de Cálculo 341-Arredondamento de Líquido Insuficiente](https://tdn.totvs.com/pages/viewpage.action?pageId=452719800)  e será descontado no envelope do período seguinte no código de cálculo 419-Desconto do Arredondamento de Líquido Insuficiente.

[Códigos de Cálculo](https://tdn.totvs.com/pages/viewpage.action?pageId=452719279)
