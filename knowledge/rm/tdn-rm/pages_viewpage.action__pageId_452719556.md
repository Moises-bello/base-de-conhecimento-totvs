---
content_hash: 53f729fe1ec92bae9a336fe06cc0d46102f0893ade28f2a48481eb49b09dcf1a
fetched_at: '2026-06-29T00:10:08.673844+00:00'
page_id: '452719556'
product: rm
source: tdn-rm
title: 'GPS - FAP: Fator Acidentário de Prevenção'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719556
version: 4
---

falseATENÇÃO:A partir da versão 12.1.2406, esse processo foi descontinuado. A GPS foi substituída pela DCTFWeb.  

* Para a geração do lançamento financeiro da DCTFWeb, consulte a documentação: [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=727915586)
* Para conferência dos valores da DCTFWeb, consulte a documentação: [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=717708785)

**SAT / RAT / FAP**  
   
**SAT:** Seguro de Acidente do Trabalho  
É uma contribuição devida à Previdência Social, a título de seguro de acidente do trabalho, pago pelo empregador sobre a folha de pagamento e recolhido na guia de INSS (GPS).  
   
A alíquota do SAT é determinada pelo grau de risco da empresa.  
Essa alíquota pode ser de 1%(leve), 2%(médio) ou 3%(grave). No caso, específico da construção civil, cujo grau de risco é 3%, para a grande parte do setor, a alíquota SAT também é de 3%, ou seja, as empresas de construção civil em geral recolhem o SAT na alíquota máxima, que é de 3%.  
   
O SAT teve sua descrição alterada para RAT – Riscos Ambientais do Trabalho  
   
**RAT: Riscos Ambientais do Trabalho**  
Representa a contribuição da empresa, prevista no inciso II do artigo 22 da Lei 8212/91, e consiste em percentual que mede o risco da atividade econômica, com base no qual é cobrada a contribuição para financiar os benefícios previdenciários decorrentes do grau de incidência de incapacidade laborativa (GIIL-RAT).   
A alíquota de contribuição para o RAT será de 1% se a atividade é de risco mínimo; 2% se de risco médio e de 3% se de risco grave, incidentes sobre o total da remuneração paga, devida ou creditada a qualquer título, no decorrer do mês, aos segurados empregados e trabalhadores avulsos. Havendo exposição do trabalhador a agentes nocivos que permitam a concessão de aposentadoria especial, há  
acréscimo das alíquotas na forma da legislação em vigor.  
O\_que\_é\_RAT\_(Riscos\_Ambientais\_do\_Trabal   
   
**FAP: Fator Acidentário de Prevenção**  
Lei Nº10.666, 08/05/2003, Art. 10.  
É o fator multiplicador do RAT(SAT). O FAP pode reduzir o RAT(SAT) em até 50% e aumentá-lo em até 100%. No caso da construção civil, o RAT(SAT) pode variar entre 1,5% e 6%. O FAP supostamente veio para ressarcir a Previdência das despesas com benefícios concedidos e por outro lado individualizar o pagamento RAT(SAT), a empresa que investe em segurança e medicina no trabalho paga menos RAT(SAT).  
   
   
**Parametrizando o FAP no RM Labore**  
Em Administração de Pessoal | Cálculos | Valores Fixos  
Criar com a finalidade 'Alíquota FAP' informando o percentual a ser aplicado.  
   
Em Encargos | Guia de INSS | Guia de INSS  
No cálculo do campo 'Acidente Trabalho' é considerado o percentual acidente trabalho da seção, conforme a quebra informada, multiplicado pelo valor fixo 'Alíquota FAP' com vigência corrente.  
   
**Exemplo:**   
Valor Fixo FAP = 0,98%  
Percentual Acidente Trabalho = 2%  
Acréscimo Aposentadoria Especial 15 anos = 12%  
Funcionário com aposentadoria especial de 15 anos e remuneração de R$1.000,00.  
Funcionário sem aposentadoria especial e remuneração de R$600,00.  
   
O cálculo para encontrar o percentual do Acidente Trabalho e aplicar sobre a remuneração de R$1.000,00 é: (2 (Acidente Trabalho) \* 0,98 (FAP)) + 12 (acréscimo) = 13,96%  
   
O cálculo para encontrar o percentual do Acidente Trabalho e aplicar sobre a remuneração de R$600,00 é: (2 (Acidente Trabalho) \* 0,98 (FAP)) = 1,96%  
   
O valor do Acidente de Trabalho é: (1.000,00 \* 13,96%) + (600,00 \* 1,96%) = R$151,36  
   
   
Em Encargos | Guia de INSS | SEFIP | Geração SEFIP  
   
Em Folha Mensal | Folha Analítica  
Disponibilizado o campo INSS SAT (Ajustado).  
   
Em Encargos | Cadastros | Encargos  
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Guia de INSS
