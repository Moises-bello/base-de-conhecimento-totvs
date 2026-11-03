---
article_id: 360033906273
category: GPE - eSocial - Carga Inicial
content_hash: bb73a34e108e97d9dda1c1dae4940d4637a64ab03ba1a655e40c39ba01cbf41a
fetched_at: '2026-06-28T22:45:03.330964+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-2299/S-1020/S-1005 - Como informar
  Tomador de Serviço ao eSocial
type: support-article
updated_at: '2025-07-28T17:13:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033906273-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-S-1020-S-1005-Como-informar-Tomador-de-Servi%C3%A7o-ao-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27476414535319)Tempo aproximado para leitura: **00:02:00min  
  
Dúvida**Como informar Tomador de Serviço ao eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**O padrão do Protheus é informar Estabelecimentos e Lotações Tributárias através do cadastro de Centro de Custo.   
No SIGAGPE foi disponibilizado um novo controle dessas informações, porém, **ATENÇÃO**, ele é **OPCIONAL** e uma vez que passou a utilizá-lo não será possível voltar ao formato anterior, para mais informações e como parametrizar, acesse a documentação: [RH - Novo Controle de Lotações](http://tdn.totvs.com/x/PCcxHQ).  
No caso de Tomadores de Serviço poderá criar um Centro de Custo e informar os dados do Tomador do Serviço no cadastro da Lotação e informar o Tipo de Lotação mais adequado na sua situação.  
  
Haverá situações que será gerado o evento S-1005 e S-1020 ou somente o S-1020, porém isso depende do seu cenário e Tipo de Lotação informado no cadastro do Centro de Custo, segue abaixo o link para um artigo que discorre sobre esse conceito no caso de Obras.  
  
[RH - Linha Protheus - GPE- eSocial - Obras - S-1005 x S-1020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030600113/)    
  
Quando o Trabalhador prestou serviço em mais de um local será necessário realizar Rateio para fazer a proporção da Folha de Pagamento em cada local (Centro de Custo), para mais informações sobre a Programação de Rateio acesse o artigo abaixo:  
  
[RH - Linha Protheus - GPE - Como realizar a programação de rateio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018658931)  
  
É importante ressaltar que para o eSocial será enviado o evento S-1200/S-2299 separado por Estabelecimento e Lotação Tributária e o conteúdo desse evento é influenciado nas informações do Centro de Custo que consta histórico de pagamento do SIGAGPE (SRC, SRD e etc).  
  
**Não deverá ser enviado os dados de tomador no S-1020 se tpLotacao for igual a [01, 10, 21, 24, 90, 91, 92]. Nos demais casos, observar conteúdo exigido para o campo [dadosLotacao/nrInsc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/index.html#1020_infoLotacao_inclusao_dadosLotacao_nrInsc), conforme [Tabela 10](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/tabelas.html#10).**

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**".*
