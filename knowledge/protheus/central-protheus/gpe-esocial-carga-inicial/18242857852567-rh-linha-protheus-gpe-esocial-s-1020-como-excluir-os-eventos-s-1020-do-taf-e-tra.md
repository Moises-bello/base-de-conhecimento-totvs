---
article_id: 18242857852567
category: GPE - eSocial - Carga Inicial
content_hash: cb57c449b06b498181fa6b9c88fddefa811a194eacefbef28e9cc84179baa33e
fetched_at: '2026-06-28T22:45:03.319685+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1020 - Como excluir os eventos S-1020
  do TAF e transmitido para o governo pelo GPE
type: support-article
updated_at: '2024-11-27T20:08:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18242857852567-RH-Linha-Protheus-GPE-eSocial-S-1020-Como-excluir-os-eventos-S-1020-do-TAF-e-transmitido-para-o-governo-pelo-GPE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18242847542167) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**  
Como excluir os eventos S-1020 do TAF e governo pelo GPE?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acessar a rotina **Carga Inicial** no módulo **GPE (Gestão de Pessoal)**.  
Caminho: Miscelânea > eSocial > Carga Inicial:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18242869489303)**  
  
2. Informar no campo **Data de Referência** a mesma data que foi enviado o evento que esta sendo excluído;  
3. Em **Processamento**selecionar a opção **Exclusão em Lote**;  
4. Selecionar o evento **S-1020** e a filial que deseja excluir o evento;  
5. Pode realizar um **filtro** em Outras Ações > Filtro S-1020;  
**Obs.: Caso não seja realizado nenhum filtro, todos os eventos S-1020 serão excluídos**  
6. Após isso, vá em **Confirmar** e a exclusão será enviado ao **TAF**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18255405476503)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18255451316631)  
  
7. Acessar a rotina **Lotações Tributárias** no módulo **TAF**Caminho: Atualizações > Eventos eSocial > Lotações Tributárias:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18255482516759)  
  
8. Verificar se os registros ficaram com a legenda vermelha;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18255672604439)  
  
9. Conforme informado no MOS S-1.1, o evento S-3000 não pode ser utilizado para exclusão dos evento S-1020. O evento é excluído mediante o envio do próprio evento com o preenchimento do grupo [exclusao]. Conforme print do XML abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18255655218327) **Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos".  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
