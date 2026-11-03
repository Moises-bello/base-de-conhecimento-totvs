---
article_id: 28342402593943
category: RH - Férias
content_hash: 1c4ebbc5c2e3ef4aeb624e7ba51340d9bee146991ccee565b68c569d2f3e3f9f
fetched_at: '2026-06-28T22:43:58.310271+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: 'RH - Linha Protheus - GPE - Mensagem ao calcular férias coletivas: O saldo
  de férias que restará é inferior a 5 dias. Conforme Artigo 134 parágrafo 1º da CLT,
  as férias não devem ser concedidas com menos de 5 dias.'
type: support-article
updated_at: '2025-08-06T17:03:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28342402593943-RH-Linha-Protheus-GPE-Mensagem-ao-calcular-f%C3%A9rias-coletivas-O-saldo-de-f%C3%A9rias-que-restar%C3%A1-%C3%A9-inferior-a-5-dias-Conforme-Artigo-134-par%C3%A1grafo-1%C2%BA-da-CLT-as-f%C3%A9rias-n%C3%A3o-devem-ser-concedidas-com-menos-de-5-dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28342402573335) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao calcular férias coletivas é gerado log com a mensagem:  
O saldo de férias que restará é inferior a 5 dias. Conforme Artigo 134 parágrafo 1º da CLT, as férias não devem ser concedidas com menos de 5 dias.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28343123872279)  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões   
  
**Causa**A mensagem é gerada e o cálculo não é executado, pois restará um saldo inferior a 5 dias, ficando em desacordo com o Artigo 134 da CLT.

[Implementações da reforma trabalhista](https://tdn.totvs.com/pages/viewpage.action?pageId=312149147)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28342386903959)

**Exemplo de cenário**

-Funcionário foi admitido em 01/06/2024 e possui um saldo de férias proporcionais.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28343123877527)  
  
-A empresa irá conceder 15 dias de férias coletivas a partir de 20/12/2024.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28343123880983)

-Ao realizar o cálculo é gerado a ocorrência e o cálculo não é executado, pois em 20/12/2024 o funcionário já terá direito a 17,5 dias de férias e restariam apenas 2,5 de saldo (funcionário com menos de um ano)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28343123872279)

**Solução**A mensagem será apresentada quando o saldo restante for inferior 5 dias, portanto a empresa deve avaliar como deverá ser executado o cálculo e quantidade de dias de férias.  
  
A empresa pode avaliar também se é viável desabilitar as regras de cálculo de férias via parâmetro MV\_REFTRAB, deixando-o com o conteúdo SRI (Conteúdo padrão: FSRI).

#### [Implementações da reforma trabalhista](https://tdn.totvs.com/pages/viewpage.action?pageId=312149147)

**Saiba Mais**

[RH - Linha Protheus - GPE - Como calcular férias coletivas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000101721-RH-Linha-Protheus-GPE-Como-calcular-f%C3%A9rias-coletivas)  
[RH - Linha Protheus - GPE - Como considerar os dias 24/12, 25/12, 31/12 e 01/01 como Licença Remunerada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024725433-RH-Linha-Protheus-GPE-Como-considerar-os-dias-24-12-25-12-31-12-e-01-01-como-Licen%C3%A7a-Remunerada?source=search)  
[RH - Linha Protheus - GPE -  Como funciona o calculo de férias coletivas para funcionários que possuem menos de um ano de empresa, sendo calculado sobre os Dias de Férias Coletivas informadas nos parâmetros de cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050201374-RH-Linha-Protheus-GPE-Como-funciona-o-calculo-de-f%C3%A9rias-coletivas-para-funcion%C3%A1rios-que-possuem-menos-de-um-ano-de-empresa-sendo-calculado-sobre-os-Dias-de-F%C3%A9rias-Coletivas-informadas-nos-par%C3%A2metros-de-c%C3%A1lculo)
