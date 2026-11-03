---
article_id: 360050706213
category: GPE - eSocial - Periódicos
content_hash: 03af5dfbfb22e18600d4d40ab6c111b434a0ced8e53a8eaf77dbd2450f4a246a
fetched_at: '2026-06-28T22:45:09.898024+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-5001 - Quando existe na folha a verba
  de ID 1412 (Devolução INSS) o INSS do trabalhador fica incorreto no governo
type: support-article
updated_at: '2025-07-25T14:10:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050706213-RH-Linha-Protheus-GPE-eSocial-S-5001-Quando-existe-na-folha-a-verba-de-ID-1412-Devolu%C3%A7%C3%A3o-INSS-o-INSS-do-trabalhador-fica-incorreto-no-governo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33713594612503) Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**Quando existe na folha a verba de ID 1412 (Devolução INSS) o INSS do trabalhador fica incorreto no governo. **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**A diferença entre valores de **INSS** Folha e **eSocial** pode ocorrer devido a verba de ID **1412** não ter incidência para previdência no eSocial. Se essa verba tem incidência para INSS folha também deve ter para o governo. Conforme documentação: [DRHESOCP-16891 DT Cadastro da Verba de Id 1412](https://tdn.totvs.com/x/jNxvI)  
  
**Solução**1. No SIGAGPE acesse o cadastro de verbas no caminho: Atualizações > Definições Cálculo > Verbas;  
  
2. Acesse a aba eSocial e deixe o campo CD. INC. CP com **31**;  
  
3. Assim que confirmar o sistema vai mostrar uma tela para ser definido qual será o período inicial de vigência que a rubrica deve ser gerada. A data inicial da rubrica não pode ser posterior a competência da folha que está com o erro;![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075728954)  
  
4. Transmita a rubrica para o governo;  
  
5. Retifique o evento S-1200, caso já tenha transmitido o evento S-1210 será necessário excluir o S-1210, para depois transmitir o S-1200.  
  
**Observação**  
Caso na folha a incidência já esteja correta, verifique a incidência da rubrica no governo.  
[S-1010 - Como consultar no site do eSocial dados do evento S-1010 (Tabelas de Rubricas)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043153534)  
  
**Importante**Os dados utilizados nos exemplos são meramente ilustrativos, cabe ao usuário avaliar a sua necessidade e legislação vigente para realizar as configurações.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[Como conferir o retorno do governo no evento S-5001 com a folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
