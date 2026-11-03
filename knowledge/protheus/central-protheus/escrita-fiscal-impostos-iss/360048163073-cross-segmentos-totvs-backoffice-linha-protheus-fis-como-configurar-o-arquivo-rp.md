---
article_id: 360048163073
category: Escrita Fiscal - Impostos - ISS
content_hash: c9183d640774bbb077a4a8244adec017fe550d1e1d219666a0b1250d014c8120
fetched_at: '2026-06-28T22:39:35.204725+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o
  arquivo RPS.DOT para utilização na rotina MATA916
type: support-article
updated_at: '2021-06-10T13:22:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048163073-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-arquivo-RPS-DOT-para-utiliza%C3%A7%C3%A3o-na-rotina-MATA916
---

**Dúvida:**

Como faço para utilizar a rotina de impressão de RPS via MATA916.  
  
**Ambiente:**

Protheus – Faturamento – A partir da versão 11.80.  
  
**Solução:**

**Imposto do RPS – Recibo Provisório de Serviços**  
Após a emissão dos RPSs será possível imprimi-los, através de duas maneiras distintas: através de integração com o MS-Word® ou através da rotina de impressão gráfica**.**  
  
**Integração com o MS-Word®**  
A rotina disponibiliza um modelo padrão para impressão do RPS, através de um arquivo .DOT. Esse arquivo pode ter o seu layout alterado, de acordo com as necessidades de cada empresa. Para tanto, basta abrir o arquivo .DOT no MS-Word® e efetuar as alterações necessárias.  
Esta rotina não terá funcionalidade no ambiente Linux, pelo fato de não ser possível a utilização do MS-Word®. Caso o ambiente seja Linux, é necessário utilizar a rotina de impressão gráfica.  
  
No módulo **Configurador (SIGACFG)**, acesse **Ambiente/ Cadastros/ Menus**, insira a opção de impressão do RPS no menu do módulo**Livros Fiscais (SIGAFIS)**.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome do menu** | **Submenu** | **Nome da rotina** | **Programa** | **Tabelas** |
| Relatórios | Impressão Doctos. | Impressão RPS | MATA916 | SA1, SA2, SF3, SC5, SC6, SC9 |

Em **Relatórios/Impressão Doctos./Impressão RPS**(MATA916), informe os parâmetros da rotina conforme instruções a seguir:

**Diretório .DOT ?**  
· Informe o diretório em que o arquivo padrão de impressão (.DOT) está gravado.   
Exemplo: C:\MP8\SYSTEM\.  
**Arquivo .DOT ?**  
· Informe o nome do arquivo padrão de impressão, incluindo a extensão .DOT. Ex.: RPS.DOT  
**Emissão inicial ?**  
· Informe a data de emissão inicial dos RPSs que deverão ser selecionados para impressão.  
**Emissão final ?**  
· Informe a data de emissão final dos RPSs que deverão ser selecionados para impressão.  
**Cliente inicial ?**  
· Informe o código do cliente inicial dos RPSs que deverão ser selecionados para impressão. Caso deseje que todos os RPSs do período, independente dos clientes, sejam selecionados, deixe esta pergunta em branco.  
**Cliente final ?**  
· Informe o código do cliente final dos RPSs que deverão ser selecionados para impressão. Caso deseje que todos os RPS do período, independente dos clientes, sejam selecionados, informe ZZZZZZ.  
**Quanto à opção automática ?**  
· Informe, caso a opção automática seja selecionada na próxima tela:  
· Imprimir: para que os RPSs selecionados sejam automaticamente enviados à impressora.  
· Gravar: para que os RPSs selecionados sejam gravados para posterior impressão.  
**Diretório destino ?**  
· Caso a opção **Gravar** tenha sido selecionada na pergunta anterior, será necessário definir em qual diretório os RPSs gerados serão gravados. Exemplo: C:\RPS\.  
**RPS inicial ?**  
· Informe o número do RPS inicial para seleção dos documentos a imprimir. Caso deseje que todos os RPS das seleções anteriores sejam processados, deixe esta pergunta em branco.  
**RPS final ?**  
· Informe o número do RPS final para seleção dos documentos a imprimir. Caso deseje que todos os RPS das seleções anteriores sejam processados, informe ZZZZZZ.  
**Imprime cancelados ?**  
· Informe se os documentos cancelados devem ser considerados na seleção dos RPSs para impressão.  
  
Clique em **Confirmar**.  
  
É apresentada uma nova janela, com os RPSs selecionados através dos parâmetros da rotina. Nesta janela, existem duas opções de impressão:  
  
· **Manual**  
O RPS selecionado na tela será processado e enviado ao arquivo de modelo no MS-Word, sendo possível manipulá-lo.  
  
· **Automática**  
Todos os RPSs que estão sendo apresentados na janela serão diretamente impressos ou gravados para posterior impressão, de acordo com o que foi definido nas perguntas do relatório.  
Tanto na opção manual, como na automática, serão gerados os RPSs de acordo com o modelo definido pelo arquivo .DOT  
  
***PODERÁ ACESSAR A OUTRA ROTINA DE IMPRESSÃO DO RPS  EM GRÁFICO MUITO PRÁTICA A UTILIZAÇÃO  
MATR968  IMPRESSÃO GRÁFICA***
