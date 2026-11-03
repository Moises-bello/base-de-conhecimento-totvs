---
article_id: 360037333714
category: GPE - eSocial - Não Periódicos
content_hash: 9ed89eb797dd915f7734fcb4e08e3304f80a2b89762f860a529b5fc893a3b7a1
fetched_at: '2026-06-28T22:45:04.583606+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 / S-2206 - De forma técnica como
  funciona a vinculação de horários com o S-2200 e S-2206, e quais as tabelas utilizadas
type: support-article
updated_at: '2026-06-16T11:26:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037333714-RH-Linha-Protheus-GPE-eSocial-S-2200-S-2206-De-forma-t%C3%A9cnica-como-funciona-a-vincula%C3%A7%C3%A3o-de-hor%C3%A1rios-com-o-S-2200-e-S-2206-e-quais-as-tabelas-utilizadas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19459202519703) Tempo aproximado para leitura: 02:00 min**  
  
**Dúvida**  
De forma técnica como funciona vinculação de horários com o S-2200 e S-2206, e quais as tabelas utilizadas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
As informações abaixo tem caraterísticas técnicas com intuito de detalhar para o profissional de TI a origem e regras das informações utilizadas no evento S-2200 e S-2206 referente a horário de trabalho.  
Para conhecer o **De/Para** dos campos GPE x TAF consulte o link: [Correspondência Layouts eSocial x Protheus](https://tdn.totvs.com/x/BYETEQ)  
  
**1 - Informações de Horário no S-1050**  
Desde o leiaute S-1.0, vigente em 19/07/2021 o evento S-1050 (Tabela de Horários/Turnos de Trabalho) foi descontinuado.  
  
As informações do Horários/Turnos de Trabalho devem ser enviados no cadastro do trabalhador (enviado pelo S-2200) e nas alterações contratuais (enviado pelo S-2206).  
  
Em ambos os eventos, as informações são enviadas no grupo de informações [horContratual](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1.1-nt-01-2023/index.html#r_2200_vinculo_infoContrato_horContratual):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19459202533911)  
  
**2- Informações de Horário no S-2200 / S-2206**  
No **S-2200 / S-2206** as informações de Horário tem origem na tabela **SRA** (funcionários) do GPE onde o sistema utiliza informações dos campos Turno, Regra, Sequencia, e Tp.Reg.J.Tra para gravar no TAF as informações referente ao horário do trabalhador nas tabelas **C9V, CUP, CRQ** (S-2200) **e T1V, T3U** (S-2206).  
Caminho SIGAGPE: A*tualizações > Funcionários > Funcionários*  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048926234)  
  
Caminho SIGATAF: A*tualizações > Eventos Esocial > Trabalhador > Cadastro Trabalhador*  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049823853)  
  
**Exemplo XML S-2200 / S-2206:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19459202538391)**  
  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)  
[Artigos S-2206](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055237854)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
