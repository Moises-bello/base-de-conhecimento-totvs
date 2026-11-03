---
article_id: 36782681484055
category: TAF - eSocial - Relatório
content_hash: f5368b512792d1e62a0f29a8b466e0b9200fa3ca04ae776ba958fc7658db73fd
fetched_at: '2026-06-28T22:45:19.923419+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH (Linha Protheus) - eSocial - TAF eSocial - Relatório FGTS - Não conclui
  a geração e trava em uma porcentagem fixa
type: support-article
updated_at: '2026-06-17T19:14:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36782681484055-RH-Linha-Protheus-eSocial-TAF-eSocial-Relat%C3%B3rio-FGTS-N%C3%A3o-conclui-a-gera%C3%A7%C3%A3o-e-trava-em-uma-porcentagem-fixa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36782651978519) Tempo aproximado para leitura: 00**:00:54 min**  
  
**Ocorrência**  
Ao gerar o relatório de FGTS, ele trava , não conclui a geração e trava em uma porcentagem fixa.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Relatório TAF - (TAFA552A)- Todas as versões  
  
**Solução**  
  
1. Se certifique que esteja com a última expedição contínua do TAF aplicada.

Links: 12.1.2310 - <https://suporte.totvs.com/portal/p/10098/download#detail/1126399>;

12.1.2410 - <https://suporte.totvs.com/portal/p/10098/download#detail/1174332>

2. Caso o problema persista, aplique a patch adicional abaixo:

Link 12.1.2310 - https://suporte.totvs.com/portal/p/10098/download?e=1220581

Link 12.1.2410 - <https://suporte.totvs.com/portal/p/10098/download?e=1220579>

Link 12.1.2510 - <https://suporte.totvs.com/portal/p/10098/download?e=1220582>

3. Caso o erro persista, realizar abertura de chamado junto do suporte TOTVS, informando:

* Ative a chave FWTRACELOG=1 no appserver.ini na chave do seu ambiente do TAF
* Após habilitar, **renomeie** o(s) **console.log** existente(s). **Gere o erro**na rotina Painel eSocial, e encaminhe para o suporte o(s)**novo(s) arquivo(s) console.log**
* Anexe o arquivo de log do dbaccess
* Nos encaminhe um vídeo demonstrando os filtros que está utilizando para a geração do relatório

**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [**TOTVS Informa**](https://informa.totvs.com/)selecione em categorias a área e pesquise por "**Eventos**"  
  
Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina:[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
