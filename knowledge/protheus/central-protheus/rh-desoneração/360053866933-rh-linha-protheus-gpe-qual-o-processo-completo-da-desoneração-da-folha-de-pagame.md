---
article_id: 360053866933
category: RH - Desoneração
content_hash: 355ae1c4d6254a61bcac059705fc2c832a50bd333ab07d1dde35682a9bdef967
fetched_at: '2026-06-28T22:43:42.249645+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Qual o processo completo da Desoneração da Folha
  de Pagamento
type: support-article
updated_at: '2025-03-21T12:24:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053866933-RH-Linha-Protheus-GPE-Qual-o-processo-completo-da-Desonera%C3%A7%C3%A3o-da-Folha-de-Pagamento
---

**Dúvida**Qual o processo completo da Desoneração da Folha de Pagamento?  
  
**Ambiente**TTOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Objetivo deste artigo é orientar sobre o passo a passo relacionado as Configurações para que o Sistema calcule corretamente a Desoneração na Folha de Pagamento.  
  
**1. Configurações dos parâmetros**Via Configurador, na rotina **Parâmetros**, pelo caminho >**Ambiente** >**Cadastros** >**Parâmetros**, parametrize o **MV\_DESFOL** com o **ANO** e **MÊS** de inicio da desoneração da folha de pagamento:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087824014)  
  
**2. Manutenção de Tabela S037**Na rotina **Manutenção Tabelas**, pelo caminho >**Atualizações** >**Definições de Cálculo** >**Manutenção Tabelas**, na **Tabela S037** defina qual tipo de desoneração a empresa se enquadra (Pura ou Mista) e informe na coluna "**Recolhe s/ Fatur**." (**S** ou **M**):

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087828534)  
Para saber quais os tipos de Desoneração consulte nossa documentação [MP - GPE - Quais são os tipos de Desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052977154-MP-GPE-Quais-s%C3%A3o-os-tipos-de-Desonera%C3%A7%C3%A3o-?source=search)  **3. Cadastro de Período**Na rotina **Períodos**, pelo caminho >**Atualizações** >**Definições de Cálculo** >**Períodos**, atente-se ao período da folha/13º que está ativo no cadastro de Períodos, pois o período selecionado que será considerado para o cálculo da desoneração.  
 [![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088972033)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052977154-MP-GPE-Quais-s%C3%A3o-os-tipos-de-Desonera%C3%A7%C3%A3o-?source=search)  
  
**4. Cadastro de Verbas**Para a desoneração, os IDs considerados são:   
ID 0973 - Base provento - Valor > INSS sobre Faturamento  
ID 0148 - Base provento - Valor > INSS parte empresa  
ID 0318 - Base provento - Valor > Salario base

Consulte eles na rotina **Verbas**, pelo caminho >**Atualizações** >**Definições de Cálculo** >**Verbas**,   
  
**5. Cálculo da Folha de Pagamento**Calcule primeiramente a folha de pagamento, para que exista movimento para os funcionários.  
Consulte o cálculo pela rotina **Cálculo por Funcionários**, pelo caminho >**Consultas** > **Cálculos** > **Por funcionários** ou emita o relatório da folha para conferir se o cálculo foi efetuado.  
Sem o cálculo da folha e movimentação de notas nas Filiais envolvidas não é possível efetuar a desoneração.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087829354)  
  
**6. Manutenção de Tabela S033**O Sistema busca os valores para calcular a desoneração de duas formas:   
> **Integração de notas do Faturamento/Financeiro** - Pela integração, a Tabela S033 é populada somente no momento da **execução da desoneração**, onde na desoneração a pergunta Verificar Integração? deve ficar com uma das opções de **2-Faturamento**, **3-Financeiro** ou **4-Ambos**;  
> **Manutenção manual da Tabela S033** - Pelo caminho >**Atualizações** >**Definições de Cálculo** >**Manutenção Tabelas**, na Tabela S033 informe **manualmente** os valores das notas a serem consideradas na desoneração, neste caso, **essa manutenção obrigatoriamente deve ser realizada antes do cálculo da desoneração**.  
  
Para o teste deste documento, foi lançado manualmente a tabela S033:  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088984573)  
  
Para orientação de como informar manualmente os valores na Tabela S033, consulte a documentação a seguir: [MP - GPE - Orientação passo a passo da tabela S033](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052976634-MP-GPE-Orienta%C3%A7%C3%A3o-passo-a-passo-da-tabela-S033?source=search)  
**7. Execute a Rotina de Desoneração da Folha - GPEM013**Na rotina **Desoneração Folha**, pelo caminho >**Miscelânea** >**Cálculos** >**Desoneração Folha**, preencha as perguntas dos parâmetros da desoneração de acordo com a necessidade de cálculo, lembrando que o Sistema buscará o período selecionado no cadastro de Períodos:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087830554)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087830674)  
  
Neste momento a empresa deve verificar se o valor do Faturamento do período virá de integração com o Faturamento/ Financeiro ou se será informado manualmente na tabela S033, os valores pertinentes ao Faturamento do mês.  
  
No log de ocorrência do exemplo deste documento apresentou um percentual de 4.585193% a ser considerado como INSS parte empresa, significa que a empresa teve desoneração mista:  
  
![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088984653)

**OBS.:** Para casos de desoneração Mista, se no log o Sistema apresentar a mensagem que 95% da sua receita é desonerada, será considerado 100% de desoneração, não havendo proporcionalização.  
  
Neste momento caso a empresa tenha rodado a desoneração com integração com o Faturamento/ ou Financeiro, é criado a tabela SV5, onde demonstra todos os valores de notas que entraram na desoneração com o TIPO 1 e as que não entraram com o TIPO 2.

