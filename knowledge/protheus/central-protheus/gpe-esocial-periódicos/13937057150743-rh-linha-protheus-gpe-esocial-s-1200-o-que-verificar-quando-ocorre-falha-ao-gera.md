---
article_id: 13937057150743
category: GPE - eSocial - Periódicos
content_hash: 2ef68b0fe812ce674ecc62bafe96e0467919582cb6ce7d2db7ae4d5bfc69b301
fetched_at: '2026-06-28T22:45:08.702994+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - O que verificar quando ocorre
  falha ao gerar o S-1200 de Trabalhador sem Vinculo
type: support-article
updated_at: '2025-07-24T17:51:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13937057150743-RH-Linha-Protheus-GPE-eSocial-S-1200-O-que-verificar-quando-ocorre-falha-ao-gerar-o-S-1200-de-Trabalhador-sem-Vinculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21788428199063) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**O que verificar quando ocorre falha ao gerar o S-1200 de autônomo? O que analisar quando não gera periódico de autônomo?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Verifique os itens abaixo quando ao gerar os eventos periódicos de autônomos, o sistema **apresenta falha ou não integra**: **1.** Deve existir **apenas um evento S-2300 com status 4 - ACEITO e número de recibo.** Nem todo autônomo terá o evento S-2300, pois no leiaute nem todas as categorias são obrigatórias. Porém se houver, verifique o status no módulo 84 ou Middleware.  
**2.** Os campos Cod. Unico (**RA\_CODUNIC)** e Matricula (**C9V\_MATTSV**) devem ter a mesma informação, caso o autônomo tenha o evento S-2300.  
**3.** Caso o campo Matricula (**C9V\_MATTSV**) esteja em branco, verifique se o campo Controle de matricula TSV (**RA\_DESCEP)**está preenchido. Esses dois campos possuem duas validações:  
  
**3.1 - Primeiro cenário**  
   Cod. Unico (RA\_CODUNIC**) = preenchido**  
   Matricula (C9V\_MATTSV) = **vazio**  
   Controle de matricula TSV (RA\_DESCEP**)**= **vazio**(não pode preencher caso o C9V\_MATTSV esteja         vazio)   
   **Matrícula deve estar vazio no cadastro do trabalhador no portal eSocial**  
   
**3.2 - Segundo Cenário**  
   Cod. Unico (RA\_CODUNIC**) = preenchido**  
   Matricula (C9V\_MATTSV) = **preenchido**(com mesma informação do campo RA\_CODUNIC)  
   Controle de matricula TSV (RA\_DESCEP**)**= **1**(com os dois campos acima preenchido e este vazio, vai     dar erro)   
  **Matrícula deve estar preenchida no cadastro do trabalhador no portal eSocial**  
  
**4.** O campo **C9V\_DTINIV**está com a mesma informação do campo Data Admissão (**RA\_ADMISSA**)  
**5.** Nos casos do autônomo ter o evento S-2300, sua categoria para o eSocial não pode estar contida no parâmetro **MV\_NTSV**.  
**6.**Em casos que não tem o evento S-2300, a categoria para o eSocial deve estar contida no parâmetro **MV\_NTSV**.  
  
Para verificar o conteúdo do parâmetro MV\_NTSV, vá no Configurador em **SIGACFG > Ambiente > Cadastros > Parâmetros**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24319022053271)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24319009005335)  
  
Para mais detalhes referente ao parâmetro **MV\_NTSV**, verifique a documentação abaixo:  
[RH Linha Protheus - GPE - eSocial - Novo controle de autônomos - Parâmetro MV\_NTSV](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410718721687-RH-Linha-Protheus-GPE-eSocial-Novo-controle-de-aut%C3%B4nomos-Par%C3%A2metro-MV-NTSV)  
  
Caso seu campo **RA\_DESCEP esteja com conteúdo 1** e **C9V\_MATTSV vazio**, será necessário **aplicar o pacote** abaixo que foi disponibilizado para correção e **executar o *rdmake* ATUDESCEP** conforme artigo: [RH - Linha Protheus - GPE - eSocial - Funcionalidade do rdmake ATUDESCEP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8559365211543) para ajustar o RA\_DESCEP. Ou o inverso também, deve ser executado o *rdmake*.  
  
Para verificar a matricula (**C9V\_MATTSV**) do Trabalhador Sem Vinculo no módulo 84, acesse o menu: **Atualizações > Eventos eSocial > Trabalhador >** **Cadastro Trabalhador**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24319022084503)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21788400947095)  
  
Para verificar o campo **Contr. Mat. TSV** (RA\_DESCEP), acesse o módulo 07 em: **Atualizações > Funcionários > Gestão Funcionários**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24319022101271)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21788431222679)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
