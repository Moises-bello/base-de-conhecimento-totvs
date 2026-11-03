---
article_id: 27283652157719
category: GPE - eSocial - Processo Trabalhista
content_hash: 3f77be17ede1e2f8082ed54044edcca48f36d6192b8a56d1a4e70b34e29bd0f5
fetched_at: '2026-06-28T22:45:00.479988+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2500 - Quais informações básicas para
  incluir processo por responsabilidade indireta
type: support-article
updated_at: '2024-10-23T20:18:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27283652157719-RH-Linha-Protheus-GPE-eSocial-S-2500-Quais-informa%C3%A7%C3%B5es-b%C3%A1sicas-para-incluir-processo-por-responsabilidade-indireta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27283652141207) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais informações básicas para incluir processo por responsabilidade indireta?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para geração do S-2500 em casos de processo por responsabilidade indireta, é necessário informar o trabalhador que não é cadastrado como funcionário da empresa. Veja abaixo sobre responsabilidade indireta de acordo com o [MOS S-1.3](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-publicado-com-marcacoes.pdf) página 323  
  
**8. Responsabilidade indireta**  
**8.1.** Em caso de determinação judicial para pagamento do valor da condenação pelo responsável indireto (subsidiário ou solidário), o evento S-2500 deve ser enviado por esse responsável. Neste caso, o declarante, deve observar as seguintes regras:  
  
**a)** caso a responsabilidade seja compartilhada entre mais de um devedor, o valor das bases a ser informado deve corresponder à cota parte do declarante;  
  
**b)** mesmo que o vínculo já tenha sido declarado no eSocial pelo responsável direto, o declarante deve  
criar uma matrícula para identificar o vínculo neste evento, em exceção à regra prevista no item 1.6.1,  
alínea “a” deste evento;  
Para o Protheus a matricula deve ser informada na rotina Dados eSocial (TAFA552D), conforme imagem abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27283652142615)  
  
**c)** deve ser preenchido o campo {indContr} com [N] e o campo {tpContr} com [8];  
indContr = Informação do Evento  
tpContr = Tipo de Vinculo  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27283696053143)  
  
**d)** o grupo [ideResp] deve ser preenchido para identificar o responsável direto, com os campos {tpInsc} e {nrInsc} preenchidos.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27283652146199)  
  
**e)** o prazo para envio deste evento é o dia 15 do mês seguinte à data em que houver a determinação  
judicial para o cumprimento da decisão pelo responsável indireto.  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[RH - Linha Protheus - GPE - eSocial - S-2500 - Como incluir trabalhador para processos em casos de responsabilidade indireta e qual a regra do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25171652151191-RH-Linha-Protheus-GPE-eSocial-S-2500-Como-incluir-trabalhador-para-processos-em-casos-de-responsabilidade-indireta-e-qual-a-regra-do-eSocial)  
[Artigos RH Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".*
