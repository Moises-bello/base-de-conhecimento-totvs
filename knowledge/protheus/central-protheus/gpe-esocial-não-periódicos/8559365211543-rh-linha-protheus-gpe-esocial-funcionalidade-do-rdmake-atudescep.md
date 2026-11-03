---
article_id: 8559365211543
category: GPE - eSocial - Não Periódicos
content_hash: d1a3ab5f7eab5d542b7ce174f27660b94e3e2a38402e96ee1e8e12d53689d365
fetched_at: '2026-06-28T22:45:04.378987+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Funcionalidade do rdmake ATUDESCEP
type: support-article
updated_at: '2026-06-16T12:51:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8559365211543-RH-Linha-Protheus-GPE-eSocial-Funcionalidade-do-rdmake-ATUDESCEP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25649678061463) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Qual a funcionalidade do rdmake ATUDESCEP?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O rdmake **ATUDESCEP**, efetuará a alimentação do campo **RA\_DESCEP** (controle de matrícula TSV) dos registros de trabalhadores sem vínculo, que possuam evento S-2300 gerado com informação de matrícula de acordo com o leiaute S-1.0, sem o campo preenchido, e já integrados ao TAF ou Middleware.  
  
O rdmake também ajustará o conteúdo do campo **RA\_DESCEP** (Controle de matricula TSV), quando o evento S-2300 foi enviado sem as informações de matricula e o campo possua conteúdo  
  
O programa só deve ser executado caso apresente a inconsistência reportada acima, após atualização do dicionário de dados.  
  
Além da **compilação do Rdmake,** para o correto funcionamento da rotina é necessário possuir o **grupo de perguntas UPDDESCEP** em seu ambiente. Caso não exista, ele deve ser criado manualmente, seguindo as orientações abaixo:

* Acesse no Configurador (SIGACFG), o menu Base de Dados > Dicionário > Base de Dados > Perguntas: Selecione a opção Incluir;
* Informe o Grupo **UPDDESCEP** e complete os campos com as informações abaixo:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **Pergunta** | **Tipo** | **Tamanho** | **Consulta Padrão** | **Validação** | **Objeto** | **Conteúdo (Text/Range)** |
| 1 | Filial ? | Caracter | 99 | XM0 |  | 4 - Range | RA\_FILIAL |
| 2 | Matricula ? | Caracter | 99 | SRA |  | 4 - Range | RA\_MAT |

Documentação completa: <https://tdn.totvs.com/pages/releaseview.action?pageId=658751522>  
  
Para a utilização da rotina, deverá ser efetuado a inclusão manual no menu do módulo SIGAGPE, cadastrando o item como função de **usuário**.  
  
O **rdmake ATUDESCEP** está disponível na pasta rdmake do pacote de expedição continua:   
[Atualização de Arquivos fontes RH Expedição Continua](https://suporte.totvs.com/portal/p/10098/download?e=1070590#all/all/all/search/rh_expedicao_continua)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
