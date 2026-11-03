---
article_id: 360020224111
category: GPE - eSocial - Periódicos
content_hash: 0d82fb16d704b0537cbf94c3bdbe05f0746b6e7f37200f64a755572fbf094d2b
fetched_at: '2026-06-28T22:45:07.457602+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial/DCTFWEB - Salário-Família pago pela empresa
  e sua Compensação na DCTFWEB
type: support-article
updated_at: '2025-07-25T19:49:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020224111-RH-Linha-Protheus-GPE-eSocial-DCTFWEB-Sal%C3%A1rio-Fam%C3%ADlia-pago-pela-empresa-e-sua-Compensa%C3%A7%C3%A3o-na-DCTFWEB
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33723598924439) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**Salário-Família pago pela empresa e sua Compensação na **DCTFWEB.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Causa**Conforme o manual da DCTFWEB a compensação do salário-família e salário-maternidade deve ocorrer automaticamente, porém isso ocorre quando os eventos foram enviados de forma lógica,  cronológica e preenchido corretamente (Exemplo: S-2200, S-2230, S-1200, etc).  
Fonte: [Manual Web DCTF web](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/manuais/manual-dctfweb/manual-dctfweb-atualizacao-janeiro2025_versao_final.pdf)  
  
**Solução**Para o **eSocial** a verba com ID de cálculo **0034 - Salário-Família** deverá ser enviada através do evento **S-1010** com a Natureza **1409 - Salário-Família** e Código de Incidência Tributária de Contribuição Previdenciária igual a **51 - Salário-Família**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015949692)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015993451)  
  
No cálculo da folha de pagamento do Trabalhador no **GPE** não há alteração.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015993551)  
  
O mesmo ocorre no evento **S-1200**, a informação vai normalmente como qualquer outra remuneração.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015949912)  
  
O valor total de Salário-Família pago pela empresa será apresentando no evento **S-5011**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015950852)  
  
Obs.: Vale ressaltar que que as incidências e naturezas deverão ser analisadas internamente por cada empresa.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
