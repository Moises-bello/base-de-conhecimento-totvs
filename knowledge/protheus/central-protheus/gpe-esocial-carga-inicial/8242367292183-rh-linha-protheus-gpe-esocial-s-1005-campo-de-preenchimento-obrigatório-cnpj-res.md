---
article_id: 8242367292183
category: GPE - eSocial - Carga Inicial
content_hash: 31474e830211fd035037e11357a14904774d184c2c3e8e1f609b3a3711f339fb
fetched_at: '2026-06-28T22:45:03.163584+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1005 - Campo de preenchimento obrigatório,
  CNPJ responsável pela inscrição no cadastro de obras da RFB
type: support-article
updated_at: '2024-08-20T18:15:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8242367292183-RH-Linha-Protheus-GPE-eSocial-S-1005-Campo-de-preenchimento-obrigat%C3%B3rio-CNPJ-respons%C3%A1vel-pela-inscri%C3%A7%C3%A3o-no-cadastro-de-obras-da-RFB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25783221417239) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Código da ocorrência: 1 - Campo de preenchimento obrigatório: CNPJ responsável pela inscrição no cadastro de obras da RFB.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**De acordo com o leiaute simplificado, no evento S-1005 a *tag* **cnjpResp** tem preenchimento obrigatório e exclusivo por Pessoa Jurídica e se [ideEstab/tpInsc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-nt-06-2022-html/index.html/index.html#1005_infoEstab_inclusao_ideEstab_tpInsc) = [4]. Informação obrigatória se [iniValid](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-nt-06-2022-html/index.html/index.html#1005_infoEstab_inclusao_ideEstab_iniValid) >= [2022-04].  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8241633032215)  
  
O **preenchimento** do **CNPJ Responsável** deve ser através da tabela **S119** - **Dados eSocial - Matriz/Filiais** ou pelo **Cadastro de Obras Próprias eSocial** (RJ4), quando for utilizado o novo controle de Lotações.  
  
Para **acessar** a tabela **S119**, entre em Atualizações - Definições Cálculo - **Manutenção de Tabelas** - S119:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8241958142999)  
  
Caso utilize o novo controle de Lotações, acesse Atualizações - Cadastro - eSocial Obras/Lotações - **Obras Próprias:**  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8242279633815)  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[S-1005 - Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos](https://tdn.totvs.com/pages/viewpage.action?pageId=286510545)
