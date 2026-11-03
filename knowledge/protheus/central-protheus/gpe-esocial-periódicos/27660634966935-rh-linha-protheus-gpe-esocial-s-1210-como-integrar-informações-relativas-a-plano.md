---
article_id: 27660634966935
category: GPE - eSocial - Periódicos
content_hash: d0879e6083b7104d5ecd938b64c40f68dea9f3a89476fb1ea172b13f2377c27e
fetched_at: '2026-06-28T22:45:07.390564+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1210 - Como integrar informações relativas
  a planos de previdência complementar no evento S-1210
type: support-article
updated_at: '2025-07-25T18:01:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27660634966935-RH-Linha-Protheus-GPE-eSocial-S-1210-Como-integrar-informa%C3%A7%C3%B5es-relativas-a-planos-de-previd%C3%AAncia-complementar-no-evento-S-1210
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27660634930967) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como integrar informações relativas a planos de previdência complementar no evento S-1210?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução****1.** Configure a (s) verba (s) de previdência complementar na rotina de Verbas, através do menu: **Atualizações > Definições cálculos > Verbas > aba eSocial**, conforme **instruções do [boletim técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=789982783)**1 - Privada: **codIncIRRF** em S-1010 = [46, 47, 48]  
2 - FAPI: **codIncIRRF** em S-1010 = [61, 62, 66]  
3 - Funpresp: **codIncIRRF** em S-1010 = [63, 64, 65]**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27660657055639)**  
**2.** Cadastrar os dados dos fornecedores de Previdência Complementar na **tabela S073** através do menu: **Atualizações > Definições Cálculos > Manutenção Tabelas > Tabela S073.** Deve-se, **obrigatoriamente**, informar o**código**, **CNPJ**, **Nome e verba de desconto** e também as verbas principais de FAPI ou Previdência Privada nos campos reservados para todos os tipos de Previdência Complementar.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27660634937879)   
**3.** Realize o relacionamento do funcionário com o fornecedor na rotina **Manutenção de Previdência** acessando o menu: **Atualizações > Benefícios > Previdência Complementar > Manutenção de Previdência.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27660657063959)  
  
Observação:** É possível incluir a previdência complementar em lote, clicando em **Outras Ações > Geração Automática**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27660657065495)  
 **4.** Realize o lançamento da verba na Folha de Pagamento do(s) funcionário(s)   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27660657067159)  
  
**5.** Calcular a Folha de Pagamento e integrar o evento S-1210  
  
**Saiba Mais**Para saber mais, consulte os links abaixo:  
[RH - Linha Protheus - GPE - Como cadastrar a Previdência complementar para DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022683331-RH-Linha-Protheus-GPE-Como-cadastrar-a-Previd%C3%AAncia-complementar-para-DIRF)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página *[TOTVS Informa](https://informa.totvs.com/)* selecione em categorias a área e pesquise por "Eventos".
