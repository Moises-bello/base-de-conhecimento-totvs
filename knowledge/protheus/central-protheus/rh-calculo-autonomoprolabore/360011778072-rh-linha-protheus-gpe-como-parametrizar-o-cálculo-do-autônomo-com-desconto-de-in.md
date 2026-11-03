---
article_id: 360011778072
category: RH - Calculo Autonomo/Prolabore
content_hash: 5e2005191142085fa05894ff18c3b0363d19f1e3207c3eb5734bad8263f7f39b
fetched_at: '2026-06-28T22:43:15.158634+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar o cálculo do autônomo com desconto
  de INSS retido por outro empregador
type: support-article
updated_at: '2025-04-15T17:45:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011778072-RH-Linha-Protheus-GPE-Como-parametrizar-o-c%C3%A1lculo-do-aut%C3%B4nomo-com-desconto-de-INSS-retido-por-outro-empregador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26249825365143) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como parametrizar o cálculo do autônomo com desconto de INSS retido por outro empregador -  **GPEM020**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 11.80  
  
**Solução**Embasamento teórico - Legislação:trabalhador avulso - Portaria nº3107, de 7/04/71: Entende-se como trabalhador avulso, no âmbito do sistema geral da previdência social, todo trabalhador sem vínculo empregatício que, sindicalizado ou não, tenha a concessão de direitos de natureza trabalhista executada por intermédio da respectiva entidade de classe.  
Com a edição da Lei nº 5890/73 o trabalhador avulso foi integrado no sistema previdenciário na condição de autônomo.  
  
Tratativa do sistema **Protheus**:Para parametrizar o cálculo do autônomo deverá ser seguido os seguintes passos:  
  
- No exemplo abaixo iremos demonstrar o cálculo do salário de um autônomo com o lançamento dos valores de INSS recolhidos por outra empesa.  
  
- Para tratamento do cálculo do INSS de funcionários com mais de um vínculo empregatício devem ser utilizados os seguintes identificadores:  
**0288- Base Inss Outras Empresas ( Verba Tipo Base);**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26249833559319)  
  
**0289- INSS Outras Empresas (Verba Tipo Base);**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26249825368983)  
  
**0290- Base Inss 13o. Outras Empresas ( Verba Tipo Base);**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26249833561623)  
  
**0291- INSS 13o. Outras Empresas (Verba Tipo Base);**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26249833563159)  
  
Acesse o **Cadastro de verbas** (**GPEA040)** em **Atualizações > Cadastros > Verbas (GPEA040)** e atrele a uma verba os identificadores de cálculo conforme descritos acima.   
  
Acesse a rotina Manutenção de tabelas em **Atualizações > Definições de Cálculos > Manutenção tabelas (GPEA320) >** selecione **a tabela S037 e** clique em **Incluir** se não houver informações na tabela ou **Outra Ações > Alterar** se já existir informações na tabela**:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26249825378583)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26249825381399)  
  
Acesse o **cadastro de autônomos** através **GPEA265** - **Atualizações > Funcionários > Contribuinte Individual (GPEA265):**  
- Verificar também o campo **Calculo INSS** (**RA\_INSSAUT**), que permite efetuar tratamento para cálculo do INSS dos funcionários autônomos e estrangeiros, incluindo o cálculo patronal, cujos países de origem possuam acordo com o Brasil.   
Obs.: Na versão 12 o campo **RA\_INSSAUT**, fica na aba Estrangeiro.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26249825385623)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26249825388311)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26249833588759)  
  
Acesse a rotina Lançamentos por Funcionários em **Atualizações > Lançamentos > Por Funcionários (GPEA580)** e lance as verbas criadas com os id's 0288 e 0289 o valor base e desconto do INSS recolhido na empresa onde o autônomo prestou serviço:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26249825404183)  
  
Execute o cálculo da **folha de pagamento em** **Miscelânea > Cálculos > Por Roteiro (GPEM020):**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26249825405719)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26249833596055)  
  
Acesse a rotina Lançamentos por Funcionários em **Atualizações > Lançamentos > Por Funcionários (GPEA580)Selecione o funcionário > Visualizar > Outras ações > Consultar Cálculo** para verificar o cálculo realizado **![](https://centraldeatendimento.totvs.com/hc/article_attachments/26277976920983)**Resumo de cálculo:

Verba 191= é o valor informado no campo RA\_SALARIO  
Verba 705= A soma das verbas com incidência para IR, neste caso apenas a verba 191=  R$2200,00  
Verba 747 = Corresponde a 20% (de acordo com o que foi configurado na rotina manutenção tabelas) sobre as verbas com incidência para INSS, neste caso a verba 191= R$2200,00  
Verba 786 = Base de INSS autônomo/prolabore sobre as verbas com incidência para INSS, neste caso a verba 191= R$2200,00  
Verba 713 = Valor líquido a receber, neste caso como houve descontos de INSS na folha o valor será de R$1958,00.  
Verba 836 = Valor base da verba que gerou o desconto de INSS na empresa onde o autônomo prestou serviço.  
Verba 837 = Valor do desconto de INSS recolhido na folha do autônomo na empresa onde o mesmo prestou serviço.  
  
**Saiba mais**  
[Como parametrizar o calculo de Autonomo com desconto de INSS retido por outro empregador](http://tdn.totvs.com/pages/viewpage.action?pageId=235580406)

[Manual de cálculo Multiplos Vinculos](https://tdn.totvs.com/pages/releaseview.action?pageId=552575179#ids-id3)

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