**O log de ocorrências** que é gerado no momento que é executada a rotina de desoneração fica salvo dentro na **pasta spool** dentro da sua **pasta protheus data ,**lembrando que se o mesmo não for renomeado será substituído quando a rotina for executada novamente.  
  
Para verificação dos valores integrados, analise a **Tabela S033** na rotina **Manutenção de Tabelas** que foi populada após rodar a desoneração e criada a tabela SV5.  
  
Para mais informações sobre a desoneração com integração do Faturamento, consulte a documentação [Desoneração da Folha de Pagamento (Faturamento)](https://www.google.com/url?q=https://tdn.totvs.com/pages/viewpage.action?pageId%3D561840577&sa=D&source=hangouts&ust=1599215281751000&usg=AFQjCNFM1ILmzzLUoaRbRP5ugLnAOgb5Mw)     
  
**8. Verificação dos valores na folha de pagamento**Após calcular a folha de pagamento e efetuar o calculo da desoneração não é necessário realizar novamente o cálculo da folha para assumir os valores de desoneração, pois esse processo é realizado durante o cálculo da desoneração. As verbas com Ids 0973 e 0148, já estarão com os valores pertinentes a desoneração, basta efetuar a conferência:

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087841174)  
  
No cenário acima, o Sistema gerou no resumo geral o valor da **Contribuição Devida** da tabela S033 na verba com ID 0973 e calculou a parte proporcional que refere-se ao INSS Parte Empresa, por não ter desonerado 100% - desoneração mista.  
  
Memória de cálculo:  
5.400,00 \* 4.585193% = **247,59**

**OBSERVAÇÔES**- A desoneração é para a empresa e deve ser considerado todas as matriculas que possuem Contribuição Previdenciária. Se atente a somatória dos PROCESSOS da empresa. Exemplo: 00001/ 00003/ 00005;

- Desconsidere as Categorias que não possuem a contribuição previdenciária. Exemplo: Estagiário;

- A desoneração não será efetuada se na Filial que deseja desonerar, não tiver funcionário vinculado, pois depende do cálculo da folha para que seja calculado a desoneração.

- Para que a verba de ID 0973 (INSS Faturamento) seja apresentada no relatório da folha é necessário que  o parâmetro Impr. Total Filial esteja parametrizado com "**SIM**".

**9. Cálculo de Desoneração Rateada por Matrícula**Se a empresa optar em ratear o valor desonerado por matricula deve habilitar o parâmetro MV\_RAT0973.  
Para mais informações, acesse a documentação [RH - Linha Protheus - GPE - Como ratear o valor da desoneração entre os funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008542221)  
  
Para conferencia da verba de desoneração rateada por funcionário, segue documentação [MP - GPE - Como conferir o cálculo da desoneração quando o sistema está definido para ratear o INSS sobre Faturamento ID 0973 na tabela SRC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053045734-MP-GPE-Como-conferir-o-c%C3%A1lculo-da-desonera%C3%A7%C3%A3o-quando-o-sistema-est%C3%A1-definido-para-ratear-o-INSS-sobre-Faturamento-ID-0973-na-tabela-SRC?source=search)**10. Cálculo da desoneração Pura**Se a empresa se enquadra na desoneração Pura, segue link de orientação: [MP - GPE - Cálculo de Desoneração Pura](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053888253-MP-GPE-C%C3%A1lculo-de-Desonera%C3%A7%C3%A3o-Pura?source=search)  
  
**11.Emissão da DARF de desoneração**Após calculada a desoneração da folha de pagamento, e conferido se o resultado está correto na verba com id 0973, deve ser emitida a DARF para o recolhimento da mesma.  
Segue link com as orientações: [MP - GPE - Emissão da DARF de desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053891513-MP-GPE-Emiss%C3%A3o-da-DARF-de-desonera%C3%A7%C3%A3o?source=search)

**IMPORTANTE:** Além do parâmetro MV\_DESFOL, o sistema disponibiliza outros parâmetros para atender as necessidades de cada empresa.  
Consulte os principais parâmetros no link abaixo.  
 [RH - Linha Protheus - GPE - Quais são os principais parâmetros utilizados no cálculo da desoneração?](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg1R%2BDUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1Mzc1MzY1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUXVhaXMtcyVDMyVBM28tb3MtcHJpbmNpcGFpcy1wYXIlQzMlQTJtZXRyb3MtdXRpbGl6YWRvcy1uby1jJUMzJUExbGN1bG8tZGEtZGVzb25lcmElQzMlQTclQzMlQTNvLQY7CFQ6DnNlYXJjaF9pZEkiKTQ4YjBhMmQxLWM4ZTEtNDliZC04NTliLTdlZmNjZGE0ODY0MgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiblJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBRdWFpcyBzw6NvIG9zIHByaW5jaXBhaXMgcGFyw6JtZXRyb3MgdXRpbGl6YWRvcyBubyBjw6FsY3VsbyBkYSBkZXNvbmVyYcOnw6NvPwY7CFQ6EnJlc3VsdHNfY291bnRpAugD--d52ffd397ec6d99dce04db3fd76b9ac52d9814cc)

**Saiba Mais**[Artigos RH -  Desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109152-RH-Desonera%C3%A7%C3%A3o)  
[MP - FAT - Desoneração - Criação da Tabela SV5](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049591434-MP-FAT-Desonera%C3%A7%C3%A3o-Cria%C3%A7%C3%A3o-da-Tabela-SV5?source=search)
