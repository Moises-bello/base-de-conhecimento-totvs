---
article_id: 4402811329943
category: PONTO ELETRÔNICO
content_hash: c719e6b29c2450c3edc5607dbed0de0cc7af8ac7405b3b13e4e534f7b375c25c
fetched_at: '2026-06-28T22:44:36.701453+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Quais são os parâmetros do Espelho de Ponto
  gerado através do MEU RH
type: support-article
updated_at: '2026-06-19T13:58:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402811329943-RH-Linha-Protheus-MEU-RH-Quais-s%C3%A3o-os-par%C3%A2metros-do-Espelho-de-Ponto-gerado-atrav%C3%A9s-do-MEU-RH
---

**Dúvida**  
Quais são os parâmetros do Espelho de Ponto gerado através do MEU RH?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Para realizar a download do Espelho de Ponto você pode conferir o artigo artigo: [**RH - Linha Protheus - MEU RH - Como realizar o download do espelho de ponto no MEU RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012179441)  
  
Esse Espelho de Ponto gerado através do **MEU RH** é idêntico ao impresso através do módulo **16-SIGAPON** (**PONR010**), porém o usuário final do **MEU RH** não tem conhecimento sobre os parâmetros de impressão, sendo assim foi definido que esse relatório seguirá um parâmetro padrão, os detalhes estão descritos através do [**Boletim Técnico Relatórios Meu RH Protheus**](https://tdn.totvs.com/display/NPR/Relatorios+Meu+RH+Protheus)**.**  
  
Entretanto, devido a necessidade de algumas Empresas foi disponibilizado a possibilidade de customização desse relatório através do RDMAKE **IMPESP.PRX**, ou seja, cada Empresa pode definir os parâmetros de impressão entre outros. O artigo sobre a disponibilização da melhoria pode ser acessado através do link: [**RHMOBILE01-15325 DT Espelho de Ponto Personalizado no Meu RH**](https://tdn.totvs.com/display/NPR/RHMOBILE01-15325+DT+Espelho+de+Ponto+Personalizado+no+Meu+RH)  
  
A partir da versão do fonte RHNP06 de 10/06/2021, no momento da impressão será verificado a existência do RDMAKE **IMPESP.PRX** no RPO do **MEU RH**, caso não exista o download/impressão seguirá o padrão (**PONR010**).  
  
**Lista dos parâmetros envolvidos na rotina:**  
  
**MV\_ABOSEVE** - Deduz Horas Abonadas das Horas Apontadas sem a necessidade de associar um motivo a um evento. Onde "S" - Deduz e "N" - Não Deduz (Valor Padrão)   
**MV\_COLMARC** - Numero máximo de conjuntos de Entrada e Saída a serem considerados num período de marcações. Ex: 4 --> para 8 marcações.   
**MV\_DABERTO** - Informe a quantidade de dias corridos após o fim do período para manutenção do ponto pelos funcionários.   
**MV\_GETMAUT** - Carregar as Marcações automáticas nos processos de Leitura/Apontamento de Marcações. "S" - Carrega (Valor Padrão) e "N" - Não Carrega   
**MV\_HORASDE** - Digitação da fração de horas no movimento mensal (SRC) será em minutos ? (S)im ou (N)ao   
**MV\_IMPBHBX** - Listar Banco de Horas baixado no Portal GCH?   
**MV\_MRHDPER** - Informe o numero de dias que serão somados a data final do período do ponto (conforme **MV\_PONMES**), para a liberação do prox. período   
**MV\_NOMESOC** - Visualização do Nome Social para o Meu RH.   
**MV\_PONMES** - Período de Apontamento em aberto para a Apuração das Marcações/Apontamentos no Ponto Eletrônico Será atualizado pelo sistema no Fechamento Mensal.  
**MV\_SUBABAP** - Gerar Hrs de Abono no Evento Relacionado subtraindo-as das Horas Calculadas quando Motivo Não Abona Horas e possui Evento. S=Sim ; N=Não   
**MV\_TCFBHVL** - Indica como será exibido o saldo do banco de horas no App Meu RH. Onde .T. = horas valorizadas, e .F. = horas reais (padrão).   
**MV\_PAPONTA** - Período para apontamento das marcações 0131  
  
Alguns parâmetros, são referenciados somente se o *RDMAKE* **IMPESP, for customizado**.  
  
**Importante**  
Caso tenha algum problema no download/impressão do arquivo, por gentileza efetue as validações do artigo: [**RH - Linha Protheus - MEU RH - O que fazer quando download de demonstrativo apresenta "Falha ao carregar documento PDF"?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042996014)  
  
Para saber como Compilar o RDMAKE no seu RPO acesse o artigo: [**MP - Compilação de RDMakes**](https://tdn.totvs.com/pages/viewpage.action?pageId=73077498). Os clientes que utilizam o serviço **TOTVS** ***CLOUD***devem solicitar os dados para compilação junto ao atendimento do ***CLOUD***([URA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115014381228-EC-URA-Fluxo-de-telefonia-4003-0015)).  
  
**Saiba Mais**  
[**RH - Linha Protheus - MEU RH - Como registrar a marcação de Ponto através da rotina Relógio (Geolocalização)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050355093)  
[**RH - Linha Protheus - MEU RH - Como verificar o espelho de ponto em período futuro**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5223165502359)  
[**RH - Linha Protheus - MEU RH - É possível ocultar/exibir o relatório do espelho de ponto conforme o perfil do usuário**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421930223383)  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)  
[**CLIQUE AQUI** para conferir Roadmap do MEU RH - Protheus](https://tdn.totvs.com/display/NPR/Roadmap+-+Protheus)
