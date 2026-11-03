---
article_id: 4407283911063
category: Evento S-2240
content_hash: ff1b67d31adb6a7fe0a5fbd6cb60976b05cacb5aaf62b2a32c38864eee3ade5f
fetched_at: '2026-06-28T22:45:23.431594+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar o evento S-2240 com necessidade de EPI
  e conferir essa geração no  TAF
type: support-article
updated_at: '2025-03-03T18:20:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407283911063-RH-Linha-Protheus-MDT-Como-gerar-o-evento-S-2240-com-necessidade-de-EPI-e-conferir-essa-gera%C3%A7%C3%A3o-no-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372892043927)**Tempo aproximado para leitura: **01:00:00 min  
  
Dúvida**Como gerar o evento S-2240 com necessidade de EPI e conferir essa geração no TAF?    
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Objetivo deste artigo é orientação geral e mapeamento dos passos necessários para geração do evento S-2240 com necessidade de EPI, cada empresa pode ter um cenário específico portanto é importante avaliar nossa documentação centralizadora sobre a geração do eventos S-2240, os parâmetros que podem interferir ou configurar para atender as diferentes necessidades de cada empresa.  
Consulte a documentação no link <https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais+-+S-2240>  
  
**1-** Cadastro do Risco, deve possui o campo **Nec EPI = SIM  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407280775575)  
  
2-** Verifique se o funcionário está exposto ao Risco.

Para visualizar esta tela acesse **Atualizações > PPRA > Risco** > Posicione no risco e entre como **alterar** > clique em **Outras Ações > Funcionário exposto.**Dica: Caso não saiba qual risco o funcionário está exposto emita o relatório para conferencia. Consulte:  
[RH - Linha Protheus - MDT - Como emitir o relatório de Riscos por Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5429821522071)  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407283965207)  
  
**3-** Realize o relacionamento do **Risco** com o **EPI.**Através da opção **Outras ações → relacionamento** ou Podem ser utilizados as rotinas:  
**EPI x Risco** (MDTA130), **Risco x EPI** (MDTA125) ou **Relacionamentos** (MDTA181).   
Neste exemplo estou usando a opção de relacionamento. Vincule o EPI necessário.  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407283975703)  
  
**4-** É necessário realizar a entrega deste EPI ao funcionário exposto ao Risco.   
Projetei a entrega do EPI ao Funcionário através da rotina **Funcionário x EPI**Selecionei minha matricula 000002 - funcionária eSocial e realizei  a entrega do epi **01 Óculos.**   
  
![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407283982615)  
  
**5-** Conferencia no evento no TAF .   
Ao conferir no TAF o evento gerado S-2240, sobre os dados do EPI através do caminho:   
**Módulo 84 atualizações → eventos não periódicos → Cond Amb Trabalho****Posicione no trabalhador -> Visualizar -> Posicione na aba fatores de risco**, será apresentados as informações sobre o EPI.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420133248151)  
  
**6-**Esse campo **Certif EPI** é um campo de controle do TAF não temos como alterar essa nomenclatura é apenas um código.  
Se entrar como alterar e posicionar no campo terá uma opção de pesquisa por lupa.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420133248151)  
  
**7-** Ao visualizar o pesquisa, *o conteúdo do campo **Desc EPI** esta relacionado ao **C.A do EPI entregue**.*

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420133365655)  
  
![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407284047255)  
  
Veja também o link: [Condições em que os EPI's não serão Enviados ao SIGATAF/Middleware](https://tdn.totvs.com/x/PkCbJg)**  
Abaixo deixo dois vídeos, sendo o primeiro com orientações sobre os parâmetro **eSocial** no medicina, e o segundo demonstrando o processo de geração do **S-2240**(Riscos) para o **eSocial**.  
  
How To | SIGAMDT eSocial SST - Parâmetros eSocial no Medicina  
  
  
How To | SIGAMDT eSocial SST - S-2240 Como Gerar Riscos com EPI  
  
  
**Observação**

* Para saber todas as **Premissas**, **Conceitos**, **Como Gerar**, **Informações técnicas**clique [aqui!](https://tdn.totvs.com/x/YkqlGw)
* Para Saber mais sobre o cadastro de risco consulte: [Para que server a rotina Riscos (MDTA180) e como incluir](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056319213)
* Para ver mais vídeos acesse o artigo: [Existe vídeos com o passo a passo de geração dos eventos SST (Medicina e Segurança do Trabalho) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410314804631)
* Para saber como corrigir inconsistências apresentadas no log de geração siga as orientações do artigo: [Como corrigir os erros ou inconsistências gerados no log ao tentar gerar eventos eSocial no SIGAMDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414522104471)

**Consulte: [RH - Linha Protheus - MDT - eSocial - S-2240 - O que enviar para avaliação do suporte quando não gera o evento S-2240](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9864112621463-RH-Linha-Protheus-MDT-eSocial-S-2240-O-que-enviar-para-avalia%C3%A7%C3%A3o-do-suporte-quando-n%C3%A3o-gera-o-evento-S-2240)  
  
  
Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
