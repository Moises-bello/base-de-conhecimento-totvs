---
article_id: 360050701833
category: RH - Provisão
content_hash: 7d2e6aa037ec394fb11fc056a79f4945667bef222ecd7da9549102355f1ef2b4
fetched_at: '2026-06-28T22:43:55.712664+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Calcular as Provisões de Férias com o adiamento
  do valor de de 1/3 - Medida Provisória 927 (MP-927)
type: support-article
updated_at: '2025-08-21T12:45:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050701833-RH-Linha-Protheus-GPE-Como-Calcular-as-Provis%C3%B5es-de-F%C3%A9rias-com-o-adiamento-do-valor-de-de-1-3-Medida-Provis%C3%B3ria-927-MP-927
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34341367846935) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como realizar parametrização do cálculo de Provisão de Férias para atender o adiamento do valor de 1/3 conforme MP 927, mas demonstrando o valor à ser pago futuramente?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**Foi efetuado o procedimento para **adiar o pagamento do 1/3 de férias** no cálculo de férias do funcionário, conforme documentação disponível [aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045596313). Ao efetuar o **cálculo de provisão de férias**, o valor do **1/3 de férias não é mais demonstrado no relatório**. Da mesma forma, a baixa desse valor também não era gerada quando da quitação na folha de pagamento, através da geração do valor pela rotina **PGTFER927**, de acordo a este [tutorial](https://tdn.totvs.com/x/cvTAI).

Para que na situação acima o saldo do valor do 1/3 de férias adiado seja mantido na conta até o seu efetivo pagamento na folha, foi feito uma alteração no cálculo da provisão e foi disponibilizado um arquivo .prx de exemplo contendo a implementação dos pontos de entrada **GP070P13**, **GP070COD** e  **GP070FBX**.

Para implementar a solução, siga o passo a passo:  
  
1. Aplique o Pacote de Atualização abaixo:

12.1.2210: <https://suporte.totvs.com/portal/p/10098/download#detail/1080347>   
Importante: Aplique-o primeiro em base teste e faça um Backup do RPO antes.

2. Para Baixar o arquivo .prx que contém o exemplo da implementação dos pontos de entrada [Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=552107654&preview=/552107654/552107801/exemplo.prx) ;  
  
3. O arquivo deverá alterado conforme necessidade e compilado no RPO, não é necessário cadastrá-lo no menu pois o arquivo somente contém implementações de pontos de entrada.

**Informação**  
Cada ponto de entrada possui uma finalidade diferente:

* **GP070P13:**irá retornar o valor de 1/3 de férias adiado para o saldo da provisão.
* **GP070COD:**por padrão, o sistema somente considera as verbas dos IDs de cálculo 0077, 0079, 0090 e 0095 para efetuar a baixa de 1/3 de férias. Com o ponto de entrada, será possível considerar a verba gerada na folha através da rotina **PGTFER927**.
* **GP070FBX:**por padrão, o sistema somente verifica e realiza a baixa de férias em período que o funcionário está de férias. Como a quitação do 1/3 de férias na folha poderá ocorrer em período que o funcionário não está de férias, o ponto de entrada irá forçar a verificação da baixa mesmo nesse período.

Dessa forma, quando o sistema efetuar o cálculo da provisão de férias, através da execução do ponto de entrada **GP070P13** será efetuado uma validação para buscar o valor da verba de base de 1/3 de férias adiado gerado no cálculo de férias e esse valor será retornado ao saldo da provisão de férias. Isso ocorrerá a partir do cálculo de férias que teve o 1/3 de férias adiado até o período em que ocorrer a quitação do 1/3 de férias na folha.

Quando for efetuado a quitação do 1/3 de férias adiado na folha, através do ponto de entrada **GP070COD**será adicionado o código da verba da folha para que o sistema efetue a baixa desse valor na coluna de 1/3 de férias. E, através do ponto de entrada **GP070FBX**, o sistema irá verificar e efetuar a baixa do 1/3 de férias mesmo em período em que o funcionário não esteja de férias, pois por padrão não ocorre essa verificação para evitar processamento desnecessário.  
  
 **Importante:** Conforme explicado acima, os pontos de entrada irão alterar o cálculo da provisão. Dessa forma, caso seja necessário recalcular as provisões, antes de realizar tal procedimento, deverá ser avaliado os impactos na **Contabilização das Provisões** dos períodos anteriores, mas vale lembrar que os valores de 1/3 de Férias serão ajustados nos cálculos de provisão do mês atual de forma automática, não sendo necessário reprocesso de períodos anteriores.  
  
**Saiba Mais**Para adquirir mais conhecimentos acesso o(s) *link*(s) abaixo:  
[8581039 DRHPAG-35723 DT Cálculo e baixa de 1/3 de férias na provisão quando o 1/3 não foi calculado nas férias devido MP 927](https://tdn.totvs.com/pages/releaseview.action?pageId=552107654)
