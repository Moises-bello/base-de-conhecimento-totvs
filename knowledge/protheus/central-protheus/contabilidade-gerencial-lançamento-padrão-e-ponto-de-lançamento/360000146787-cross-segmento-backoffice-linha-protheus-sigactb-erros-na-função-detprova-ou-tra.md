---
article_id: 360000146787
category: Contabilidade Gerencial - Lançamento Padrão e Ponto de Lançamento
content_hash: 9f2011a7b1a669ea9493395fd5c5744b7fdbab638d301ae675c0bd112da9f1f8
fetched_at: '2026-06-28T22:40:34.096588+00:00'
product: protheus
section_id: 1500001549002
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- Erros na função DETPROVA
  ou TRANSLCTA
type: support-article
updated_at: '2023-04-18T12:15:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000146787-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Erros-na-fun%C3%A7%C3%A3o-DETPROVA-ou-TRANSLCTA
---

**Ocorrência**Em qualquer módulo do ERP Protheus, ao tentar realizar o processo de contabilização é apresentada a ocorrência na função DETPROVA ou TRANSLCTA, gerando error.log

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Causa**Erros na função DETPROVA ou TRANSLCTA normalmente são erros de configuração do Lançamento Padrão do cliente. Este é causado devido à informações errôneas dentro do cadastro de integração.  
  
**Solução**

1. Localize em seu system (PROTHEUS) o arquivo ERROR.LOG

2. Abra com um editor de texto e localize pela palavra **CPADRAO.**

**OBS.: CPADRAO** é o código de lançamento padrão que está com problema.

3. Após encontrar, abrir o ERP e localizar no menu do sistema a rotina de Lançamento Padronizado (CTBA080).

4. Realizar a busca do lançamento padrão correspondente ao **CPADRAO** informado no error.log

5. Avalie todos os campos de formula do cadastro de lançamento padrão, seguindo a seguinte sequencia:

a. Verifique se as expressões utilizadas estão corretas

b. Caso esteja utilizando customizações nestes campos, verifique se estão compiladas dentro do seu RPO e/ou se estão habilitadas dentro do cadastro de personalizações (dentro do menu cadastro no configurador (SIGACFG) )

c. Caso esteja referenciando um campo do sistema, verifique se o mesmo está como usado e/ou disponível para utilização.
