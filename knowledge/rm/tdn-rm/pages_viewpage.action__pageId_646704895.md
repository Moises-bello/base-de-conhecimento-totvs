---
content_hash: 93299c321e635aeea875d95bb7fb42aee18958b558c6c5801a68adc2a4a9f6c6
fetched_at: '2026-06-29T00:11:11.495740+00:00'
page_id: '646704895'
product: rm
source: tdn-rm
title: PIX - Conciliação - Nova API
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=646704895
version: 23
---

Ativação da Nova API para executar a Conciliação

 Atualizar o sistema para as versões indicadas:

* PATCH 12.1.31.260 ou superior
* PATCH 12.1.32.206 ou superior
* PATCH 12.1.33.128 ou superior

falseIMPORTANTE

 É necessário realizar liberação dos acessos aos usuários cadastrados no RAAS para que a opção Totvs WebService seja exibida.

Em seguida siga os passos abaixo:

Acesse ***BackOffice > Gestão Financeira > Movimentações bancárias*** e clique em ***Conciliação***, conforme imagem abaixo:

Em seguida, realize o filtro e selecione ***Processos > Importação do Arquivo de Conciliação**.*

Neste momento aparecerá a tela de conciliação para selecionar os campos pertinentes, então, marque: ***TOTVS Pagamento Instantâneo >Importar e conciliar automaticamente e TOTVS WebService,*** conforme imagem abaixo*:*

Em seguida, clique em *Avançar.*

Não é necessário informar a data.  
Caso sua versão tenha a opção de "Considerar data de liquidação", pode desmarcá-la.

Obs: Para agendamento de job, seguir o mesmo padrão.
