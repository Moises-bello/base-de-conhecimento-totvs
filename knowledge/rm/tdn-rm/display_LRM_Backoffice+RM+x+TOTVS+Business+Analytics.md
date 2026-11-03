---
content_hash: 0f53f6094180d245a1d42098ed5d5b2aa72bbc80ff2aee91dd65dfb9179bdf99
fetched_at: '2026-06-29T00:09:36.964724+00:00'
page_id: '425459547'
product: rm
source: tdn-rm
title: Backoffice RM x TOTVS Business Analytics
type: documentation
url: https://tdn.totvs.com/display/LRM/Backoffice+RM+x+TOTVS+Business+Analytics
version: 5
---

**TOTVS Business Analytics**

---

A integração TOTVS Business Analytics com aplicativos BI (Business Intelligence) irá proporcionar a comunicação com outros aplicativos BI de outras linhas TOTVS e também com linhas terceiras de uma maneira padrão.  
    
 Esta integração irá utilizar o conceito de Stage Area, que é apenas um repositório de dados intermediário (Conjunto de tabelas), o importante é que este terá o mesmo formato para todos os BackOffices da TOTVS (Todos utilizarão do mesmo diagrama de banco de dados para criação das tabelas, ou seja, as tabelas pertencentes no Stage Area existirão na base de todos os BackOffices TOTVS). O BI ficará responsável por sincronizar os dados do Stage Area para as tabelas internas do BI.   
    
 Com este padrão adotado o BI poderá recuperar todos os dados do BackOffice de forma padrão, ou seja, esta comunicação não mudará conforme o BackOffice TOTVS utilizado.  
   
    
 O preenchimento da Stage Area irá acontecer via Conceitos, que devem ser importados na visão do Configurador. A utilização de Conceitos como recurso de carga à Stage Area irá possibilitar aos clientes que agendem Jobs de execução conforme sua necessidade.  
    
 A criação da Stage Area irá acontecer via tela do Configurador, sendo que as tabelas da Stage Area estão disponíveis a partir da versão 11.50.  
    
 Como o conjunto de tabelas do RM é bastante extenso e complexo foram criadas views que representam os dados a serem importados do BackOffice RM, e os Conceitos não irão ler diretamente os dados das tabelas do BackOffice RM e sim das views que representam estas tabelas, conforme figura abaixo:  
    
   
    
 Além de executar o Configurador deve ser realizada a parametrização da integração. Neste momento a aplicação irá configurar, mapear as tabelas que deverão ser utilizadas e itens que serão usados como filtro quando realizar a extração dos dados para a criação das views.

* Saiba sobre **Configurador**,
* Saiba sobre **Parâmetros**,
* Saiba sobre **Dimensões/Fatos e Período Inicial e Final de Extração**,

**Observação.:**

Informamos que os indicadores abaixo descritos não são contemplados pela linha RM:  
  
**Segmento Materiais:**

* Materiais / Gestão de importação /Importação – faturamento
* Materiais / Gestão de importação /Importação – Despesas
* Materiais / Gestão de importação /Importação - Acompanhamento
* Materiais / Gestão da Qualidade / Qualidade Carteira
* Materiais / Gestão da Qualidade / Qualidade

**Segmento Finanças**

* Finanças/ Gestão do Fluxo Financeiro / Fluxo de Caixa Realizado
* Finanças/ Gestão do Fluxo Financeiro / Fluxo de Caixa Previsto

**Segmento Controladoria**

* Controladoria / Gestão Contábil e Orçamentária / Indicadores Gerenciais
* Controladoria / Gestão Contábil e Orçamentária / Orçamento

**Produção**

* Todos
