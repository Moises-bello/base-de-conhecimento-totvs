---
article_id: 360027615931
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 38c3e57b5c16d5544517c069a89a5a412e30251d3007ca4c0bc0eaab5daae8bc
fetched_at: '2026-06-28T22:45:21.153313+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Eventos Não Periódicos - S-2205 e S-2206
  - Registro não pode ser alterado, pois encontra-se em processo de transmissão
type: support-article
updated_at: '2026-06-26T12:10:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027615931-RH-Linha-Protheus-TAF-eSocial-Eventos-N%C3%A3o-Peri%C3%B3dicos-S-2205-e-S-2206-Registro-n%C3%A3o-pode-ser-alterado-pois-encontra-se-em-processo-de-transmiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26429464284311) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Ao acessar a rotina **Cadastro Trabalhador** (TAFA421) e tentar realizar uma alteração contratual é apresentada a seguinte mensagem **Registro não pode ser alterado, pois encontra-se em processo de transmissão.  
![altera__o1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360027093331)  
  
Causa**Ocorre por que existem alterações cadastrais ou contratuais pendentes de transmissão ou exclusões que não estão corretamente indicadas nas tabelas T1V(S-2206) ou T1U(S-2205).  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões.  
  
**Solução  
1.** Acesse na rotina **Cadastro Trabalhador** (TAFA421), filtrada pelo funcionário que foi apresentada a mensagem e acesse Outras Ações > Histórico de Alterações e valide se todos os registros estão com status de transmissão como **Transmitido Válido**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26429452689559)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26429452695447)  
  
**2.** Caso exista algum sem protocolo de transmissão, transmita-o ou realize o ajuste de recibo (caso o evento já conste no eSocial) para que a mensagem não seja mais apresentada, caso todos possuam siga o passo 3;  
  
Para mais detalhes sobre o ajuste de recibo do evento, verifique documentação abaixo:  
[RH - Linha Protheus - TAF - eSocial - Funcionalidades - Como realizar ajuste de recibo do eSocial no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672-RH-Linha-Protheus-TAF-eSocial-Funcionalidades-Como-realizar-ajuste-de-recibo-do-eSocial-no-TAF)  
  
**3.** Acesse a rotina **Exclusão de Eventos** (TAFA266) e acesse a Outras Ações > Ajuste Status de Exclusão, desta forma todos os registros deletados do eSocial por meio do evento S-3000 serão atualizados (STATUS=7 e ATIVO=2).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26429464315031)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26429464322455)  
Para mais detalhes sobre o ajuste do status de exclusão, verifique documentação abaixo:  
[RH - Linha Protheus - TAF - eSocial - Não Periódicos - S-3000 - Como ajustar status de exclusão no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055468253-RH-Linha-Protheus-TAF-eSocial-N%C3%83O-PERI%C3%93DICOS-Como-ajustar-status-de-exclus%C3%A3o-no-TAF-S-3000)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
