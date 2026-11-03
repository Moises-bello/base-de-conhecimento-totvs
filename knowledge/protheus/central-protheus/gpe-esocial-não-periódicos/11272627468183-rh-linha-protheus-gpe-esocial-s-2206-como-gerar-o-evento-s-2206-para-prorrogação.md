---
article_id: 11272627468183
category: GPE - eSocial - Não Periódicos
content_hash: 362f8d31c46061d75a1169e0fb4e8f43373158e4a7d55672e9b185f73dbbf219
fetched_at: '2026-06-28T22:45:05.966416+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial -S-2206 - Como gerar o evento S-2206 para
  prorrogação e atualização do contrato de trabalho
type: support-article
updated_at: '2026-06-16T11:50:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11272627468183-RH-Linha-Protheus-GPE-eSocial-S-2206-Como-gerar-o-evento-S-2206-para-prorroga%C3%A7%C3%A3o-e-atualiza%C3%A7%C3%A3o-do-contrato-de-trabalho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24484620403223) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como gerar o evento S-2206 para prorrogação e atualização do contrato de trabalho?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Efetuados ajustes na geração do evento pela alteração do campo de tipo de contrato (**RA\_TPCONTR**) no cadastro do funcionário, e para levar a tag **dtTerm** apenas no **contrato indeterminado** (**tipo 1**), possibilitando a correta geração dos eventos S-2200/S-2206 sem a necessidade de limpar a data de término do contrato (RA\_DTFIMCT).  
  
Para a integração do evento S-2206 na prorrogação/ateração do contrato de experiência, foi criado o job **GPEM026J()** para execução via Schedule.  
O sistema irá buscar os registros da tabela SRA com tipo de contrato determinado (RA\_TPCONTR=2) cuja data de término (**RA\_DTFIMCT**) esteja inferior à data de execução do job e processar de acordo:

* Prorrogação do contrato (registros com data de prorrogação (RA\_VCTEXP2) superior à data do Término): o campo RA\_DTFIMCT será atualizado com a data da prorrogação para geração do evento S-2206, gravando o conteúdo anterior na tabela de histórico (SR9);
* Alteração do tipo de contrato (registros com a mesma data em ambos os campos): o campo RA\_TPCONTR será alterado para 1 (indeterminado), gravando o conteúdo anterior na tabela de histórico e efetuando a geração do evento.

Para que alterações na data de término do contrato via cadastro do funcionário sejam gravadas na tabela de histórico (SR9), será disponibilizada alteração de dicionário na Expedição Contínua RH: **acesse as atualizações através da página de entregas legais:** [**eSocial | Protheus - Entregas Legais**](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
  
Alternativamente pode ser implementada via Configurador, para mais informações acesse o [**Boletim Técnico**](https://tdn.totvs.com/pages/viewpage.action?pageId=729219455)**.**  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[Leiaute eSocial Trabalhador Temporário](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/leiautes-esocial-nt-05-2022-html/index.html#2200_vinculo_infoRegimeTrab_infoCeletista_trabTemporario)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
