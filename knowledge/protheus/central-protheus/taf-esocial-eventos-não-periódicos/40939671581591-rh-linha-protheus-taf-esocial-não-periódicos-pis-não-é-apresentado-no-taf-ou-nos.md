---
article_id: 40939671581591
category: TAF - eSocial - Eventos Não Periódicos
content_hash: c08ebb3a61f8f91640f0638ceee2f8a324cc77cee7cd7f3785895f3b94bf3b03
fetched_at: '2026-06-28T22:45:18.071833+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Não Periódicos - PIS não é apresentado
  no TAF ou nos eventos S-2200/S-2300
type: support-article
updated_at: '2026-06-03T15:49:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40939671581591-RH-Linha-Protheus-TAF-eSocial-N%C3%A3o-Peri%C3%B3dicos-PIS-n%C3%A3o-%C3%A9-apresentado-no-TAF-ou-nos-eventos-S-2200-S-2300
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40939632381207) Tempo aproximado para leitura: **HH:05:00 min**  
  
**Dúvida**  
Por que o número do PIS está preenchido corretamente no cadastro do funcionário, em meu ERP (RM, Datasul, GPE) mas não é carregado ou atualizado no TAF e não aparece nos eventos S-2200/S-2300?  
  
**Ambiente**  
TOTVS RH - Linha Protheus - TAF eSocial - Eventos Não Periódicos - S-2200 (TAFA278)  e S-2300 (TAFA279) - todas as versões  
  
**Solução**

Na versão atual do leiaute do eSocial, a informação do **PIS/NIS** não é mais enviada por meio dos eventos **S-2200 (Cadastramento Inicial/Admissão do Trabalhador)** e **S-2300 (Trabalhador Sem Vínculo de Emprego/Estatutário)**.

Atualmente, o ambiente do eSocial realiza a identificação do trabalhador utilizando o **CPF**, buscando automaticamente as demais informações cadastrais necessárias.

Dessa forma, mesmo que o PIS esteja cadastrado no ERP (RM, Datasul, GPE) , essa informação não será transportada para o TAF através dos eventos S-2200 e S-2300, pois o campo deixou de existir no leiaute vigente do eSocial.

**Link do leiaute do eSocial:**  
<https://www.gov.br/esocial/pt-br/documentacao-tecnica>

**Saiba Mais**

Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos"

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
