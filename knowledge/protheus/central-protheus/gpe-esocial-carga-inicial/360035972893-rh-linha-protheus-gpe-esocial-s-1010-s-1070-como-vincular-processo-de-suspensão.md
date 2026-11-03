---
article_id: 360035972893
category: GPE - eSocial - Carga Inicial
content_hash: 38c1ea064492aeb3144a76c6dcd78bda7c4d1bae0c4e8d0f603f1334839f74bd
fetched_at: '2026-06-28T22:45:03.305393+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1010 / S-1070 - Como vincular processo
  de suspensão de incidência no cadastro de Rubricas do TAF
type: support-article
updated_at: '2024-06-05T18:17:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035972893-RH-Linha-Protheus-GPE-eSocial-S-1010-S-1070-Como-vincular-processo-de-suspens%C3%A3o-de-incid%C3%AAncia-no-cadastro-de-Rubricas-do-TAF
---

**Dúvida**S-1010 / S-1070 - Como vincular processo de suspensão de incidência no cadastro de Rubricas do TAF?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
 **Solução**  
Para cadastrar um processo e vincular ao evento realize os seguintes passos:

1. Certifique-se de existir um evento 'S-1070 - Tabela de Processos Administrativos/Judiciais' no TAF com recibo do RET (Governo). Esse evento é preenchido através do SIGAJURI ou diretamente no TAF em "Atualizações > Eventos eSocial > Tabelas > Processos Administrativos/Judiciais". Em caso de duvidas consulte: [S-1070 - Onde cadastrar o evento S-1070 Processos Administrativos/Judiciais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012057432-MP-GPE-eSocial-S-1070-Onde-cadastrar-o-evento-S-1070-Processos-Administrativos-Judiciais?source=search).
2. Acesse o cadastro de Rubricas do TAF em "Atualizações > Eventos eSocial > Tabelas > Rubricas", filtre o Código de Rubrica com a Suspensão e pressione Alterar.  
     
   No cadastro da Rubrica altere os campos da Incidência Suspensa por um código apropriado para situação e informe os dados do processo (S-1070) na aba indicada para essa mesma Incidência.  
     
   ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047077213)
3. Transmita ao RET (Governo) através do Monitoramento do TAF o evento S-1070 e S-1010 vinculado ao processo.

**Observação:** Há situações em que o RET (Governo) retorna o evento com inconsistência, normalmente esse retorno estão relacionados a incidência tributária que não está condizente com o processo informado ou devido a problemas no ambiente, nesta segunda situação sugiro a leitura do artigo: [MP - GPE - eSocial - S-1070 - Erro de retorno do RET 8 - Descrição : Grupo #39;Informacoes da Suspensao#39; deve ser preenchido. Verifique as condicoes de preenchimento no leiaute](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034639874)  
  
**Importante**Os dados utilizados nos exemplos são meramente ilustrativos, cabe ao usuário avaliar a sua necessidade e legislação vigente para realizar as configurações.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[Artigos S-1010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051971613)[Artigos S-1070](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052499193)  
[MP - GPE - eSocial - S-5001 - Cálculo incorreto da suspensão do valor do INSS no E-Social](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018770072)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)
