---
content_hash: f8aaa2a85dbbc73e6269bf69a2b19ad896d89889f4b74be55ea490f68b4c685e
fetched_at: '2026-06-29T00:10:50.755795+00:00'
page_id: '562967728'
product: rm
source: tdn-rm
title: Reajuste - Price - Configurando Deságio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=562967728
version: 8
---

Atenção!

O Deságio do PRICE não funciona quando há o componente de ***Resíduo*** no Planos de Financiamento.

Neste cenário, para se calcular o deságio é preciso fazer um **Aditivo de Renegociação** retirando este componente do novo grupo de parcelas para que, neste novo grupo, seja aplicado o deságio.

Clique aqui para entender o **[cálculo realizado no Deságio](https://tdn.totvs.com/pages/releaseview.action?pageId=435105138)**.

Para planos de financiamento PRICE que possuem deságio, e somente neste cenário, é necessário que alguns parâmetros sejam definidos conjuntamente, permitindo o cálculo do deságio em parcelas antecipadas.

No TOTVS Construção Gestão de Imóveis (TCGI), marque o Parâmetro de Deságio, conforme imagem a seguir:

Ainda no TCGI, marque o parâmetro que permite o recálculo para parcelas enviadas a banco, conforme imagem a seguir:

Depois vá até o TOTVS Gestão Financeira (TGF), e marque os seguintes parâmetros para que o cálculo de deságio possa ser realizado na baixa por antecipação, conforme imagem a seguir:

No TOTVS Gestão Financeira será necessário marcar ainda o parâmetro para permitir o reajuste de lançamentos registrados ou remetidos ao banco.

Após a configuração dos parâmetros conforme apresentado o sistema realizará o deságio de parcelas antecipadas corretamente em todos os processos relacionados ao cálculo com deságio.

Para emissão de boletos de antecipação com deságio de parcelas PRICE, é absolutamente necessário marcar os parâmetros apresentados, pois no retorno bancário, precisamos calcular o deságio dessas parcelas através do reajuste.

OBSERVAÇÃO: Se os parâmetros relacionados ao deságio não forem definidos, é necessário desmarcar o parâmetro que utiliza deságio.

O modo de Cálculo de Baixa parcial é obrigatório que seja proporcional, uma vez que prioritário, o sistema irá baixar todo o desconto na primeira baixa, se houver a segunda baixa, irá descontar novamente, sendo que o correto é proporcionar o desconto conforme o percentual de baixa.
