---
article_id: 360016635091
category: GPE - eSocial - Carga Inicial
content_hash: 38309c5362354420735cc3384844cc7835678b69829f86a4a21ce76596fb85c7
fetched_at: '2026-06-28T22:45:03.159485+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1005 - Após a transmissão dos eventos
  iniciais (carga inicial), como enviar alterações nos eventos de Estabelecimentos
  para o TAF de forma individual
type: support-article
updated_at: '2023-09-26T15:59:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016635091-RH-Linha-Protheus-GPE-eSocial-S-1005-Ap%C3%B3s-a-transmiss%C3%A3o-dos-eventos-iniciais-carga-inicial-como-enviar-altera%C3%A7%C3%B5es-nos-eventos-de-Estabelecimentos-para-o-TAF-de-forma-individual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17819811170327) Tempo aproximado para leitura: **00:02:30 min  
  
Dúvida**Após a transmissão dos eventos iniciais (carga inicial), como enviar alterações nos eventos de Estabelecimentos para o TAF  de forma individual?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Para as empresas que necessitam incluir/alterar eventos de Tabelas após já terem efetuada a Carga Inicial para o governo existe a possibilidade de fazer a geração individual dos novos eventos do GPE para o TAF sem que haja a necessidade de gerar uma nova Carga Inicial.   
Nesse caso, para que o evento seja transmitido para o TAF como uma alteração do S-1005 é necessário que o parâmetro **MV\_RHTAF** esteja com conteúdo **.T.** (*SIGACFG > Configurador > Ambiente > Cadastros > Parâmetros*) para que ocorra integração automática.   
Após procedimento, a alteração das informações pode ser realizada na tabela **S037** e **S038**.  
Caminho: *SIGAGPE > Atualizações > Definições Cálculo > Manutenção Tabelas > Selecione a Tabela > Outras Ações > Alterar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17819710732567)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17820016501655)*OU  
Acesse a rotina de **Carga Inicial**.  
*Caminho: SIGAGPE > Miscelânea > eSocial > Carga Inicial:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17819797373079)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17819883651991)*1. Preencha a **Data de Referência** desejada para o início de validade do registro a ser enviado;  
2. Selecione o evento que será enviado e marque sua empresa/filial;  
3. Em **Outras Ações**, será apresentado os eventos para aplicação do filtro.**Observação**Caso a **data base** do sistema esteja em um mês diferente do mês inicial do evento que já está no TAF, o sistema **vai incluir um novo registro** no TAF com uma nova data inicial, se a **data base** estiver no mesmo mês o sistema vai gerar uma **retificação** do mesmo registro.  
  
**Artigos Relacionados**  
[RH - Linha Protheus - GPE - eSocial - S-1010 - Após a transmissão dos eventos iniciais (carga inicial), como enviar um único registro para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046341633)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[Artigos S-1005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050822873)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
