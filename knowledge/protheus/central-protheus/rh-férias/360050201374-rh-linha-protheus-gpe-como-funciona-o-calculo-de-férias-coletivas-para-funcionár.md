---
article_id: 360050201374
category: RH - Férias
content_hash: d69a7da8827ba6adb9744c28b52bc654e75b9c0e3c4e7245079e73a2811c9ce8
fetched_at: '2026-06-28T22:43:59.264212+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE -  Como funciona o calculo de Férias Coletivas para
  Funcionários que possuem menos de um ano de empresa, sendo calculado sobre os Dias
  de Férias Coletivas informadas nos parâmetros de cálculo
type: support-article
updated_at: '2025-09-02T17:45:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050201374-RH-Linha-Protheus-GPE-Como-funciona-o-calculo-de-F%C3%A9rias-Coletivas-para-Funcion%C3%A1rios-que-possuem-menos-de-um-ano-de-empresa-sendo-calculado-sobre-os-Dias-de-F%C3%A9rias-Coletivas-informadas-nos-par%C3%A2metros-de-c%C3%A1lculo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30143550199703)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como funciona o calculo de Férias Coletivas para Funcionários que possuem menos de um ano de empresa, sendo calculado sobre os Dias de Férias Coletivas informadas nos parâmetros de cálculo?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Neste cenário, temos duas situações:  
**1.** Funcionário possui **menos** dias de direito em relação aos dias de Férias Coletivas que serão concedidas  
**2.** Funcionário possui **mais** dias de direito adquiridos em relação a quantidade de dias de Férias Coletivas que serão concedidas.  
  
**É importante destacar:**-Nas duas situações haverá [**troca de período aquisitivo**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018992811-RH-Linha-Protheus-GPE-Como-o-sistema-altera-o-Per%C3%ADodo-Aquisitivo-do-Funcion%C3%A1rio-ap%C3%B3s-c%C3%A1lculo-de-F%C3%A9rias-Coletivas) assim que o período da Folha for fechado, gerando assim uma nova linha com o novo período aquisitivo.  
-Validar também como está o conteúdo do parâmetro [**MV\_REFTRAB**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050966774-RH-Linha-Protheus-GPE-Par%C3%A2metro-MV-REFTRAB?source=search)

**-> Funcionamento para Funcionário com menos dias de direito:**  
Na primeira situação, o sistema calcula a quantidade **total** dos dias já **adquiridos** pelo Funcionário e **complementa** o restante dos dias como **Licença Remunerada Mês ou Mês Seguinte** (se houver), que serão demonstradas no cabeçalho de Férias.  
**OBS:** A Licença Remunerada é paga somente na Folha de Pagamento, **não transitando no cálculo de Férias**.   
  
Em um cenário onde o Funcionário possui apenas 12,5 dias adquiridos, e a empresa vai conceder 15 dias de Férias Coletivas, no cálculo serão demonstrados:  
- **Dias Vencidos:** 12,5  
- **Dias de Férias**: 15  
- **Dias de Licença Remunerada (Mês e/ ou Mês Seguinte)**: 2,5

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10169929639703)  
 **-> Funcionamento para Funcionário com mais dias de direito adquirido:**  
No segundo caso, o sistema calcula os dias de Férias Coletivas de acordo com o informado nos parâmetros de cálculo, e deixa o **saldo restante em aberto** no Controle de Dias de Direito.  
  
Em um cenário onde o Funcionário possui 22,5 dias adquiridos, e a empresa vai conceder 15 dias de Férias Coletivas, no cálculo serão demonstrados:  
- **Dias Vencidos**: 22,5  
- **Dias de Férias**: 15

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10169944100759)**

**Saiba Mais:**[RH - Linha Protheus - GPE - Como o Sistema altera o período aquisitivo do funcionário após cálculo de férias coletivas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018992811-RH-Linha-Protheus-GPE-Como-o-Sistema-altera-o-per%C3%ADodo-aquisitivo-do-funcion%C3%A1rio-ap%C3%B3s-c%C3%A1lculo-de-f%C3%A9rias-coletivas?source=search)  
[RH - Linha Protheus - GPE - Como Funciona a Rotina Controle de Dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015671131-RH-Linha-Protheus-GPE-Como-Funciona-a-Rotina-Controle-de-Dias-de-Direito?source=search)  
[RH - Linha Protheus - GPE - Como calcular licença Remunerada nas férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024725433-RH-Linha-Protheus-GPE-Como-calcular-licen%C3%A7a-Remunerada-nas-f%C3%A9rias?source=search)  
[RH - Férias](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597291-RH-F%C3%A9rias)

[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)
