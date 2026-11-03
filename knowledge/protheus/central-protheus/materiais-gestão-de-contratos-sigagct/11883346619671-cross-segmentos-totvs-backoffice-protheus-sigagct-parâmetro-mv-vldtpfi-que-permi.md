---
article_id: 11883346619671
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 00a3656d4215dc2f047312826f4d5a0a2e9a3b1686e317fc1a873245290e8cd1
fetched_at: '2026-06-28T22:37:24.012190+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Parâmetro MV_VLDTPFI
  que permite Gerar Contratos diferentes de Fixo a partir de uma Cotação
type: support-article
updated_at: '2023-01-25T11:00:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11883346619671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Par%C3%A2metro-MV-VLDTPFI-que-permite-Gerar-Contratos-diferentes-de-Fixo-a-partir-de-uma-Cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**  
Novo Parâmetro MV\_VLDTPFI que permite Gerar Contratos diferentes de Fixo a partir de uma Cotação  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Solução**O sistema obrigava o usuário a informar um tipo de contrato fixo ao realizar a geração de um contrato através do processo de cotação.

Disponibilizado o parâmetro **MV\_VLDTPFI**, que permite desativar a validação do tipo de contrato, possibilitando a inclusão de um contrato de qualquer tipo durante o processo de cotação.

Para configurar o sistema de maneira que funcione conforme o desejado , será necessário criar o parâmetro **MV\_VLDTPFI** na base local, conforme orientação abaixo.

Acessar o menu configurador do Protheus:

Base de dados→ Dicionário→Base de Dados

![](https://tdn.totvs.com/download/attachments/682437129/image2022-4-25_10-3-14.png?version=1&modificationDate=1650894794977&api=v2)

Na tela gerada, clicar em "Parâmetros" e em seguida no botão "adicionar"

![](https://tdn.totvs.com/download/attachments/682437129/image2022-4-25_10-4-16.png?version=1&modificationDate=1650894794850&api=v2)

Na tela gerada, preencher as informações conforme abaixo

* + Nome de Var. = MV\_VLDTPFI
  + Tipo = Lógico
  + Cont. Por = .F.
  + Descrição = Valida o tipo do contrato durante a geração do contrato oriundo de uma cotação**(.T. = Valida, .F. = Não valida)**

![](https://tdn.totvs.com/download/attachments/682437129/image2022-4-25_10-37-0.png?version=1&modificationDate=1650894794163&api=v2)

![](https://tdn.totvs.com/download/attachments/682437129/image2022-4-25_10-38-24.png?version=1&modificationDate=1650894793963&api=v2)

Após preencher os dados, basta clicar em salvar e em seguida acessar o Protheus para efetuar a inclusão do contrato por meio do processo de análise de cotação.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como gerar contratos no módulo Gestão de Contratos a partir de uma Cotação ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016503491-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-gerar-contratos-no-m%C3%B3dulo-Gest%C3%A3o-de-Contratos-a-partir-de-uma-Cota%C3%A7%C3%A3o-?source=search)

[13692556 DMANMAT02-37888 DT Contrato gerado por cotação flexível](https://tdn.totvs.com/x/CSqtK)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
