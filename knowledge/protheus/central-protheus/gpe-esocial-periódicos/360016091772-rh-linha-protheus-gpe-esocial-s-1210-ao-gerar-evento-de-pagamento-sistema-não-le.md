---
article_id: 360016091772
category: GPE - eSocial - Periódicos
content_hash: 9ffa95f9882f15b8812aa061c7e6a6923d426d7c95941cf19c860c27456666ea
fetched_at: '2026-06-28T22:45:08.873813+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1210 - Ao gerar evento de pagamento
  sistema não leva as informações da rescisão.
type: support-article
updated_at: '2025-07-23T13:41:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016091772-RH-Linha-Protheus-GPE-eSocial-S-1210-Ao-gerar-evento-de-pagamento-sistema-n%C3%A3o-leva-as-informa%C3%A7%C3%B5es-da-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27476416353943)Tempo aproximado para leitura: **00:02:00min****Dúvida**Ao gerar evento S-1210, sistema não envia para o TAF as informações sobre o desligamento do funcionário.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todos as versões  
  
**Solução**Ao gerar a **rescisão**no SIGAGPE, deve-se **integrar** o roteiro **RES** através da rotina de integração de roteiros, calcular a **folha de pagamento** do funcionário e após a geração da folha o sistema irá gravar na tabela **SRC** o conteúdo da **rescisão**,caso o período já esteja **fechado** a informação será coletada da tabela **SRD**. Após a gravação correta no SIGAGPE deve-se integrar o evento S-1210 ao TAF. Porém recomendamos marcar a opção **Considerar dados do período em aberto**para que o sistema considere informações dos períodos **aberto** e **fechado** para geração  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27476409842199)  
  
Importante estar com o ambiente atualizado com as Expedições Continuas **GPE** e **TAF**[Pacote e Dicionário Correções Expedição Continua RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)[Pacote e Dicionário Correções Expedição Continua TAF](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/TAF_EXPEDICAO_CONTINUA.ZIP)   
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página *[TOTVS Informa](https://informa.totvs.com/)* selecione em categorias a área e pesquise por "Eventos".
