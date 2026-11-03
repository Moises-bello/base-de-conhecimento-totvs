---
article_id: 1500008090002
category: Anuais
content_hash: 1fe9a7f04acb309e4c61c554fbb52f012c0b24ed794aa75105eb7564b26dc426
fetched_at: '2026-06-28T22:46:51.131921+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - DIRF/Informe de Rendimentos: Rendimentos Recebidos Acumuladamente'
type: support-article
updated_at: '2025-03-13T10:06:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008090002-RH-RM-FOP-DIRF-Informe-de-Rendimentos-Rendimentos-Recebidos-Acumuladamente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura **00:04:00 min  
  
Dúvida**Como é realizado o processo para cálculo e lançamento de RRA?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de pagamento - Todas as versões  
  
**Solução**No TOTVS Folha de Pagamento, para gerar as informações dos Rendimentos Recebidos Acumuladamente dos funcionários que receberam este tipo de verba, existem dois processos:

* **Parametrização via Histórico de RRA - INSERIDO MANUALMENTE**

Caso as verbas sejam **oriundos das decisões das Justiças do Trabalho, Federal, Estaduais e do Distrito Federal**, deverá cadastrar o Histórico de RRA, que está localizado no cadastro dos Funcionários.

* No cadastro de funcionários, o histórico estará disponível no menu **Anexos I Históricos I Histórico RRA**

Exemplo:![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011675702/mceclip1.png)  
  
Visualização no Informe de Rendimentos:Os dados preenchidos no histórico serão impressos nos campos do item 6 – RENDIMENTOS RECEBIDOS ACUMULADAMENTE-ART 12-A DA LEI N7.713, de 1988:*![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011953641/mceclip3.png)*- Os campos referentes a **Dados do Advogado(a)** e **Nro Processo** passam a ser obrigatórios;

- Deverão ser incluídos históricos específicos, para cada processo de um mesmo funcionário;

- Deverão ser incluídos históricos específicos, para cada dependente o valor da Pensão Alimentícia.

* **Parametrização Via Cálculo / Lançamento de Diferenças**

Caso as verbas sejam **provenientes do trabalho**, não por processo judicial, deverá ser lançado no envelope os eventos provenientes de diferença salarial por dissidio, com os códigos de cálculo específicos para RRA.

Para realizar o processo corretamente, execute os seguintes passos:

1. Acesse o menu Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Geral e marque a flag **Utiliza Cálculo de RRA****![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011961801/mceclip6.png)**2. Cadastre todos os códigos de calculo específicos para RRA conforme tabela abaixo:

| **Código de Cálculo** | **Descrição** |
| --- | --- |
| 204 | Base IRRF RRA |
| 205 | INSS Descontado RRA |
| 206 | Pensão Alimentícia Judicial RRA |
| 207 | IRRF RRA |
| 208 | Base IRRF RRA Férias |
| 209 | INSS Descontado RRA Férias |
| 210 | Pensão Alimentícia Judicial RRA Férias |
| 211 | IRRF RRA Férias |
| 212 | Base IRRF RRA 13º Salário |
| 213 | INSS Descontado RRA 13º Salário |
| 214 | Pensão Alimentícia Judicial RRA 13º Salário |
| 215 | IRRF RRA 13º Salário |
| 216 | Mês RRA |
| 217 | Mês RRA Férias |
| 218 | Mês RRA 13º Salário |

3. Para que o sistema tenha referência para cálculo dos valores, cadastre a tabela de cálculo IRRF de RRA no menu **Administração de Pessoal I Cálculos I Tabelas de cálculos**  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011954461/mceclip5.png)

* Deverá cadastrar tabela de IRRF de RRA com vigência no ano referência dos eventos, se o pagamento das diferenças for em janeiro 2021 retroativo a 12/2020, irá cadastrar a tabela de 2020;
* Deverá cadastrar as faixas de calculo IRRF de RRA com os valores específicos, para o cálculo correto do desconto;
* Deverão ser incluídos históricos específicos, para cada dependente o valor da Pensão Alimentícia.

4. Depois de realizar a alteração salarial poderá executar a rotina de diferença salarial:  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011967641/mceclip7.png)  
  
5**.** No envelope do funcionário, serão lançados os eventos de base para RRA:  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011696562/mceclip8.png)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011698022/mceclip9.png)  
  
6**.** Visão do informe de rendimentos:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011752362/mceclip10.png)

* Para calculo das diferenças, será verificado como ano anterior o mês e ano de competência e não o caixa (data de pagamento);
* Para geração do informe de rendimentos, será validado o mês e ano caixa (data de pagamento);

**Saiba mais**[FOP\_0003\_DIRF - Rendimentos Recebidos Acumuladamente (RRA)](https://tdn.totvs.com/pages/releaseview.action?pageId=208347807)
