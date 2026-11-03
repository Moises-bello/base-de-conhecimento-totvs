---
article_id: 360049923054
category: GPE - eSocial - Periódicos
content_hash: 5f6827b084019bfe267d1de06b25dabe62d19c48f10aa7a2a74328c4974b6542
fetched_at: '2026-06-28T22:45:07.620683+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1010 - Inconsistência do RET - Ocorrência
  244 - Natureza da rubrica invalida
type: support-article
updated_at: '2025-07-22T20:48:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049923054-RH-Linha-Protheus-GPE-eSocial-S-1010-Inconsist%C3%AAncia-do-RET-Ocorr%C3%AAncia-244-Natureza-da-rubrica-invalida
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21618448538391)**Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Sequência: 000001 - Tipo: Erro - Codigo da ocorrência: 244  
Localização: /eSocial/evtTabRubrica/infoRubrica/inclusao/dadosRubrica/natRubr  
Descrição: Natureza da rubrica invalida.Acao Sugerida: O valor informado no campo devera existir e estar valido no periodo na Tabela 3 (Natureza das Rubricas da Folha de Pagamento).  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Essa inconsistência de retorno ocorre quando enviado o S-1010 ao eSocial com um **código de natureza descontinuado** pelo eSocial.  
  
Exemplo:  
Algumas naturezas das rubricas foram descontinuadas pelo eSocial, entre elas 1801 e 9220 (término em 30/06/2021) e as 2902, 2920 e 9290 (término 31/07/2021)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404719044119)  
  
Com isso é **necessário escolher outra natureza** para enviar esses valores para o governo. Destacamos, que o governo não informa qual rubrica utilizar, dessa forma a escolha é de responsabilidade do empregador.   
Importante ressaltar que essa inconsistência pode ocorrer para qualquer natureza que tenha seu término determinado pelo governo.  
  
[Como ajustar incidência e validade de rubricas no governo, TAF e GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512-RH-Linha-Protheus-GPE-eSocial-S-5001-Como-ajustar-incid%C3%AAncia-e-validade-de-rubricas-no-governo-TAF-e-GPE)   
  
**Solução**1. Após estar com o pacote [Expedição Continua RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA) aplicado, acesse o SIGAGPE para atualizar as tabelas do eSocial conforme artigo: [Como atualizar as tabelas S047, S048, S049, S054, S056 e S057](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016801271-MP-GPE-eSocial-Como-atualizar-as-tabelas-S047-S048-S049-S054-S056-e-S057-conforme-layout-2-5-01-do-eSocial?source=search)  
  
2. Acesse o cadastro de verbas no caminho: Atualizações > Definições Cálculo > Verbas;  
  
3. Acesse a aba eSocial e ajuste para a **Natureza** desejada;  
  
4. Assim que confirmar o sistema vai mostrar uma tela para ser **definido qual será o período inicial de vigência que a rubrica** deve ser gerada. A data inicial da alteração da rubrica deverá ser igual ou anterior  a competência do S-1200 que está com a inconsistência:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404727131159)  
  
5. Transmita a rubrica para o governo.  
  
  
Caso haja alguma inconsistência de retorno ocorre quando enviado o S-1200 ao eSocial, informando que existe alguma rubrica com um **código de natureza descontinuado** pelo eSocial, é necessário retifique o evento S-1200, para que seja considerado a rubrica ajustada. Caso já tenha transmitido o evento S-1210 será necessário excluir o S-1210, para depois transmitir o S-1200.  
  
**Importante**Os dados utilizados nos **exemplos** são meramente ilustrativos, cabe ao usuário avaliar a sua necessidade e legislação vigente para realizar as configurações.  
  
Para consultar quais naturezas estão vigentes acesse a tabela de [Natureza do leiaute.](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-01-2024-rev-03-10-2024/tabelas.html#03)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[Como consultar no site do eSocial dados do evento S-1010 (Tabelas de Rubricas)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043153534-RH-Linha-Protheus-GPE-eSocial-S-1010-Como-consultar-no-site-do-eSocial-dados-do-evento-S-1010-Tabelas-de-Rubricas?source=search)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
