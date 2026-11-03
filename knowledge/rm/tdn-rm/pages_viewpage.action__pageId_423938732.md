---
content_hash: 022938e4b2b3f81d1dbef893449352f825ebad851b02823301834fc44a211632
fetched_at: '2026-06-29T00:09:28.637492+00:00'
page_id: '423938732'
product: rm
source: tdn-rm
title: Defaults Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938732
version: 3
---

Defaults contábeis são informações padrões definidas para o débito e/ou para o crédito, compondo assim um padrão para a contabilização. Estes defaults ou padrões poderão ser utilizados quando na parametrização de Eventos Contábeis for definido que ao gerar a contabilização de determinada operação o sistema utilize automaticamente nas partidas a serem geradas as informações aqui cadastradas como default.

Cada default informado no débito e/ou no crédito irá gerar uma partida no lançamento da contabilização da operação, onde cada partida receberá o valor correspondente ao percentual informado em cada default.

O sistema é bastante flexível permitindo que se informe, por exemplo, apenas default para o débito ou apenas para o crédito, com ou sem informações gerenciais, ou ainda, que os defaults informados não fechem em 100%. Isto é possível porque no momento da geração da contabilização utilizando um evento contábil o sistema gera as partidas com as informações definidas aqui no default contábil, mas antes de mandar para a contabilidade, permite que o usuário dê manutenções nas informações, sendo possível assim que se ajuste ou informe os dados faltantes.

Exemplo de uma contabilização gerada a partir de um evento contábil parametrizado para utilizar as informações do Default Contábil.

**Cadastro do Default Contábil**

Débito

Conta contábil: 1.1.1.1.001 / Centro de Custo: 01 / 10%

Conta contábil: 1.1.1.1.004 / Conta gerencial: 5.01 / Centro de Custo: 01 / 30%

Crédito

Nenhum dado cadastrado como default.

Valor da operação contábil

R$ 1000,00

**Lançamento gerado pelo sistema**

1ª. Partida a Débito: Conta contábil: 1.1.1.1.001 / Centro de Custo: 01 / Valor R$ 100,00

2ª. Partida a Débito: Conta contábil: 1.1.1.1.004 / Conta gerencial: 5.01 / Centro de Custo: 01 / Valor R$ 300,00

Neste caso o usuário deverá incluir partidas a Débito até completar o valor faltante de R$ 600,00 ou ajustar as partidas que foram geradas automaticamente e deve também incluir o Crédito correspondente, sempre fechando em 100%. Através do botão "Opções" (localizado na barra inferior da janela) é possível visualizar as informações contábeis de Débitos e as de Créditos separadamente ou juntas, conforme sua escolha.
