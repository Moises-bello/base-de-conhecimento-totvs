---
content_hash: d1c0f98acd52cea1ea96cd279bcfecac6a78d402e021c8823ba8647738650adf
fetched_at: '2026-06-29T00:08:30.246604+00:00'
page_id: '272413469'
product: rm
source: tdn-rm
title: 100048 MEDU-69 DT ECF Automação Lalur B Origem Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272413469
version: 15
---

# ECF - Escrituração Contábil Fiscal

# Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Fiscal* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *ECF* | *Escrituração Contábil Fiscal* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Simulação* | *Simulação do Evento Tributário* | | *Encerramento* | *Encerramento do Período de Apuração* | | *Evento Tribuário* | *Cadastro do Evento Tributário* | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** | *Não se Aplica* |
| **Ponto de Entrada:** | *Não se Aplica* |
| **Ticket Relacionados** | *MEDU-69* |
| **Requisito (ISSUE):** | *FIS000428* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server; Oracle* |
| **Tabelas Utilizadas:** | DITMEVCTRB; |
| **Sistema(s) Operacional(is):** | Windows |

# **Implementação Linha RM**

**Legislação**

[Link da Legislação](http://tdn.totvs.com/pages/viewpage.action?pageId=268570059)

**Gestão Patrimonial**

Foi solicitado um serviço do modulo Gestão Patrimonial que retorne os valores da depreciação ajustada do patrimônio nos cenários contábil e fiscal.  
 Esta implementação foi realizada através da Issue: **MEDU-736**

[Link Cálculo Depreciação Ajustada - Gestão Patrimonial](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.CalculoDepreciacao.aspx)

## **Gestão Fiscal**

### **1 - Cadastro Gestão Fiscal -> Obrigações Principais -> Evento Tributários -> Regras Tributária**

Nos grupos de Adição e Exclusão será exibida a opção "Patrimonial" no campo "Origem da Informação".

Com a origem Patrimonial selecionada as pastas Efeito Parte B, Processos Judiciais/Administrativos e Patrimônio serão exibidas.  
 Na nova pasta "Patrimônio" serão exibidas as opções de seleção dos cenários de cálculo Contábil e Fiscal.

Observação: Após a seleção dos cenários no grupo de adição a mesma parametrização dos cenários serão consideradas no grupo de exclusão ou vice e versa.

### **2 - Cadastro Gestão Fiscal -> Obrigações Principais -> Evento Tributários -> Simulação – Regra de Apuração**

Implementação da pasta Patrimônio na simulação para detalhamento dos patrimônios que formam o valor processado do Item do Evento.

Os dados desta pasta podem ser exportados em formato .xlsx ou .txt para conferência dos valores que estão sendo gerados nos grupos de Adição ou Exclusão.

Observação: Esta pasta será exibida quando tem item do Evento de origem Patrimonial devidamente parametrizado e com registros a serem exibidos.

### **3 – Serviço de Cálculo do Evento Tributário que é executado através dos processos de Encerramento dos Períodos IRPJ\CSLL ou Simulação do Evento Tributário.**

Implementação do cálculo do evento tributário com considerando a parametrização da origem Patrimonial.

Os parâmetros Informados para execução do serviço do Gestão Patrimonial que retorna os valores da depreciação ajustada são: Código da Coligada, Lista de Filiais mesma raiz CNPJ ou somente a filial SCP, Data Início da Escrituração, Data Final do Período, Código do Cenário Fiscal e Código do Cenário Contábil

   
 Este serviço retorna os devidos valores calculados da depreciação ajustada por patrimônio então é calculado o resultado com [Valor Depreciação Contábil] - [Valor Depreciação Fiscal].

   
 Se o resultado deste cálculo somado a todos os patrimônios for positivo então o valor é incluído no item do evento tributário do grupo de Adição.   
 Caso o valor seja negativo então é incluído no grupo de Exclusão.

**Observação: O Item de Apuração com origem Patrimonial será exibido normalmente no detalhamento da apuração após o encerramento do Período IRPJ\CSLL**

**Para que o cálculo do valor da depreciação seja corretamente carregado para a apuração do tributo a [liberação da competência](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.LiberacaoCompetencia.aspx) no TOTVS Gestão Patrimonial deverá obedecer a periodicidade dos tributos IRPJ e CSLL.**

**Ex.: Se a apuração do primeiro trimestre estiver sendo executada,  no TOTVS Gestão Patrimonial deverão estar [liberadas as competências](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.LiberacaoCompetencia.aspx) de janeiro, fevereiro e março.**

### **4 – Gestão Fiscal -> Obrigações Principais -> Período de Apuração IRPJ\CSLL -> Processos -> Gerar Lançamentos Automáticos (Efeito na Parte B)**

O processo passara a considerar origem Patrimonial na geração dos lançamentos com Efeito na parte B.

### **5 – Geração da Rotina Federal ECF - Escrituração Contábil Fiscal**

Considerar lançamentos Lalur B com vinculo a um item de apuração com origem Patrimonial gerando quando existente os registros\_GoBack M305\M355 da ECF.
