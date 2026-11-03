---
article_id: 4408149159959
category: esocial - Periódicos
content_hash: 155733d622cdb6fac7c104ae56aa637579552b11c1d60e591fd9b1f14603e736
fetched_at: '2026-06-28T22:47:09.487430+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - S-1200 para autônomos do Gestão Financeira quando
  há desconto de INSS em outra empresa
type: support-article
updated_at: '2024-06-14T15:18:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408149159959-RH-RM-FOP-eSocial-S-1200-para-aut%C3%B4nomos-do-Gest%C3%A3o-Financeira-quando-h%C3%A1-desconto-de-INSS-em-outra-empresa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24180618241943) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como configurar o TOTVS Gestão Financeira para geração de S-1200 de autônomos quando já ocorreu desconto de INSS em outra empresa?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Quando um **autônomo** registrado no **TOTVS Gestão Financeira** possui desconto de INSS em outra empresa, é preciso realizar algumas configurações para que o S-1200 gere corretamente o grupo **infoMV** (Informação de Múltiplos Vínculos). Para realizar essas configurações, siga os passos abaixo:

1. Acesse o cadastro de **Cliente e Fornecedor** no Gestão Financeira ou no Folha de Pagamento;  
1.1. Selecione o autônomo desejado e clique em **Anexos | Múltiplos Vínculos Autônomos**;  
1.1.1. Insira um novo registro informando o CNPJ/CPF e número de inscrição da outra empresa que o funcionário possui vínculo, categoria do funcionário nessa outra empresa, competência que o funcionário teve desconto de INSS, a base de INSS e o valor descontados na outra empresa. Salve o registro;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408149443991)

1.2. Ainda no cadastro do **Cliente e Fornecedor** acesse **Anexos | eSocial**;  
1.2.1. Preencha o campo **Indicador de Desconto da Contribuição Previdenciária do Declarante** considerando a opção **2** quando o autônomo ainda possui INSS a ser descontado ou **3** quando já tiver ocorrido todo o desconto em outro vínculo, não restando desconto a ser realizado no vínculo atual;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408135217943)

1.3. No lançamento financeiro realizado para o autônomo, acesse a aba **Valores | Tributos** e exiba os dados para o cálculo do INSS;

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408149732631)

1.3.1. Na tela que será aberta, preencha o campo **Base de INSS em outra empresa** para que o sistema possa calcular corretamente o **Valor** de **INSS do Empregado;**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408149759255)

2. Ao gerar o XML para o autônomo, o sistema trará o grupo **infoMV** preenchido, além de gerar o grupo **infoPerApur** com a remuneração paga ao autônomo no vínculo atual.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408135596695)

**Importante**  
Para a geração do XML de qualquer autônomo do Gestão Financeira, deve-se primeiramente acessar o menu **Configurações | Parametrizador | eSocial** e preencher os campos das etapas **Autônomos e Externos 1/2** e **Autônomos e Externos 2/2.**  
  
**Saiba mais**  
Para mais informações sobre a geração de S-1200 para autônomo do Gestão Financeira, acesse:  
     - [- Geração do S-1200 e S-1210 para autônomos do Gestão Financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015349532)  
     - [Como gerar as tags de remuneração outro emprego para autônomos do Totvs Gestão Financeira a partir da versão 12.1.26.](https://tdn.totvs.com/pages/releaseview.action?pageId=500293432)
