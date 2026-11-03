---
article_id: 13646497307415
category: GPE - eSocial - Processo Trabalhista
content_hash: 8a05b163aaa2e63412eb73b04095bbdd5486a0dd8de6e88a29c5481a2aea0d6c
fetched_at: '2026-06-28T22:45:00.627739+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2500 - Como enviar as informações de
  Vara para o evento S-2500
type: support-article
updated_at: '2024-06-19T18:13:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13646497307415-RH-Linha-Protheus-GPE-eSocial-S-2500-Como-enviar-as-informa%C3%A7%C3%B5es-de-Vara-para-o-evento-S-2500
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24294507149847) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como enviar as informações de Vara para o evento S-2500?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**De acordo com o leiaute S-1.1 deve ser enviado o código de identificação da Vara em que o processo tramitou e preencher com a sigla da Unidade da Federação onde está localizada a Vara.  
Para que o sistema gere corretamente as informações devemos seguir os passos a seguir:  
 **1º** Acesse Atualizações > Processos Trabalhistas > Cadastros > Varas e clique em Atualizar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13646082720791)  
  
**2º** Após confirmar o cadastro, acesse Atualizações > Processos Trabalhistas > Processos > Processo (APTA100) para incluir  vara no processo que deve ser criado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13646227306007)  
  
**3º** Acesse a rotina Dados eSocial (TAFA552D) e verifique se a Vara foi levada corretamente:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13646335470871)  
  
Exemplo do xml do evento S-2500:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13646469080727)  
  
O id da vara é código atribuído pelo TRT estipulado no processo trabalhista, essa informação deve ser incluída manualmente no cadastro da vara. O meu exemplo foi 1000, mas de acordo com o leiaute deve ser o **Código de identificação da Vara em que o processo tramitou**. O esocial **não tem uma tabela padrão no leiaute**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14124917733527) **Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Premissas para geração dos eventos de processos trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847)  
  
**Próximos Treinamentos**[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
[TOTVS RESPONDE TOTVS RH (TODAS AS LINHAS) ESOCIAL](https://rhinforma.totvs.com/2023/04/04/totvs-responde-totvs-rh-todas-as-linhas-esocial-processo-trabalhista/)  
  
Essa documentação também pode ser **acessada 24h e diretamente do Protheus,** através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
