---
article_id: 41095399829015
category: GPE - eSocial - Periódicos
content_hash: 0144603ba7e83e2846bdeade3860f7f5f28e519fa6022d9da8e621db9cd70877
fetched_at: '2026-06-28T22:45:07.291178+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - PIS - Rubricas de Férias e Abono
  Salarial
type: support-article
updated_at: '2026-06-19T19:31:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41095399829015-RH-Linha-Protheus-GPE-eSocial-S-1200-PIS-Rubricas-de-F%C3%A9rias-e-Abono-Salarial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41095399804695) Tempo aproximado para leitura: **00:06:00**  
  
**Dúvida**  
Como enviar as alterações de férias referente ao abono salarial do PIS, em casos de valores duplicados?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Com base no [Manual de Orientações para o Abono Salarial](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/trabalhador/abono-salarial/manual-de-orientacao-para-o-empregador-atualizado-22-05.pdf) e após identificar a possibilidade de duplicação dos valores de férias para esse fim, foi disponibilizada nova rotina para consulta e tratamento destas informações.

Para facilitar a consulta desta orientação e as alterações sistêmicas, a documentação foi centralizada [nesta página,](https://tdn.totvs.com/x/XmvlPw) leia as publicações e as alterações descritas na mesma.  
  
Todas as alterações sistêmicas estão informadas e detalhadas na página centralizada da tratativa do Abono PIS, leia o [item 2-Alterações Sistêmicas](https://tdn.totvs.com/pages/viewpage.action?pageId=1071999838#observacoes-observacoes1)

A rotina **GPEM948 - Inconsistência Abono Salarial** busca apresentar os funcionários que teriam direito ao Abono PIS, mas que devido as verbas de Férias e com natureza 1016 existirem nos demonstrativo de férias e folha, apresentam duplicidade de valores.  
Esta rotina fará a gravação de uma verba no cálculo de férias da verba de Id 1987 - Informativa Dedutora PIS nas Férias, esta verba visa zerar os valores de natureza 1016 neste demonstrativo, além disso pode reduzir o valor da verba de Id 1870 para compor a base de INSS corretamente

Será necessário atualização de fontes e dicionário. Atenção aos releases sem garantia estendida.  
  
**Fontes:**  
12.1.2310:<https://r.totvs.io/p/1253635>   
12.1.2410:<https://r.totvs.io/p/1253636>   
12.1.2510:<https://r.totvs.io/p/1253634>  
  
**Dicionário**:  
12.1.2310: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1123885>   
12.1.2410: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1170810>  
12.1.2510: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1221795>   
  
Após atualização, o sistema criará o grupo de perguntas porém o menu deve ser incluido manualmente como função Protheus:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41095399806103)  
  
**Veja também o processo detalhado**: [**Como corrigir possíveis divergências relacionadas ao pagamento do Abono Salarial**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/41104133754263-RH-Linha-Protheus-GPE-eSocial-Rubricas-de-F%C3%A9rias-e-Abono-Salarial-PIS)  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:  
[Boletim tecnico Tela Funcionários PIS - DICIONÁRIO](https://tdn.totvs.com/pages/releaseview.action?pageId=1072000343)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
