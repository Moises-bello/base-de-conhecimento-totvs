---
article_id: 21787061523991
category: MDT - PCMSO
content_hash: a0735c54c79c1b6120514e6a982cf27064f9d30cb02ed34f4a026d766ac0a6f2
fetched_at: '2026-06-28T22:44:28.476757+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Orientações específicas para ajuste no campo Filial
  (TM5_FILFUN) na rotina Exames do Funcionário (MDTA120)
type: support-article
updated_at: '2025-09-03T14:18:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21787061523991-RH-Linha-Protheus-MDT-Orienta%C3%A7%C3%B5es-espec%C3%ADficas-para-ajuste-no-campo-Filial-TM5-FILFUN-na-rotina-Exames-do-Funcion%C3%A1rio-MDTA120
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21787061513239) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Orientações específicas para ajuste no campo Filial (TM5\_FILFUN) na rotina Exames do Funcionário (MDTA120).  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**  
Em algumas situações, ao incluir exames para novos funcionários, o sistema não apresentava a Filial do funcionário, o registro era salvo e não apresentava a informação no browser, apenas na tabela (TM5). A orientação informada só irá corrigir registros que estão com o campo Filial em branco na tabela (TM5\_FILFUN).  
  
**Solução**Será necessário executar um compatibilizador para efetuar o ajuste nos registros.  
  
O compatibilizador esta disponível na documentação: [Compatibilizador Filial do Funcionário - TM5\_FILFUN](https://tdn.totvs.com/pages/releaseview.action?pageId=825319806)  
  
Para executar o compatibilizador após compilado o fonte, acessar o **Configurador (SIGACFG)**:  
  
Selecionar as opções do menu: Ambiente / Cadastros / Menus.  
Selecionar somente o módulo **Medicina e Segurança do Trabalho** e clicar em **O**k:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21787334393751)  
  
Posicionar sobre a pasta **SIGAMDT** no **lado esquerda da tela** e clicar em **Adicionar**, clicar em SIM para todos nas demais mensagens que aparecerem:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21787352721687)  
  
Selecionar uma pasta para adicionar a chamada no compatibilizador, neste caso utilizei a pasta **Miscelânea / Arquivos** e clicar em **Novo item**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21787352725527)  
  
Adicionar um nome ao novo item, neste caso utilizei SQA TM5. Após em **Programa** adicionar a chamada do compatibilizador utilizando **U\_SQATM5**.  
  
Selecionar o módulo **Medicina e Segurança do Trabalho** e clicar em **Ok**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21787334417175)  
  
Clicar em **Gerar** para gerar o novo menu, colocar o módulo a ser gerado **SIGAMDT**, clicar em **Gerar** e responder sim para demais mensagens em tela: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21787352734615)  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21787334421399)  
  
Após gerar o menu sair do Configurador, acessar o módulo **SIGAMDT** e acessar a rotina onde foi criado o compatibilizador, neste caso **Miscelânea / Arquivos / SQA TM5:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21787352742679)**Após executado será apresentado a mensagem mencionando que o processo foi executado e os registros estarão corrigidos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21787352746391)  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-BR/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-BR/sections/9198712823575-Assistente-Virtual-Carolina)
