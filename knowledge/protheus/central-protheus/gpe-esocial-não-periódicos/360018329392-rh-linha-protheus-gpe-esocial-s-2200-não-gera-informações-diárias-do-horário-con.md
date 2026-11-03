---
article_id: 360018329392
category: GPE - eSocial - Não Periódicos
content_hash: 589f6d6eee06385c175f87f627e1146a3ba89137d12e951789b39a0fa46e642f
fetched_at: '2026-06-28T22:45:04.547132+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Não gera Informações Diárias
  do Horário Contratual no TAF
type: support-article
updated_at: '2026-06-16T13:35:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018329392-RH-Linha-Protheus-GPE-eSocial-S-2200-N%C3%A3o-gera-Informa%C3%A7%C3%B5es-Di%C3%A1rias-do-Hor%C3%A1rio-Contratual-no-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41262144350359) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Ao gerar o evento **S-2200** não estão sendo encaminhadas as informações diárias do horário contratual do **GPE** para o **TAF**, referente ao tipo de dia e horário diário. O que precisa ser validado para que esta informação seja integrada?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Para que as informações referentes aos campos da aba "Informações Diárias do Horário Contratual" no vínculo do funcionário do **TAF**, por meio da geração do evento S-2200, é necessário validar:  
  
**1.** Se o sistema está com as últimas atualizações disponíveis aplicadas. Estas atualizações podem ser validadas no *link*:  
<http://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais>  
  
**2.** Conferência do compartilhamento das tabelas do **GPE** e do **TAF**, que podem ser analisado a partir do link:  
[MP - GPE - eSocial - Como deve ser definido o Compartilhamento de Tabelas SIGAGPE x SIGATAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004178832/)  
  
**3.** Importante validar como está sendo gerado o conteúdo da *tag* **tpJornada** no ***xml***, que irá informar o tipo de jornada de trabalhado que o funcionário está vinculado. Se o conteúdo for "3 - **Funções Específicas**", os dados de dia e horários não serão encaminhados ao **TAF**, pois funcionários vinculados a este tipo não possuem horários definidos.  
  
**4.** Verifique os cadastros de **Turno de Trabalho** e **Tabela de Horario Padrão**.  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:  
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)    
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****".*
