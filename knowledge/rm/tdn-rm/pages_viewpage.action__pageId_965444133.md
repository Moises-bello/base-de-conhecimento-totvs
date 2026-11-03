---
content_hash: 8006c2a8f312fde2e57b837bef054f3d90f997a51ec47681b9f1664458b6d08d
fetched_at: '2026-06-29T00:12:14.092023+00:00'
page_id: '965444133'
product: rm
source: tdn-rm
title: Boleto Híbrido - Dúvidas Frequentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=965444133
version: 7
---

Abaixo apresentamos as respostas a algumas dúvidas que são frequentes em relação ao Boleto Híbrido:

Dica!

O prazo de validade do QR Code PIX do Boleto Híbrido, é de 24hs após a emissão do Boleto Híbrido. Cientes desta Regra de Negócio, segue a sugestão de consulta SQL para tratar os *[Dias Adicionais de Validade (do QRCODE PIX) após o Vencimento](https://tdn.totvs.com/pages/viewpage.action?pageId=908344227#0-1:~:text=Dias%20adicionais%20de%20validade%20ap%C3%B3s%20o%20vencimento%3A)* do Boleto Híbrido:

```
SELECT DAY(DATEADD(DD, - DAY (DATEADD(M, 1, FB.VENCIMENTO)), DATEADD(M, 1, FB.VENCIMENTO))) AS ULTIMODIAMES,
       DAY(FB.VENCIMENTO) DIA,
       (DAY(DATEADD(DD, - DAY (DATEADD(M, 1, FB.VENCIMENTO)), DATEADD(M, 1, FB.VENCIMENTO))) - DAY(FB.VENCIMENTO)+1) QTDE_DIAS
FROM FBOLETO FB (NOLOCK)
WHERE FB.CODCOLIGADA =:FRM_COLBOLETO
  AND FB.IDBOLETO =:FRM_IDBOLETO
```

* **Como parametrizar o relatório do boleto híbrido com código de barras e qr code pix?**

> **Resposta:** Para parametrizar o relatório do boleto híbrido com código de barras e qr code pix siga as instruções da documentação [Cross Segmentos - Backoffice RM - BI - QRCode no RM Reports](https://urldefense.proofpoint.com/v2/url?u=https-3A__centraldeatendimento.totvs.com_hc_pt-2Dbr_articles_360028429732-2DCross-2DSegmentos-2DBackoffice-2DRM-2DBI-2DQRCode-2Dno-2DRM-2DReports&d=DwMFaQ&c=euGZstcaTDllvimEN8b7jXrwqOf-v5A_CdpgnVfiiMM&r=If-DBoguiNTzwo46I6xR9lbYeXSux6j9aF-Ofg2oUro&m=heR6OD0FjrhLZ-4xAFvr2txA9G0ZcaqRgMYnYKyCU_gy5xXbYPn_Ym7e66hMoaOP&s=Ho6L0DXfhSg46oeKBBoUci73ivJovY_w0ursHv7Ebp8&e=):
>
> Basicamente basta criar uma cópia do relatório de boletos atuais e acrescentar o campo com o qr code pix, associando esse campo à uma consulta SQL que referencie o campo QRCODEPIX, da tabela FBOLETO, atualizar o vínculo desta tabela no relatório em questão.
>
> Segue abaixo um relatório de exemplo, onde utilizamos o tamanho de módulo "5", o modo de compactação "byte" e a versão "6",  para tratar o QR Code PIX.

* **É possível cancelar baixa de um lançamento associado a um boleto híbrido para fazer ajustes?**

> **Resposta:** Sim. É possível cancelar a baixa de um lançamento/boleto associado ao boleto híbrido e refazer as correções necessárias.
>
> Após esses ajustes, para baixá-lo novamente, basta executar o processo de Ajuste de Transação, para que o sistema baixe esse lançamento automaticamente.  
> Cientes do que foi explicado acima, recomendamos que o agendamento para o processo de ajuste de transação, tenha um intervalo, que permita ao usuário realizar todos os processos necessários para que essa baixa seja refeita automaticamente pelo sistema.  
> Reforçamos que caso seja necessário quaisquer ajustes na contabilização, pode-se executar o processo para recontabilizar essa baixa, ao invés de desfazê-la.

* **Quando um cliente realiza o pagamento de um boleto híbrido pelo código de barras, esse boleto é baixado de que forma no RM? É preciso executar o Ajuste de Transação do Boleto Híbrido ou o processo do Retorno Bancário?**

> **Resposta:** Quando um cliente realiza o pagamento do Boleto Híbrido por meio do código de barras este título será **baixado automaticament**e pelo processo de **Ajuste de Transação** da Visão de Boleto Híbrido, assim que a compensação bancária deste valor ocorrer.
>
> Ou seja, se houver um agendamento de execução deste processo, o sistema irá baixá-lo automaticamente, assim que o banco compensar esse título.

* **Quando tento gerar um boleto híbrido em uma coligada/filial, o sistema apresenta a exceção abaixo. Como corrigir?**

*****"ProcessorSelectionCriteriaNotFound Não foi possível realizar a transação, por favor verifique os critérios de seleção no painel do RaaS., ProcessorServiceError Houve um erro ao realizar a comunicação com o outro serviço: Não foi possível identificar o critério para a seleção da processadora através da unidade de negócio informada."*****

> **Resposta:** Para corrigir este problema é preciso realizar as ações abaixo:
>
> 1 - Associe o CNPJ da Coligada/Filial à uma conta na [Shipay](https://totvs.wl.shipay.com.br/#/login);
>
> 2 - Acesse a sua página de login a TechFin Pagamentos:
>
> * No menu lateral, acesse a opção Critério de Seleção
> * Clique no botão NOVO
> * Em unidade de negócio, selecione a empresa desejada
> * Em tipo de pagamento, selecione Link/QRCode
> * Em processadora, selecione TOTVS Pagamentos
> * Em modalidade, selecione Boleto Híbrido
> * Em status, selecione Ativo
> * Feito isso, salve o cadastro
>
> Este processo deve ser realizado para todas as unidades de negócios cadastradas no portal TECHFIN PAGAMENTOS.
>
> Segue a documentação deste processo:  
> [Definindo Critério de Seleção](https://tdn.totvs.com/pages/releaseview.action?pageId=628374101)

* **Parametrizei as informações de contas da Coligada/Filial no RAC e gerei um boleto híbrido para uma filial, porém ao executar o processo de Ajuste de Transação, o RM apresenta a exceção abaixo. Como corrigir?**

***"Ocorreu um erro ao solicitar o token de acesso: StatusCode: 400, ReasonPhrase: 'Bad Request', Version: 1.1, Content: System.Net.Http.StreamContent, Headers:  
{  
  Transfer-Encoding: chunked  
  Connection: keep-alive  
  Pragma: no-cache  
  Strict-Transport-Security: max-age=3153600; includeSubDomains  
  X-Cache: Error from cloudfront  
  X-Amz-Cf-Pop: GRUx-P1  
  X-Amz-Cf-Id: WrNjRt5V84-D2FZSwrmOQxCoOhqm7E0mUp9bE0nEWMrxH0hy\_jLQ=  
  Cache-Control: no-store, no-cache, max-age=0  
  Date: Wed, 09 Jul 20  
Via: 1.1 [8330b772be14b6be13c78e1a810de.cloudfront.net](http://8330b772be14b6be13c78e1a810de.cloudfront.net) (CloudFront)  
  Content-Type: application/json; charset=UTF-8  
}."***

> **Resposta:** A mensagem acima é apresentada devido à falta de parametrização das Credenciais para a filial em questão.
>
> Para corrigir, no TOTVS Gestão Financeira, acesse o menu Ambiente > Parâmetros > TOTVS Gestão Financeira > Contas a Receber > Boleto Híbrido e preencha os dados da "Etapa 2 - Configurações por Filial" e preencha as informações solicitadas.

* **É possível configurar o prazo para Protesto do Boleto Híbrido e acompanhar essa ação?**

> **Resposta:** Sim e não.  
> É possível sim, registrar um boleto com informações de protesto, basta preencher as informações na aba *Protesto*, do anexo de *Configurações Adicionais do Boleto Híbrido*, essa informação é enviada ao banco no registro do boleto. No entanto, não há nem no RM e nem na Techfin, um meio de fazer a gestão destes títulos em protesto.  
> Essa ação deve ser realizada à parte de acordo com o processo de cada Cliente.

* **Durante a execução do processo de Registro de Boleto Híbrido, o sistema apresentou a exceção baixo, Como resolve-la?**

**"*Transação: ## Boleto: ####. Erro: ProcessorServiceError Houve um erro ao realizar a comunicação com o outro serviço: {'buyer': {'email': ['Not a valid email address.']}}.*"**

> **Resposta:** O e-mail informado no cadastro do [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=425459224) não é válido. Entre em contato com este cliente e atualize o cadastro de e-mail.
>
> Quando executado para um lote de registros, esta exceção não impede o processamento dos demais registros, sendo registrado no log, apenas os cenários que precisam ser tratados.
