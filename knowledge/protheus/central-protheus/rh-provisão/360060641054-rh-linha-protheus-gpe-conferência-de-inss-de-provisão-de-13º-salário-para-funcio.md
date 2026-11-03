---
article_id: 360060641054
category: RH - Provisão
content_hash: 216c53e80762954d32723751c5497719e6f1f419d900b2dd0e220ba5b1016cf5
fetched_at: '2026-06-28T22:43:55.873943+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Conferência de INSS de Provisão de 13º Salário
  para Funcionária Afastada por Maternidade no Ano - NT 20/2020
type: support-article
updated_at: '2025-08-21T12:45:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060641054-RH-Linha-Protheus-GPE-Confer%C3%AAncia-de-INSS-de-Provis%C3%A3o-de-13%C2%BA-Sal%C3%A1rio-para-Funcion%C3%A1ria-Afastada-por-Maternidade-no-Ano-NT-20-2020
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34341316784151) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como Conferir o INSS de Provisão de 13º Salário para Funcionária Afastada por Maternidade no Ano, de Acordo com a Norma Técnica 20/2020 (NT-20/2020)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Foi efetuado ajuste para que as verbas referentes a Maternidade nos roteiros FOL (folha), RES (rescisão) e 132 (segunda parcela do 13º) não entrem na composição da base dos encargos patronais, de acordo com a **Norma Técnica 20/2020**.

Este já está disponível na execução dos cálculos de Folha, Rescisão, 2ª Parcela do 13º, e **Provisão de 13º Salário**.

Para implementar a solução nos cálculos de Provisão, siga o passo a passo:  
  
1. Aplique o Pacote de Atualização de acordo com a Versão e Release de sua base:  
  
[Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
  
Importante: Aplique-o primeiro em base teste e faça um Backup do RPO antes.

2. Verifique se nos Cálculos do 13º Salário, o INSS Patronal foi calculado desconsiderando as verbas de Maternidade. Para mais informações sobre esta configuração, [Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=576982919);  
   
3. Acesse : Miscelânea / Provisões / Provisões de Férias e 13º Salário (**GPEA070**), e Calcule as Provisões para os funcionários;  
  
4. Acesse : Relatórios / Provisões / Provisão 13º Salário (**GPER090**), e imprima o Relatório de Provisão para Conferência.  
  
Exemplo - Funcionária Afastada por Licença Maternidade à partir de 01/12/2020:  
  
- Lançamento da Ausência:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001931562)  
  
- Cálculo da 2ª Parcela do 13º Salário:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100825794)  
  
- Relatório de Provisão de 13º Salário:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001982601)

**Conferência do INSS Patronal**:

Base do INSS - Verbas de Maternidade x % de INSS Patronal.

Base Encargos Empresa = 3600,00 – 258,33 – 25,83 – 25,83 = 3290,01

% Empresa = 3290,01 \* 0,20 = 658,00

% Terceiros = 3290,01 \* 0,058 = 190,82

% Acid. Trabalho = 3290,01 \* 0,023 = 75,67

Total Encargos = **924,49**

Veja que o mesmo valor calculado na Folha de 13º Salário é apresentado como Baixa na Provisão de 13º Salário.

Saiba Mais:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=589502878>
