---
article_id: 360058145453
category: RH - Relatórios Folha
content_hash: d744c3ec46281b7368b3754b83d74c8a7a618c654247c05e87a2b8bf9eec5855
fetched_at: '2026-06-28T22:43:17.618057+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema apresenta mensagem de Atenção Falha na
  conexão com o servidor de e-mail The connection failed
type: support-article
updated_at: '2025-07-31T18:39:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058145453-RH-Linha-Protheus-GPE-Sistema-apresenta-mensagem-de-Aten%C3%A7%C3%A3o-Falha-na-conex%C3%A3o-com-o-servidor-de-e-mail-The-connection-failed
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16026473716375) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Sistema apresenta mensagem de **Atenção:** Falha na conexão com o servidor de e-mail *The connection failed*, ao enviar recibo de pagamento (Holerite/Contracheque)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Faça uma nova configuração para servidor de e-mail e realize teste usando este novo servidor.  
  
Segue exemplos de configuração de SMTP  para alguns servidores de e-mail:  
  
**Servidor SMTP:** smtp.terra.com.br:587  
**login do email:** emailteste  
**Senha:** \*\*\*\*\*\*  
**Conta de email:** emailteste@terra.com.br  
**Autenticação requerida:** Sim  
**Utiliza Conexão segura:** Sim  
**Utiliza Conexão segura TLS:** Sim  
  
**Gmail**  
Ao configurar o SMTP do provedor GMAIL, isso esta ocorrendo pois Google criou uma ferramenta de segurança que deve ser ativado no email no cliente para que seja possível o TSS autenticar com esse SMTP, segue abaixo link de configurações necessárias:

<https://tdn.totvs.com/display/tec/Application+Server+-+Uso+de+e-mail+com+GMail>   
  
**Servidor SMTP:** smtp.gmail.com:587  
**Login do email:** emailteste  
**Senha:** \*\*\*\*\*\*  
**Conta de e-mail:** emailteste@gmail.com  
**Autenticação requerida:** Sim  
**Utiliza Conexão segura:** Sim  
**Utiliza Conexão segura TLS:** Sim  
  
**Outlook**  
  
**Servidor SMTP:** pod51028.outlook.com:587  
**login do email:** emailteste@suaempresa.com.br  
**Senha:** \*\*\*\*\*\*  
**Conta de email:** emailteste@suaempresa.com.br  
**Autenticação requerida:** Sim  
**Utiliza Conexão segura:** Sim  
**Utiliza Conexão segura TLS:** Sim  
  
  
**Locaweb**  
  
**Servidor SMTP:** smtplw.com.br:587  
**login do email:** emailteste  
**Senha:** \*\*\*\*\*\*  
**Conta de email:** emailteste@suaempresa.com.br  
**Autenticação requerida:** Sim  
**Utiliza Conexão segura:** Sim  
**Utiliza Conexão segura TLS:** Sim  
  
**Atenção**  
O **sua empresa** é para quem utiliza um **domínio PRÓPRIO da empresa.  
Exemplo:**  [smtp.alexandre.com.br:587](http://smtp.alexandre.com.br:587/)

**Para Saber mais**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)

[RH - Linha Protheus - GPE - Parametrização para envio do recibo e relatórios por e-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010079207-RH-Linha-Protheus-GPE-Parametriza%C3%A7%C3%A3o-para-envio-do-recibo-e-relat%C3%B3rios-por-e-mail)

[RH - Linha Protheus - GPE - Parâmetros usados no envio de E-mail/ Workflow](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10951339224215-RH-Linha-Protheus-GPE-Par%C3%A2metros-usados-no-envio-de-e-mail-workflow)

[RH - Linha Protheus - GPE - Há possibilidade do recibo de pagamento enviado por e-mail conter senha para abertura do arquivo PDF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031791293-RH-Linha-Protheus-GPE-H%C3%A1-possibilidade-do-recibo-de-pagamento-enviado-por-e-mail-conter-senha-para-abertura-do-arquivo-PDF?source=search)

[RH - Linha Protheus - GPE - Como configurar uma mensagem no recibo de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016749491-RH-Linha-Protheus-GPE-Como-configurar-uma-mensagem-no-recibo-de-pagamento?source=search)

[RH - Linha Protheus - GPE - É possível selecionar algumas verbas de base na impressão do recibo de pagamento?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053637593-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-selecionar-algumas-verbas-de-base-na-impress%C3%A3o-do-recibo-de-pagamento-?source=search)

[RH - Linha Protheus - GPE - Impressão recibo de pagamento em lote](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15071538591511-RH-Linha-Protheus-GPE-Impress%C3%A3o-recibo-de-pagamento-em-lote?source=search)

[RH - Linha Protheus - GPE - É possível realizar a impressão de vários períodos de uma única vez do recibo de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034948933-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-realizar-a-impress%C3%A3o-de-v%C3%A1rios-per%C3%ADodos-de-uma-%C3%BAnica-vez-do-recibo-de-pagamento?source=search)

[RH - Linha Protheus - GPE - Como customizar o fonte do recibo de pagamento (RDMAKE para a rotina GPER030)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016654371-RH-Linha-Protheus-GPE-Como-customizar-o-fonte-do-recibo-de-pagamento-RDMAKE-para-a-rotina-GPER030-?source=search)

[RH - Linha Protheus - GPE - Recibo de pagamento em PDF imprime apenas o cabeçalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059487973-RH-Linha-Protheus-GPE-Recibo-de-pagamento-em-PDF-imprime-apenas-o-cabe%C3%A7alho?source=search)

[RH - Linha Protheus - GPE - Como enviar recibo de pagamento e relatórios por e-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012781151-RH-Linha-Protheus-GPE-Como-enviar-recibo-de-pagamento-e-relat%C3%B3rios-por-e-mail?source=search)

[RH - Linha Protheus - GPE - Impressão Recibo de Pagamento - Pergunta "Impressão Correta", para que serve?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270772-RH-Linha-Protheus-GPE-Impress%C3%A3o-Recibo-de-Pagamento-Pergunta-Impress%C3%A3o-Correta-para-que-serve-?source=search)

[RH - Linha Protheus - GPE - Como parametrizar a impressão do recibo de pagamento para matriculas aleatórias?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036175113-RH-Linha-Protheus-GPE-Como-parametrizar-a-impress%C3%A3o-do-recibo-de-pagamento-para-matriculas-aleat%C3%B3rias-?source=search)

[RH - Linha Protheus - GPE - Como configurar o recibo de pagamento para enviar por e-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028985851-RH-Linha-Protheus-GPE-Como-configurar-o-recibo-de-pagamento-para-enviar-por-e-mail?source=search)
