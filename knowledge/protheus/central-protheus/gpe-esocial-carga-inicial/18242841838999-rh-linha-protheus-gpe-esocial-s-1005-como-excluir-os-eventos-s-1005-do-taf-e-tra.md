---
article_id: 18242841838999
category: GPE - eSocial - Carga Inicial
content_hash: b9cfdd98049556b3cf4769b7a5ecdd14177a85e451997a40a1c70a43948e9b76
fetched_at: '2026-06-28T22:45:03.188935+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1005 - Como excluir os eventos S-1005
  do TAF e transmitido para o governo pelo GPE
type: support-article
updated_at: '2025-03-03T20:18:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18242841838999-RH-Linha-Protheus-GPE-eSocial-S-1005-Como-excluir-os-eventos-S-1005-do-TAF-e-transmitido-para-o-governo-pelo-GPE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18242797964951) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**  
Como excluir os eventos S-1005 do TAF e governo pelo GPE?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
**1.** Acessar a rotina **Carga Inicial** no módulo **GPE (Gestão de Pessoal)**.  
Caminho: Miscelânea > eSocial > Carga Inicial:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18242833214743)**  
  
**2.** Informar no campo **Data de Referência** a mesma data que foi enviado o evento que esta sendo excluído;  
**3.** Em **Processamento**selecionar a opção **Exclusão em Lote**;  
**4.** Selecionar o evento **S-1005** e a filial que deseja excluir o evento;  
**5.** Pode realizar um **filtro** em Outras Ações > Filtro S-1005;  
**Obs.: Caso não seja realizado nenhum filtro, todos os eventos S-1005 serão excluídos**  
**6.** Após isso, vá em **Confirmar** e a exclusão será enviado ao **TAF**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18246283075351)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18246254547991)  
  
**7.** Acessar a rotina **Estab, Obras ou Unid. Órg. Públicos** no módulo **TAF**;Caminho: Atualizações > Eventos eSocial > Estab, Obras ou Unid. Órg. Públicos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18243614165527)  
  
**8.** Verificar se os registros ficaram com a legenda vermelha;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18246263382039)  
  
**9.** Conforme informado no MOS S-1.1, o evento S-3000 não pode ser utilizado para exclusão dos evento S-1005. O evento é excluído mediante o envio do próprio evento com o preenchimento do grupo [exclusao], conforme print do XML abaixo:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18246276877591)**

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
