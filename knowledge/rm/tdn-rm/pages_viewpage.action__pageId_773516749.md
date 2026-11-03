---
content_hash: bc4aa98cfddec8ccf9810f1fdef6405d811fa6962d6ce8d0a6823aa56a00525c
fetched_at: '2026-06-29T00:11:36.775028+00:00'
page_id: '773516749'
product: rm
source: tdn-rm
title: Usar Token para solicitar Autorização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773516749
version: 2
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Configurações**
3. **Utilização**
4. **Estrutura do base64**
5. **Conclusão**

## **01. VISÃO GERAL**

Esta funcionalidade tem como objetivo, preencher a tag **identificadorBeneficiario** do XML de solicitação de autorização para o web service da operadora de saúde, quando utilizar o web service da **Orizon** e somente para os convênios **Bradesco** ou **Mediservice**.

Nesta situação, esta tag deve ser preenchida com um valor convertido em base64, do QrCode da carteira digital, ou das trilhas da carteira magnética.

## **02. CONFIGURAÇÔES**

Para utilizar esta nova funcionalidade, é necessário efetuar algumas configurações no contrato do convênio.

Acessar: Cadastros > Faturamento > Condições contratuais

Na aba Eletrônicos III > aba Geral I, marcar a opção "Usa código validação"

Na aba Eletrônicos III > aba Web Services, verificar se estão preenchidas as URLs da operadora, usuário e senha.

Na aba Eletrônicos III > aba WS Config, marcar a opção "Realiza a integração por web service da Orizon", com o prefixo "ans".

## **03. UTILIZAÇÂO**

Esta funcionalidade foi adicionada nos processos de envio do XML para a operadora, localizado no registro de atendimento.

Acessar: Atendimento > Recepção > Registro de Atendimentos > Criar um novo ou editar um existente.

Depois acessar: Guia / Autorização > Criar ou editar um registro da guia > Processos > Solicitar Autorização.

Nesse momento, se as configurações mencionadas estiverem corretas, exibirá uma tela para que seja informado o token do beneficiário.

Ou o motivo de ausência do token.

Com as opções:

1. Beneficiário internado
2. Beneficiário em situação de urgência/emergência
3. Intermitência/Instabilidade de sistema e regularização do atendimento após saída do beneficiário do prestador de serviço
4. Beneficiário em coleta domiciliar
5. Material para exames enviado ao prestador por terceiros
6. Beneficiário não possui celular

## **04. ESTRUTURA DO BASE64**

Este valor em base64 pode ser gerado de duas formas.

1. Utilizando dados do atendimento e o código do token informado, para gerar os dados do QrCode da carteira digital.
2. Utilizando dados do atendimento para gerar as trilhas contidas na carteirinha magnética.

### QrCode

Utilizando como exemplo o texto contido na leitura do QrCode de uma carteirinha digital.

{QRCODE|999999999999999:847093:-23.50147:-46.855713:0}

Onde:

1. 1. 999999999999999  
      Número da carteirinha
   2. 847093  
      Token
   3. -23.50147:-46.855713:0  
      Geolocalização

O número da carteirinha está localizado no Registro de Atendimento, campo "Cód. Usuário Convênio"

O token foi informado ao solicitar a autorização.

A geolocalização, no caso de informar o token sem efetuar a leitura do QrCode, deve ser informada como "00:00:7", resultando algo similar a:  
{QRCODE|999999999999999:847093:00:00:7}

### Leitura magnética

De acordo com o manual, os dados da carteirinha possuem duas trilhas, onde:

Trilha 1, composta por 79 caracteres alfanuméricos, incluindo sentinela de início e sentinela de término.

Trilha 2, composta por 40 caracteres numéricos, incluindo sentinela de início e sentinela de término.

Utilizaremos como exemplo, as trilhas abaixo efetuadas na leitura magnética em uma carteirinha:

%B9601775035001694005 JAMES ELIAS               27105010211001   ?  
;9601775035001694005=27105010211001000?

Onde:

1. 1. 9601775035001694005  
      Número da conta primária (ou número da carteirinha)
   2. JAMES ELIAS  
      Nome do cliente
   3. 2710  
      Data de validade em AAMM
   4. 501  
      Código do serviço (FIXO)
   5. 0  
      Verificação do PIN (contra senha) (FIXO)
   6. 2110  
      Data de emissão da carteirinha em AAMM
   7. 01  
      Via da carteirinha

Os dados para montar as trilhas são obtidas no registro de atendimento.

Observação.  
Não há no sistema a data de emissão da carteirinha, sendo assim está sendo gerado com "0000".

## **05. CONCLUSÃO**

Como resultado do processamento, teremos informado na tag **identificadorBeneficiario** um valor em convertido em base64.

Como visto acima em "**Estrutura do base64"**, existem duas maneiras de gerar a informação para a tag, com isso, se prioriza o token, ou seja,  
se há um token informado, gera-se o texto do QrCode, senão tentará gerar as trilhas da carteirinha magnética.
