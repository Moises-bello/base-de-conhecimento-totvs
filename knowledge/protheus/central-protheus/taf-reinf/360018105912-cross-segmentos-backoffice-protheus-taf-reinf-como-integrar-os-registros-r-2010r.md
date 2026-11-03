---
article_id: 360018105912
category: TAF - REINF
content_hash: 7eaa2e4bf1aeb571f6bf7627332760ff3119c4ce4468b758ea88eecadde8e69b
fetched_at: '2026-06-28T22:41:33.529434+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Como Integrar os Registros
  R-2010/R-2020
type: support-article
updated_at: '2023-08-23T15:04:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018105912-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-Integrar-os-Registros-R-2010-R-2020
---

**Dúvida**

Em caso de dúvidas na integração do TAF com o **Protheus** verifique os itens abaixo:

**Ambiente**

TAF - REINF - versão 12.1.17 ou superior

**Solução**

**Passo 1 - Escrituração:**

A nota precisa gerar livro fiscal (SF3/SFT), para gerar conteúdo nessas tabelas o Tipo de Entrada e Saída deverá ser configurado conforme o exemplo abaixo:

TES

**Para calcular  e tributar o ISS :**

Calcula ISS(F4\_ISS) = Sim

L.Fiscal.ISS(F4\_LFISS) = Tributado

 

**Para calcular o ISS, e não tributar:**

Calcula ISS(F4\_ISS) = Não

L.Fiscal.ISS(F4\_LFISS) = Outros

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046778994)

ou

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046779074)

 

A nota precisa calcular INSS:

[TOTVS Backoffice Linha Protheus - FIS - Configuração para cálculo de INSS (retenção).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018978571)

Caso a nota já tenha sido gerada, após a alteração, entre na rotina MATA930 e reprocesse o livro fiscal. Caso surgir alguma dúvida no processo de escrituração da nota e rotina de reprocessamento, acionar o suporte do Time Protheus Fiscal da TOTVS.

 

O Código de serviço deve estar vinculado ao produto e a rotina mata963, conforme o link abaixo. 

[Relacionamento de Código de Serviço x Tipo de Serviço - MATA963](https://tdn.totvs.com/pages/releaseview.action?pageId=346488949)

**Passo 2 - Extrator Fiscal e Integração ou TSI:**

**Caso utilize TSI:**[Configuração TSI - TAF Service Integration](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4424759792151-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-configurar-o-TSI-TAF-Service-Integration-)

O extrator fiscal não valida a data de emissão, para levar o documento para o TAF é validado a data de entrada do documento, então se a emissão foi no dia 31/01/2023, mas a nota só entrou no sistema no dia 03/02/2023, além de extrair o mês de Janeiro você deve executar o mês de Fevereiro para que a nota seja levada para o TAF.

Avalie as configurações do Extrator Fiscal, conforme o link abaixo: 

[TAF - Reinf - Configuração Extrator Fiscal para o Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422754983191-TAF-Reinf-Configura%C3%A7%C3%A3o-Extrator-Fiscal-para-o-Reinf?source=search)

Ao gerar o extrator, valide em qual filial a nota foi lançada, pois os eventos Periódicos na REINF não são centralizados, então você precisa selecionar todas as filiais que tiveram movimentação no período. 

 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021088212)

 

Para evitar que ocorra erros de integração, é importante que ao selecionar o Layout T013, seja selecionado os layouts de Cadastros também. A configuração recomendada de extração para Reinf segue abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046780094)

 

 

Efetue o processamento no modulo 84.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027345912)

 

Vá em, Miscelânea, Integração, Processamentos

 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027351211)

 

Configure o processamento conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027351371)

Após o processamento, Valide o gerenciador de integração, caso exista alguma inconsistência na integração.

 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027346492)

 

Deve ser selecionado o dia do processamento.

 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027352011)

 

Na tela a seguir é gerado um ticket, caso ocorra algum erro de integração é gerado com a legenda vermelha.

 

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15975253554711)

Caso a integração ocorra sem erros, é gerado conforme imagens abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027347092)

 

 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027347292)

Caso após as orientações acima o Layout T013 não ser importado pelo Extrator Fiscal, realize a abertura de um chamado com a Equipe TOTVS.
