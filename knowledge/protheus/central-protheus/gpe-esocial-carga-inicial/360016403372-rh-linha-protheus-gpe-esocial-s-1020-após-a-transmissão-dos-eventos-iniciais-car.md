---
article_id: 360016403372
category: GPE - eSocial - Carga Inicial
content_hash: d29ebe8e623a09b3b808dd9d9d8e33ef1d90db01d6408cdcbecf5bf794b7eabc
fetched_at: '2026-06-28T22:45:03.049983+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1020 - Após a transmissão dos eventos
  iniciais (carga inicial), como enviar um único registro de Lotação para o TAF
type: support-article
updated_at: '2026-06-18T14:13:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016403372-RH-Linha-Protheus-GPE-eSocial-S-1020-Ap%C3%B3s-a-transmiss%C3%A3o-dos-eventos-iniciais-carga-inicial-como-enviar-um-%C3%BAnico-registro-de-Lota%C3%A7%C3%A3o-para-o-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19220657775639) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Após a transmissão dos eventos iniciais (carga inicial), como enviar alterações nos eventos de Lotação para o TAF de forma individual?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Para as empresas necessitam incluir/alterar eventos de Tabelas após já terem efetuado a Carga Inicial para o governo, existe a possibilidade de fazer a geração individual dos novos eventos do GPE para o TAF sem que haja a necessidade de gerar uma nova Carga Inicial.  
  
Nesse caso para que o seja transmitido para o TAF uma inclusão/alteração do S-1020, será necessário que o parâmetro **MV\_RHTAF** (SIGACFG > Configurador > Ambiente > Cadastros > Parâmetros) esteja com o conteúdo **.T.**para que ocorra integração automática.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19220657777687)  
Após verificar se o parâmetro está ativo, poderá ser feita a alteração no **Centro de Custo**.  
Caminho: SIGAGPE > Atualizações > Cadastros > Centro de Custos.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19220673693335)  
  
**Observação**Caso a **data base** do sistema esteja em um mês diferente do mês inicial do evento que já está no TAF, o sistema vai **incluir** **um novo registro** com uma nova data inicial, se a **data base** estiver no mesmo mês o sistema vai gerar uma **retificação** do mesmo registro.  
  
Há também a opção da geração através da carga inicial filtrando apenas pelo código desejado.  
Caminho: SIGAGPE > Miscelânea > eSocial > Carga Inicial *![](https://centraldeatendimento.totvs.com/hc/article_attachments/19220673696023)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19220673697047)*1. Preencha a **data de referência** desejada para o início de validade do registro a ser enviado;  
2. Selecione o evento que será enviado e marque sua empresa/filial;  
3. Em **Outras Ações**, será apresentado os eventos para aplicação do filtro.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Artigos S-1020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051258534)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
