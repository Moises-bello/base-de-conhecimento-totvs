---
content_hash: 89f2144a0b27b5c4ebcb8898276e6ac848dc76f54169d4807190754f835513c3
fetched_at: '2026-06-29T00:10:04.715421+00:00'
page_id: '452719239'
product: rm
source: tdn-rm
title: Dados p/ INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719239
version: 4
---

Para o processamento do cálculo e do recolhimento do INSS, é importante que esta pasta tenha as informações corretas.  
   
Informe o Código de pagamento da GPS conforme tabela divulgada pelo INSS. Este campo será utilizado no SEFIP.  
   
Informe o Código de Pagamento da GPS de Terceiros correspondente a seção, desta forma, quando na Guia de INSS for recolhido exclusivamente o valor de Terceiros, o sistema considerará automaticamente o valor aqui informado.  
   
FPAS (Fundo de Previdência e Assistência Social) é o código da atividade da empresa no INSS. Este código será impresso na Guia de INSS e no e-Social.  
   
Código do Seguro de Acidentes do Trabalho (SAT) será impresso na Guia de INSS.  
   
O Percentual de Acid. De Trabalho será considerado para informação da empresa no SEFIP para cálculo da GPS.  
Conforme informação do manual do SEFIP este campo deve ser preenchido com "zeros" caso o código do FPAS informado seja 604, 647, 639 (com 100% de isenção) ou a empresa seja optante pelo Simples. Para qualquer outro FPAS será considerado o valor digitado ou se informado "zero" ou "branco" será considerado branco conforme manual do SEFIP que orienta "Sempre que não informado o campo deve ficar em branco".  
   
**Observação:**  
Ao gerar o SEFIP no código de recolhimento 650 o usuário deve mudar o "Código de Pagamento GPS" pelo código válido conforme relação constante da Instrução Normativa INSS/DC nº 02, de 20/10/99 para que o arquivo seja validado pelo Validador do SEFIP.  
Informe o valor da remuneração já multiplicado por 11.71% pagos aos autônomos da categoria 15 no campo Remun. Autônomos cat.15 não cadastrados. Sobre este valor serão recolhidos 2.5% de terceiros na GPS.   
   
**Observação:**  
Dispõe o art. 201, inciso IV, parágrafo 4º do RGPS (aprovado pelo decreto 3.048/99, alterado pelo Decreto 3.265/99) que, para a apuração da remuneração paga ou creditada a transportador autônomo pelo carreto, frete ou transporte de passageiros realizado por conta própria corresponderá, para fins de cálculo da contribuição previdenciária, bem como para terceiros (SEST/SENAT), à aplicação do percentual previsto no art. 267 do decreto (11,71%) sobre o valor bruto do frete, carreto ou transporte de passageiros.  
   
**Exemplo:**  
Portanto, tem-se que, em um frete no valor de R$ 1000,00, por exemplo, o valor sujeito à contribuição previdenciária e para terceiros, será apurado mediante a aplicação do percentual de 11,71%, encontrando-se, portanto, um valor de R117,10 (1000,00 \* 11,71%).  
Diante do exposto, pode-se concluir ser a contribuição para o SEST e SENAT correspondente a 2,5% de 11,71% do valor bruto do frete (117,10 \* 2,5 ) = 2,93 a ser descontado do carreteiro autônomo.  
Desta forma, a GPS deverá ser preenchida, lançando-se, no campo 9 (Valor de outras entidades) o valor obtido conforme cálculo acima, R$ 2,93, acrescidos do valor encontrado pela aplicação do percentual correspondente sobre a folha de pagamento dos demais empregados, caso existam, e no campo 6, os 20% da parte patronal.  
   
O Percentual de isenção de filantropia será considerado para redução das bases de cálculo das contribuições previdenciárias. Somente empresas que são beneficentes deverão informar o percentual de isenção.  
   
**Atenção:**  
Quando a empresa tem 100% de Isenção de Filantropia (FPAS 639), o campo "Percentual de Acid.de Trabalho" deve ser zerado. Desta forma, o programa SEFIP será validado corretamente.  
   
