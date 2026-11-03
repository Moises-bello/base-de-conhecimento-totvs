---
article_id: 9605361090327
category: GPE - eSocial - Não Periódicos
content_hash: 70966ce75315a6fa93e86c7dbab2138afd1b3a7ecf7b99ba526683d6831f4ec6
fetched_at: '2026-06-28T22:45:05.990973+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - S-2206 - Em qual evento é enviado a tag referente
  ao CBO (CBOCargo e nmCargo)
type: support-article
updated_at: '2026-06-16T11:50:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9605361090327-RH-Linha-Protheus-GPE-S-2206-Em-qual-evento-%C3%A9-enviado-a-tag-referente-ao-CBO-CBOCargo-e-nmCargo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25188498635671) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Em qual evento é enviado a tag referente ao CBO (CBOCargo e nmCargo)?   
Como enviar cargo/função ao eSocial?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

O evento **S-1030 foi excluído do eSocial** a partir do leiaute Simplificado (S-1.0), portanto as informações relacionadas a cargos serão transmitidos através dos eventos **S-2200/S-2300/S-2206/S-2306, na TAG 'nmCargo' e a CBO na TAG CBOCargo.**

* O evento **S-2200** - (Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador) registra a admissão de empregado ou o ingresso de servidores estatutários, a partir da implantação do eSocial. Ele serve também para o cadastramento inicial de todos os vínculos ativos pela empresa/órgão público.

![](https://tdn.totvs.com/download/attachments/714221515/image2022-9-28_11-19-26.png?version=1&modificationDate=1664375765680&api=v2)

* O evento **S-2300** - (Trabalhador Sem Vínculo de emprego/Estatutário - Início registra as informações cadastrais relativas a trabalhadores que não possuem vínculo de empego/estatutário com a empresa/órgão público.

![](https://tdn.totvs.com/download/attachments/714221515/image2022-9-28_11-20-12.png?version=1&modificationDate=1664375765557&api=v2)

* O evento **S-2206** - (Alteração de Contrato de Trabalho) registra as alterações do contrato de trabalho, tais como: remuneração e periodicidade de pagamento, duração do contrato, local, cargo ou função, jornada ou entre outras informações.

![](https://tdn.totvs.com/download/attachments/714221515/image2022-9-28_11-20-51.png?version=1&modificationDate=1664375765407&api=v2)

* O evento  **S-2306** - (Trabalhador Sem Vínculo de Emprego/Estatutário - Alteração Contratual)  é utilizado para informar a atualização dos dados contratuais relativos aos trabalhadores que não possuem vínculo emprego/estatutário com a empresa/órgão público.

![](https://tdn.totvs.com/download/attachments/714221515/image2022-9-28_11-21-22.png?version=1&modificationDate=1664375765237&api=v2)

Desta forma na versão S.1.0 a CBO correta será enviada ao enviar o evento S-2200 (Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador), para as novas admissões.   
As admissões que foram enviadas nos leiautes anteriores que não contemplava a CBO no evento S-2200 deverá ser enviado o **S-2206 (Alteração de Contrato de Trabalho) para ajustar a CBO se necessário**.  
  
Para o Protheus, podemos enviar a alteração através da rotina GPEM047: [RH - Linha Protheus - GPE - eSocial - S-2206 - Como fazer a geração de eventos de alteração contratual S-2206 / S-2306 em lote](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039570633-RH-Linha-Protheus-GPE-eSocial-S-2206-Como-fazer-a-gera%C3%A7%C3%A3o-de-eventos-de-altera%C3%A7%C3%A3o-contratual-S-2206-S-2306-em-lote)  
  
**Saiba Mais**  
[eSocial - Alteração da CBO - consultoria de Segmentos](https://tdn.totvs.com/pages/releaseview.action?pageId=714221515)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[Schedule Protheus](http://tdn.totvs.com/x/ow9FCg)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)
