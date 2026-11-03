---
content_hash: 873354040e01729a876e6b462aa14ef337141fdd7144b394fcc366ea27cb2224
fetched_at: '2026-06-29T00:10:42.718329+00:00'
page_id: '547253824'
product: rm
source: tdn-rm
title: ATUALIZAÇÃO DOS DEPENDENTES DE IRRF E DO HISTÓRICO DO NRO. DE DEPENDENTES
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547253824
version: 40
---

false

**A partir das Versões:**

* 12.1.25.274
* 12.1.26.221
* 12.1.27.176

## **ATENÇÃO!!!**

Identificamos uma situação na liberação de competência, referente ao processo de atualização de dependente de IRRF.  
Essa situação foi prontamente ajustada e disponibilizada a partir dos patches: 12.1.25.274, 12.1.26.221 e 12.1.27.176.  
Clientes que estão nas releases 12.1.28 ou inferiores a 12.1.25 não precisam se atentar a essa situação.  
   
Os patches que geraram essas inconsistências foram removidos da Central de Downloads, sendo eles:

* 12.1.25.269 a 12.1.25.273
* 12.1.26.214 a 12.1.26.220 e **12.1.26.230 a 12.1.26.238 (Somente base de dados Oracle)**
* 12.1.27.169 a 12.1.27.175  
     
     
  **IMPORTANTE:**
  1. Caso a competência já tenha sido liberada nos patches mencionados, será necessário a execução de um processo para atualização dos dependentes de IRRF. A previsão para liberação deste processo é 08/05/2020 e **deve ser executado antes do fechamento da Folha de Maio/20**.
  2. O problema na atualização de dependente de IRRF na liberação de competência ocorreu somente para o grau de parentesco "1-Filho Valido" ou "3-Menor Pobre", para estes casos o sistema desmarcou a incidência de IRRF no Cadastro do Dependente mesmo quando a idade do dependente é inferior a 22 anos ou inferior a 25 anos e é universitário.

**[PROCESSO PARA AJUSTAR OS DEPENDENTES](https://tdn.totvs.com/display/LRM/Ajuste+Dependente+IRRF)**

**ALTERNATIVA PARA AJUSTAR OS DEPENDENTES**

Caso exista algum backup anterior a liberação da competência, deverá seguir os seguintes passos:

1) Restaurar o backup (realizado antes da liberação da competência) em um ambiente **TESTE**;

2) Atualizar o ambiente **TESTE** com uma das versões mencionadas acima;

3) Liberar a Competência, para que o sistema atualize os dependentes e históricos de dependentes utilizando a nova versão.

4) Através do menu Integração | Gerador de Saídas | Layouts | Processos | Exportar Layout, exportar os dependentes e histórico de número de dependente, para os funcionários com situação diferente de "D-Demitido" e salvar em arquivo TXT, sendo os layouts:

* 09.004.003 - Exportação de Dependente
* 09.003.007 - Exportação de Históricos de Nro de Dependentes

5) Na base de **PRODUÇÃO**acessar o menu  Integração | Gerador de Saídas | Layouts | Processos | Importar Layout, e importar os arquivos do item 04);

  
Documentação Adicional

Segue os links com as documentações referentes a Importação de Dados do RM Labore:

* <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039126793-RM-FOP-Como-fazer-importa%C3%A7%C3%A3o-de-dados-do-RM-Labore->

**IMPORTANTE: Caso tenha realizado alguma modificação nas** **incidências****dos dependentes na base de PRODUÇÃO após a liberação de competência, é cenário refazer estas modificações após a importação dos arquivos.**
