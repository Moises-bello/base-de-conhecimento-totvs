---
article_id: 30277527065495
category: TAF - eSocial - Eventos de Tabelas
content_hash: ab3c61ae988a884b25f529ae841e5607e5f8f0da5d81fab7632a6a6119ed0311
fetched_at: '2026-06-28T22:45:17.194718+00:00'
product: protheus
section_id: 1500001548042
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos de Tabela - S-1000 -  Código
  da Ocorrência 750: O período de validade do item não pode ser diminuído, pois este
  item esta sendo utilizado em outro evento já enviado.'
type: support-article
updated_at: '2026-06-25T11:24:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30277527065495-RH-Linha-Protheus-TAF-eSocial-Eventos-de-Tabela-S-1000-C%C3%B3digo-da-Ocorr%C3%AAncia-750-O-per%C3%ADodo-de-validade-do-item-n%C3%A3o-pode-ser-diminu%C3%ADdo-pois-este-item-esta-sendo-utilizado-em-outro-evento-j%C3%A1-enviado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30277527046167) Tempo aproximado para leitura: **00:03:00 min****Ocorrência****Ao tentar transmitir o evento S-1000 (Informações do Empregador/Contribuinte/Órgão Público) ao eSocial é retornada a inconsistência abaixo:  
  
Sequência: 000001 - Tipo: Erro - Código da Ocorrência: 750  
Descrição: O período de validade do item não pode ser diminuído, pois este item esta sendo utilizado em outro evento já enviado.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões.  
  
**Causa**O eSocial localizou eventos remuneratórios dentro do Portal do eSocial com data posterior a igual ou posterior a nova data de início de validade do S-1000.  
  
**Solução**Para corrigir o erro:  
  
**1.** Valide se existem eventos remuneratórios (S-2299, S-1200, S-1210, etc.) com data igual ou posterior a nova data de início de vigência do S-1000;  
**2.** Caso houver, realize a exclusão do evento e envie o S-3000 para o governo;  
**3.** Após isso, tente transmitir novamente o S-1000;  
**4.** E, com o S-1000 transmitido com sucesso, gere e envie novamente os eventos que haviam sido excluídos.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
