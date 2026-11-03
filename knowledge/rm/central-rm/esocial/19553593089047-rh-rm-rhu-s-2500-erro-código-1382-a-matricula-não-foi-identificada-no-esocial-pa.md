---
article_id: 19553593089047
category: eSocial
content_hash: e92ff983a3908a8e48daa9dcf0a1216a3f400f19e853bb41206e4144bc8f3e80
fetched_at: '2026-06-28T22:47:15.373304+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - S-2500: Erro código 1382: A matricula não foi identificada
  no eSocial para o trabalhador informado'
type: support-article
updated_at: '2026-06-02T18:55:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19553593089047-RH-RM-RHU-S-2500-Erro-c%C3%B3digo-1382-A-matricula-n%C3%A3o-foi-identificada-no-eSocial-para-o-trabalhador-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19553607936535) Tempo aproximado para leitura: 00**:02:00 min**  
  
 **Dúvida**  
Ao gerar o XML do evento S-2500 aparece a mensagem de erro: **Erro código 1382: A matricula não foi identificada no eSocial para o trabalhador informado.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34.263**, **12.1.2205.211**, **12.1.2209.155**e superiores.  
  
**Solução**  
 Para correção deste erro, será necessário validar as informações referente a matrícula apontada para o funcionário no cadastro do Contrato de Trabalho.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34094183377943)

De acordo com o Leiaute do eSocial, caso o funcionário tenha as informações no evento S-2190, S-2200 ou S-2300 no declarante, um destes eventos deverão possuir a mesma matrícula informada no campo destacado na imagem acima. Além disso, deverá informar no campo **'****Informações do evento****'** a opção **'Sim'.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34094183380247)

Caso o funcionário não tenha as informações em um desses eventos, deverá ser criada uma nova matrícula para o funcionário, de acordo com a regra de validação do Leiaute e também devem informar a opção **'Não'** para o campo **'****Informações do evento****'**

**Importante**

Normalmente, esta matrícula já encontra-se atribuída no cadastro do funcionário que estão informando, isto se existir o cadastro do mesmo no RM.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26717938457239)

Após estas validações, salve as modificações feitas e gere o XML novamente para efetuar o envio do evento.

**Saiba mais**  
Para maiores informações sobre os cadastros, acesse os links abaixo:

     - [RH - RM - RHU - eSocial: Processos Trabalhistas - Perguntas e respostas do evento webinar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18727698331543-RH-RM-RHU-eSocial-Processos-Trabalhistas-Perguntas-e-respostas-do-evento-webinar)  
     - [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783-RH-RM-RHU-eSocial-S-2500-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2500)  
     - [RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855-RH-RM-RHU-eSocial-S-2501-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2501)
