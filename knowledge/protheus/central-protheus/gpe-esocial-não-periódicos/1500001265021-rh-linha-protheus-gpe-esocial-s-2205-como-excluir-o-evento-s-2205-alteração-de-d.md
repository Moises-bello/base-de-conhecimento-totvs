---
article_id: 1500001265021
category: GPE - eSocial - Não Periódicos
content_hash: 444235a40d9a1ff1bcd9a35ae2906d08208c295a32615379411b82d8c91d31e6
fetched_at: '2026-06-28T22:45:04.645947+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2205 - Como excluir o evento S-2205
  (Alteração de Dados Cadastrais do Trabalhador) no gestão de pessoal
type: support-article
updated_at: '2026-06-16T10:37:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001265021-RH-Linha-Protheus-GPE-eSocial-S-2205-Como-excluir-o-evento-S-2205-Altera%C3%A7%C3%A3o-de-Dados-Cadastrais-do-Trabalhador-no-gest%C3%A3o-de-pessoal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41258391322775) Tempo aproximado para leitura: **00:02:00**  
  
**Dúvida**  
Como excluir o evento **S-2205 Alteração** Cadastral no gestão de pessoal (SIGAGPE)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**  
Não é possível fazer a exclusão do evento **S-2205** (Alteração de Dados Cadastrais do Trabalhador) através do modulo Gestão de Pessoal (**SIGAGPE**), a exclusão desse evento deve ser feita diretamente no modulo Totvs Automação Fiscal (**SIGATAF**).  
  
**1.** Para excluir o evento **S-2205** (Alteração de Dados Cadastrais do Trabalhador) no **TAF** acesse o modulo 84 Totvs Automação Fiscal (**SIGATAF**) no caminho: Atualizações > Eventos eSocial > Trabalhador > Cadastro Trabalhador (**TAFA421**).   
  
**2.** Localize o registro do trabalhador e clique no botão **Outras Ações > Excluir Registro**, selecione o evento **S-2205** e confirme.  
  
Antes da exclusão é importante saber se o **S-2205** já está no governo (com número de recibo), ou se ele ainda não foi transmitido para o governo. Isso porque caso o **S-2205** esteja no governo será gerado o evento **S-3000** (Exclusão de Eventos), que deve ser posteriormente transmitido ao eSocial.  
  
**Dica**  
O usuário consegue saber se o evento está transmitido ou não acessando o botão **Outras Ações > Exibir Histórico de Alterações**. Localize o evento **S-2205** pela coluna **Nome Evento** e verifique se a coluna **Status de Transmissão** está como **Transmitido Válido**, se estiver com esse **Status** significa que o evento já foi transmitido.  
  
Exemplos:  
1. Exclusão de uma evento **S-2205** que não foi transmitido ao governo.  
![s-2205_taf.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360102346813)  
  
2. Exclusão de uma evento **S-2205** que foi transmitido ao governo, gerando o **S-3000**.  
![s-2205_governo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001263002)  
  
**Observações**

* No exemplo 2 é necessario transmitir o evento **S-3000** ao governo para que a exclusão do **S-2205** seja concluída.
* Para saber como visualizar evento **S-2205** no site do **eSocial** consulte o artigo: [**MP - GPE - eSocial - S-2205 - Como consultar no site do eSocial dados do evento S-2205 (Dados Cadastrais)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043282053)

**Saiba Mais**  
Para saber mais consulte os links abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****".*
