---
article_id: 32766365144087
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: 635cf7348b709b1248db6733dfd8c15708c0ecb6ec4fc411d0715c5d3502791f
fetched_at: '2026-06-28T22:37:49.261112+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Contas a
  Receber - FINA713 - Monitor a registrar para clientes cloud
type: support-article
updated_at: '2025-06-13T14:44:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32766365144087-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Financeiro-Contas-a-Receber-FINA713-Monitor-a-registrar-para-clientes-cloud
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32766365119767) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a transmissão de recebimentos, no Monitor de pendências fica com status "**A Registrar"**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32766330040087)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões homologadas  
  
**Causa**Este incidente ocorre devido à configuração incorreta do sistema para o JOB FINA713, que é o responsável pelo envio das cobranças online.

**Cenários de ocorrência deste erro:**

**1 - JOB CADASTRADO SEM GRUPO DE EMPRESAS**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32767091874071)**

**Documentação**

[Configuração dos Jobs (Comunicação bancaria online)](https://tdn.totvs.com/pages/releaseview.action?pageId=667370586)

**Solução**  
O JOB deve ser configurado com o código do ***Grupo de Empresas*** informado como parâmetro.

Exemplo: Para o grupo de empresas com o código 01, a configuração será: **`FINA713('01')`**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32767091876247)

**Cenários de ocorrência deste erro:  
2 - JOB CADASTRADO COM MAIS DE UMA FILIAL**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32767107421847)**

**Documentação**

[Configuração dos Jobs (Comunicação bancaria online)](https://tdn.totvs.com/pages/releaseview.action?pageId=667370586)  
  
**Solução**  
A configuração dos JOBs deve ser realizada de forma individual por ***Grupo de Empresas***, sendo necessário cadastrar apenas um agendamento para uma única filial.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32767566907671)

**Cenários de ocorrência deste erro:**

**3 - TABELA XX1 COM DUPLICIDADE DA ROTINA FINA713****![](https://centraldeatendimento.totvs.com/hc/article_attachments/32767091878679)**

Em muitos casos, as bases são clonadas e com isso, os dados de outros ambientes são levados para as tabelas de agendamento **(XX0/XX1),** um ambiente que o campo **XX1\_ENV** é diferente, não é apresentado, porém, causa erro no envio da cobrança, pois se trata de uma função que recebe o parâmetro de **Grupo de empresas.**

**Solução**  
Deve-se verificar a existência de outros JOBs cadastrados nas tabelas XX0/XX1 e realizar a remoção dos registros indevidos.

**Cenários de ocorrência deste erro:**

**4 - AGENTE PARADO NO SERVIÇO DE SCHEDULE**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32767091879831)**

Caso esteja sendo utilizado o serviço de fila ***Scheduler*** (e não o novo serviço ***Smart Scheduler***), deve-se verificar no cadastro de agentes se:

* O agente está devidamente cadastrado e inicializado na URL/porta do servidor de *Schedule*;
* O código do agente está configurado para o *Grupo de Empresas* correto.

Segue exemplo abaixo:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32767091881495)**

**Importante**Caso o agente esteja sendo criado para outro **codigo / url do servidor** diferente do seu serviço de **Schedule (Geralmente Porta 6800)**

**Solução**

É necessário excluir o agente existente, certificar-se de que o usuário está devidamente logado no serviço de *Schedule* (WF) e, em seguida, criar um novo agente através do caminho: **Outras Ações > Criar agentes padrões**.  
 **Exemplo de login no WF  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32767091882903)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32767091884823)  
  
Importante**

Caso o ambiente seja **12.1.2410**, deve acessar a URL do Schedule, caso não tenha conhecimento sobre a URL, **solicitar ao CLOUD via atendimento**

**Obs:**Caso o ambiente esteja usando o **SMARTSCHEDULE** não é necessário o uso de agentes

**Cenários de ocorrência deste erro:**

**5 - JOB FINA713 SEM FILIAL CADASTRADA (XX2)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32767091886103)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32767107432343)**

**Documentação**

**[Configuração dos Jobs (Comunicação bancaria online)](https://tdn.totvs.com/pages/releaseview.action?pageId=667370586)**

A configuração dos jobs deve ser única por Grupo de Empresas. sendo necessário cadastrar apenas um agendamento para uma filial.

Exemplo:

Empresa T1

Filiais: D MG 01 , D MG 02 , D RJ 01 , D RJ 02 , D SP 01 , D SP 02

Apenas 1 cadastro de agendamento no schedule para 1 Empresa/Filial para que o schedule execute apenas 1 chamada e fique a cargo do job executar para o grupo de empresas todo.

**Empresa/Filial = T1/D MG 01 ; → Correto**

**Empresa/Filial = T1/D MG 01 ;T1/D MG 02 ;T1/D RJ 01 ; → Incorreto**

**Empresa/Filial = T1; → Incorreto → schedule executa chamada para todas as filiais.**

**Solução**

Deve acessar a rotina e cadastrar uma filial central para que possa executar corretamente.

**6 - LAYOUT DE CONFIGURAÇÃO COM CUSTOMIZAÇÕES INCORRETAS**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32767091889815)**

A configuração de contas em **Novo Gestor Financeiro (FINA710) - Comunicação Bancaria**, pode estar com sintaxes invalidas em **ADVPL** como, **funções, somas, informações de numeros passando virgula, entre outros.****Solução**

Deve-se verificar se há alterações nos campos padrão e, se necessário, ajustá-los para os valores originais. Em seguida, realizar um novo teste. Caso o envio ocorra corretamente, recomenda-se revisar a codificação implementada.

**Cenários de ocorrência deste erro:**

**7 - LAYOUT COM VALOR DE ABATIMENTO VAZIO**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32767107435671)**

**Configuração de Contas >> FINA710 - Comunicação Bancária**  
  
**SOLUÇÃO**

No Protheus, é necessário que o campo **Valor de Abatimento** em alguns bancos seja preenchido, certifique-se que o campo **Valor Abatimento** está preenchido na configuração de contas  
  
**Saiba mais**  
[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)  
[Configuração dos Jobs (Comunicação bancaria online)](https://tdn.totvs.com/pages/releaseview.action?pageId=667370586)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Configuração e Funcionalidade da transmissão de boletos API](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16665077816471-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Configura%C3%A7%C3%A3o-e-Funcionalidade-da-transmiss%C3%A3o-de-boletos-API)
