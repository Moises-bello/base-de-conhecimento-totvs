---
article_id: 360000666227
category: Contabilidade Gerencial - Calendário Contábil
content_hash: 479e1e98f8a3af752260e29d4fee43a41a65319ec33ff7f4715e6b83c7267970
fetched_at: '2026-06-28T22:41:03.392179+00:00'
product: protheus
section_id: 1500001537301
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como funciona o cache
  no ambiente contábil '
type: support-article
updated_at: '2022-03-10T11:38:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000666227-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-funciona-o-cache-no-ambiente-cont%C3%A1bil
---

**Dúvida**Fiz o desbloqueio do calendário contábil (CTBA010) e o sistema ainda acusa "calendário fechado/bloqueado" ao realizar um lançamento contábil.  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**O parâmetro MV\_CTBCACH foi criado para atender a rotina Lançamento Contábeis Automáticos(CTBA102), ele indica se o calendário contábil, moeda, câmbio e as entidades contábeis (Plano de Contas, Centro de Custos, Item Contábil e Classe de Valor) devem utilizar as informações em cachê, a fim de otimizar a performance.  
É importante ressaltar que quando o parâmetro estiver habilitado, as informações são estáticas, isto é, não são atualizadas de imediato.   
  
Exemplo:   
Se o parâmetro for habilitado (MV\_CTBCACH = 1 - padrão), um usuário pode utilizar a rotina Lançamento Contábil Automático e usuário pode bloquear o calendário.   
Com o parâmetro desabilitado (MV\_CTBCACH = 0), a informação do bloqueio é imediata, pois a busca é efetuada na base de dados.  
Como estas informações normalmente não são alteradas com frequência, o valor padrão do parâmetro é habilitado, para otimização de performance, portanto desabilitar o parâmetro pode ocasionar em lentidão no Sistema.
