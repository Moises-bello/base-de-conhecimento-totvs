---
article_id: 360033938073
category: GPE - eSocial - Periódicos
content_hash: 06f373772bf1cf7ee320673bca4638289a8b395620bd47a51e8a76a3d730abb7
fetched_at: '2026-06-28T22:45:07.627380+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1020 - Inconsistência do RET - 247
  - Codigo de Terceiros incompativel com o FPAS informado.Acao Sugerida: Para classificacao
  tributaria igual a [01, 02, 03, 04], informar 0000'
type: support-article
updated_at: '2025-07-25T16:11:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033938073-RH-Linha-Protheus-GPE-eSocial-S-1020-Inconsist%C3%AAncia-do-RET-247-Codigo-de-Terceiros-incompativel-com-o-FPAS-informado-Acao-Sugerida-Para-classificacao-tributaria-igual-a-01-02-03-04-informar-0000
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16432577637143)**Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Inconsistência do RET - 247 - Codigo de Terceiros incompatível com o FPAS informado. Ação Sugerida: Para classificação tributaria igual a [01, 02, 03, 04], informar 0000. Nos demais casos, o valor informado no campo devera ser compatível com o código FPAS que consta na Tabela 4 (Códigos e Alíquotas de FPAS/Terceiros).  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**   
Esse retorno ocorre pois a classificação tributaria da empresa foi transmitida como Simples Nacional ou MEI no evento **S-1000** para o governo. Nesses casos o Governo avisa ao usuário que o **código** de **Terceiro** é incompatível com o **FPAS** da empresa.  
De acordo com o item 7.1, página 108 do documento [MOS 1.3](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-publicado-com-marcacoes.pdf) as empresas optantes pelo **Simples Nacional** (Classificação Tributária [01, 02 ou 03]) e o **MEI** (Classificação Tributária [04]) devem informar o FPAS conforme a atividade (tabela 4) e o código de terceiros [0000].   
  
Abaixo descrição das classificações de acordo com layout 1.3:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28267112569495)  
  
**​​****Solução**Para correção verifique no **SIGAGPE**, **TAF** e **S-1020 (Lotações Tributárias)** no portal [**eSocial**](https://login.esocial.gov.br/login.aspx) se está definido o código de Terceiro com **0000**.  
  
**SIGAGPE**  
Menu: Atualizações > Definições calculo > Manutenção Tabelas > **S038 Outras Entidades**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042891314)  
  
**Automação Fiscal - TAF**  
Menu: Atualizações > Eventos eSocial > Tabelas> **Lotações Tributárias**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042890854)  
  
**Site [eSocial](https://login.esocial.gov.br/login.aspx)**  
Deve ser verificado no cadastro da tabela evento **S-1020** se código de terceiros está correto e igual ao **GPE** e **TAF**.  
  
**Atenção:** Caso não exista no TAF o código de terceiros **0000** deve ser verificado se o sistema está atualizado com os últimos pacotes disponíveis na página [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw).  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[Artigos S-1020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051258534)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
