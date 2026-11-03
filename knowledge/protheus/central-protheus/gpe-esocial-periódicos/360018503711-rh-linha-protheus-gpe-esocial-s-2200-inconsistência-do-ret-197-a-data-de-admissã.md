---
article_id: 360018503711
category: GPE - eSocial - Periódicos
content_hash: ee0941f4d95157d65bcd0fbb2a844ad5f87fbf57334160e4c2ff6746fbba6231
fetched_at: '2026-06-28T22:45:09.083745+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Inconsistência do RET - 197
  - A data de admissão do trabalhador não poderá ser anterior a data de abertura da
  empresa ou posterior a data de encerramento
type: support-article
updated_at: '2025-07-25T20:13:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018503711-RH-Linha-Protheus-GPE-eSocial-S-2200-Inconsist%C3%AAncia-do-RET-197-A-data-de-admiss%C3%A3o-do-trabalhador-n%C3%A3o-poder%C3%A1-ser-anterior-a-data-de-abertura-da-empresa-ou-posterior-a-data-de-encerramento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31646067619223) Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**Inconsistência do **RET** - 197 -  A data de admissão do trabalhador não poderá ser anterior a data de abertura da empresa ou posterior a data de encerramento  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa   
1.** Normalmente este erro está associado a divergência de informações no evento S-2200 no campo Cad. Inicial. Indicar se o evento se refere a cadastramento inicial de vínculo (data de admissão do trabalhador anterior à data de início de obrigatoriedade do empregador ao eSocial) ou se refere a uma admissão (data de admissão igual ou posterior à data de início de obrigatoriedade do empregador ao eSocial):  
S - Sim (Cadastramento Inicial);  
N - Não (Admissão).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14811301222935)  
  
**2.** A causa também pode estar relacionada  é importante verificar os campos de **Informações de Sucessão de Vínculo Trabalhista**. Caso tenha transferência entre raiz de CNPJ diferentes.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14811438426391)  
  
**Solução****1.**Verificar a opção correta a ser utilizada em cada caso.  
**2.** No caso de sucessão de vínculo os campos precisam ser preenchidos com informação da empresa anterior e quando ocorreu a transferência.  
Se a transferência ocorreu na mesma base do **Protheus** a informação deve constar no histórico do Trabalhador, mas na ausência dessas informações na base do **GPE** você deverá alimentar a informação manualmente no **TAF**.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
