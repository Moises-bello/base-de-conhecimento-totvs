---
article_id: 360035045193
category: RH - Folha de Pagamento
content_hash: 0329ccde9bc55b7f2d19bf4b713cc91def4034bf75115053b6145ee3c8f833a3
fetched_at: '2026-06-28T22:44:11.938555+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE -  Tratar Repositório de Fórmulas com Balance
type: support-article
updated_at: '2025-08-22T19:33:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035045193-RH-Linha-Protheus-GPE-Tratar-Reposit%C3%B3rio-de-F%C3%B3rmulas-com-Balance
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26326996937495)  Tempo aproximado para leitura: **00:02:00 min****Dúvida**Sempre que recriamos o **RPO** de formulas em meu ambiente com Balance, o sistema apresenta erro de falha de compilação em diversos roteiros.   
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - GPE – Todas as versões  
  
**Solução**Por padrão, a pasta com o repositório de fórmulas e roteiros do SIGAGPE é **criada** no **mesmo** **diretório** definido ***SOURCEPATH*** do appserver.ini. Com a utilização de ***balance,*** cada *slave* pode possuir um um SOURCEPATH diferente, criando um repositório de fórmulas/roteiros diferente para cada *slave,* dificultando o processo de atualização, que teria que ser feito duplicando manualmente os repositórios.

**Atenção:**

1. Para os ambientes com configurações de Balanceamento de carga *(Balance)* com mais de 1 servidor físico o diretório de formulas deverá ser direcionado para a mesma pasta e neste caso deverá ser configurado utilizando o caminho da rede.

**Exemplo:**

[P12BALANCEDGRID]

FORMPATH=\\IP(caminho)\Protheus12\apo\_balanced **< Informar aqui o caminho para gravação do seu RPO de fórmulas>**

2. Se existir mais de um ambiente porem apontando para o mesmo TOPALIAS (banco de dados) o caminho do FORMPATH deve ser igual.

   
**Exemplo:**

* **1º Ambiente:**

[P12BALANCEDGRID]

TOPALIAS=P12\_BANCODEDADOS

FORMPATH=C:\Protheus12\apo\_balanced **< Informar aqui o caminho para gravação do seu RPO de fórmulas>**

 

* **2º Ambiente:**

[P12BALANCEDGRID\_HOMOLOG]

TOPALIAS=P12\_BANCODEDADOS

FORMPATH=C:\Protheus12\apo\_balanced **< Informar aqui o caminho para gravação do seu RPO de fórmulas>**

 

* **3º Ambiente:**

[P12BALANCEDGRID\_DESE"]

TOPALIAS=P12\_BANCODEDADOS

FORMPATH=C:\Protheus12\apo\_balanced **< Informar aqui o caminho para gravação do seu RPO de fórmulas>**

* **4º Ambiente:**

[P12OUTROS]

 TOPALIAS=**OUTROBANCODEDADOS**

 FORMPATH=D:\outros\APO\_OUTROs **< Informar aqui o caminho para gravação do seu RPO de fórmulas>**

**Observações**

- Somente no **4º exemplo** o banco é **diferente** então o caminho do FormPath deve ser diferente.

- A regra da chave FormPath deve ser configurada em **todos** appserver.ini.

Como boa prática orienta-se**não** realizar a configuração de Repositórios transitando pela rede, porém para o caso especifico de **formulas,** é necessário a existência de apenas **um único repositório** (RPO). Quanto à performance, o impacto será mínimo devido ao tamanho (pequeno) do RPO de fórmulas.

**Saiba Mais**

[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)

[Documentação Técnica - Repositório de Fórmulas com Balance](https://tdn.totvs.com/pages/viewpage.action?pageId=208345362)

[RH - Linha Protheus - GPE - Como configurar o GRID para cálculos do GPE](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXxbsgAQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDI4OTA2NTQ5OTktUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY29uZmlndXJhci1vLUdSSUQtcGFyYS1jJUMzJUExbGN1bG9zLWRvLUdQRQY7CFQ6DnNlYXJjaF9pZEkiKTVhYjM0OTk3LTNlYmEtNDE3MS1hYWRlLTI1MWVhNTFiNTE0NwY7CEY6CXJhbmtpCToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDXJwbyBncmlkBjsIVDoScmVzdWx0c19jb3VudGkBkg%3D%3D--ee0938790dc46cc720f48f179d9f69bc407045b6)

[RH - Linha Protheus - GPE - Como executar cálculos da folha de pagamento sem customizações (mnemônicos, roteiros, fórmulas e pontos de entrada)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgIkMXSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB5Gh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxODQ0ODM5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1leGVjdXRhci1jJUMzJUExbGN1bG9zLWRhLWZvbGhhLWRlLXBhZ2FtZW50by1zZW0tY3VzdG9taXphJUMzJUE3JUMzJUI1ZXMtbW5lbSVDMyVCNG5pY29zLXJvdGVpcm9zLWYlQzMlQjNybXVsYXMtZS1wb250b3MtZGUtZW50cmFkYQY7CFQ6DnNlYXJjaF9pZEkiKWVhYWJhNWI4LTkwMmMtNDNlMi1iYzMwLTU3MDgzMTllMzgyZQY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDGJhbGFuY2UGOwhUOhJyZXN1bHRzX2NvdW50aQs%3D--b7e22890b9b0fae7acf0d2b7a153e99239aef74a)
