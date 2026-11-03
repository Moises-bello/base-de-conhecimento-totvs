---
article_id: 36745889106071
category: RH - Folha de Pagamento
content_hash: 7ae7028be9f92c00c018ce5f7c6a01b9bb17115dcaede5837c3ff9a453718c3d
fetched_at: '2026-06-28T22:44:16.254107+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Redução Gradual da Faixa do IRRF - LEI Nº 15.270
  de 2025
type: support-article
updated_at: '2026-03-16T12:23:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36745889106071-RH-Linha-Protheus-GPE-Redu%C3%A7%C3%A3o-Gradual-da-Faixa-do-IRRF-LEI-N%C2%BA-15-270-de-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36745889093655) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Atualizações sobre a [Lei nº 15.270 de 26 de novembro de 2025](https://in.gov.br/en/web/dou/-/lei-n-15.270-de-26-de-novembro-de-2025-671614220) que trata sobre a dedução progressiva do recolhimento de IR para quem possui rendimentos entre 5.000,01 e 7.350,00.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**

📚Pacote de adequação para atualização do Protheus IRRF 2026:  
🔸12.1.2310:<https://suporte.totvs.com/portal/p/10098/download?e=1123885>(**SOMENTE COM GARANTIA ESTENDIDA**)  
🔸12.1.2410:<https://suporte.totvs.com/portal/p/10098/download?e=1170810>  
🔸12.1.2510:<https://suporte.totvs.com/portal/p/10098/download?e=1221795>  
  
Em atendimento à **Lei nº 15.270, de 26 de novembro de 2025**, foram criados dois novos campos na **tabela S002 – Tabela de Imposto de Renda**, com o objetivo de viabilizar o cumprimento da nova legislação, vigente a partir de **janeiro de 2026**.  
Os novos campos são:

* **Limite Redução**: Neste campo deve ser informado o valor limite que será considerado para aplicação da dedução. Esse valor será comparado com o total de rendimentos sujeitos à tributação, antes das deduções legais.  Atualmente, o valor definido é **R$ 7.350,00**.
* **Índice Redução**: Constante utilizada no cálculo da redução, em conjunto com o Limite de Redução e o total de rendimentos tributáveis do funcionário. Atualmente, o índice definido é **0,133145**.

![image-2025-12-23_15-7-52.png](https://tdn.totvs.com/download/attachments/1019327956/image-2025-12-23_15-7-52.png?version=1&modificationDate=1766513272507&api=v2)

Os campos **Limite de Redução** e **Índice de Redução** devem ser devidamente parametrizados **antes do início dos cálculos**, garantindo que a apuração do **Imposto de Renda** ocorra em conformidade com a legislação vigente **para o ano de 2026**.

A partir da parametrização desses campos, o cálculo do valor da redução será realizado conforme a fórmula abaixo:

**Valor da Redução = (Limite de Redução × Índice de Redução) − (Rendimentos Tributáveis × Índice de Redução)**

Na sequência, serão apresentados **exemplos práticos**, considerando as tabelas de **Imposto de Renda e INSS vigentes**.

**Exemplo 01:**

Rendimentos Tributáveis = 7.000,00  
INSS = 789,60  
Base de IR = 6210,40  
IR (Antes da redução) = ( 6210,40 \* 0,275 ) - 908,73 = 799,13  
Valor da Redução = ( 7350,00 \* 0,133145 ) - ( 7000,00 \* 0,133145 ) = 46,60  
IR após redução = 799,13 - 46,60 = 752,53

**Exemplo 02:**

Rendimentos Tributáveis = 7.400,00  
INSS = 845,60  
Base de IR = 6554,40  
IR (Antes da redução) = ( 6554,40 \* 0,275 ) - 908,73 = 893,73  
\*Não possui redução, pois os rendimentos são superiores a 7350,00

**Exemplo 03:**

Rendimentos Tributáveis = 5.500,00  
INSS = 579,60  
Base de IR = 4892,80 (Considera dedução simplificada - 607,20)  
IR (Antes da redução) = ( 4892,80 \* 0,275 ) - 908,73 = 436,79  
Valor da Redução = ( 7350,00 \* 0,133145 ) - ( 5500,00 \* 0,133145 ) = 246,32  
IR após redução = 436,79 - 246,32 = 190,47

**Observação**: Para criação dos campos da S002 basta aplicar a atualização dos fontes, não sendo necessário executar UPDDISTR.

**Dica**: Para conferência dos valores calculados, recomenda-se a ativação da **memória de cálculo** para visualização das bases utilizadas.  
É **fundamental** a criação de uma **nova linha da tabela de IR** com as novas faixas e preenchimento dos novos campos, mesmo que a receita não efetue qualquer alteração na faixa, para que cálculos de anos anteriores como o dissídio sejam efetuados corretamente.  
Se os novos campos **não forem informados**, o cálculo seguirá da forma **antiga**.

**Importante**

Criação dos novo identificadores de cálculo:   
**1982 – Redução IRRF Folha;**

**1983 - Redução IRRF Férias;**

**1984 - Redução IRRF 13° Salario;**

**1985 - Redução IRRF Adiantamento.**  
Nessa verba, quando existente, será registrado o valor da redução calculado pelo sistema, conforme a fórmula apresentada anteriormente.  
A verba deverá ser criada como **Base de Desconto**, sem qualquer incidência de cálculo.  
Na aba **eSocial**, configurar com **Natureza 9989**, **Incidência CP 00**, **Incidência IRRF 9** e **Incidência FGTS 00**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37776226940951)

A **tabela de IRRF permanece inalterada**, conforme definida pela legislação vigente. Não houve substituição da tabela nem mudanças em suas faixas ou alíquotas. **A eventual redução do valor descontado ocorre exclusivamente em função do coeficiente aplicado no cálculo.**

📚Documentação sobre esta implementação:  
🔸<https://tdn.totvs.com/pages/releaseview.action?pageId=1019327956>

**Saiba Mais:**

[Orientações Consultoria de Segmentos](https://tdn.totvs.com/pages/releaseview.action?pageId=1019343450)

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Cadastro tabela S002 - IR 2026](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37059229342871-RH-Linha-Protheus-GPE-Cadastro-tabela-S002-IR-2026)

[RH - Linha Protheus - GPE - Geração da Memória de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057115114-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-da-Mem%C3%B3ria-de-C%C3%A1lculo)
