---
article_id: 360060420434
category: RH - Provisão
content_hash: 2a77e6260ce793a15f7ada197d06f09a6e4809a26012a16c93b76b9d311bf780
fetched_at: '2026-06-28T22:43:55.748980+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Conferir o Cálculo de Provisão de 13º Salário
type: support-article
updated_at: '2025-10-24T13:18:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060420434-RH-Linha-Protheus-GPE-Como-Conferir-o-C%C3%A1lculo-de-Provis%C3%A3o-de-13%C2%BA-Sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32904168408983)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como Conferir o Cálculo de Provisão de 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Para conferir do cálculo de **Provisão de 13º Salário**, realize os seguintes passos:

1. Acesse: Atualizações / Lançamentos / Ausências (**GPEA240**), e verifique se houve lançamento de Afastamento no Ano Corrente, onde o funcionário perda o direito ao avo de 13º Salário, para confirmar a quantidade de Avos de 13º Salário apresentada no Cabeçalho da Provisão;  
  
2. Acesse: Atualizações / Funcionários / Funcionários (**GPEA010**), e verifique o campo Salário (RA\_SALARIO), o mesmo valor deve ser apresentado no Cabeçalho da Provisão;  
  
3. Acesse: Relatórios / Lançamentos / Demonstrativos de Médias (**GPER080**), e emita o relatório de médias de 13º Salário com a mesma Data de Referência de cálculo da Provisão. O Valor da Média de Pagamento será apresentada na verba com Identificador de Cálculo 0267, e na coluna "Adicionais", no Relatório de Provisão;  
  
4. Acesse: Atualizações / Funcionários / Funcionários (**GPEA010**), e verifique se o Funcionário possui Adicionais (Adicional por Tempo de Serviço, Insalubridade, Periculosidade, Adicional de Transferência ou Cargo de Confiança, na aba Adicionais. Se o funcionário tem direito à qualquer um destes adicionais o valor Proporcional aos avos de 13º salário será somado à verba com Identificador de Cálculo 0267, e na coluna "Adicionais", no Relatório de Provisão;  
  
5. Acesse: Atualizações / Definições de Cálculo / Manutenção de Tabelas (**GPEA320**), e acesse as tabelas S033, S037 e S038 para identificar Alíquota de INSS (% empresa, % Acidente de Trabalho e % Terceiros) e a Alíquota de FGTS;  
  
6. Acesse: Relatórios / Provisão / Provisão 13º Salário (**GPER090**) e emita o Relatório de Provisão de 13º Salário, e confirme se os Saldo anterior de provisão está correto.   
Faça essa validação pela linha "**Anter**" do relatório, confirme se os valores estão iguais aos valores calculados na linha "Atual" do Relatório de Provisão de 13º Salário do mês Anterior.  
  
7. Realize a conferência dos valores de Provisão de 13º Salário considerando as orientações dos passos de 1 à 6 listados acima, considerando a linha "**Atual**" do relatório;  
  
8. A Linha "**No Mês**" do Relatório de Provisão de 13º Salário apresenta o ajuste entre o Saldo Atual e o valor provisionado até o mês anterior, portanto subtraia o valor atual do valor anterior para validar o valor no mês.  
  
Veja um Exemplo prático de conferência de Relatório de Provisão do mês de Novembro:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001777521)  
  
Conferência dos valores Anteriores (Relatório de Provisão de Outubro):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001778081)  
  
Veja que os valores da linha "Atual" do relatório do mês 10/2020, são exatamente os mesmos da linha "Anter" do relatório do mês 11/2020.  
  
Conferência dos valores Atuais:

- **VALOR**: Salário / Meses do ano x Avos de direito = 2.236,42 / 12 x 11 = **2.050,05**  
- **ADICIONAIS**: Funcionário tem direito à Adicional de Periculosidade de R$ 670,93.  
Periculosidade / Meses do ano x Avos de Direito = 670,93 / 12 x 11 = **615,02**  
- **1o PARCELA**: Valor pago de 1ª Parcela de 13º Salário. Neste exemplo, este funcionário não teve Antecipação de 13º, portanto o valor fica zerado.  
- **TOTAL 13o**: Soma do Valor, Adicional e 1ª Parcela = 2.050,05 + 615,02 = **2.665,07**- **INSS**: Total 13o x Alíquota INSS = 2.665,07 x 27,80% = **740,88**- **FGTS:** Total 13o x 8% = 2.665,07 x 8% = **213,20**  
- **TOTAL ENCARGOS**: Soma do INSS e FGTS = 740,88 + 213,20 = **954,08**  
- **TOTAL GERAL:** Soma do Total 13o e Total Encargos = 2.665,07 + 954,08 = **3.619,15**

Conferência do Ajuste do Mês:

- **VALOR**: Atual - Anterior = 2.050,05 - 1.863,68 = **186,37**  
- **ADICIONAIS**: Atual - Anterior = 615,02 - 559,10 = **55,92**  
- **1o PARCELA**: Atual - Anterior = **0**  
- **TOTAL 13o**: Atual - Anterior = 2.665,07 - 2.422,78 = **242,29**- **INSS**: Atual - Anterior = 740,88 - 673,53 = **67,35**- **FGTS:** Atual - Anterior = 213,20 - 193,82 = **19,38**  
- **TOTAL ENCARGOS**: Atual - Anterior = 954,08 - 867,35 = **86,37**  
- **TOTAL GERAL:** Atual - Anterior = 3.619,15 - 3.290,13 = **329,03**

**Saiba Mais:**[RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o) [Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
