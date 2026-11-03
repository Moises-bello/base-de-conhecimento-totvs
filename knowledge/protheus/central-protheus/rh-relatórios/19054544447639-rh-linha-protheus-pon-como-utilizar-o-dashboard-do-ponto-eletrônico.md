---
article_id: 19054544447639
category: RH - Relatórios
content_hash: 830958f2ce5c12eee7bc12262679da7cd1b884f2c6e2c1e9a46b7717ef0b8993
fetched_at: '2026-06-28T22:44:43.507455+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Como utilizar o Dashboard do Ponto Eletrônico
type: support-article
updated_at: '2025-08-13T18:17:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19054544447639-RH-Linha-Protheus-PON-Como-utilizar-o-Dashboard-do-Ponto-Eletr%C3%B4nico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19054575591447) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como utilizar o *Dashboard* do Ponto Eletrônico?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) Ponto Eletrônico - A partir da versão 12.1.33  
  
**Solução**No módulo do Ponto Eletrônico (SIGAPON), acessar a rotina *Dashboard* (PONA480) em **Relatórios > Mensal > *Dashboard***.  
Inicialmente, o sistema sempre irá carregar os filtros com conteúdos padrões, sendo:  
- data de início: a partir da data atual, será mostrado como data início dois dias anteriores ao dia de hoje, por exemplo: hoje é dia 30.08, então a data início será o dia 28.08;  
- data de término: a partir da data atual, será mostrado como data de término um dia anterior ao dia de hoje, por exemplo: hoje é dia 30.08, então a data de término será o dia 29.08;  
- para o filtro de filial, será preenchido com todas as existentes.  
  
Para realizar a alteração do filtro, basta alterar os campos do filtro e posteriormente clicar em Atualizar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19061101402519)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19061118170903)

Cada vez que o filtro for atualizado, clicando em **Atualizar** a data e hora informados no campo superior direito em **Última atualização às** será atualizado, com isso, poderemos ver em qual dia e hora o *Dashboard* foi atualizado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19061118175383)

Será possível realizar a alteração dos filtros informando a data inicial e final do período em que o sistema irá buscar as informações dos indicadores, porém, o intervalo do período **não**poderá ser superior a **60 dias**. Por exemplo: ao preencher a Data de Inicio com 01/01/2022 automaticamente o calendário do campo Data de Término será bloqueado para dias superiores à 02/03/2022.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19061101427479)

Caso a Data de Término seja digitada manualmente para o dia 03/03/2022, o campo ficará destacado em vermelho, sinalizando que o conteúdo é inválido, e se mesmo assim for clicado em Atualizar, o sistema irá exibir a seguinte mensagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19061118203927)

Com todos os filtros corretos, será possível realizar a atualização do *Dashboard:*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19061118209559)

**Saiba mais:**[Dashboard Ponto Eletrônico](https://tdn.totvs.com/display/public/PROT/SIGAPON+-+Dashboard+Ponto#SIGAPONDashboardPonto-01.VIS%C3%83OGERAL)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
