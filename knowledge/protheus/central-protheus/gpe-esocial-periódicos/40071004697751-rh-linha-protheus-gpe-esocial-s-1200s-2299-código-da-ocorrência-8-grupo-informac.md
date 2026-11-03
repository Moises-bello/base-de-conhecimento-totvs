---
article_id: 40071004697751
category: GPE - eSocial - Periódicos
content_hash: e81419a385866129bdb0e4893a4c056b40b0929e82c4aac683ff0a17e8203617
fetched_at: '2026-06-28T22:45:08.812556+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - Código da Ocorrência
  : 8 - Grupo ''Informacoes de desconto do emprestimo em folha'' deve ser preenchido'
type: support-article
updated_at: '2026-04-28T17:05:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40071004697751-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-C%C3%B3digo-da-Ocorr%C3%AAncia-8-Grupo-Informacoes-de-desconto-do-emprestimo-em-folha-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40070971117335) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Ao enviar o evento , é retornado a mensagem:Grupo 'Informacoes de desconto do emprestimo em folha' deve ser preenchido  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Causa**  
O erro ocorre quando existe no XML S-1200/S-2299 alguma rubrica com natureza 9253 (Empréstimos eConsignado - desconto) porém não foi gerado no XML as informações complementares do empréstimo em folha (tag descFolha).

Isso ocorre, geralmente, em duas situações:

* Quando a **modalidade do empréstimo não está corretamente preenchida no cadastro**;
* Ou quando, a verba de **provisão de crédito de férias ou em outra verba** foi utilizada indevidamente a natureza de rubrica **9253**.

Como consequência, a *tag* **descFolha** não é gerada no XML, ocasionando a inconsistência.

**Solução:**

Gere o relatório do S-1200 ou S-2299  e localize a verba que possui natureza 9253  
[**RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no módulo GPE**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-m%C3%B3dulo-GPE?source=search)  
[**RH - Linha Protheus - GPE - eSocial - S-2299 - Como gerar o relatório de conferencia do evento S-2299**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12927984951191-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-o-relat%C3%B3rio-de-conferencia-do-evento-S-2299?source=search)

**Cenário 1 :**  
As informações de empréstimo ecosnignado não foram cadastradas corretamente na rotina de valores futuros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40070973211671)

Para solucionar valide a documentação e realize o recalculo após correção: [RH - Linha Protheus - GPE - eSocial - Como gerar valores referente ao eConsignado nos eventos de remuneração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27451839338263-RH-Linha-Protheus-GPE-eSocial-Como-gerar-valores-referente-ao-eConsignado-nos-eventos-de-remunera%C3%A7%C3%A3o)

**Cenário 2:**  
As verbas de provisionamento ou outra verba possui natureza 9253 incorretamente.

*Exemplo de configuração incorreta:*  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40070973213207)

Para solucionar ajuste a natureza das verbas , conforme documentação e gere o evento novamente:  
[RH - Linha Protheus - GPE - Como cadastrar as verbas de Provisionamento nas Férias e Adiantamento referente ao eConsignado (Programa Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35930650152471-RH-Linha-Protheus-GPE-Como-cadastrar-as-verbas-de-Provisionamento-nas-F%C3%A9rias-e-Adiantamento-referente-ao-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador)

**Cenário 3:**  
A verba de desconto econsignado foi incluída manualmente na folha, rescisão ou férias

Quando a verba é incluída manualmente ao invés de ser gerada pela rotina de valores futuros , as informações complementares na tag descFolha não é levada automaticamente.

Outro ponto importante é que o desconto econsignado deve ser realizado somente em folha ou rescisão , nas férias deve ser levado as verbas de provisionamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40070973213975)

Para solucionar é necessário realizar a geração da informação corretamente pela rotina de valores futuros e calcular novamente a folha ou rescisão.   
[RH - Linha Protheus - GPE - eSocial - Como gerar valores referente ao eConsignado nos eventos de remuneração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27451839338263-RH-Linha-Protheus-GPE-eSocial-Como-gerar-valores-referente-ao-eConsignado-nos-eventos-de-remunera%C3%A7%C3%A3o)

Caso a folha já esteja fechada e não seja possível o recalculo , de forma paliativa, será necessário editar o evento no TAF e incluir as informações complementares manualmente:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40070971122071)

**Saiba Mais**

Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**".*
