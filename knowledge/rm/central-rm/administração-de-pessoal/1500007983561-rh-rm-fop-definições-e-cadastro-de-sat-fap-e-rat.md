---
article_id: 1500007983561
category: Administração de Pessoal
content_hash: 604f296ff75a923bd670a16b0ee02b341ee952ef87cb2d29154ef8b139d83a0f
fetched_at: '2026-06-28T22:47:02.185689+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Definições e cadastro de SAT, FAP e RAT
type: support-article
updated_at: '2025-03-12T10:04:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007983561-RH-RM-FOP-Defini%C3%A7%C3%B5es-e-cadastro-de-SAT-FAP-e-RAT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura**:00:01:20 min****Dúvida**O que são as siglas SAT, FAP e RAT?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução****SAT:** **Seguro de Acidente do Trabalho**É uma contribuição devida à Previdência Social, a título de seguro de acidente do trabalho, pago pelo empregador sobre a folha de pagamento e recolhido na guia de INSS (GPS). A alíquota do SAT é determinada pelo grau de risco da empresa. Essa alíquota pode ser de 1% (leve), 2% (médio) ou 3% (grave). No caso, específico da construção civil, cujo grau de risco é 3% para a grande parte do setor, a alíquota SAT também é de 3%, ou seja, as empresas de construção civil em geral recolhem o SAT na alíquota máxima.

O SAT teve sua descrição alterada para RAT – Riscos Ambientais do Trabalho  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011743101/mceclip0.png)  
  
**RAT: Riscos Ambientais do Trabalho**Representa a contribuição da empresa, prevista no inciso II do artigo 22 da Lei 8212/91, e consiste em percentual que mede o risco da atividade econômica, com base no qual é cobrada a contribuição para financiar os benefícios previdenciários decorrentes do grau de incidência de incapacidade laborativa (GIIL-RAT).  
  
**Importante**A alíquota de contribuição para o RAT será de 1% se a atividade é de risco mínimo; 2% se de risco médio e de 3% se de risco grave, incidentes sobre o total da remuneração paga, devida ou creditada a qualquer título, no decorrer do mês, aos segurados empregados e trabalhadores avulsos. Havendo exposição do trabalhador a agentes nocivos que permitam a concessão de aposentadoria especial, há acréscimo das alíquotas na forma da legislação em vigor.  
  
**FAP: Fator Acidentário de Prevenção**Lei Nº10.666, 08/05/2003, Art. 10. É o fator multiplicador do RAT(SAT). O FAP pode reduzir o RAT(SAT) em até 50% e aumentá-lo em até 100%. No caso da construção civil, o RAT(SAT) pode variar entre 1,5% e 6%. O FAP supostamente veio para ressarcir a Previdência das despesas com benefícios concedidos e por outro lado individualizar o pagamento RAT(SAT), a empresa que investe em segurança e medicina no trabalho paga menos RAT(SAT).  
  
**Parametrizando o FAP no TOTVS Folha de Pagamento**  
1. Acesse **Administração de pessoal | Seções** e edite a seção centralizadora. Depois acesse  **Anexos** | **FAP por estabelecimento empresarial**; **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417911146391/mceclip0.png)**2. Abrirá uma tela para cadastro da alíquota. Informe a data inicial e final da vigência do FAP e o valor da alíquota. Veja abaixo:  
  
![fap_1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360009704391/fap_1.jpg)  
  
Em **Encargos | Guia de INSS | Guia de INSS**, no cálculo do campo **Acidente Trabalho** é considerado o percentual acidente trabalho da seção conforme a quebra informada, multiplicado pelo valor fixo **Alíquota FAP** com vigência corrente.  
  
**Exemplo**  
Valor Fixo FAP = 0,98%  
Percentual Acidente Trabalho = 2%  
Acréscimo Aposentadoria Especial 15 anos = 12%  
Funcionário com aposentadoria especial de 15 anos e remuneração de R$1.000,00.  
Funcionário sem aposentadoria especial e remuneração de R$600,00.  
O cálculo para encontrar o percentual do Acidente Trabalho e aplicar sobre a remuneração de R$1.000,00 é: (2 (Acidente Trabalho) \* 0,98 (FAP)) + 12 (acréscimo) = 13,96%  
O cálculo para encontrar o percentual do Acidente Trabalho e aplicar sobre a remuneração de R$600,00 é: (2 (Acidente Trabalho) \* 0,98 (FAP)) = 1,96%  
O valor do Acidente de Trabalho é: (1.000,00 \* 13,96%) + (600,00 \* 1,96%) = R$151,36  
  
**Saiba mais**Para outras informações sobre o cadastro do FAP, clique aqui. [FAP: Fator Acidentário de Prevenção](https://tdn.totvs.com/pages/viewpage.action?pageId=452719556)
