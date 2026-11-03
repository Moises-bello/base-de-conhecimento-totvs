---
article_id: 360018837632
category: Escrita Fiscal - Impostos - ICMS
content_hash: 5e0fd0126789cd0f9d701444256c43ab4be8c27004fe242ce75a97253b1842e5
fetched_at: '2026-06-28T22:39:25.971442+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Livros Fiscais - ICMS
  de Pauta X MVA
type: support-article
updated_at: '2022-12-01T13:59:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018837632-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Livros-Fiscais-ICMS-de-Pauta-X-MVA
---

**Dúvida**Como configurar o ICMS de Pauta X MVA no Protheus.   
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
  
**Solução**  
Foi realizado o tratamento para atender o DECRETO N.º 37.699, DE 26 DE AGOSTO DE 1997 (Regulamento do ICMS), aonde na hipótese em que o preço praticado pelo remetente, acrescido dos valores correspondentes a frete, seguro, impostos, contribuições e outros encargos transferíveis ou cobrados do destinatário, ainda que por terceiros, for igual ou superior a 90% (noventa por cento) do preço final ao consumidor, deverá ser utilizado o MVA ao invés da Pauta, para a base de cálculo do ICMS Retido.

**Procedimentos para Configuração**  
Acesse o cadastro da Tes - Tipos de Entrada e Saída e configure os campos Aplica Marg.(F4\_APLIIVA) com a opção 5 e % Def.MVA/Pa(F4\_OUTPERC) com valor maior que Zero.  
  
**Informações Importantes**  
  
Exemplo: Um situação em que a Pauta de "Produto X" for R$ 70,00, se eu vender com um preço MAIOR ou IGUAL a R$ 63,00, devo alterar a fórmula de cálculo e usar o percentual de MVA.

Cálculo: R$ 70,00 \* 90% = R$ 63,00.

Veja que R$ 63,00 atingiu 90% do Valor de Pauta, logo deve ser utilizado o Valor do MVA para calcular a base do ICMS ST.

Supondo que o MVA configurado seja de 50% a base de calculo será:

R$ 63,00 \*(1+(50/100)) = R$ 94,50

Caso o Valor fosse MENOR que R$ 63,00 seria utilizado o Valor de Pauta para o Cálculo.

Se o valor for de R$ 62,00 não atinge os 90%, logo o cálculo será o Valor de Pauta, que no caso é R$ 70,00.

**Configurar os campos:**

**-Aplica Marg. (F4\_APLIIVA)** = 1=Sim;2=Nao;3=Maior/Menor;4=Ating.75%;5=Out.%    
  
Aplica margem de lucro configurada no produto/exceção, quando o valor do item for maior/menor, atingir 75% do valor ou maior/igual que o percentual definido no campo F4\_OUTPERC para que seja aplicado o calculo de pauta ou ICMS ST   
  
**Opções:**

1-Sim: Aplica margem de lucro quando o valor unitário for maior que o valor da pauta de ICMS

2-Não: Não irá afetar o cálculo

3-Maior/Menor: Irá aplicar a margem independente do valor unitário ser maior ou menor que o valor da pauta de ICMS.

4-Quanto o Valor do Produto atingir 75% do Valor da Pauta, deve ser aplicada Margem de lucro.

5-Considerar o % definido no campo F4\_OUTPERC, para utilizar o MVA ao invés da Pauta.

**-% Def.MVA/Pa (F4\_OUTPERC)**

Informe o percentual para que quando o valor do produto atingir, o percentual definido neste campo, aplique a Margem de Lucro (MVA) ao invés da Pauta.  
  
Maiores informações, consultar a documentação:   
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=697250549>

<https://tdn.totvs.com/pages/releaseview.action?pageId=697250317>
