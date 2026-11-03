---
article_id: 1500000621421
category: RH - Provisão
content_hash: 92880c800d37a38826211b80e833307e21d2c773fb54fc96d6d253b97976fc05
fetched_at: '2026-06-28T22:43:55.734035+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Calcular uma Simulação do 13º Salário nas
  Provisões
type: support-article
updated_at: '2025-06-17T19:58:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000621421-RH-Linha-Protheus-GPE-Como-Calcular-uma-Simula%C3%A7%C3%A3o-do-13%C2%BA-Sal%C3%A1rio-nas-Provis%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32880404636439)** Tempo aproximado para leitura:**00:03:00 min**

**Dúvida**Como Calcular uma Simulação do 13º Salário nas Provisões?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todos os Releases.  
  
**Solução**A premissa para cálculo das Provisões, é ter cálculo de Folha de Pagamento para os funcionários, para a composição do Salário Base no cabeçalho da provisão (Id 0318).  
Portanto, enquanto não houver cálculo da folha de pagamento, não será possível realizar os cálculos de provisão, pois o sistema apresentará o salário da provisão zerado.  
  
Para solucionar essa dúvida, realize os seguintes passos:

**Exemplo 1:**

1. Replique o seu Ambiente de Produção em uma Base de Testes;  
  
2. Acesse: Atualizações / Definições de Cálculo / **Períodos** (**GPEA400**), e verifique se o roteiro 132 e FOL do período de Dezembro já está cadastrado e Ativo;  
  
3. Acesse: Miscelânea / Cálculos / **Por Roteiros** (**GPEM020**), e Processe os cálculos de 13º Salário (132);  
  
4. Acesse: Miscelânea / Fechamento / **Período** (**GPEM120**), e realize o Fechamento do Roteiro 132;  
  
5. Acesse: Miscelânea / Cálculos / **Por Roteiros** (**GPEM020**), e Processe os cálculos da Folha (FOL) de Dezembro;  
  
6. Acesse: Miscelânea / Provisões / **Provisões de Férias e 13º Salário** (**GPEA070**) e Processe os cálculos de Provisão de Dezembro;  
  
7. Acesse: Relatórios / Provisões / **Provisão 13º Salário** (**GPER090**) e preencha os Parâmetros para emissão do Relatório de Provisão.  
O sistema apresentará um valor aproximado de 13º salário nas verbas de Baixas de 13º Salário.

**Importante**: Esse procedimento não deverá ser realizado em base de Produção, tendo em vista que não será possível reabrir as Folhas de Pagamento Fechadas para ajuste.

**Exemplo 2:**

1. Exporte a Tabela SRT em Excel através da Consulta Genérica. Acesse: Consultas > Cadastros > Genéricos, em seguida informe a tabela SRT e Clique em "OK".   
  
2. Selecione a opção "Exp. CSV" e em seguida "Ponto e Vírgula (;) e Confirmar.  
  
![exporta SRT.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18057484336023)  
Será gerado um arquivo em Excel com os cálculos de Provisão.  
  
3. Abra o Arquivo da atbela SRT em Excel, e filtre na última competência calculada de provisão (coluna Data Cálculo) e o Tipo de Provisão de 13º Salário (Coluna Provisão).  
  
4. Insira um Fórmula dividindo os valores de 13º que serã apresentados pelos avos de direito e multiplicando por 12 meses.  
Exemplo: Se o último cálculo de provisão for da competência 09/2023, insira uma fórmula dividindo os valores por 9 e multiplicando por 12.  
![Simulacao 13.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18057489052055)  
  
Desta forma, serão calculadas prévias de valores de 13º Salário, Adicionais, Médias, INSS Patronal, FGTS e PIS sobre o 13º salário nas verbas abaixo:  
  
Id 0136 - Valor de 13º Salário  
Id 0267 - Adicionais e Médias de 13º Salário;  
Id 0137 - INSS Patronal de 13º salário;  
Id 0138 - FGTS de 13º Salário;  
Id 0421 - PIS de 13º Salário.

Vale lembrar que estes valores serão apenas uma Simulação de 13º salário, pois até o efetivo pagamento Horas Extras, Comissões, Bonificações, Adicionais, Faltas, Afastamentos e Desligamentos poderão alterar o valor do 13º salário.

**Saiba Mais:**[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
