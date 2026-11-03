---
article_id: 18242851254423
category: GPE - eSocial - Carga Inicial
content_hash: e1ddab52d3cfc7f70d12eed9fe1ac3b90ad7b39d8a295942b3487234dda71ee8
fetched_at: '2026-06-28T22:45:03.253617+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1010 - Como excluir os eventos S-1010
  do TAF e transmitido para o governo pelo GPE
type: support-article
updated_at: '2023-10-13T18:47:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18242851254423-RH-Linha-Protheus-GPE-eSocial-S-1010-Como-excluir-os-eventos-S-1010-do-TAF-e-transmitido-para-o-governo-pelo-GPE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18242836145687) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**  
Como excluir os eventos S-1010 do TAF e governo pelo GPE?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acessar a rotina **Carga Inicial** no módulo **GPE (Gestão de Pessoal)**.  
Caminho: Miscelânea > eSocial > Carga Inicial:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18242844707223)**  
  
2. Informar no campo **Data de Referência** a mesma data que foi enviado o evento que esta sendo excluído;  
3. Em **Processamento**selecionar a opção **Exclusão em Lote**;  
4. Selecionar o evento **S-1010** e a filial que deseja excluir o evento;  
5. Pode realizar um **filtro** em Outras Ações > Filtro S-1010;  
**Obs.: Caso não seja realizado nenhum filtro, todos os eventos S-1010 serão excluídos**  
6. Após isso, vá em **Confirmar** e a exclusão será enviado ao **TAF**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18247807509783)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18247836042647)  
  
7. Acessar a rotina **Rubricas** no módulo **TAF**;Caminho: Atualizações > Eventos eSocial > Rubricas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18247851051287)  
  
8. Verificar se os registros ficaram com a legenda vermelha;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18247874703767)  
  
9. Conforme informado no MOS S-1.1, o evento S-3000 não pode ser utilizado para exclusão do evento S-1010. O evento é excluído mediante o envio do próprio evento com o preenchimento do grupo [exclusao]. **Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
