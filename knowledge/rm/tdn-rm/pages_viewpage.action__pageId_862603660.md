---
content_hash: c01bbbdd7ea2bc9d0e8d03c3053779855371228cf3c2febe28313c3ae88456b1
fetched_at: '2026-06-29T00:11:55.635827+00:00'
page_id: '862603660'
product: rm
source: tdn-rm
title: Dashboard Ponto - Gera os indicadores de Funcionários e Marcações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862603660
version: 32
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Função: | Criar um processo com todas as informações do Dashboard |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHJORNRM-6774](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-6774)  [DRHJORNRM-6775](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-6775) |

## **02. SITUAÇÃO/REQUISITO**

Criar um processo com todas as informações do Dashboard garantindo performance na geração do Relatório.

**03. SOLUÇÃO**

* Foi criado o processo **" Gera os indicadores de Funcionários e Marcações "**, em Relatórios| Análise| Dashboard. Esse processo irá gravar as informações em tabelas garantindo melhor performance na visualização do relatório Dashboard .
* Na tela do Dashboard foi criado o  botão **"Recalcular" .** Por **default** virá com a opção "**Não"** e o sistemairá buscar as informações geradas do processo **"Gera os indicadores de Funcionários e marcações",** caso informe **"Sim"**, o sistema irá calcular todas as informações com base na seleção.

Para utilizar o novo processo o usuário deverá realizar os seguintes procedimentos:

Acesse o Totvs Automação de Ponto, através do Menu **Serviços Globais**-**Segurança**-**Perfis** e permita acesso ao item 06.02.03.03-Gera os indicadores de Funcionários e Marcações.

Importante:

* Será necessário realizar a execução do Processo "Gera indicadores de Funcionários e Marcações" , caso utilize o botão **"Recalcular -Não".** Ao efetuar a abertura do Dashboard de marcações, caso não tenha sido executado será listada as filiais com os totais zerados.
* Sempre que desejar carregar novas informações, deverá após informar Data de Início, Data de Término, selecionar o local , Recalcular(Não-Sim) e clicar em ***Atualizar**.*
* Os campos "Data de Início" e "data de Término" da tela do Dashboard passou a considerar a data atual.

**04. VERSÕES**

12.1.2406\_157 e superiores

## **05. EXEMPLO DE UTILIZAÇÃO**

11Gerando os Indicadores de Funcionários e Marcações

Acesse o menu Relatórios| Análise| Dashboard e selecione " Gera os indicadores de Funcionários e Marcações ", será demonstrada a tela a seguir.

**Semanal:** Será executada a rotina para 7 dias, considerando a data de hoje.

*Exemplo:*Hoje é dia 03/09/2024, o período que será gravado nas tabelas será 28/08/2024 a 03/09/2024.

**Quinzenal:** Será executada a rotina para 15 dias, considerando a data de hoje.

*Exemplo:* Hoje é dia 03/09/2024,  o período que será gravado nas tabelas será  20/08/2024 a 03/09/2024.

**Mensal:**Será executada a rotina para 30 dias, considerando a data de hoje.

*Exemplo:* Hoje é dia 03/09/2024,  o período que será gravado nas tabelas será  05/08/2024 a 03/09/2024.

**Quantidade de dias:** Será executada a rotina de acordo a quantidade de dias informado, considerando a data de hoje.

No campo Quantidade Dias, deverá ser informado um valor entre 1 e 60. Caso seja diferente o sistema irá demonstrar mensagem para o usuário.

*Exemplo:*

Quantidade de dias igual 5.

A Data de hoje é 03/09/2024. Será considerado o período  03/09/2024 a 30/08/2024.

2Gerando Relatório Dashboard botão "Recalcular - Não ".

O botão recalcular **"Não",** irá buscar as informações gravadas na geração do processo **" Gera os indicadores de Funcionários e Marcações " .**

Acessar o menu Relatórios| Análise| Dashboard , informar a  data de Início, data de Término, selecionar  o local , verifique a opção do botão Recalcular **"Não"**  e Selecione **"Atualizar"** .

Será visualizado o Dashboard conforme tela a seguir:

3Gerando Relatório Dashboard botão "Recalcular - "Sim". ".

O botão recalcular **"Sim",** irá buscar as informações calculadas.

Para a geração do Dashboard, deverá acessar o menu Relatórios| Análise| Dashboard , informar a  data de Início, data de Término, selecione  o local , verifique o botão Recalcular **"Sim"**  e Selecione **"Atualizar"** .

Confirmado o botão **"Sim"** e selecionado **"Atualizar".**

## **06. ASSUNTOS RELACIONADOS**

[Dashboard Ponto](https://tdn.totvs.com/display/public/LRM/Dashboard++Ponto)
