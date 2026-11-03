---
article_id: 360047003413
category: eSocial - Cadastros
content_hash: bc4b105c81d8775dacd43ccc274dc453884edef343989f216472ee659520659f
fetched_at: '2026-06-28T22:47:14.602566+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: TOTVS RH - Linha RM - eSocial - MP 936 - Suspensão temporária do contrato de
  trabalho
type: support-article
updated_at: '2021-07-22T19:31:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047003413-TOTVS-RH-Linha-RM-eSocial-MP-936-Suspens%C3%A3o-tempor%C3%A1ria-do-contrato-de-trabalho
---

**Dúvida**Como gerar informações ao eSocial sobre a MP 936 que permite ao empregador suspensão temporária do contrato de trabalho de seus empregados pelo prazo de 60 dias que poderá ser fracionado em até dois períodos de 30 dias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - eSocial - A partir dos patchs 12.1.28.101, 12.1.27.167, 12.1.26.212 e 12.1.25.267  
  
**Solução**Para o eSocial as informações a serem enviadas para atender à MP 936 deverão ser levadas nos eventos S-2230 e S-1010/S-1200 com rubrica específica. Para correta geração siga os passos abaixo:  
1. Acesse **Folha de Pagamento |** **Configurações | Parametrizador | Folha de Pagamento | eSocial | De/Para | De/Para de afastamento**e preencha o De/Paracom o tipo de afastamento e motivo que serão vinculados ao funcionário. O campo **Cód. Motivo eSocial** deverá ser o código **37** **Suspensão Temporária do contrato de trabalho nos termos da MP 936****/2020**;

![](https://tdn.totvs.com/download/attachments/545621865/image2020-4-15_20-13-34.png?version=1&modificationDate=1586992414797&api=v2)

1.1. Após a vinculação acima e o cadastro do afastamento no funcionário, o evento **S-2230 - Afastamento Temporário** será gerado com o motivo **37 – Suspensão temporária do contrato de trabalho nos termos da MP 936/2020**;

![](https://tdn.totvs.com/download/attachments/545621865/image2020-4-15_20-21-2.png?version=1&modificationDate=1586992862736&api=v2)

2. Acesse **Folha de Pagamento | Administração de Pessoal | Eventos** e localize o evento destinado ao pagamento de verbas referente à suspensão temporária do contrato;  
2.1. Edite o cadastro do evento e no campo **Natureza da Rubrica (eSocial)** insira a natureza **1619 Ajuda Compensatória MP 936**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066602494/mceclip0.png)

**Importante**  
Deve-se realizar também a **atualização do TAF** para o último pacote acumulado (liberação a partir de 17/04/2020) para correta integração dos eventos com as novas rubricas e código de afastamento.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068012133/mceclip0.png)

O gatilho **S-1010** gerado deverá possuir competência vigente a partir de **04-2020** conforme exemplo abaixo

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067647853/mceclip1.png)

**Saiba Mais**  
Para maiores informações sobre a MP 936 acesse:  
      • [MP 936 - Suspensão temporária do contrato de trabalho](https://tdn.totvs.com/pages/releaseview.action?pageId=545621865)
