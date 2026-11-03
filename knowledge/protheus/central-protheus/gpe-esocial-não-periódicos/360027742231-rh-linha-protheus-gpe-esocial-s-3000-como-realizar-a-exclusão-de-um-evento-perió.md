---
article_id: 360027742231
category: GPE - eSocial - Não Periódicos
content_hash: 7f9d57063be8e26c66e6e3700b833d6f67b036a55c4a5f1b54edd7442207ad95
fetched_at: '2026-06-28T22:45:05.958878+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-3000 - Como realizar a exclusão de
  um Evento Periódico S-1200 e S-1210
type: support-article
updated_at: '2026-06-16T11:23:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027742231-RH-Linha-Protheus-GPE-eSocial-S-3000-Como-realizar-a-exclus%C3%A3o-de-um-Evento-Peri%C3%B3dico-S-1200-e-S-1210
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18147489007383) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar a exclusão de um Evento Periódico no eSocial S1200 e S-1210?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**  
A premissa básica para que exista um evento S-3000, é que o **evento que deseja excluir esteja protocolizado** no RET (Governo), ou seja, no TAF esse evento ficará com Status **4 - Consistente** e com **recibo** preenchido.  
  
Para gerar um evento S-3000 para excluir um evento Periódico da base do RET (Governo) você tem duas opções no Protheus:  
  
**1.** **Opção de Exclusão disponível na rotina de Eventos Periódicos do GPE (GPEM034):**  
Acesse a rotina Eventos Periódicos e ao preencher o campo **Processo** com a opção de **Exclusão** o Sistema vai gerar um evento S-3000 para os eventos que no TAF estão com Status "4 - Consistente" e com recibo preenchido.  
Caminho: GPE > Miscelânia > eSocial > Eventos Periódicos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18147059436311)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27476418721431)  
  
**ATENÇÃO:** O Sistema vai observar as opções selecionadas na rotina, então tomar muito cuidado no momento de selecionar os eventos **S-1200** e/ou **S-1210** e no momento de preencher o **Filtro**.  
  
**2. Opção de Exclusão disponível nas rotinas do TAF:**  
Ao acessar a rotina do TAF, **por exemplo**, Folha de Pagamento (TAFA250) onde é possível consultar os eventos S-1200 por Trabalhador você pode filtrar o Trabalhador e período que deseja excluir, em seguida acessar **Outras Ações > Excluir > Excluir Registro**, porém reforço que só será gerado um evento S-3000 se o evento que deseja excluir estiver no TAF com Status "4 - Consistente" e com recibo preenchido.  
Caminho S-1200: TAF > Atualizações > Eventos eSocial > Periódicos > Folha de Pagamento  
Caminho S-1210: TAF > Atualizações > Eventos eSocial > Periódicos > Pgto. Rend. Trab.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18147410349719)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27476412114327)  
  
Para excluir eventos Periódico **SEM RECIBO** do RET (Governo) e com Status **DIFERENTE** de "4 - Consistente" utilize a rotina [TAF - Limpeza de Eventos Periódicos](http://tdn.totvs.com/x/o4IEGw) (TAFEXCESOC).  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [*TOTVS Informa*](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos".
