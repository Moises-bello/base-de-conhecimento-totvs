---
article_id: 4407668411799
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 8cb8eb4e1c608ba7dd9dfd2ed7f07faeb58862a6ce78a38137c171591ae56181
fetched_at: '2026-06-28T22:39:57.431057+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Falha de
  schema: Element ''dthremissao'': ''AAAA-MM-DDT:SS'' is not a valid value of the
  atomic type'
type: support-article
updated_at: '2025-07-18T14:45:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407668411799-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Falha-de-schema-Element-dthremissao-AAAA-MM-DDT-SS-is-not-a-valid-value-of-the-atomic-type
---

**Ocorrência**Ao realizar a transmissão de um RPS ocorre a falha de schema abaixo.  
  
Exemplos:  
![](https://totvssuporte.zendesk.com/attachments/token/kIETK1HYUMPAvX9A39LyJWvcx/?name=inline-1564526635.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/PSVXaQN9gknlfa4VhYZGXNAOp/?name=inline1304307824.png)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Documentos Eletrônicos - Todas as versões.  
  
**Causa**Esse incidente ocorre por conta das informações da tabela SF2 estarem vindo vazias, mais precisamente pelos campos F2\_EMISSAO ou F2\_HORA (mais comum).  
  
A tag <dthremissao> deve ser montada da seguinte forma: '*AAAA-MM-DDT**HH:MM**:SS'  
(A=ANO, M=MÊS,D=DIA,H=HORA,M=MINUTOS,S=SEGUNDOS)*  
  
Note que pelos prints acima acabou faltando após o T de Time a hora e minuto da emissão.  
Esses conteúdos são extraídos do F2\_HORA, com a única exceção dos segundos, que é gerado automaticamente pelo próprio rdmake NFSEXMLENV (registrados em ambos os prints acima).  
  
**Solução**Para esses casos, se acessar a SF2, irá notar que o F2\_HORA está com conteúdo vazio:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407663970071/mceclip0.png)  
  
Por se tratar de uma informação obrigatória nos schemas/layout das prefeituras essa informação deverá ser registrada.  
Nesse caso a equipe responsável pela orientação do preenchimento desse campo é a de Faturamento, pois ocorre no momento da preparação do documento, **portanto deverá acionar eles, detalhar a necessidade e aguardar orientação.**
