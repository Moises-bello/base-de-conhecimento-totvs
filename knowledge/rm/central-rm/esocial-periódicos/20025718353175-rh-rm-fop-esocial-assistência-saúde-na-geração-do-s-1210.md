---
article_id: 20025718353175
category: esocial - Periódicos
content_hash: 5f053b479d8da7ad6897b4edbc3ca28cd27115dd8447ad3953d8512c7292f608
fetched_at: '2026-06-28T22:47:09.166476+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Assistência Saúde na geração do S-1210
type: support-article
updated_at: '2025-07-02T18:05:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20025718353175-RH-RM-FOP-eSocial-Assist%C3%AAncia-Sa%C3%BAde-na-gera%C3%A7%C3%A3o-do-S-1210
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23949138145815)Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**  
Como configurar o sistema para correta geração da **Assistência Saúde** (grupos **planSaude** e **infoDepSau**) na geração do evento S-1210 (S-1.2) ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir das versões 12.1.2302.235, 12.1.2306.182, 12.1.2310.116 e superiores  
  
**Solução**

O grupo **planSaude** representa o plano de saúde coletivo e é composto por três informações:

* Dados da **operadora** **de saúde**;
* **Valor do plano** de saúde do **Titular**;
* Grupo **infoDepSau**, onde consta o CPF e valor do plano do **Dependente**, caso haja.

Sendo assim, vamos apresentar em partes as configurações necessárias para correta geração das informações no S-1210 de cada um desses itens:

* **Operadora de Saúde**

1. Acesse o menu **eSocial | Operadora Saúde | Cadastro Operadora de Saúde** e inclua um novo registro;
2. Informe o CNPJ , o nome e o registro ANS da operadora de saúde em questão;
3. Na aba **Eventos da Operadora**, informe a verba utilizada no envelope de pagamento do funcionário. Tal verba deve possuir a natureza de rubrica **9219 - Desconto de assistência médica ou odontológica** para o eSocial e o código de cálculo **14 - Assistência Médica** para a DIRF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20027979440535)

* **Valor do plano de saúde do Titular**

Para geração do plano de saúde do titular (*tag* **vlrSaudeTit**), o sistema irá verificar o **Histórico de Assistência Saúde** e as verbas de **natureza de rubrica 9219** da **Ficha Financeira** do funcionário, apontadas também no cadastro da Operadora de Saúde. Conforme Manual de Orientação do eSocial, a **coparticipação** também deverá ser enviada através da **rubrica 9219** (MOS S-1200 item 13.2). 

* **Grupo infoDepSau (dados do dependente)**

No grupo ***infoDepSau*** serão geradas as informações de dependente de plano de saúde coletivo empresarial: **CPF do dependente** e o **valor** relativo a dedução do rendimento tributável correspondente a pagamento a **plano de saúde do** **dependente**.

Para correta geração no XML, é necessário que:

1. No cadastro do dependente, aba **Incidências**, esteja selecionada a opção Assistência Médica;
2. No cadastro do funcionário, anexo **Históricos | Histórico Assistência Saúde**, esteja discriminado o valor do plano de saúde por dependente.

* **Outras informações importantes**

O histórico de assistência saúde (dependente e/ou titular) poderá ser preenchido de forma automática, utilizando a função de fórmula ***SALVAVALDEP*** ou através de importação de dados. Abaixo segue documentação para auxílio:

* [Parametrização do Plano de Saúde para gravação no histórico (SALVAVALDEP)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009552422)
* [Layout Para Importação de Histórico de Assistência à Saúde](https://tdn.totvs.com/pages/releaseview.action?pageId=452719369)

No caso de **férias**, a fim de evitar a duplicidade de valores gerados no evento S-1210, é importante garantir que a rubrica associada aos eventos em **Eventos do Recibo** e **Eventos da Folha** para assistência médica não seja a mesma, e que as devidas incidências sejam mantidas apenas na verba de natureza 9219. Abaixo segue documentação detalhada:

* [Como cadastrar assistência de saúde nas férias do funcionário para correta geração da incidência no XML S-1210](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20039309735191)

Caso o valor informado no histórico de assistência saúde para o dependente seja menor que o da Ficha Financeira, a **diferença** será gerada para o titular, ainda que não conste informações para o titular no histórico.

Exemplo:

*Envelope do funcionário Edmilson, constando R$100 de assistência médica*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20176301409303)

*Histórico de Assistência Saúde, constando R$50,00 para a dependente Mariane*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20176301415831)

*XML do S-1210, período de apuração 09/2023, constando R$50 para o dependente e R$50,00 (diferença entre o histórico e envelope) para o titular*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20176301421079)

Certifique-se que os dados a seguir estejam **compatíveis entre histórico e ficha financeira**: mês e ano da competência, período, tipo de movimento, evento e data de pagamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20176301434007)

* **XML S-1210**

Abaixo, segue XML de exemplo, com dados gerados pelo sistema após preenchimento do histórico de assistência saúde e cadastro da operadora de saúde:

*Histórico Assistência Saúde*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20258510923031)

*Envelope de Pagamento Agosto/23 com pagamento em Setembro/23*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20258510946071)

*XML do período de apuração 09/2023 (correspondente ao pagamento 05/09/2023), gerando os grupos **planSaude** e **infoDepSau***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20258532746775)

**Importante**  
Para o eSocial, o **plano odontológico** também deve ser informado no grupo ***planSaude***utilizando as mesmas naturezas de rubrica do plano médico. Caso possua dependente de plano odontológico, também deve-se marcar **Assistência Saúde** no cadastro do dependente.

**Saiba mais**  
Para mais informações, acesse:

* [Alterações para atender ao Leiaute S-1.2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18576806660119)
* [Novidades eSocial - Linha RM](https://tdn.totvs.com/display/public/LRM/Novidades+eSocial+-+Linha+RM)

Vídeo do Webinar Tira Dúvidas: **Leiaute S-1.2 - Assistência Saúde, Pensão e Reembolso Médico - Linha RM**
