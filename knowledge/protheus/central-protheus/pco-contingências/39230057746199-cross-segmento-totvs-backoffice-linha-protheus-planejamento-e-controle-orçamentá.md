---
article_id: 39230057746199
category: PCO - Contingências
content_hash: ac439287e4843aa6021be2f875a350810321eb2e767a5b8166db6fcb7a6898cb
fetched_at: '2026-06-28T22:37:12.154716+00:00'
product: protheus
section_id: 1500001539761
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Planejamento e Controle
  Orçamentário - Como bloquear a geração de contingências duplicada
type: support-article
updated_at: '2026-03-23T14:59:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39230057746199-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Planejamento-e-Controle-Or%C3%A7ament%C3%A1rio-Como-bloquear-a-gera%C3%A7%C3%A3o-de-conting%C3%AAncias-duplicada
---

Para bloquear a solicitação de nova contingência duplicada na rotina PCOA530-Contingencias do Protheus, utilize o Ponto de Entrada PCOA5306, que permite criar validações customizadas. É necessário cadastrar uma chave no campo AKA\_CHVCTG da tabela AKA e usar a variável Paramixb[1] para verificar duplicidade. O retorno da validação deve ser lógico: .F. para bloquear e .T. para permitir a inclusão.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39230057734295) Tempo aproximado para leitura: 00:05 min  
  
**Dúvida**  
**Como bloquear a solicitação de uma nova contingência quando já existe uma registrada.**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Microsiga Protheus) - Planejamento e Controle Orçamentário - A partir da versão 12.  
  
**Solução**  
Para validar e impedir a inclusão de contingências duplicadas na rotina PCOA530-Contingencias , deve-se utilizar o Ponto de Entrada [**PCOA5306**](https://tdn.totvs.com/display/public/PROT/DT+PE+PCOA5306+-+Contingencias+duplicadas).

Este Ponto de Entrada é acionado logo após algumas validações padrão do sistema, sendo o recurso ideal para criar validações adicionais customizadas que travem a rotina.

1. Para que o Ponto de Entrada seja efetivamente acionado, é obrigatório ter uma chave cadastrada no campo `AKA_CHVCTG` da tabela AKA.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39230066656791)
2. Utilizar a variável  `Paramixb[1]` ela traz a chave da contingência que está prestes a ser incluída, correspondendo à macro execução do campo `AKA_CHVCTG`.
3. O retorno da sua customização (`lRet`) deve ser obrigatoriamente do tipo Lógico.
4. Retorne `.F.` (Falso) caso a validação identifique a duplicidade e precise impedir a inclusão, ou `.T.` (Verdadeiro) para permitir que a contingência seja salva.

**Saiba Mais**  
[PCOA5306 - Contingencias duplicadas](https://tdn.totvs.com/display/PROT/DT+PE+PCOA5306+-+Contingencias+duplicadas)  
[SIGAPCO Utilização de Contingência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018523352-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Utiliza%C3%A7%C3%A3o-de-Conting%C3%AAncia)  
[How To PCO - Planejamento e Controle Orçamentário](https://tdn.totvs.com/pages/viewpage.action?pageId=763235880&draft=true)
