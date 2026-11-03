---
article_id: 27273529122327
category: GPE - eSocial - Processo Trabalhista
content_hash: 48a2a736bc3e52b792306730570ae7c0a573c91a070cc8595dac831d35cdd262
fetched_at: '2026-06-28T22:45:00.486237+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2500 - Quais os tipos de contrato existem
  no evento S-2500
type: support-article
updated_at: '2024-10-23T20:21:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27273529122327-RH-Linha-Protheus-GPE-eSocial-S-2500-Quais-os-tipos-de-contrato-existem-no-evento-S-2500
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27273555211287) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais tipos de contrato existem no leiaute do S-2500 que irão preencher a tag tpContr?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**No campo {tpContr} do grupo [infoContr] deve ser declarada a condição do processo judicial  
ou da demanda submetida à CCP ou ao Ninter, considerando a situação do vínculo antes e após o  
processo trabalhista:  
  
**1 – Trabalhador com vínculo formalizado, sem alteração nas datas de admissão e de**  
**desligamento**: esse código deve ser utilizado para o caso em que o trabalhador já tinha seu vínculo  
devidamente reconhecido e não houve mudança em suas datas de admissão e desligamento.  
  
**2 – Trabalhador com vínculo formalizado, com alteração na data de admissão**: esse código deve  
ser utilizado para o caso em que o trabalhador já tinha seu vínculo devidamente reconhecido, mas  
houve mudança em sua data de admissão, mantendo-se inalterada a data de desligamento;  
  
**3 – Trabalhador com vínculo formalizado, com inclusão ou alteração de data de desligamento:**  
esse código deve ser utilizado para o caso em que o trabalhador já tinha seu vínculo devidamente  
reconhecido, mas houve mudança em sua data de desligamento, mantendo-se inalterada a data de  
admissão. Se o vínculo já tiver sido encerrado antes do início da obrigatoriedade de envio dos eventos  
não periódicos ao eSocial, deve ser utilizado o {tpContr} = [7];  
  
**4 – Trabalhador com vínculo formalizado, com alteração na data de admissão e inclusão ou**  
**alteração de data de desligamento**: esse código deve ser utilizado para o caso em que o trabalhador  
já tinha seu vínculo devidamente reconhecido, mas houve mudança em suas datas de admissão e  
desligamento. Se o vínculo já tiver sido encerrado antes do início da obrigatoriedade de envio dos  
eventos não periódicos ao eSocial, deve ser utilizado o {tpContr} = [7];  
  
**5 – Empregado com reconhecimento de vínculo**: esse código deve ser utilizado para o caso em  
que o vínculo de emprego foi reconhecido no processo trabalhista e não existe nenhuma informação  
previamente prestada no eSocial. Esse código não deve ser utilizado para os casos em que já houve  
prestação de informações relativas ao trabalhador, na qualidade de TSVE. Nesse caso, deve ser  
utilizado o {tpContr} = [9];  
  
**6 - Trabalhador sem vínculo de emprego/estatutário (TSVE), sem reconhecimento de vínculo**  
**empregatício**: esse código deve ser utilizado para o caso em que o processo trabalhista não versar  
sobre vínculo de emprego, inclusive quando o evento está sendo enviado por responsável indireto.  
Esse código deve ser utilizado também nos casos em que a decisão versa apenas sobre pagamento de  
diferença de parcelas devidas a trabalhador sem vínculo. Quando esse evento for enviado por  
responsável indireto, o grupo [ideResp] deve ser preenchido;  
  
**7 - Trabalhador com vínculo de emprego formalizado em período anterior ao eSocial**: este código  
deve ser utilizado para todas as situações em que o vínculo de emprego foi formalizado e encerrado  
em período anterior ao início da obrigatoriedade dos eventos não periódicos do eSocial. Esse código  
deve ser utilizado também nos casos em que a decisão judicial reconheceu, em relação a esses  
vínculos, alteração da data de admissão ou de desligamento originariamente declaradas;  
  
**8 - Responsabilidade indireta**: este código deve ser utilizado para os casos em que o declarante  
deste evento é o responsável indireto, conforme item 8 deste evento, exceto nos casos de trabalhador  
sem vínculo de emprego/estatutário;   
  
**9 - Trabalhador cujos contratos foram unificados (unicidade contratual)**: este código deve ser  
utilizado quando a condenação determinar a unificação de vínculos, conforme descrito no item 4  
deste evento. Esse código deve ser utilizado também nos casos em que a decisão judicial reconheceu  
vínculo de emprego de trabalhador em relação ao qual já houve prestação de informações na  
qualidade de TSVE.

**Assista** nossos **treinamentos** realizados pelo Suporte e pela Consultoria de Segmentos:  
[Tira Dúvidas **Suporte RH Protheus** - Tema eSocial Processos Trabalhistas](https://youtu.be/wrrD8zP_dOg)  
[**Espaço Legislação** | eSocial Layout S 1 1 e Processo Trabalhista |TOTVS RH Linha Protheus](https://www.youtube.com/watch?v=JWYVqg056NQ&list=PLXa8l0dq5zRkxpHqPKL7ZVYHt3urJ9VeM&index=11)  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Artigos RH Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".*
