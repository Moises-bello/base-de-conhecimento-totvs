---
article_id: 360019194451
category: RH - Folha de Pagamento
content_hash: 52e3cdedcacac6ba792e96c745cd2e32dab47bc66ad1d6cd43294ccb62a8e80c
fetched_at: '2026-06-28T22:44:12.021375+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo da folha para Comissionado Puro quando
  possui afastamento
type: support-article
updated_at: '2025-08-12T12:49:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019194451-RH-Linha-Protheus-GPE-C%C3%A1lculo-da-folha-para-Comissionado-Puro-quando-possui-afastamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17471626867479) Tempo aproximado para leitura: **00:02:45 min**

**Ocorrência**Cálculo da folha para Comissionado Puro quando possui afastamento menor do que 15 dias. O sistema carrega a verba de auxilio doença com ID 0041 separadamente da verba de Garantia de Comissão.  
  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - GPE - Todas as versões

**Solução**

Basicamente o Sistema utiliza como base de cálculo

- Cadastro do **sindicato:** Campo **Garantia** **de** **Comissão** (aba Outras Informações)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25432057818519)  
  
- Cadastro do **Tipo de Ausências:** Campo **Número de Meses** para Cálculo de Médias e **Categorias** para Cálculo de Médias

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25432066544535)  
   
- Mnemônicos **P\_PROPCOMS** e **P\_PDMEDAFA**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25283784318103)

Por se tratar de um funcionário **comissionado** sem um salário informado na SRA, o sistema também faz a separação das verbas de pagamento da garantia de Comissão. Caso o valor da comissão seja maior que a garantia de comissão informada no cadastro do Sindicato vinculado ao cadastro do Funcionário, a verba de garantia de comissão (id de cálculo 0347) não será gerada no cálculo.  
  
**Exemplo de cálculo**  
  
Cadastro do sindicato - Garantia de Comissão:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25432057818519)

Lançamento da Ausência:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25432057824535)

Tipo da ausência:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25432066544535)  
  
Cadastro do mnemônico **P\_PROPCOMS**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25432057830167)

Cadastro do mnemônico **P\_PDMEDAFA**- No exemplo o mnemônico está em branco pois só será preenchido caso deseje que outras verbas sem ser de Comissão ou DSR Comissão entre para o cálculo das médias. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25432057832471)

Demonstrativo de média gerado pelo GPER080   
- Como o funcionário tem histórico de médias geramos o Demonstrativo de médias em Relatórios >  Lançamentos > Demonstrativo médias

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25432066566679)**   
Como a soma da Comissão e DSR é superior a Garantia de Comissão o sistema considera somente as médias para o cálculo dos dias de Afastamento.

**Comissão:** R$ 3.125,10  
**DSR Sobre Comissão:** R$ 462,98  
**Garantia de Comissão:** R$ 1.662,00  
**Meses de Média de Comissão (ausência 004)**: 12  
**Médias no relatório:** R$ 3.750,12

**Sistema realiza o seguinte calculo:**

**1º Valor total de Médias / Meses de média de comissão no cadastro da ausência**

R$3750,12/12= R$312,51

**2º Valor de Média / dias de cálculo período**

R$312,51/30= R$10,417

**3º Valor dias \* Dias afastamento**

R$10,417\*4= 41,668 (Arredondando R$41,67)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25432066568727)

**Observação:**

O calculo realizado pelo sistema está de acordo com a orientação da consultoria de segmentos: <https://tdn.totvs.com/pages/releaseview.action?pageId=267808379>

**Saiba mais:**

**[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)**

[RH - Linha Protheus - GPE - Como realizar admissão de comissionado puro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420684082071-RH-Linha-Protheus-GPE-Como-realizar-admiss%C3%A3o-de-comissionado-puro?source=search)

[RH - Linha Protheus - GPE - Como configurar o Sistema para calcular médias no afastamento para funcionários comissionados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058704233-RH-Linha-Protheus-GPE-Como-configurar-o-Sistema-para-calcular-m%C3%A9dias-no-afastamento-para-funcion%C3%A1rios-comissionados?source=search)

[RH - Linha Protheus - GPE - Como considerar outras verbas além de comissão para o cálculo de médias na ausência de funcionário comissionado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8248914155159-RH-Linha-Protheus-GPE-Como-considerar-outras-verbas-al%C3%A9m-de-comiss%C3%A3o-para-o-c%C3%A1lculo-de-m%C3%A9dias-na-aus%C3%AAncia-de-funcion%C3%A1rio-comissionado?source=search)

[RH - Linha Protheus - GPE - Como parametrizar o cálculo de Horas Extras/RSR para Comissionado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012420731-RH-Linha-Protheus-GPE-Como-parametrizar-o-c%C3%A1lculo-de-Horas-Extras-RSR-para-Comissionado?source=search)

[RH - Linha Protheus - GPE - Desconto de faltas e atrasos para comissionado puro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041228333-RH-Linha-Protheus-GPE-Desconto-de-faltas-e-atrasos-para-comissionado-puro?source=search)
