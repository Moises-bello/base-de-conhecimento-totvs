---
content_hash: fb4a10213b018ea51b0e908ff1d7e6788695b50eea13413df0569ec65d4a95f1
fetched_at: '2026-06-29T00:11:16.142334+00:00'
page_id: '662433187'
product: rm
source: tdn-rm
title: Autônomo cadastrado no Financeiro com valor do serviço diferente do valor original
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=662433187
version: 10
---

false

**A partir das Versões:**

* + 12.1.32.245
  + 12.1.33.185
  + 12.1.34.103

# Objetivo:

---

       O objetivo deste documento é apresentar a tratativa no envio da remuneração do autônomo quando o valor do serviço é diferente do valor original informado no lançamento financeiro cadastrado.

---

* Note que no lançamento financeiro, o valor original é diferente do valor do serviço.

* Em RH | Folha de pagamento | Configurações | Parametrizador | Integrações | Gestão Financeira marque o parâmetro "Considerar valor do serviço em vez de valor original", conforme abaixo:

# **SEFIP**

* Será gerado conforme o valor do serviço.

# **Guia de INSS**

* Será gerado conforme o valor do serviço.

# **MANAD**

* Será gerado conforme o valor do serviço.

# **Folha A****nalítica**

* Será gerado conforme o valor do serviço.

# **eSocial**

* Em RH | Folha de pagamento | Configurações | Parametrizador | eSocial - Parâmetros | Configurações Gerais | Autônomos e Externos 1/2 foi criado o campo para a informação da verba sem incidência, conforme abaixo:

Ao gerar XML do evento S-120, será utilizado o evento informado no parametriizador para lançar o valor da remuneração do autônomo:

Ao gerar o XML do evento S-1210 será gerado o valor do liquido considerado o valor total do lançamento, conforme abaixo:
