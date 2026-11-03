---
article_id: 360055361773
category: Encargos
content_hash: e85e448049e3032e178e0d48a28006214d06228d74555118e423217942a72e0b
fetched_at: '2026-06-28T22:46:53.301942+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Como gerar SEFIP Retificadora
type: support-article
updated_at: '2025-01-07T18:46:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055361773-RH-RM-FOP-Como-gerar-SEFIP-Retificadora
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15328495913879)***Tempo aproximado para leitura: **00:10:15 min****Dúvida**Como gerar Sefip 8.4 para retificação de valores a menor em outras competência?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A Sefip retificadora para valores recolhidos a menor deve ser gerada com o valor a ser corrigido, conforme Manual do Sefip, capítulo I item 8.1.  
  
8.1 – Recolhimento e declaração complementar para o FGTS  
  
Recolhimento e declaração complementar para o FGTS é o valor da diferença de remuneração do trabalhador das categorias 01, 02, 03, 04, 05, 06 e 07, sobre a qual não houve recolhimento e/ou declaração anterior.  
  
Para melhor entendimento da solução, considere o seguinte exemplo: O empregador/contribuinte transmitiu a GFIP/Sefip contendo 10 trabalhadores, com recolhimento ao FGTS. Para um trabalhador o valor da remuneração foi informado de forma parcial, ou seja, foi informado R$800,00, sendo que a remuneração integral era R$1000,00.  
  
Deve ser gerada nova GFIP/Sefip, informando a remuneração complementar deste trabalhador, R$ 200,00, no campo **Remuneração sem 13º Salário** e a remuneração integral, R$1000,00, no campo **Base de Cálculo da Previdência Social**. Para tanto, deve ser informada a opção **Sim** no campo **Remuneração Complementar para o FGTS**. Os demais trabalhadores, que não possuem diferenças de remuneração, também devem constar da mesma GFIP/Sefip, com a modalidade 9, e os mesmos dados e fatos geradores informados anteriormente. Neste caso deverão ser feitos alguns tratamentos no sistema para que o sistema gere o arquivo do Sefip.

**Para funcionários a serem retificados que tiveram recolhimento de FGTS a menor:**  
  
1. Criar eventos com Código de Cálculo 189 e 188.  
Como deverão ser criados os eventos:  
  
São dois os casos a serem considerados para a criação dos eventos. O primeiro caso é o de recolhimentos de diferenças pagas na competência atual, pois na época o pagamento foi menor, cujo valor deve ser recolhido em atraso. O segundo caso é o de recolhimento efetuado a menor na época do pagamento, onde o pagamento foi feito corretamente, mas as bases informadas no Sefip estavam erradas.  
 **1º Caso:** O evento de CC 189 deverá ser criado como provento, sem incidências, com o valor da soma das diferenças apuradas e pagas na competência atual. Caso exista diferença também de INSS calculado com a tabela da época, o evento de CC 188 deve ser informado como desconto. Exemplo:  
  
Na competência 10/2005 foram pagos os eventos:  
DIAS TRABALHADOS ........R$800,00  
INSS 7,65% .......................R$61,20  
O correto deveria ter sido pago o valor de:  
DIAS TRABALHADOS ........R$1000,00  
INSS 7,65% .......................R$90,00  
  
Então na competência atual a empresa vai utilizar os eventos descritos acima, CC 189 e 188, para pagamentos das diferenças e desconto do INSS que seria o valor de R$90,00 – R$61,20 = R$28,80. Importante não confundir com diferença por dissídio e acordos coletivos que se tratam de outra situação.  
  
**2º Caso:** O evento de CC 189 deverá ser criado como base de cálculo, sem incidências, com o valor da soma das diferenças apuradas e pagas na competência atual. Caso exista diferença também de INSS, calculado com a tabela da época, o evento de CC 188 deve ser informado como base de cálculo.  
Exemplo:  
  
Na competência 10/2005 foram pagos os eventos:  
DIAS TRABALHADOS ........R$800,00  
INSS 7,65% .......................R$61,20  
  
Após isso foi gerado o Sefip com os valores apresentados acima. Após isso foi recalculada a folha, ou pago um outro evento, que resultou em um aumento da base. A empresa deveria ter gerado o Sefip com este novo valor e não gerou.  
  
O correto deveria ter sido pago o valor de:  
DIAS TRABALHADOS ........R$800,00  
HORAS EXTRAS .............. R$200,00  
INSS 7,65% ......................R$90,00  
  
Então na competência atual a empresa vai utilizar os eventos descritos acima, CC 189 e 188, ambos como base de cálculo para pagamentos das diferenças e INSS que seria o valor de R$90,00 – R$61,20 = R$28,80. Importante não confundir com diferença por dissídio e acordos coletivos que se tratam de outra situação.  
  
2. Lançar no movimento atual do funcionário a retificar o valor a complementar. Exemplo: Na competência 10/2005 foi recolhido R$800,00 e deveria ser recolhido R$1000,00. A competência atual é a 12/2005. Na competência atual deverá ser lançado o evento com CC 189 com valor de R$200,00, valor a ser complementado. Caso exista valor de INSS a corrigir, informe também o evento de CC 188.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9069453488279)  
  
Os eventos de CC 188 e 189, dos casos apresentados acima, podem ser calculados por fórmula conforme necessidade do cliente, porém em alguns casos os valores deverão ser apurados manualmente. Não é possível o sistema atender todas as situações em face de diversos fatores que causam estas inconsistências, já que para o Sefip os valores complementares devem ser gerados discriminadamente.  
Um exemplo que pode ser atendido por fórmula é o do caso de um determinado evento não ter sido recolhido em uma competência por estar com as incidências informadas de forma errada, assim é possível criar uma fórmula na competência atual que retorne o valor do evento na referida competência.  
  
**MV(mês desejado, ano do evento, 'numero do evento')**  
  
3. Entrar no módulo **Folha de pagamento | Encargos | Sefip | Geração da Sefip**;  
  
4. Colocar a **competência** a que se refere o pagamento:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9069530282263)  
  
5. Informar também nas opções de **Recolhimento FGTS** e/ou **Recolhimento Previdência social** a opção **GRF em atraso** ou **GPS em atraso**, conforme o pagamento a ser retificado.  
  
6. Na opção **Modalidade** informe a modalidade a ser utilizada, para o caso de recolhimento executado a menor a modalidade deverá ser **Branco**.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9069884913175)  
  
7. Clique em avançar até a tela de Seleção de coligadas, selecione a coligada correta e vá em **Utilizar parâmetros específicos**:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9069901784983)  
  
8.  Nos parâmetros específicos da coligada, acesse a aba Retificação, habilite o parâmetro **Retificação de valores** e informe o evento criado em Remuneração folha com CC 189 e CC 190 conforme abaixo:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9070000502295)  
  
9. Colocar a competência onde está lançado o evento que foi marcado no campo **Origem dos eventos**, na tela demonstrada acima.   
  
10. Calcular valores e gerar Sefip. Guarde este arquivo gerado em um local separado para não ser substituído pelo arquivo a ser gerado para os funcionários que não tiveram alterações.  
  
**Para o restante dos funcionários cujo os dados não sofreram alterações:**1. Criar filtro com os demais funcionários relacionados no mês a retificar;  
  
2. Na rotina Geração da Sefip campo **Modalidade** confirmar o restante dos funcionários como **Modalidade 9**:  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6649496295959)  
3. O validador do Sefip não gera guia complementar de INSS para pagamento. Esta guia de GPS deve ser gerada pelo sistema;  
  
4. Acessar a aba **Encargos | Guia de INSS**  
  
5. Na rotina para geração da GPS, habilitar a opção **Utilizar parâmetros específicos**  e **Retificação de valores**, informando os eventos com código de cálculo;  
  
6. Marcar retificação Sefip:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9070131563927)  
7. Calcular valores e gerar a Guia de INSS.

**Saiba mais**  
[SEFIP retificadora de valores recolhidos a menor](https://tdn.totvs.com/display/public/LRM/SEFIP+retificadora+de+valores+recolhidos+a+menor)
