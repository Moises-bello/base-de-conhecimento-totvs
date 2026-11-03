---
article_id: 360050594013
category: RH - Relatórios
content_hash: 102f7e1e8fad0f3a502000a333d37b6249530ea709911bd9f25686667e8e1e7f
fetched_at: '2026-06-28T22:44:43.482701+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Como gerar o Relatório de Faltas (PONR160)
type: support-article
updated_at: '2025-10-08T17:06:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050594013-RH-Linha-Protheus-PON-Como-gerar-o-Relat%C3%B3rio-de-Faltas-PONR160
---

**Dúvida**Como gerar e qual a finalidade do Relatório de Faltas, através da rotina **PONR160**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O **Relatório de Faltas** foi desenvolvido para gerar em um intervalo de parâmetros, todos os eventos classificados como Falta e apontados para o funcionário.  
  
O Relatório pode ser impresso de forma **analítica** ou **sintética,** e as horas poderão ser exibidas em **Sexagesimal** ou **Centesimal.**As informações vem da tabela de apontamentos ou histórico de apontamentos de acordo com o período selecionado, ou seja, o relatório pode ser gerado para períodos abertos ou fechados.  
  
As tabelas que o Relatório de Faltas, faz referência são:  
**SPH** - Histórico de Apontamentos  
**SPC** - Apontamentos  
  
Após a execução do Apontamento, o sistema irá gerar os eventos de Faltas:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076426153)  
  
  
Para gerar o relatório, deve ser acessado o **módulo 16-SIGAPON** acessar em **Relatórios> Diversos> Faltas****,**os parâmetros serão exibidos conforme abaixo:  
  
**- Filiais?:** Informe intervalo de filiais que deseja considerar para impressão do relatório. Para definir intervalos de dados sequenciais, utilize hifen (1-3) e para os nao sequenciais, ponto e virgula (3;5;1). Utilizar aspas simples para desconsiderar hifens nos conteúdos. Exemplo: '000001-1'-'000004-9';000006;0000008-'000009-8'  
**- Centro de Custos?:** Informe intervalo de Centros de Custo que deseja considerar para impressão do relatório. Para definir intervalos de dados sequenciais, utilize hifen (1-3) e para os nao sequenciais, ponto e virgula (3;5;1). Utilizar aspas simples para desconsiderar hifens nos conteúdos. Exemplo: '000001-1'-'000004-9';000006;0000008-'000009-8'  
**- Departamento?:** Informe intervalo de Departamentos que deseja considerar para impressão do relatório. Para definir intervalos de dados sequenciais, utilize hifen (1-3) e para os nao sequenciais, ponto e virgula (3;5;1). Utilizar aspas simples para desconsiderar hifens nos conteúdos. Exemplo: '000001-1'-'000004-9';000006;0000008-'000009-8'  
**- Matricula?:** Informe intervalo de matrículas que deseja considerar para impressão do relatório.Para definir intervalos de dados sequenciais, utilize hifen (1-3) e para os nao sequenciais, ponto e virgula (3;5;1). Utilizar aspas simples para desconsiderar hifens nos conteúdos. Exemplo: '000001-1'-'000004-9';000006;0000008-'000009-8'  
**- Tipo Relatório?:** Informe se deseja que o Relatório seja impresso de Forma Analítica, onde será descriminado com detalhes, ou Sintética, onde será descriminado Resumidamente.  
**- Período?:** Para definir intervalos de tempo (periodo a ser considerado), utilize hifen (dd/mm/aa-dd/mm/aa ou dd/mm/aaaa-dd/mm/aaaa) e para os nao sequenciais, ponto e virgula (dd/mm/aa;dd/mm/aa ou dd/mm/aaaa;dd/mm/aaaa).  
**- Categorias?:** Informe ou selecione uma Categoria p/ Funcionários para filtro dos dados.**- Situação?:** Informe ou Selecione as Situações dos Funcionários para Filtro dos dados.  
**- Horas em?:** Informe qual o formato que deseja adotar para a impressão das horas no relatório: Sexagesimal ou Decimal. Se escolhida a opção Sexagesimal, os minutos serão apresentados na quantidade real, se a escolha for a opção Centesimal, a quantidade de minutos será convertida para centésimos de hora.  
  
Exemplo de utilização:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19069608504599)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19069629874327)  
  
  
O relatório será gerado de acordo com a parametrização, podendo ser verificado todos os eventos de Faltas:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075234554)  
  
  
Cabe ressaltar que neste relatório, serão impressos apenas os eventos cadastrados com os **id's de ponto 008A, 010A, 032A, 034A, 007N, 009N, 033N, 035N e 043A** - relacionados as faltas não autorizadas e autorizadas, respectivamente.  
  
  
  
**Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
