---
article_id: 18192204656663
category: Materiais - Compras (SIGACOM)
content_hash: e7e983885c6ccac6877e2274099d091c44aaa996755b3aaa2f441e98695c4b78
fetched_at: '2026-06-28T22:41:13.154397+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao acessar a consulta
  padrão de alguns campos, os registros bloqueados não aparecem como cinza
type: support-article
updated_at: '2023-10-11T14:27:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18192204656663-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-acessar-a-consulta-padr%C3%A3o-de-alguns-campos-os-registros-bloqueados-n%C3%A3o-aparecem-como-cinza
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18192189241751) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Nas rotinas MATA103 (documento de entrada), MATA121(pedido de compra), MATA110(Solicitação de Compra) e Pré-nota(MATA140), ao acessar a consulta padrão das entidades contábeis, os registros bloqueados não estão cinzas, dificultando a identificação do usuário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18191095515287)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18191061864855)

**Ambiente**Protheus – Compras – A partir da versão 12.33  
  
**Solução**

O campo tratado para a linha da consulta ficar cinza é o campo reservado \_MSBLQL. As tabelas de contabilidade estão utilizando um campo diferente para tratar o bloqueio, \_BLOQ. Porém, esse campo \_BLOQ não possui tratativa para mudar o estilo da linha tanto na consulta como no browse da rotina. Dessa forma, é necessário realizar o processo detalhado abaixo para incluir o campo reservado \_MSBLQL.

1. Abrir a tabela no configurador, clicar em editar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18191978541207)

       2. Clicar na opção "campos reservados"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18191989601815)

       3. Selecionar a opção "Bloqueio automático"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18192007575319)

       4. O campo \_MSBLQL será incluído na última posição da tabela

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18192073525143)**

       5. Salvar alteração realizada

Obs. para salvar as telas do Protheus devem ser fechadas.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18192028725143)**

***Saiba mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
