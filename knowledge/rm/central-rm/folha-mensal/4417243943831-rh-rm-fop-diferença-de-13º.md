---
article_id: 4417243943831
category: Folha Mensal
content_hash: c2241b0cbc529c2b2af5545385171de13cb0cbdcea79b0a79bca13e21f26bb6e
fetched_at: '2026-06-28T22:46:59.276473+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Diferença de 13º
type: support-article
updated_at: '2025-01-21T18:40:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417243943831-RH-RM-FOP-Diferen%C3%A7a-de-13%C2%BA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min****Dúvida**Como realizar a parametrização e o lançamento da Diferença de 13º?  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A diferença de 13º salário pode ocorrer quando o funcionário tiver reajuste salarial no mês dezembro e já tiver recebido o 13º com o salário anterior. Esta diferença poderá ser paga na competência dezembro ou janeiro, dependendo do mês de competência em que o usuário se encontra.   
  
1. Primeiramente, será necessário realizar a parametrização do evento de Código de Cálculo 66, conforme competência em que se encontra. Portanto, siga as orientações abaixo:

* **Cálculo da Diferença de 13º na competência de Dezembro**

Ao pagar a diferença de 13º salário no mês de Dezembro o sistema assumirá o evento com [Código de Cálculo 66](https://tdn.totvs.com/pages/releaseview.action?pageId=452718372). Portanto, deverá ser lançado o código de cálculo 66 com incidência em INSS 13º. Para isso, acesse: **Administração de Pessoal | Eventos | Eventos** e verifique se o evento está cadastrado e parametrizado corretamente, conforme imagens abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417221048599/mceclip0.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417227779991/mceclip1.png)

* **Cálculo da Diferença de 13º na competência de Janeiro**

Ao pagar a diferença de 13º salário no mês de Janeiro o sistema assumirá o evento com [Código de Cálculo 66](https://tdn.totvs.com/pages/releaseview.action?pageId=452718372). Porém, deverá ser lançado o código de cálculo 66 com incidência em INSS Folha, dissidio não. Isto acontece porque o provento pago em janeiro participa do cálculo de INSS de Folha e utiliza a tabela de cálculo de INSS de janeiro, ou seja, o recolhimento de INSS será feito juntamente com a folha de janeiro, conforme legislação vigente. O evento deverá incidir também em IRRF 13º salário. Para isso, acesse: **Administração de Pessoal | Eventos | Eventos** e verifique se o evento está cadastrado e parametrizado corretamente, conforme imagens abaixo:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417227980695/mceclip3.png)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417228116887/mceclip4.png)  
  
Ao calcular a diferença em Janeiro se existir alguma média discriminada o sistema irá lançar toda a diferença no evento com o Código de Cálculo 66.  
  
2. Após realizar a parametrização necessário da Diferença de 13º, conforme competência desejada, o lançamento dessa será através do caminho: **Folha Mensal | Diferença de 13º**.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417228348055/mceclip5.png)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417243766423/mceclip6.png)  
  
**Evento de Diferença:** Ao pagar a diferença de 13º salário no mês de Dezembro o sistema assumirá o evento com Código de Cálculo 66 cadastrado no Grupo 0 no campo **Evento de Diferença**, caso o evento não esteja cadastrado o sistema assumirá o 1º evento cadastrado com código de cálculo 66 na tabela de eventos.  
  
**Dissídio:** O campo **dissídio** é marcado **sim** quando o cálculo da diferença for por dissidio. Quando estiver em competência diferente de Dezembro e Janeiro este parâmetro ficará desabilitado, porque nestes meses somente a diferença de 13º por dissidio pode ser paga.  
  
**Permite lançamento de restituição de IRRF 13º:** Marcando esse parâmetro ao recalcular o envelope da 2º parcela de 13º e o valor de IRRF ficar menor que o descontado, o sistema irá lançar a restituição de IRRF de forma automática no processamento da diferença de 13º. Este parâmetro deve ser utilizado antes do envio do valor descontado para receita.  
  
**Importante**

* Para o cálculo de diferença por dissídio de 13º salário deverá ser utilizado o [Código de Cálculo 180 - Diferença de 13º Salário por Dissídio.](https://tdn.totvs.com/pages/releaseview.action?pageId=452718369)
* Para o cálculo de diferença de 13º salário deverá ser utilizado o [Código de Cálculo 66 - Diferença 13º Salário](https://tdn.totvs.com/pages/releaseview.action?pageId=452718372), seja na competência de dezembro ou janeiro. A diferença entre o lançamento da diferença de 13º na competência de dezembro e janeiro seria apenas as incidências dos eventos. Portanto, é necessário a criação de dois eventos de código de cálculo 66, sendo um com incidência em INSS de 13º e o outro com incidência em INSS Folha.
* Não será tratada a emissão da Guia de INSS por dissídio pelo sistema. Esta guia deve ser emitida pelo validador do SEFIP com os códigos de recolhimentos específicos para estes fins, sendo o código de recolhimento de FGTS de dissídio = 650 - Recolhimento ao FGTS e informações à Previdência Social relativo a dissídio coletivo, reclamatória trabalhista ou conciliação perante as Comissões de Conciliação Prévia, no prazo ou em atraso.

**Glossário  
INSS-** Instituto Nacional do Seguro Social**IRRF-** Imposto de Renda Retido na Fonte **FGTS-** Fundo de Garantia do Tempo de Serviço  
  
**Saiba Mais**  
[RH - RM - FOP - 13º Salário: Eventos de diferença de 13 por dissídio não cadastrados no Sindicato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015057451-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-Eventos-de-diferen%C3%A7a-de-13-por-diss%C3%ADdio-n%C3%A3o-cadastrados-no-Sindicato)  
[Diferença de 13º Salário](https://tdn.totvs.com/pages/releaseview.action?pageId=4812466#:~:text=Referente%20a%3A%2037%2C88%20(,)%20%3D%20R%2418%2C94.&text=A%20diferen%C3%A7a%20de%2013%C2%BA%20sal%C3%A1rio%20tamb%C3%A9m%20poder%C3%A1%20ser%20calculada%20quando,o%20valor%20do%20sal%C3%A1rio%20anterior.)
