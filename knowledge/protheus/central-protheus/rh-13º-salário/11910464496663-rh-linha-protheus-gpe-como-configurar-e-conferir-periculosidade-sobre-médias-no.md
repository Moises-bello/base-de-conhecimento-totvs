---
article_id: 11910464496663
category: RH - 13º salário
content_hash: 8ce931366d0c996b5b5bd843b5e25e20afbf37d2cb6264f6a5134df36d73b53b
fetched_at: '2026-06-28T22:44:00.591158+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como Configurar e Conferir Periculosidade Sobre
  Médias no 13º Salário
type: support-article
updated_at: '2025-07-25T19:08:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11910464496663-RH-Linha-Protheus-GPE-Como-Configurar-e-Conferir-Periculosidade-Sobre-M%C3%A9dias-no-13%C2%BA-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29273582503319) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como Configurar e Conferir Periculosidade Sobre Médias no 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as Versões  
  
**Solução**Há empresas que entendem que a verba de Periculosidade deve compor o valor das Médias para o pagamento do 13º Salário dos funcionários, porém como o Adicional de Periculosidade compõe a remuneração mensal do funcionário, a verba não deverá ser definida como Média, para que não haja cálculos de valores indevidos nas Médias.  
  
Para atender à esta demanda, foi disponibilizado o mnemônico **P\_ADISMED** para que seja possível definir se o adicional de Periculosidade deve ser calculados também sobre as Médias de 13º Salário.  
  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse: Atualizações / Definições de Cálculo / **Verbas** (GPEA040) e inclua as verbas indicadas abaixo:

- Identificador de cálculo **1649 -** Periculosidade Sobre Medias 13º 1ª Parcela.  
Para facilitar o cadastro, utilize como base a verba de Identificador de cálculo **1633**.- Identificador de cálculo **0181 -** Periculosidade Sobre Medias 13º 2ª Parcela.Para facilitar o cadastro, utilize como base a verba de Identificador de cálculo **1291**.  
  
**Importante:** A configuração das Verbas/Rubricas com relação a Natureza e as Incidências Tributárias é algo particular de cada Empresa e que deve ser analisado em conjunto com o departamento Jurídico e Contábil.  
  
2. Verifique se as Verbas que compõem as Médias (Horas Extras, Adicional Noturno, DSR, Bonificações, Gratificações, Comissões, etc.), estão com Sim no campo "**Periculosidade**" (**RV\_PERICUL**);  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11908923741975)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11908769351703)

3. Acesse: Atualizações / Cadastros / **Sindicatos** (GPEA340) e Confirme se o Adicional de Periculosidade está configurado com a Base de Cálculo "**Salário + Verbas**":  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11908848979479)

4. Acesse: Atualizações / Definições de Cálculos / **Mnemônicos** (GPEA300). Localize o Mnemônico **P\_ADISMED** e verifique se está configurado com .T. :  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11908979636375)  
  
5. Em seguida, prossiga com os Cálculos do 13º Salário.

**Exemplos**

**Exemplo 1** - 1ª Parcela do 13º Salário Integral (12/12 avos):  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11909360754071)  
**Memória de Cálculo**:  
Verba 009 - 13º Salário:  Salário / 12 x Avos de Direito x 50% = 3.000,00 x 50% = 1.500  
Verba 282 - Médias Horas : Valou apurado no Relatório de Médias x 50% = 61,66  
Verba 286 - Peric. 13º Sal : 30% sobre a Verba de 13º x 50% = 1.000,00 x 30% = 450,00  
Verba 368 - Peric. Sobre Médias: 30% sobre a verba de Médias = 61,66 x 30% = 18,50

**Exemplo 2** - 2ª Parcela do 13º Salário Integral (12/12 avos):  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11909075745175)  
**Memória de Cálculo**:  
Verba 010 - 13º Salário:  Salário / 12 x Avos de Direito = 3.000,00  
Verba 061 - Médias Horas : Valou apurado no Relatório de Médias = 269,72  
Verba 107 - Peric. 13º Sal : 30% sobre a Verba de 13º = 3.000,00 x 30% = 900,00  
Verba 370 - Peric. Sobre Médias: 30% sobre a verba de Médias = 269,72 x 30% = 80,92

**Exemplo 3** - 1ª Parcela do 13º Salário Proporcional (6/12 avos):

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11909858007831)

**Memória de Cálculo**:  
Verba 009 - 13º Salário:  Salário / 12 x Avos de Direito x 50% = 3.000,00 / 12 x 6 x 50% = 750,00  
Verba 282 - Médias Horas : Valou apurado no Relatório de Médias x 50% = 61,66  
Verba 286 - Peric. 13º Sal : 30% sobre a Verba de 13º x 50% = 750,00x 30% = 225,00  
Verba 368 - Peric. Sobre Médias: 30% sobre a verba de Médias = 61,66 x 30% = 18,50

**Exemplo 4 -** 2ª Parcela do 13º Salário Proporcional (6/12 avos):

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11909221322391)

**Memória de Cálculo**:  
Verba 010 - 13º Salário:  Salário / 12 x Avos de Direito = 3.000,00 / 12 x 6 = 1.500,00  
Verba 061 - Médias Horas : Valou apurado no Relatório de Médias = 269,72  
Verba 107 - Peric. 13º Sal : 30% sobre a Verba de 13º = 1.500,00 x 30% = 450,00  
Verba 370 - Peric. Sobre Médias: 30% sobre a verba de Médias = 269,72 x 30% = 80,92

**Dica:** Para facilitar a conferência, tanto das Médias, como da Periculosidade sobre Médias, emita o relatório de médias pela Consulta de Cálculo do Funcionário.  
Acesse com o Roteiro de Cálculo ainda aberto (131 para 1ª Parcela ou 132 para 2ª Parcela): Atualizações / Lançamentos **Por Funcionário** (GPEA580) / Selecione o Funcionário e clique em Visualizar / Informe o Roteiro 131 ou 132 e em seguida clique em Outras Ações e Médias.

Será emitido o Relatório de Médias de 13º salário, destacando no Cabeçalho dados importantes como O Valor de Cada Adicional e o Salário Incorporado do Funcionário, e nos Totalizadores são destacados os valores de Médias de Pagamento e Periculosidade sobre Médias:  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11910090055319)  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11910175215511)  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11910218103703)

**Saiba mais****Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>**

[Artigos 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio?page=1#articles)
