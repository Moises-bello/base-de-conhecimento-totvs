---
article_id: 26482535559063
category: TAF - eSocial - Eventos de Tabelas
content_hash: a26e4f1d14b5c3a84684c1aa24941c4144fb6e1a21388fc845418598acef242e
fetched_at: '2026-06-28T22:45:17.142204+00:00'
product: protheus
section_id: 1500001548042
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos de Tabela - S-1010 - Código
  da Ocorrência 105: O evento a ser excluído/retificado (alterado) não foi localizado
  na base de dados do eSocial.'
type: support-article
updated_at: '2026-06-25T11:08:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26482535559063-RH-Linha-Protheus-TAF-eSocial-Eventos-de-Tabela-S-1010-C%C3%B3digo-da-Ocorr%C3%AAncia-105-O-evento-a-ser-exclu%C3%ADdo-retificado-alterado-n%C3%A3o-foi-localizado-na-base-de-dados-do-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26482535542679) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**No módulo do TAF (84), ao tentar realizar a transmissão do evento S-1010 é apresentada a inconsistência com Código da Ocorrência 105: O evento a ser excluído/retificado (alterado) não foi localizado na base de dados do eSocial.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões.  
  
**Causa**  
Esse incidente ocorre, pois o evento é gerado como retificação/alteração, porém não é localizado o evento original na base de dados do eSocial.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Realize o ajuste de status de exclusão através da rotina **Exclusão de Eventos** no TAF:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26482535546263)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26482496725015)  
Para mais detalhes, verifique a documentação abaixo:  
[RH - Linha Protheus - TAF - eSocial - Não Periódicos - S-3000 - Como ajustar status de exclusão no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055468253-RH-Linha-Protheus-TAF-eSocial-N%C3%83O-PERI%C3%93DICOS-Como-ajustar-status-de-exclus%C3%A3o-no-TAF-S-3000)  
  
2. Integre novamente o evento S-1010 a partir do GPE, conforme vídeo How To abaixo:  
[How To | eSocial - Carga Inicial - Envio Eventos de Tabela](https://www.youtube.com/watch?v=16mOmMqgAPc)  
  
3. Verifique se o evento foi gerado corretamente como inclusão (tag **indRetif = 1)** e tente transmitir novamente.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
