---
content_hash: 6138fda47b674ec26d85224a87ed7845e14bfce55fb74815d1f1a503f4cd916b
fetched_at: '2026-06-29T00:11:04.481561+00:00'
page_id: '627729108'
product: rm
source: tdn-rm
title: 'S-1200 e S-1210: Recibo de Férias no leiaute S-1.0'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=627729108
version: 20
---

false

**A partir das Versões:**

* 12.1.29.278
* 12.1.31.193
* 12.1.32.131
* Ou superiores
1true1ObjetivoObjetivo

Apresentar os tratamentos que foram realizados na geração dos eventos S-1200 e S-1210 conforme MOS da versão S-1.0 referente ao recibo de férias.

2ParametrizaçãoParametrização

Será necessário realizar a associação de eventos no "De/Para eventos férias eSocial (S-1200)" no Parametrizador | eSocial | Configurações Gerais 6/7 e Parametrizador | eSocial | Configurações Gerais 7/7, conforme exemplo abaixo:

Informações da parametrização [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=645896860)

3GeraçãoGeração

Exemplo do processo de férias no produto de folha de pagamento:

1) Cadastrar e Lançar as férias

Recibo de Férias

2) No envelope de pagamento será lançado os eventos referentes ao recibo de férias e a verba de dias trabalhados:

3) Ao gerar o xml do evento S-1200 serão gerados dois grupos <DmDev>, sendo um com a tag <ideDmDev> conforme o número do envelope de pagamento e outro <ideDmDev> conforme recibo de férias (o numero do ideDmDev será da data de pagamento das férias).

<ideDmDev> conforme envelope de pagamento, eventos de IRRF e base de INSS serão substituidos pelos eventos cadastrados no parametrizador.

<ideDmDev> com a data de pagamento conforme recibo de férias e eventos colocados no parametrizador 

**Atenção:**

* Caso possua eventos de médias no recibo de férias esses eventos serão somados aos eventos de antecipação de férias.
* Caso utilize tomador de serviço o recibo de férias será gerado para o tomador empresa.

4) Ao gerar o evento S-1210 será gerado o líquido correspondente ao dois recibos.
