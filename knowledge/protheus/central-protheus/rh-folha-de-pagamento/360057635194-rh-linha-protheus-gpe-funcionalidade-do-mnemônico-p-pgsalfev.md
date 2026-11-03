---
article_id: 360057635194
category: RH - Folha de Pagamento
content_hash: 5c5c7fbcfb80269b64f17b007711a9161dffdc836fd5fba82e1b5d28b38c479a
fetched_at: '2026-06-28T22:44:14.953996+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionalidade do mnemônico P_PGSALFEV
type: support-article
updated_at: '2025-04-15T20:39:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057635194-RH-Linha-Protheus-GPE-Funcionalidade-do-mnem%C3%B4nico-P-PGSALFEV
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26354748482327) Tempo aproximado para leitura: 00:04:00 min**  
**Dúvida**Quais as funcionalidades do mnemônico P\_PGSALFEV?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**O mnemônico **P\_PGSALFEV** era utilizado para alterar os dias de divisão de cálculo na folha de fevereiro.

Tomemos por base o seguinte cenário de exemplo:

P\_PGSALFEV = .T.

Admissão = 20/02/2019.

Salário = 5000,00

Temos

Dias Trabalhados = 28 - 20 + 1 = 9 Dias

5000,00 / 30 \* 9 = 1500,00

Contudo, há o questionamento de que, se são utilizados **30 dias para a divisão**, devem ser considerados 30 dias para a contagem dos dias trabalhados. Com isso, foi feita a **seguinte alteração**.  
  
Com o mnemônico ativado serão considerados 30 dias tanto para a divisão quanto para os dias trabalhados.

**P\_PGSALFEV = .T.**

Admissão = 20/02/2022.

Salário = 5000,00

Temos

Dias Trabalhados = 30 - 20 + 1 = 11 Dias

5000,00 / 30 \* 11 = 1500,00

Caso o mnemônico esteja com **.F.** será realizado o seguinte cálculo.

Admissão = 20/02/2022.

Salário = 5000,00

Temos

Dias Trabalhados = 28 - 20 + 1 = 9 Dias

5000,00 / 28 \* 9 = 1607,14.

**Observação**

Nesse caso, como fica a utilização do mnemônico P\_DIASADM?

R: Nesse cenário, o mnemônico P\_DIASADM não terá efeito, pois já existe o P\_PGSALFEV. Sendo assim, o P\_DIASADM será tratado para meses de 31 dias.

**Saiba Mais**

[Salário Proporcional - Calculo nos meses de 28, 29 e 31 dias Empregado Mensalista](https://tdn.totvs.com/pages/releaseview.action?pageId=631324291#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosTUTP78Sal%C3%A1rioProporcional%E2%80%93C%C3%A1lculonosMesesde28,29ou31dias%E2%80%93EmpregadoMensalistaV3-2.NormasApresentadaspeloCliente)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
