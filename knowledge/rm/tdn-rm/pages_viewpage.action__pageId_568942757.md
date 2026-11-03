---
content_hash: d1940022dae3db304f73b2fea15ecb685d07ee063663755c62a7a264809bb592
fetched_at: '2026-06-29T00:10:51.563682+00:00'
page_id: '568942757'
product: rm
source: tdn-rm
title: Como realizar a alteração do campo <ideDmDev> na entrada em produção caso trabalhe
  com mês caixa?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=568942757
version: 7
---

false

**A partir das Versões:**

* 12.1.27.287
* 12.1.28.199
* 12.1.29.123

# Objetivo:

---

Através deste processo o usuário poderá relacionar o código do período da folha de pagamento com o código de período do sistema terceiro através de um valor fixo ou fórmula, para realizar a alteração do campo <ideDmDev> na geração do evento S-1210 na entrada em produção caso trabalhe com mês caixa.

1true1Execução do scriptExecução do script

Para a liberação do De/Para de Período será necessário executar o script através do sistema RM.Atualizador.exe.

2De/Para de Período usando FórmulaDe/Para de Período usando Fórmula

Acesse o menu RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | De/Para | De/Para de Período

Cadastre um novo De/Para, no exemplo abaixo será realizado a alteração do período "1" da folha para uma formula.

Criado uma fórmula para concatenar a palavra "TESTE" com o campo MATRICULAESOCIAL usando a função TABFUNC

Funcionário abaixo possui envelope cadastrado para o período "1"  conforme De/para.

Ao gerar o Xml do evento S-1210 o sistema irá substituir o campo <ideDmDev> para o valor calculado pela formula cadastrada no De/Para de período.

3De/Para de Período usando valor fixoDe/Para de Período usando valor fixo

Acesse o menu RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | De/Para | De/Para de Período

Cadastre um novo De/Para, no exemplo abaixo será realizado a alteração do período "1" da folha para o valor fixo do Período eSocial "4568".

Funcionário abaixo possui envelope cadastrado para o período "1"  conforme De/para.

Ao gerar o Xml do evento S-1210 o sistema irá substituir o campo <ideDmDev> para o valor cadastrado no De/Para de período.
