---
article_id: 9324927169559
category: RH - Portaria 671
content_hash: dbedc492b3d1729597369b22d35e0bbd678037ce4568d325e1b122571e7955c1
fetched_at: '2026-06-28T22:44:44.407939+00:00'
product: protheus
section_id: 32419326556951
source: central-protheus
title: RH - Linha Protheus - PON - Espelho de Ponto de acordo com a Portaria 671
type: support-article
updated_at: '2025-10-07T13:01:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9324927169559-RH-Linha-Protheus-PON-Espelho-de-Ponto-de-acordo-com-a-Portaria-671
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35461143858327) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como imprimir o Espelho de Ponto de acordo com a Portaria 671?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**De acordo com a nova **Portaria 671** do MTE, foram necessárias **inclusões de dados no Espelho de Ponto**, conforme abaixo:  
**- CPF do funcionário;**  
**- Data de admissão do funcionário;**  
**- Data de emissão do relatório;**  
**- Período demonstrado no relatório;**  
**- Duração da jornada realizada a cada dia;**  
**- Horários contratuais do funcionário;  
- Marcações Desconsideradas;**  
**- Legenda/Flag com o Tipo da Marcação.**  
  
Para **habilitar essas informações no Espelho de Ponto**, é necessário **criar o parâmetro** **MV\_PORT671** no módulo **Configurador** e deixá-lo com **conteúdo .T.** conforme exemplo:  
- **Nome da Variável** **=** MV\_PORT671  
- **Tipo** **=** Lógico  
- **Descrição** **=** Indica se as alterações da Portaria 671 estão habilitadas no ambiente:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9324160478743)  
  
  
Com isso, o **Espelho de Ponto** será impresso desta forma:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9607194911127)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9607237231127)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9607333708951)  
  
  
**O que é importante detalhar sobre os novos dados:**  
- O **período** exibido no **cabeçalho do Espelho de Ponto** se trata do **período de apontamento** utilizado para impressão do relatório;  
- **Emissão** se trata da **data real** em que o **Espelho foi gerado**;  
**- CPF** de acordo com o **Cadastro do Funcionário (SRA)**;  
- **Admissão** de acordo com o **Cadastro do Funcionário (SRA)**;  
- A coluna **"Jornada"** foi criada para demonstrar a **quantidade de horas trabalhadas no dia**, com base nas **marcações realizadas** pelo funcionário. **Horas Extras, Atrasos, Saídas Antecipadas/Expediente são contabilizadas** para exibição desta coluna, bem como **horas realizadas em horário noturno também**. **Importante ressaltar** que as **horas noturnas** são calculadas e exibidas de **forma reduzida**. Exemplos:  
-> Funcionário com horário das **08h - 12h - 13h - 17h**  
-> Se forem feitas as seguintes marcações: **08h - 12h - 13h - 18h**, na coluna de **Jornada** será exibido um total de **09h**;  
-> Se forem feitas as seguintes marcações: **08h - 12h - 13h - 23h**, na coluna de **Jornada** será exibido um total de **14h09** (sendo: 13h normais + 01h09 noturnas já convertidas);  
-> Se forem feitas as seguintes marcações: **10h - 12h - 13h - 17h**, na coluna de **Jornada** será exibido um total de **06h**.  
- O quadro de **"Marcações Desconsideradas"** mostra marcações que **vieram do arquivo AFD**, não foram **classificadas/ordenadas**, porém, **existem nas tabelas de marcação (SP8/RFE e SPG/RFH)** para eventuais fiscalizações trabalhistas;  
- O quadro de **"Horários"** no **rodapé do Espelho de Ponto** foi criado para mostrar em detalhes a **montagem do calendário** para o período, ou seja, são validados os dados de: **Tabela de Horário Padrão vinculada na Troca de Turno** (sequências, quais são os horários previstos para cada dia, dias Trabalhados e Não Trabalhados, se em uma mesma sequência existem horários diferentes entre os dias) e **Exceções por Funcionário ou Período.**  
  
  
  
**Saiba mais:**  
<https://tdn.totvs.com/display/public/PROT/DRHJORNPRT-2339+DT+Espelho+de+Ponto+de+Acordo+com+a+Portaria+671>
