---
content_hash: 23f5dc7db11c7d74c67bf24e5d3995248edbb28538e4462bb2bfc160686b51b7
fetched_at: '2026-06-29T00:10:38.573558+00:00'
page_id: '544208913'
product: rm
source: tdn-rm
title: Apuração de IRPJ e CSLL com Origem Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544208913
version: 6
---

**Legislação**[Link da Legislação](https://tdn.totvs.com/pages/viewpage.action?pageId=544210606)

### **1 - Cadastro Gestão Fiscal -> Obrigações Principais -> Eventos Tributários → Estrutura → (Registro) →   Regras Tributárias**

Nos grupos de Adição do Lucro e Exclusão será exibida a opção *"Patrimonial"* no campo *"Origem da Informação"*.

Com a origem *Patrimonial* selecionada, as pastas *Efeito Parte B*, *Processos Judiciais/Administrativos* e *Patrimônio* estarão visíveis.  
Na nova pasta "*Patrimônio*", serão exibidas as opções de seleção dos cenários de cálculo Contábil e Fiscal.

Observação

Após a seleção dos cenários no grupo de adição, as mesmas parametrizações dos cenários serão consideradas no grupo de exclusão ou vice e versa.

### **2 - Cadastro Gestão Fiscal -> Obrigações Principais -> Eventos Tributários → Estrutura →  Simulação –>  Regra de Apuração**

O detalhamento dos patrimônios que formam o valor processado do *Item do Evento* está na pasta *Patrimônio* da simulação.

Os dados desta pasta podem ser exportados em formato *.xlsx* ou .*txt* para conferência dos valores que estão sendo gerados nos grupos de Adição ou Exclusão.

Informações

Esta pasta será exibida quando existe pelo menos um item do Evento de origem Patrimonial e estiver devidamente parametrizado e com registros a serem exibidos.

### **3 – Serviço de Cálculo do Evento Tributário que é executado por meio dos processos de Encerramento dos Períodos IRPJ\CSLL ou Simulação do Evento Tributário.**

O cálculo do evento tributário considera a parametrização da origem *Patrimonial*.

Os parâmetros Informados para execução do serviço do *Gestão Patrimonial*, que retorna os valores da depreciação ajustada, são: *Código da Coligada*, *Lista de Filiais* (mesma raiz CNPJ ou somente a filial SCP), *Data Início da Escrituração*, *Data Final do Período*, *Código do Cenário Fiscal* e *Código do Cenário Contábil.*

   
Este serviço retorna os devidos valores calculados da depreciação ajustada por patrimônio. Então, é calculado o resultado com [Valor Depreciação Contábil] - [Valor Depreciação Fiscal].

   
Se o resultado deste cálculo somado a todos os patrimônios for positivo, então o valor é incluído no item do evento tributário do grupo de Adição.   
Caso o valor seja negativo, então é incluído no grupo de Exclusão.

Informações

* O Item de Apuração com origem Patrimonial será exibido normalmente no detalhamento da apuração após o encerramento do Período IRPJ\CSLL

* Para que o cálculo do valor da depreciação seja corretamente carregado para a apuração do tributo a liberação da competência no TOTVS Gestão Patrimonial deverá obedecer a periodicidade dos tributos IRPJ e CSLL.

**Ex.:** Se a apuração do primeiro trimestre estiver sendo executada, no TOTVS Gestão Patrimonial deverão estar liberadas as competências de janeiro, fevereiro e março.

### **4 – Gestão Fiscal -> Obrigações Principais -> Período de Apuração IRPJ\CSLL -> Processos -> Gerar Lançamentos Automáticos (Efeito na Parte B)**

O processo considera a origem Patrimonial na geração dos lançamentos com Efeito na parte B.

### **5 – Geração da Rotina Federal ECF - Escrituração Contábil Fiscal**

Consideram-se os lançamentos Lalur B com vinculo a um item de apuração com origem Patrimonial, gerando quando existentes os registros\_GoBack M305\M355 da ECF.
