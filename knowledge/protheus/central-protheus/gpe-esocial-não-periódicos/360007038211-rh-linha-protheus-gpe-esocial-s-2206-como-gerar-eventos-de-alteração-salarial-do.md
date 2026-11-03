---
article_id: 360007038211
category: GPE - eSocial - Não Periódicos
content_hash: 65d394f8bb0162babcedc931552dd4ceb33898b6f6ef29da1d52eb1beba5ae6c
fetched_at: '2026-06-28T22:45:04.694265+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206 - Como gerar eventos de alteração
  salarial do SIGAGPE para o TAF com Job/Schedule
type: support-article
updated_at: '2026-06-16T11:25:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007038211-RH-Linha-Protheus-GPE-eSocial-S-2206-Como-gerar-eventos-de-altera%C3%A7%C3%A3o-salarial-do-SIGAGPE-para-o-TAF-com-Job-Schedule
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28057072370199)** Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
S-2206 - Como gerar eventos de alteração salarial do SIGAGPE para o TAF?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Cada alteração salarial deve gerar um registro **S-2206**, e conforme *MOS* (Manual de Orientação do eSocial) o empregador deve, ainda, enviar o evento **S-2206** – Alteração de Contrato de Trabalho informando o valor do novo **salário**, e a **data** a partir da qual ele passou a ser devido.  
Para que o envio ocorra na data devida, foi desenvolvido no sistema um **JOB** configurado através de *Schedule*, sendo assim, o sistema busca a data da alteração salarial nas tabelas *SR3* e *SR7* (Histórico Salarial) do **SIGAGPE** e envia para o TAF na data correta, depois o usuário deve efetuar a envio do evento para o **RET**.  
  
**Para configurar o JOB no Schedule execute os passos abaixo:**  
  
**1.** Acessar o modulo Configurador (**SIGACFG**) e verificar se o parâmetro **MV\_DTCGINI** está com a data que indica, a partir de quando a empresa iniciou a entrega dos eventos não periódicos.   
Exemplo: 01/03/2018 **(1º GRUPO)**. [Parâmetros Esocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048411)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091646133)  
  
**Importante:** O parâmetro [**MV\_EFDAVIS**](https://tdn.totvs.com/pages/releaseview.action?pageId=286499282) deverá estar preenchido com algum conteúdo conforme documentação abaixo:   
  
**2.** No modulo Configurador (**SIGACFG**) acesse no menu o caminho Ambiente > Schedule > Schedule > e realize a inclusão conforme imagem de exemplo abaixo.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007348111)  
  
**3.** Inclua a função de Agendamento conforme imagem de exemplo abaixo.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007279912)  
  
**4.** Inclua as empresas que a rotina será executada conforme imagem de exemplo abaixo.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007280032)  
  
**5.** Após a confirmação da empresa\filial, terminar o preenchimento dos demais campos e configurar a quantidade de acionamento no botão ocorrência conforme imagem de exemplo abaixo.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007280132)  
  
**6.** A janela de exemplo abaixo é apresentada para determinar a quantidade de acionamento do **JOB**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007348411)  
  
**7.** Configure agora os agentes, que são os responsáveis por executar os agendamentos.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007348531)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007348551)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como configurar o job schedule GPEM026B na tela PO UI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21979795766167-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-configurar-o-job-schedule-GPEM026B-na-tela-PO-UI)  
[Artigos S-2206](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055237854)  
[Schedule Protheus](http://tdn.totvs.com/x/ow9FCg)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página *[TOTVS Informa](https://informa.totvs.com/)* selecione em categorias a área e pesquise por "Eventos".
