---
article_id: 10534444019095
category: GPE - eSocial - Não Periódicos
content_hash: 16bc1729deec0febe4b645366d99fddc47f6739685921e6718c875bef8183f49
fetched_at: '2026-06-28T22:45:04.484139+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Como enviar S-2200 para empregado
  temporário categoria 106 eSocial
type: support-article
updated_at: '2026-06-16T11:51:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10534444019095-RH-Linha-Protheus-GPE-eSocial-S-2200-Como-enviar-S-2200-para-empregado-tempor%C3%A1rio-categoria-106-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41259505101719) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como enviar S-2200 para empregado temporário categoria 106 eSocial?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para atender o leiaute do eventos S-2200 para categoria 106, será necessário preencher o Cadastro de Funcionário Temporário para que o sistema gere o xml contendo os Dados sobre trabalho temporário de acordo com o solicitado pelo eSocial:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10533900188567)  
  
Ao confirmar o cadastro da categoria 106, o sistema emitirá a mensagem abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10533988810519)  
  
Após clicarmos em Confirmar, o sistema abre a tela da rotina GPEA927 - Cadastro de Funcionários Temporários  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10534012903959)  
  
Segue alguns dados solicitados neste cadastro são:  
**Motivo da contratação de trabalhador temporário** pode ter dois conteúdos (RBW\_MOTIVO):  
1. Necessidade transitória de substituição de seu pessoal regular;  
2. Acréscimo extraordinário de serviços.  
  
Se o Motivo da Contratação for 1, então é necessário informar:  
- CPF do trabalhador substituído (RBW\_CPFSUB)  
- Matrícula do trabalhador que está sendo substituído (RBW\_MATSUB)  
  
**Tipo Contratação** contendo 3 opções de preenchimento:  
1. Local sem Filiais  
2. Estudo de Mercado  
3. Contratação Superior a 3 Meses  
  
**Tipo de Inscrição** contendo duas opções conforme leiaute:  
1. CPNJ  
2. CPF  
  
**Local de Trabalho**, onde será necessário cadastrar o local através da rotina GPEA017 (locais de convocação):  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10534141431575)  
  
Ao confirmar o cadastro do trabalhador temporário, o sistema gera o evento S-2200 conforme estipulado em leiaute.  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[Leiaute eSocial Trabalhador Temporário](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/leiautes-esocial-nt-05-2022-html/index.html#2200_vinculo_infoRegimeTrab_infoCeletista_trabTemporario)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
