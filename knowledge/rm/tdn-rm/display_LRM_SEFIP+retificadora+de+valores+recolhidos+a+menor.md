---
content_hash: 3f0dd248ec4541c1f3145fe73d856eb6ae5d50c1464e653811441ad1190aa1da
fetched_at: '2026-06-29T00:05:55.141749+00:00'
page_id: '126191698'
product: rm
source: tdn-rm
title: SEFIP retificadora de valores recolhidos a menor
type: documentation
url: https://tdn.totvs.com/display/LRM/SEFIP+retificadora+de+valores+recolhidos+a+menor
version: 2
---

### **Como gerar SEFIP 8.0** **para retificação de valores recolhidos a menor em outras competências**

SEFIP retificadora para valores recolhidos a menor devem ser geradas com o valor a ser corrigido, conforme Manual do SEFIP, capítulo I item 8.1.

##### *8.1 – Recolhimento e declaração complementar para o FGTS*

*Recolhimento e declaração complementar para o FGTS é o valor da diferença de remuneração do trabalhador das categorias 01, 02, 03, 04, 05, 06 e 07, sobre a qual não houve recolhimento e/ou declaração anterior.* 

*Exemplo:*

*O empregador/contribuinte transmitiu a GFIP/SEFIP contendo 10 trabalhadores, com recolhimento ao FGTS. Para um trabalhador o valor da remuneração foi informado de forma parcial, ou seja, foi informado R$ 800,00, sendo que a remuneração integral era R$ 1.000,00.*  
  *Deve ser gerada nova GFIP/SEFIP, informando a remuneração complementar deste trabalhador (R$ 200,00) no campo **Remuneração sem 13º Salário** e a remuneração integral (R$ 1.000,00) no campo **Base de Cálculo da Previdência Social**. Para tanto, deve ser informada a opção "Sim" no campo **Remuneração Complementar para o FGTS**. Os demais trabalhadores, que não possuem diferenças de remuneração, também devem constar da mesma GFIP/SEFIP, com a modalidade 9, e os mesmos dados e fatos geradores informados anteriormente."*   
   
Neste caso deverão ser feitos alguns tratamentos no sistema para que o sistema gere o arquivo do SEFIP.

**PARA OS FUNCIONÁRIOS A SEREM RETIFICADOS (Que tiveram recolhimento de FGTS a menor)**   
   
**1 -** Criar eventos com CC 189 e 188.   
 Como deverão ser criados os eventos:  
   
São dois os casos a serem considerados para a criação dos eventos. O primeiro caso é o de recolhimentos de diferenças pagas na competência atual (pois na época o pagamento foi menor) cujo valor deve ser recolhido em atraso. O segundo caso é o de recolhimento efetuado a menor na época do pagamento, onde o pagamento foi feito corretamente, mas as bases informadas no SEFIP estavam erradas.  
  **1º Caso:** O evento de CC 189 deverá ser criado como provento (sem incidências) com o valor da soma das diferenças apuradas e pagas na competência atual. Caso exista diferença também de INSS (calculado com a tabela da época) o evento de CC 188 deve ser informado como desconto. Exemplo:  
  
 Na competência 10/2005 foram pagos os eventos:  
 DIAS TRABALHADOS ........R$ 800,00  
 INSS 7,65% .......................R$ 61,20   
 O correto deveria ter sido pago o valor de:  
 DIAS TRABALHADOS ........R$ 1000,00  
 INSS 7,65% .......................R$ 90,00

Então na competência atual a empresa vai utilizar os eventos descritos acima (CC 189 e 188) para pagamentos das diferenças (não confundam com diferença por dissídio e acordos coletivos que se tratam de outra situação) e desconto do INSS que seria o valor de R$ 28,80 (R$ 90,00 – R$ 61,20).

**2º Caso:** O evento de CC 189 deverá ser criado como base de cálculo (sem incidências) com o valor da soma das diferenças apuradas e pagas na competência atual. Caso exista diferença também de INSS (calculado com a tabela da época) o evento de CC 188 deve ser informado como base de cálculo.   
 Exemplo:  
 Na competência 10/2005 foram pagos os eventos:  
 DIAS TRABALHADOS ........R$ 800,00  
 INSS 7,65% .......................R$ 61,20   
   
