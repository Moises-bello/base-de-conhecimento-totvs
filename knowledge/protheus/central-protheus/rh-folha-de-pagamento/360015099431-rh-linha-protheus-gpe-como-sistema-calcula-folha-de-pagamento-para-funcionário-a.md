---
article_id: 360015099431
category: RH - Folha de Pagamento
content_hash: 0eb0a8486d1402c60f1e5f76b1d5ac3ee2d2e97cc5a5c23f78c70f56fb29166f
fetched_at: '2026-06-28T22:44:14.801296+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como sistema calcula folha de pagamento para funcionário
  afastado, com MV_DIASPER igual a 2
type: support-article
updated_at: '2025-08-06T17:22:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015099431-RH-Linha-Protheus-GPE-Como-sistema-calcula-folha-de-pagamento-para-funcion%C3%A1rio-afastado-com-MV-DIASPER-igual-a-2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26355778489623) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como sistema realiza o cálculo da folha de pagamento de um funcionário afastado e o parâmetros MV\_DIASPER = 2?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
 **Solução**Conceitualmente sabemos que o pagamento é realizado sempre pelos dias do mês, porém, o Sistema  possibilita a **configuração do cálculo** utilizando **dias** **do** **mês** ou considerando o mês com **30 dias,** através do parâmetro **MV\_DIASPER,** que calculará seguindo os mesmos critérios para **todas** as categorias.

O parâmetro foi criado para atender a necessidade de cálculo por categoria (por exemplo, **horistas**, que devem ser calculados sempre pelos **dias do mês**) e outras por 30 dias mensais (por exemplo, **mensalistas).** Para isso devemos seguir os seguintes passos:  
  
**Exemplos:**

* Processo **00001 – Contribuinte Celetista/Mensal:** no período correspondente ao de cálculo, cadastrar o campo **Dias de Cálculo** (RCF\_DCALCM) igual a **30**.
  + Neste processo **não devem** ser vinculados funcionários **Horistas.** É necessário cadastrar um processo **específico** (00005, por exmplo) a ser usado para funcionários da categoria horista e [transferir os funcionários desta categoria para este processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051970893-RH-Linha-Protheus-GPE-Transfer%C3%AAncia-de-funcion%C3%A1rio-por-processo);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26355794371735)

* Processo **00005 - Contribuinte Celetista/ Horista:**
* no período correspondente ao de cálculo, cadastrar o campo **Dias de Cálculo** (RCF\_DCALCM) igual aos **dias do mês**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26355778499735)

**Observações:** O inicializador padrão do campo **Dias de Cálculo** (RCF\_DCALCM) trará **sempre** os dias do mês preenchido de acordo com a parametrização **MV\_DIASPER:**

Configurado igual a '2' => 30 para todos os meses, exceto fevereiro (nesta ocasião trará 28 ou 29). Configurado igual a '1' => dias do período.

Sugerimos a configuração do inicializador padrão ou gatilho para considerar a diferenciação através dos processos cadastrados.

Para **afastamento** do tipo **4-Controle de Dias de Direito** (RCM\_TIPOAF) será descontado pelos **dias do salário.**

Para os demais será **descontado pelos dias de afastamento.**  
  
**Importante**

Enfatizamos a necessidade de ter um **Processo separado para horistas** com campo **Dias** **de Cálculo** (RCF\_DCALCM) = dias do mês, pois o sistema utiliza a quantidade de dias do campo **Dias Úteis** (RCF\_DUTEIS) para cálculo do **Salário** e o campo **Dias** **DSR** (RCF\_DIADSR) para cálculo do **DSR** nessa categoria, contudo, como divisor será utilizado o campo Dias de Cálculo. Ou seja, para o Horista, o campo RCF\_DCALCM, precisa ser equivalente aos campos RCF\_DUTEIS e RCF\_DIADSR.

Esse conceito **não** é possível ser alterado porque o sistema **não pode desconsiderar** o **dia** **31** sendo que este pode ser Dia **Trabalhado** ou Dia **DSR**.

Além disso, para cálculos de benefícios (VTR, VRF, VAL) podem apresentar inconsistências.

**Saiba Mais**

[TUKE03\_Calculo\_Folha\_de\_Pagamento\_MV\_DIASPER\_Afastamentos](http://tdn.totvs.com/display/PROT/TUKE03_Calculo_Folha_de_Pagamento_MV_DIASPER_Afastamentos)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