Faturamento Bruto: Utilizado para empresas Produtor Rural, veja em : [http://tdn.totvs.com.br/display/LRM/Faturamento+Bruto .](http://tdn.totvs.com.br/display/LRM/Faturamento+Bruto)  
   
As Informações para GRPS serão utilizadas para incluir observações na Guia de INSS. Somente os dados preenchidos no campo   
COMPLEMENTO das SEÇÕES de quebra para CNPJ serão gravados na GPS (eletrônica ou formulário).   
   
Os Percentuais de Acréscimo - Aposentadoria Especial são as alíquotas de contribuição destinadas ao financiamento da aposentadoria especial prevista nos arts. 57 e 58 da Lei nº 8.213/91, concedida em razão de maior incidência de incapacidade laborativa decorrente de riscos ambientais do trabalho (até junho/97, Seguro de Acidentes do Trabalho). Será acrescida dos valores digitados em pontos percentuais, conforme a atividade exercida pelo segurado a serviço da empresa permita, a concessão de aposentadoria especial após 15, 20 e 25 anos de contribuição, respectivamente.  
   
O acréscimo incide exclusivamente sobre o total das remunerações pagas ou creditadas, no decorrer do mês, aos segurados empregados e trabalhadores avulsos sujeitos a condições especiais.  
   
A contribuição adicional a que se refere acima, será exigida de forma progressiva, conforme indicado a seguir, de acordo com a atividade exercida pelo segurado que permita a obtenção de aposentadoria especial:  
   
**Observação:**  
Quando existir funcionários com aposentadoria especial, o percentual acima será acrescentado ao SAT da empresa.  
   
**Exemplo**

Percentual de acréscimo para 15 anos de aposentadoria = 4  
Percentual de acréscimo para 20 anos de aposentadoria = 3  
Percentual de acréscimo para 25 anos de aposentadoria = 2  
Percentual de Acidente de Trabalho (SAT) igual a 2%   
A remuneração dos segurados é = R$1.000,00  
No campo empresa da GPS calcula-se:  
Remuneração segurados com aposentadoria 20 anos = R$ 500,00  
Remuneração segurados com aposentadoria 15 anos = R$ 300,00  
Remuneração segurados sem aposentadoria especial = R$ 200,00  
Total remuneração = R$ 1.000,00  
R$1.000,00 \* 22% (20% empresa + 2% SAT empresa) = R$220,00  
R$ 500,00 \* 3% (percentual de acréscimo 20 anos) = R$ 15,00  
R$ 300,00 \* 4% (percentual de acréscimo 15 anos) = R$ 12,00  
Total da GPS = R$ 247,00  
   
O parâmetro de Distribuidora de Petróleo deverá ser confirmado se a seção estiver ligada a atividades de distribuição de petróleo. Se este campo estiver confirmado, o cálculo da Guia de INSS somente irá considerar os funcionários que não estiverem ligados a atividades de transporte. Os funcionários que estiverem em seções ligadas a atividades de transporte serão informados junto com a guia SEST/SENAT.  
   
Em conformidade com a Lei Complementar 110/2001, sendo isenta da Contribuição Social este parâmetro deverá ser marcado. O sistema calcula 40% de multa rescisória para empresas que sejam isentas da Contribuição Social (código da Opção pelo Simples 5 ou 6 ). Sendo assim, o campo 33 da GRFC será emitido com o valor correspondente aos 40% de multa rescisória.

**Cód. Recolhimento suspenso para terceiros**  
O campo tem como objetivo informar o código combinado dos Terceiros para os quais o recolhimento está suspenso em virtude de processos Judiciais.

**Exemplo:**

Se o contribuinte possui decisões de processos para suspensão de recolhimentos ao Sesi (0008) e ao Sebrae (0064), deve informar o código combinado das duas entidades, ou seja, 0072.  
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Processo Judicial de Terceiros/Outras Entidades
