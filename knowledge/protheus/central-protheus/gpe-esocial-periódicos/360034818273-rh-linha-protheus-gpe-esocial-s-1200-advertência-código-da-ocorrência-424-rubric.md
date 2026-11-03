---
article_id: 360034818273
category: GPE - eSocial - Periódicos
content_hash: fb2715cbe07d5506e798c7b46426c85baadf0bff181659a6e4f882540d4824a2
fetched_at: '2026-06-28T22:45:07.181885+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200 - Advertência - Código da ocorrência
  424: Rubrica não permitida em folha de decimo terceiro.'
type: support-article
updated_at: '2025-07-21T20:27:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034818273-RH-Linha-Protheus-GPE-eSocial-S-1200-Advert%C3%AAncia-C%C3%B3digo-da-ocorr%C3%AAncia-424-Rubrica-n%C3%A3o-permitida-em-folha-de-decimo-terceiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27150887725847) Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**Sequência: 000001 - Tipo: Advertência - Codigo da ocorrência: 424  
Localização: /eSocial/evtRemun/dmDev/infoPerApur/ideEstabLot/remunPerApur/itensRemun[x]/codRubr  
Descrição: Rubrica não permitida em folha de decimo terceiro.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**A inconsistência 424 ocorre quando é enviado o evento S-1200 referente ao 13º Salário (parcela final) e no conteúdo deste evento exista alguma Rubrica com Incidência diferente de 13º Salário. Conforme regra  do **eSocial** abaixo só são permitidas no S-1200 do 13º Salário rubricas com incidências especificas.  
  
**REGRA\_RUBRICA\_COMPATIVEL\_DECTERCEIRO**  
Se {indApuracao} for igual a [2] (décimo terceiro salário):  
a) No caso do evento S-1200, são permitidas apenas as rubricas cujo {codIncCP} em S-1010 seja igual a [00, 01, 12, 14, 16, 22, 26, 32, 92, 94, 96, 98], cujo {codIncIRRF} em S-1010 seja igual a [0, 1, 9, 12, 14, 32, 34, 42, 47, 52, 54, 62, 64, 68, 71, 77, 79, 81, 82, 83, 92, 94, 9012, 9014, 9032, 9034, 9054, 9832, 9834, 9042, 9047, 9052, 9062, 9064] e cujo {codIncFGTS} em S-1010 seja igual a [00, 12, 92]. Caso sejam informadas rubricas com {codIncCP}, {codIncIRRF} e/ou {codIncFGTS} diferentes dos valores acima citados, retornar "alerta";  
b) Nos casos dos eventos S-1202 e S-1207, são permitidas apenas as rubricas cujo {codIncCPRP} em S-1010 seja igual a [00, 12, 32, 91, 92] e cujo {codIncIRRF} em S-1010 seja igual a [0, 1, 9, 12, 14, 32, 34, 42, 47, 52, 54, 62, 64, 68, 71, 77, 79, 81, 82, 83, 92, 94, 9012, 9014, 9032, 9034, 9054, 9832, 9834, 9042, 9047, 9052, 9062, 9064]. Caso sejam informadas rubricas com {codIncCPRP} e/ou {codIncIRRF} diferentes dos valores acima citados, retornar "alerta";  
c) No caso do evento S-1200, são permitidas apenas as rubricas cuja {natRubr} seja diferente de [9253].  
  
**Solução**Para solucionar a inconsistência você deve analisar todas as verbas/rubricas informadas no evento S-1200 referente ao 13º Salário (parcela final) e certificar-se que todas estão com código de incidência específico para 13º Salário. Caso exista rubricas com incidências incorretas deve ser feito o ajuste, abaixo o passo a passo para analise das rubricas.  
  
**Artigo:** [Como ajustar incidência e validade de rubricas no governo, TAF e GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512)  
  
**Passo 1 -** Para verificar as verbas informadas no evento S-1200 você pode acessar no módulo TAF (84) as opções Atualizações > Eventos eSocial > Periódicos > Folha de Pagamento.  
![Jh2xpl714E.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099949014)  
  
**1.1** **-** Filtre o nome ou CPF do trabalhador, selecione o período e a opção "Visualizar".  
**OBS:** Para folha de 13° o período de apuração será apresentado somente o ano, exemplo: 2020.  
![UO1uwVrCOD.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099949174)  
  
**1.2 -** Ao abrir o evento você deverá ir na aba "**Demonstrativo de Valores"** e descer a barra de rolagem até o final da página, no último quadro você visualizará todas as verbas/rubricas existentes no evento. **OBS:** Para todas as rubricas desse evento deve ser analisada a incidência no **GPE**, **TAF**, e **Governo**.  
![rCN3JhSVsg.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099949274)  
 **1.3 -** A outra opções seria a geração do Relatório de Conferência do S-1200 onde é possível verificar as verbas geradas no S-1200 e as incidências das mesmas no GPE através da coluna "**Incidência INSS, IRRF ou FGTS eSocial**"  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no GPE antes de integrar o evento periódico para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-m%C3%B3dulo-GPE?source=search)  
  
**Passo 2 - Analise GPE**Para verificar a incidência das verbas/rubricas acesse no **módulo GPE (07)** as opções Atualizações > Definições de Cálculo > Verbas.  
![EVRjSt3UwT.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001049522)  
  
**2.1 -** Filtre a verba desejada conforme verbas enviadas no S-1200 do 13°, selecione a opção "**Visualizar**" e na aba eSocial serão apresentadas as opções destacadas na imagem abaixo.  
![o4Wrflbsu1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001049702)  
  
A **configuração das Verbas/Rubricas com relação a Natureza e as Incidências Tributárias** é algo **particular de cada Empresa** e que deve ser analisado em conjunto com o departamento Jurídico e Contábil, porém, nessa situação, no evento S-1200 referente ao 13º Salário (parcela final) deverão existir somente verbas/rubricas com incidência de 13º Salário.  
  
**2.2 -** No exemplo abaixo está destacado a Incidência de Previdência Social e nela existe o código '12' que é específico para base de Cálculo da Contribuição para a Previdência Social do 13º Salário, ou seja, se sua verba/rubrica estiver cadastrada com o código '11' o RET (Governo) retornará essa mensagem de inconsistência.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10975491730967)

**Passo 3 - Analise TAF**Seguindo a mesma lógica do **Passo 2**, verifique no Cadastro de Rubricas do TAF se as informações da aba eSocial estão condizentes com a realidade da Verba, por exemplo, se é uma verba da Natureza de 13º Salário é importante que os Códigos de Incidência Tributária sigam a mesma lógica e que estejam de acordo como esperado pelo leiaute do eSocial. Além disso, também é necessário observar se a data de Inicio de Validade dessa Rubrica contempla o Período ao qual o evento S-1200 se refere.  
![0YCJUtbP56.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099949654)  
  
**Passo 4 - Analise Governo**Verifique no site do governo no caminho Empregador > Tabelas > Rubricas, se as informações das rubricas estão corretas. As incidências devem ser iguais no **GPE, TAF** e **Governo**.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054097433)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054097333)  
  
**Saiba Mais**  
Para adquirir mais conhecimento acesse os links abaixo:   
[MP - GPE - eSocial - S-1010 - Como configurar a Natureza e Código de Incidência Tributária das Verbas/Rubricas?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023121291)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes) [*Para conhecimento dos eventos futuros, acessa a nossa página*](http://tdn.totvs.com/x/4JQYEw)[***TOTVS Informa***](https://informa.totvs.com/)[*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa*](http://tdn.totvs.com/x/4JQYEw) *[**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