A pós isso foi gerado o SEFIP com os valores apresentados acima. Após isso foi recalculada a folha, ou pago um outro evento, que resultou em um aumento da base. A empresa deveria ter gerado o SEFIP com este novo valor e não gerou.  
   
O correto deveria ter sido pago o valor de:  
 DIAS TRABALHADOS ........R$ 800,00  
 HORAS EXTRAS .............. R$ 200,00  
 INSS 7,65% ......................R$ 90,00   
   
Então na competência atual a empresa vai utilizar os eventos descritos acima (CC 189 e 188, ambos como base de cálculo) para pagamentos das diferenças (não confundam com diferença por dissídio e acordos coletivos que se tratam de outra situação) e INSS que seria o valor de R$ 28,80 (R$ 90,00 – R$ 61,20).   
   
   
 **2-** Lançar no movimento atual do funcionário a retificar (Informar o valor a complementar) Exemplo:  
 Na competência 10/2005 foi recolhido R$ 800,00 e deveria ser recolhido R$1000,00. A competência atual é a 12/2005.  
 Na competência atual deverá ser lançado o evento com CC 189 com valor de R$ 200,00 (que o valor a ser complementado)  
 Caso exista valor de INSS a corrigir informe também o evento de CC 188.  
  
    
  **ATENÇÃO:** OS EVENTOS DE CC 188 E 189 (dos dois casos apresentados acima) PODEM SER CALCULADOS POR FÓRMULA CONFORME NECESSIDADE DO CLIENTE, PORÉM EM ALGUNS CASOS OS VALORES DEVERÃO SER APURADOS MANUALMENTE.  
 Não é possível o sistema atender todas as situações em face de diversos fatores que causam estas inconsistências, já que para o SEFIP os valores complementares devem ser gerados discriminadamente.   
 Um exemplo que pode ser atendido por fórmula é o do caso de um determinado evento não ter sido recolhido em uma competência por estar com as incidências informadas de forma errada, assim é possível criar uma fórmula na competência atual que retorne o valor do evento na referida competência.  
 **MV(mês desejado, ano do evento, 'numero do evento')**   
   
   
 **3 -** Entrar no módulo "Relatórios | SEFIP"   
 **4** - Criar filtro com os funcionários a retificar (que tem estes eventos)   
 **5 -** Colocar a competência a que se refere o pagamento do complemento em Competência do SEFIP.  
  
    
 **6 -** Entrar em "Relatórios | SEFIP", na pasta "Empresa" e marcar a opção de atraso e colocar a data de pagamento.  
  
   
 **7 –** Na pasta "Modalidade" informe modalidade a ser utilizada, para o caso de recolhimento executado a menor a modalidade deverá ser "Branco".   
  
    
  **8 -** Marcar Retificação de valores e Remuneração complementar  
  
    
 **9 -** Marcar o evento criado em Remuneração folha com CC 189   
  
    
   
**10 -** Colocar a competência onde está lançado o evento que foi marcado (movimento atual)  
  
    
 **11-** Calcular valores e gerar SEFIP. Guarde este arquivo gerado em um local separado para não ser substituído pelo arquivo a ser gerado para os funcionários que não tiveram alterações.   
   
   
 **PARA O RESTANTE DOS FUNCIONÁRIOS (Que os dados não sofreram alterações)**  
 **1 -** Criar filtro com o restante dos funcionários relacionados no mês a retificar   
 **2 -** Entrar em "Relatórios | SEFIP" e na pasta "Modalidade" confirmar o restante dos funcionários como modalidade 9.  
  
    
  **3 -** O validador do SEFIP não gera guia complementar de INSS para pagamento. Esta guia de GPS deve ser gerada pelo sistema.   
 **4 -** Entrar em "Relatórios | Guia de INSS"   
 **5 -** Utilizar o filtro com os funcionários a retificar criado no relatório do SEFIP   
 **6 -** Marcar retificação SEFIP  
  
   
  **7 -** Calcular valores e Gerar Guia de INSS.
