---
article_id: 16651438061591
category: GPE - eSocial - Periódicos
content_hash: bc5b3968cc5b3caefb7ebcc86e7eb09fd6b352b98a4f33aa73c2705cad9506d0
fetched_at: '2026-06-28T22:45:09.955982+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - S-1210/S-1200 - Como enviar valores de IR para
  residentes no exterior com código de receita 0473
type: support-article
updated_at: '2025-11-11T14:50:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16651438061591-RH-Linha-Protheus-GPE-S-1210-S-1200-Como-enviar-valores-de-IR-para-residentes-no-exterior-com-c%C3%B3digo-de-receita-0473
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16651402795031) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como enviar valores de IR para residentes no exterior, com código de receita 0473?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**De acordo com o [Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica) vigente, segue informações dos eventos S-1210 e S-1200 sobre residentes no exterior:No evento **S-1210**, se o campo {**paisResidExt**} for preenchido com um código de país diferente de 105 (Brasil), devem ser preenchidas as informações complementares do grupo [**infoPgtoExt**] no mesmo evento.   
Somente com o preenchimento das informações do parágrafo acima é que é gerado o **Código de**  
**Receita 0473-01** (IRRF - RENDIMENTOS TRABALHO - RESID EXTERIOR)  
  
No evento **S-1200**, o empregado transferido para prestar serviços no exterior, nos termos da Lei nº 7.064, de 1982, pode, no todo ou em parte, ter sua remuneração paga no exterior, em moeda estrangeira. Todavia, mesmo que a remuneração seja integralmente paga no exterior, o declarante deve obrigatoriamente convertê-la em moeda nacional, e informá-la neste evento, em harmonia com as informações prestadas nos eventos S-1010 e S-1020, **conforme adiante demonstrado**:

|  |  |  |  |
| --- | --- | --- | --- |
| **Evento** | **Recebe apenas no Exterior** | **Recebe apenas no Brasil** | **Recebe no Brasil e no Exterior** |
| **S-1200** | Rubrica informativa - Natureza 9906 da Tabela 3 (remuneração recebida no exterior) | Folha normal (remuneração recebida no Brasil) | Folha Normal (remuneração recebida no Brasil) Rubrica Informativa Natureza 9906 da Tabela 3 (remuneração recebida no exterior) |
| **S-1210** | Informar lotação tributária - código 90 (Tabela 10) e FPAS 590 (Tabela 4) | Informar lotação tributária - código 90 (Tabela 10) e FPAS 590 (Tabela 4) | Informar lotação tributária - código 90 (Tabela 10) e FPAS 590 (Tabela 4) |

Necessário seguir o passo a passo de cadastro e calculo:

* Informar um contrato de trabalho na tabela RGE - Histórico de Contratos.   
  Atualizações - Funcionários - **Histórico de Contrato**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16649543210647)

* No Cadastro de Funcionários, informar o  código de Retenção de IRRF 0473  
  Atualizações - Funcionários - **Contr. Individual**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16650002367767)

* Na **aba Endereço**, deixe o campo **Res. Exterior** com **SIM**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36253990699287)

* Gerar a Folha de Pagamento em competência que está na vigência do contrato
* Leiaute S-1.1 ou superior (MV\_VLESOC e MV\_TAFVLES)
* Tabela S022 devidamente preenchida  
  Atualizações - Definição Cálculo - **Manutenção de Tabelas**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16650233552535)

* Natureza da verba de pagamento deve ser 9906  
  Atualizações - Definição Cálculo - **Verbas**
* Lotação 90 e FPAS 590

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página *[TOTVS Informa](https://informa.totvs.com/)* selecione em categorias a área e pesquise por "Eventos".
