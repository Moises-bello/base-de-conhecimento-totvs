---
content_hash: 48fda89325e94eaae19f2a0592a032d0b05ed25f1faa7d6029f71c0e0bbfd5c5
fetched_at: '2026-06-29T00:11:28.309603+00:00'
page_id: '73074440'
product: rm
source: tdn-rm
title: Visualizar boleto bancário no Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=73074440
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.00 |
| **Processo** | **:** | Visualizar boleto |
| **Subprocesso** | **:** | Visualizar boleto bancário no Portal Educacional |
| **Data da publicação** | **:** | 26/07/2013 |

**Acesse:** **RM Classis** **Ensino** **Superior/Relatórios/Gerador**

Localize o Boleto na qual deseja visualizar no Portal e dê um Duplo Clique sobre ele.

Relatório 05.014 – Boleto Banco Bradesco

Depois de aberto o relatório, seleciona a opção Campo da Base

Para que um relatório possa ficar visível no Portal Educacional é obrigatoriamente preciso ter dois campos de Base incluídos no relatórios.

Os campos são: **FLAN.IDLAN ;** **FLAN.CODCOLIGADA**

Veja um exemplo:

Pesquiso o campo que contêm FLAN. IDLAN e depois arrasto para o Relatório todo o conteúdo do Ref.Lançamento.

Neste exemplo pesquiso o campo FLAN.IDCOLIGADA e depois arrasto para o Relatório todo o conteúdo de Lançamentos.

Depois de feita estas devidas parametrizações no Relatório deve selecionar a opção Filtros como mostra o print abaixo:

O Filtro deve estar desta forma: Ref.Lancamento = Vazio e Coligada = Vazio.

Os parâmetros "Ocultar Filtros constante na janela de Filtros Temporários" "Gravar últimos valores na janela de filtros temporários" devem estar desmarcados.

Feita a parametrização do Filtro, fechar o Relatório   
   
   
   
 Seleciona o Relatório novamente e em seguida a opção: Editar

O Relatório tem que estar com estas devidas parametrizações: Tipo de Documento: Boleto - Tipo de Saída: Padrão.   
   
 **Acesse:** **TOTVS Gestão** **Financeira/Sistema/Server/Executar** **processos**

Inicie o executor de processos para ser possível visualizar o boleto no Portal.

**Vá ao** **RM Classis** **Ensino** **Superior** **e acesse:** **Opções/** **Parâmetros/Portal** **Educacional**

Dentro dos parâmetros do Portal Educacional, localize a Janela " Tesouraria"

E informe o relatório parametrizado para ser utilizado no Portal.   
   
   
 **Vá ao** **PORTAL EDUCACIONAL** **informe** **o** **usuário** **e** **senha para logar.**

Selecione a opção: 2º Via de Boleto

Selecione um dos dois lançamentos que o aluno possui e clique na Impressora.

Após feita a solicitação de impressão... Boleto impresso via Portal Educacional. Obs.: O usuário tem que ter o Programa para visualização de PDF instalado em sua máquina.
