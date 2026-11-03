---
article_id: 1500006150582
category: Integrações Nativas
content_hash: a3d33d7280a0854bbf6d2c60f5a7cf84878f0113af7797f695f1e715bfe06de1
fetched_at: '2026-06-28T22:42:35.418920+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Inclusão de O.S para Ativo
type: support-article
updated_at: '2021-09-02T20:25:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006150582-Manufatura-Linha-Protheus-MNT-Inclus%C3%A3o-de-O-S-para-Ativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)** Tempo aproximado para leitura: **00:01:00 min****Dúvida**Qual é o processo para inclusão de uma **Ordem de Serviço - O.S** para um **Ativo - SN1**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Todas as versões  
  
**Solução**Sempre que o parâmetro **MV\_NGMNAT - Integração com o Ativo Fixo** encontrar-se habilitado, a rotina **O.S. Corretiva - MNTA420** possibilita a inclusão de uma **O.S** diretamente para um **Ativo - SN1**, o qual não necessita estar vinculado a um **Bem - ST9** no ato da inclusão.  
Sobre o campo **Código Bem - TJ\_CODBEM**, ao pressionar a tecla **F7** é acionado a consulta padrão que lista os **Ativos - SN1** disponíveis, sendo que estes ativos, não necessariamente estarão vinculados a um **Bem - ST9**, nestes casos é realizado a inclusão automática de um **Bem - ST9** com as informações do**Ativo - SN1** utilizado na **O.S**, já vinculando estes dois registros. Para os campos que não existem no **Ativo - SN1**, **Família - T9\_CODFAMI**e **Calendário - T9\_CALEND**, serão preenchidos com informações genéricas, também inclusas automaticamente neste processo.
