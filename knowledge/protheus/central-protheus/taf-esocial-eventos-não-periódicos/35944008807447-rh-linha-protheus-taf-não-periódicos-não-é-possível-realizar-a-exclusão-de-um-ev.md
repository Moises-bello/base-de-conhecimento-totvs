---
article_id: 35944008807447
category: TAF - eSocial - Eventos Não Periódicos
content_hash: 3893615d8e840da02e9932b4446d6e1e9dbfb5c8c29c968890bffd4b2cd263a0
fetched_at: '2026-06-28T22:45:18.099796+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: RH - Linha Protheus - TAF - Não Periódicos - "Não é possível realizar a exclusão
  de um evento que está aguardando o retorno do fisco"
type: support-article
updated_at: '2026-06-26T11:37:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35944008807447-RH-Linha-Protheus-TAF-N%C3%A3o-Peri%C3%B3dicos-N%C3%A3o-%C3%A9-poss%C3%ADvel-realizar-a-exclus%C3%A3o-de-um-evento-que-est%C3%A1-aguardando-o-retorno-do-fisco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35944008797335) Tempo aproximado para leitura: **00:05:00min**  
  
**Dúvida**  
O que deve ser verificado quando o sistema apresentar a mensagem abaixo:

**"Não é possível realizar a exclusão de um evento que está aguardando o retorno do fisco"**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos Não Periódicos - Exclusão de Eventos, S-3000 (TAFA269) - Todas as versões.

**Solução**  
Siga as orientações abaixo:

A mensagem pode ser apresentada pelo sistema em duas situações:

1° O evento que deseja gerar o S-3000 foi transmitido ao governo, porém, ainda não teve retorno, ficando com o Status **“Aguardando Governo”**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35945000346263)

Neste cenário, não é possível excluir o evento enquanto o governo (eSocial) não fornecer o retorno;  
É necessário aguardar o retorno;

2° Em outro cenário, ao excluir o evento, gerando o S-3000, o registro de origem fica com a legenda “LARANJA”, indicando exclusão pendente de transmissão:

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35945000348183)

Nesse cenário se clicarmos na opção excluir irá apresentar a seguinte mensagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35945000349719)

A) Transmita o evento S-3000, caso ainda não tenha realizado, pelo monitor Painel eSocial;

B) Em alguns casos, após enviar o evento S-3000, ele permanece com status “Laranja”. Nesse caso, execute a rotina “Ajuste de Status de Exclusão”.

Documentação completa:  
[RH - Linha Protheus - TAF - eSocial - NÃO PERIÓDICOS - Como ajustar status de exclusão no TAF - S-3000](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055468253)

1° Acessar a rotina de exclusão de eventos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35945000351127)

2° Clicar no Botão “Outras Ações” logo em seguida “Ajuste de Status de Exclusão”:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35945000352023)

Retorne na rotina do evento e confira se o mesmo ficou com a legenda vermelha:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35945000352535)

**Saiba Mais**

**Para saber mais consulte os links abaixo:**

[**eSocial | Protheus - Entregas Legais**](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[**MOS - Manual de Orientação eSocial**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[**Perguntas Frequentes site eSocial**](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

**Para conhecimento dos eventos futuros, acessa a nossa página**[**TOTVS Informa**](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "Eventos"**

**Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina:**[**Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus)
