---
article_id: 33534166104215
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 202f15e7782f557a39746f82901af99c0fe9d452c1cc4cc0e5bb775be5608076
fetched_at: '2026-06-28T22:37:56.509728+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Contas a
  Receber - FINA717 - Monitor a registrar não envia pagamentos
type: support-article
updated_at: '2025-07-22T11:42:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33534166104215-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Financeiro-Contas-a-Receber-FINA717-Monitor-a-registrar-n%C3%A3o-envia-pagamentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33534154287255) Tempo aproximado para leitura: **00:10:00 min**  
  
**Ocorrência**  
No módulo Financeiro, ao tentar realizar a transmissão de pagamentos, no Monitor de pendências fica com status "**A Registrar"**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33534512770583)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões homologadas  
  
**Causa**  
Este incidente ocorre devido à configuração incorreta do sistema para o JOB FINA717, que é o responsável pelo envio dos pagamentosonline.

**Cenários de ocorrência deste erro:**

**1 - JOB CADASTRADO SEM GRUPO DE EMPRESAS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33534512771607)

**Documentação**

[Configuração dos Jobs (Comunicação bancaria online)](https://tdn.totvs.com/pages/releaseview.action?pageId=667370586)

**Solução**  
O JOB deve ser configurado com o código do ****Grupo de Empresas**** informado como parâmetro.

Exemplo: Para o grupo de empresas com o código 01, a configuração será: FINA717`('01')`.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33534166045079)

**Cenários de ocorrência deste erro:**  
**2 - JOB CADASTRADO COM MAIS DE UMA FILIAL**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33534166047895)**

**Documentação**

[Configuração dos Jobs (Comunicação bancaria online)](https://tdn.totvs.com/pages/releaseview.action?pageId=667370586)  
  
**Solução**  
A configuração dos JOBs deve ser realizada de forma individual por ****Grupo de Empresas****, sendo necessário cadastrar apenas um agendamento para uma única filial.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33534166048663)

**Cenários de ocorrência deste erro:**

**3 - TABELA XX1 COM DUPLICIDADE DA ROTINA FINA717![](https://centraldeatendimento.totvs.com/hc/article_attachments/33534534627479)**

Em muitos casos, as bases são clonadas e com isso, os dados de outros ambientes são levados para as tabelas de agendamento **(XX0/XX1),** um ambiente que o campo **XX1\_ENV** é diferente, não é apresentado, porém, causa erro no envio da cobrança, pois se trata de uma função que recebe o parâmetro de **Grupo de empresas.**

**Solução**  
Deve-se verificar a existência de outros JOBs cadastrados nas tabelas XX0/XX1 e realizar a remoção dos registros indevidos.

**Cenários de ocorrência deste erro:**

**4 - AGENTE PARADO NO SERVIÇO DE SCHEDULE**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33534166050967)**

Caso esteja sendo utilizado o serviço de fila ****Scheduler**** (e não o novo serviço****Smart Scheduler****), deve-se verificar no cadastro de agentes se:

* O agente está devidamente cadastrado e inicializado na URL/porta do servidor de **Schedule**;
* O código do agente está configurado para o **Grupo de Empresas** correto.

Segue exemplo abaixo:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33534154311447)**

**Importante**  
Caso o agente esteja sendo criado para outro **codigo / url do servidor** diferente do seu serviço de **Schedule (Geralmente Porta 6800)**

**Solução**

É necessário excluir o agente existente, certificar-se de que o usuário está devidamente logado no serviço de **Schedule** (WF) e, em seguida, criar um novo agente através do caminho: **Outras Ações > Criar agentes padrões**.  
  
**Exemplo de login no WF**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33534154312343)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33534166053783)**  
  
**Importante**

Caso o ambiente seja **12.1.2410**, deve acessar a URL do Schedule, caso não tenha conhecimento sobre a URL, **solicitar ao CLOUD via atendimento**

**Obs:**Caso o ambiente esteja usando o **SMARTSCHEDULE** não é necessário o uso de agentes

**Cenários de ocorrência deste erro:**

**5 - JOB FINA713 SEM FILIAL CADASTRADA (XX2)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33534534628631)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33534154314263)**

**Documentação**

[**Configuração dos Jobs (Comunicação bancaria online)**](https://tdn.totvs.com/pages/releaseview.action?pageId=667370586)

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

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33534512782103)

A configuração de contas em **Novo Gestor Financeiro (FINA710) - Comunicação Bancaria**, pode estar com sintaxes invalidas em **ADVPL** como, **funções, somas, informações de numeros passando virgula, entre outros.**  
  
**Solução**

Deve-se verificar se há alterações nos campos padrão e, se necessário, ajustá-los para os valores originais. Em seguida, realizar um novo teste. Caso o envio ocorra corretamente, recomenda-se revisar a codificação implementada.

**Saiba mais**  
[Contas a pagar (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=734394071)  
[Configuração dos Jobs (Comunicação bancaria online)](https://tdn.totvs.com/pages/releaseview.action?pageId=667370586)  
[Job de transmissão dos pagamentos - FINA717](https://tdn.totvs.com/pages/releaseview.action?pageId=772810894)
