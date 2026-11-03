---
article_id: 16478470926103
category: TAF - eSocial - Eventos Periódicos
content_hash: cab18a3c0b2a8dcb745cfb7638ab5d23fe35b62396ada0549412361b1528ddce
fetched_at: '2026-06-28T22:45:19.103622+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Não Periódicos/Periódicos - Ao excluir
  qualquer evento gera o Código da Ocorrência 459: Não foi localizado um evento para
  o recibo de entrega informado ou o mesmo foi excluído/retificado'
type: support-article
updated_at: '2024-09-25T18:55:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16478470926103-RH-Linha-Protheus-TAF-eSocial-N%C3%A3o-Peri%C3%B3dicos-Peri%C3%B3dicos-Ao-excluir-qualquer-evento-gera-o-C%C3%B3digo-da-Ocorr%C3%AAncia-459-N%C3%A3o-foi-localizado-um-evento-para-o-recibo-de-entrega-informado-ou-o-mesmo-foi-exclu%C3%ADdo-retificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16478500542359) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao realizar a exclusão (S-3000) de um evento do eSocial e tentar realizar a transmissão do novo evento integrado é retornado com o seguinte erro:  
  
**Tipo: Erro - Codigo da ocorrência: 459**  
**Descrição: Nao foi localizado um evento para o recibo de entrega informado ou o mesmo foi excluido/retificado.Acao Sugerida: Devera existir um Evento ja recebido, "Ativo" (nao excluido ou retificado), com numero de recibo de entrega igual ao informado no campo.****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões.  
  
**Causa**Após transmissão do S-3000, o evento dentro da rotina no TAF, permanece com a legenda laranja, aguardando retorno do S-3000:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16503426167063)  
  
E ao realizar uma nova integração do evento, e está integrando como uma alteração no TAF **(legenda amarela)** e não como uma nova integração **(legenda verde)**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16503506355223)  
  
O correto seria manter o registro excluído com a legenda vermelha e criar um novo registro com a legenda verde, conforme imagem abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16503633439511)  
  
**Solução**Para os cenários apresentados acima, execute o processo de ajuste de Status de Exclusão no TAF, conforme a documentação abaixo:  
[Automação Fiscal - NÃO PERIÓDICOS - Como ajustar status de exclusão no TAF - S-3000](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055468253)  
  
Após o procedimento, verifique se o evento ficou a legenda vermelha no TAF, indicando que  a exclusão recebeu retorno do governo.  
  
Com o evento excluído no TAF (legenda vermelha), integre novamente o evento para o TAF e tente transmitir novamente.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
