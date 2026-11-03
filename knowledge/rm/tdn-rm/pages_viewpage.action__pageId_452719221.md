---
content_hash: ff93d46984bf4ddbb07303f2b2e10cedabfff40048008fa5b2b1ad127baf0f0a
fetched_at: '2026-06-29T00:10:04.578354+00:00'
page_id: '452719221'
product: rm
source: tdn-rm
title: Configurações Gerais 4/7
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719221
version: 40
---

Nesta aba é possível fazer as Configurações Gerais relacionadas ao eSocial:   
   
**Quantidade de dias anterior ao período de gozo de férias para envio do S-2230 (Máx. 60 dias)**  
Este parâmetro será utilizado no processo Integrar com TAF / Middleware, validando se o início do gozo das férias é superior a data atual do sistema operacional mais a quantidade de dias informado neste parâmetro.

**Atenção:**

* + Quando o valor informado for zero, o sistema irá integrar com o TAF independente da data início do gozo das férias.
  + O valor informado não poderá ser superior a 60 dias, conforme definição no leiaute do eSocial.

Exemplo:  
Quantidade de dias parâmetro: 60  
Data atual 14/08/2024  
   
Neste exemplo as férias iniciam na data do dia 14/10/2024; Ao tentar realizar o envio ao TAF as férias não serão enviadas (será apresentada mensagem de aviso no log) e ficarão pendentes na fila de eventos, com a coluna "Fora do prazo de envio" como "sim".

Observação: Para os afastamentos (eventos S-2230 com tipo de operação Término) o sistema sempre irá considerar 15 dias a partir da data atual para não enviar (será apresentada mensagem de aviso no log) e ficarão pendentes na fila de eventos.

**Quantidade de dias de bloqueio do envio do evento S-2299**  
Este parâmetro será utilizado no processo Integrar com TAF / Middleware, validando se a data da demissão é superior a data atual do sistema operacional mais a quantidade de dias informado neste parâmetro.  
Exemplo:  
Quantidade de dias parâmetro: 9  
Data atual: 01/05/2018  
   
Neste exemplo serão enviadas para o TAF somente as demissões com data até dia 10/05/2018, as demissões a partir desta data não serão enviadas (será apresentada mensagem de aviso no log) e ficarão pendentes na fila de eventos.

**Importante:** 

O Governo já envia automaticamente o comunicado na carteira digital do funcionário após receber o evento**S-2299** ou **S-2399** pelo**eSocial**. Para que não ocorra esta comunicação indevida na carteira digital antes do comunicado formal feito pela empresa, orientamos que seja transmitido o evento **S-2299** ou**S-2399** somente no dia do desligamento ou após a comunicação da empresa sobre desligamento para o funcionário.

**Desconsiderar o campo "Observação" do histórico de afastamento p/ o evento S-2230 exceto para afastamento tipo L - Licença s/Venc.**  
Com este parâmetro marcado ao gerar o XML S-2230 para afastamento diferente de L – Licença s/Venc a tag "Observação" não será impressa.  
Com o parâmetro desmarcado o tag "Observação" será impressa para qualquer afastamento onde o campo observação estiver preenchido no histórico de afastamento.  
   
**Considerar o CID apenas para os motivos de afastamento obrigatórios ("T - Af. Ac. Trabalho" ou "O - Doença Ocupacional") na geração do XML do evento S-2230**  
Em virtude ao Código da Ética Médica, este parâmetro tem o objetivo de ocultar o código do CID no XML do evento S-2230 para os afastamentos que não sejam do Tipo 1 (T - Acidente de Trabalho ou O - Doença Ocupacional).

**Desconsiderar % de redução no cálculo da jornada - MP 936/20 (Integração com TOTVS Automação de Ponto)**

Com este parâmetro marcado ao gerar o XML S-2206 com as informações referentes ao cadastro do B.E.M. o sistema passa a desconsiderar o campo **Percentual de redução da Jornada**na geração da tag <qtdHrsSem>. 

**Gerar gatilho para trabalhador sem vínculo com categorias opcionais**   
O eSocial permite que sejam enviados eventos não periódicos para determinadas categorias de funcionários que não são obrigatórias.

Estes eventos podem ser enviados caso o empregador deseje ter algum tipo de controle sobre esses cadastros.  
   
Ao marcar esse parâmetro, serão gerados gatilhos a cada situação que dispare a necessidade de envio de um evento não periódico para os funcionários de categoria 701, 711, 712, 741 e 903.  
   
Categorias opcionais:

* 701 - Contribuinte individual - Autônomo em geral, exceto se enquadrado em uma das demais categorias de contribuinte individual;
* 711 - Contribuinte individual - Transportador autônomo de passageiros;
* 712 - Contribuinte individual - Transportador autônomo de carga;
* 741 - Contribuinte individual - Microempreendedor Individual.
* 903- Bolsista, nos termos da lei 8958/1994;

Quando o parâmetro estiver desmarcado, não serão gerados gatilhos para funcionários com as categorias mencionadas acima.  
   
É importante lembrar que, os eventos periódicos continuarão sendo gerados normalmente, porém caso possua o evento S-2300 para esses funcionários na fila de eventos, o agrupamento de informações complementares no XML dos eventos periódicos, não será gerado.

Caso não tenha enviado o S-2300 para as categorias opcionais, será incluso um grupo de informações complementares no XML dos eventos periódicos.

**Exemplo:**

Parâmetro **marcado**:

S-2300 = Será gerado

S-1200 = Não conterá <infoComplem>

Parâmetro **desmarcado**:

S-2300 = Não será gerado

S-1200 = Conterá <infoComplem>

**Considerar descrição do horário na tag <dscJorn> dos eventos S-2200 e S-2206**

Com este parâmetro marcado ao gerar o XML dos eventos S-2200 ou S-2206 no leiaute S-1.0 será levado o campo descrição do cadastro de horário para a tag <dscJorn>.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

eSocial

[Parametrizador](http://tdn.totvs.com.br/display/LRM/Parametrizador)
