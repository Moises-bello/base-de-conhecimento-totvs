---
article_id: 14229685206551
category: GPE - eSocial - Não Periódicos
content_hash: 8e4b14e1d1d025ef58dbe61b933b60211a6889b03d35b6c6c73ae8bc25a40d21
fetched_at: '2026-06-28T22:45:04.570268+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 -Lei nº 12.288 Estatuto da Igualdade
  Racial para o eSocial
type: support-article
updated_at: '2026-06-16T11:28:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14229685206551-RH-Linha-Protheus-GPE-eSocial-S-2200-Lei-n%C2%BA-12-288-Estatuto-da-Igualdade-Racial-para-o-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24317981252631) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como o sistema gera as informações da *tag* **racaCor** para o eSocial e atender a Lei nº 12.288?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
A Nova Lei determina que o Instituto Brasileiro de Geografia e Estatística (IBGE), realize pesquisa a cada cinco anos para mensurar o percentual de cada raça e etnia no setor público.  
Os campos deverão ser preenchidos pelo trabalhador com a utilização do critério da autoclassificação.  
A regra deve ser aplicada nos seguintes formulários: admissão e demissão no emprego; acidente de trabalho; inscrição de segurados e dependentes no Instituto Nacional do Seguro Social (INSS); pesquisas do IBGE; registro feito no Sistema Nacional de Emprego (Sine); e na Relação Anual de Informações Sociais (Rais).  
  
**Destacamos** que , no **eSocial, as informações de Raça/Cor já são obrigatórios** nos seguintes eventos:  
**S-2200** – Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador;  
**S-2205** – Alteração de Dados Cadastrais do Trabalhador;  
**S-2300** – Trabalhador Sem Vínculo de Emprego/Estatutário – Início;  
  
Os campos válidos para preenchimento do eSocial são **Raça e cor do trabalhador**:  
1 – Branca  
2 – Preta  
3 – Parda  
4 – Amarela  
5 – Indígena  
6 – Não informado  
  
No Protheus através do cadastro de funcionários ou cadastro de autônomos, teremos as mesmas informações de raça/cor. Para atender outras entregas legais, o sistema está com numeração diferente do esocial, entretanto para o **xml é levado corretamente a numeração estipulada no leiaute.**  
**Exemplo**:  
No cadastro do funcionário, selecionamos a opção **8 - Parda:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14229535717143)  
  
No **xml** do evento **S-2200** é levado na ***Tag*** **<racaCor> o código 3**, conforme leiaute.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14229632291351)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
