---
content_hash: 8271322a56eac7c281bae23e1b670db4c502912859bd8102689f7968277066e4
fetched_at: '2026-06-29T00:10:12.511665+00:00'
page_id: '454827940'
product: rm
source: tdn-rm
title: TOTVS Segurança e Saúde Ocupacional - Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454827940
version: 15
---

## Funcionalidades disponíveis no menu Relatórios

* [PPP](https://tdn.totvs.com/pages/viewpage.action?pageId=452719230)
* [Relatórios de Saúde (PCMSO)](https://tdn.totvs.com/pages/viewpage.action?pageId=452719423)
* [Relatórios de Segurança (PPRA)](https://tdn.totvs.com/pages/viewpage.action?pageId=452719418)
* [Relatórios de LTCAT](https://tdn.totvs.com/pages/viewpage.action?pageId=452719519)
* [Relatórios PGR](https://tdn.totvs.com.br/display/public/LRM/Como+Fazer+PGR)
* [Tipos de Relatórios](https://tdn.totvs.com/pages/viewpage.action?pageId=452718941)

## Observação: ambiente Citrix

Para a geração do relatórios PGR, PCMSO, PPRA e LTCAT é necessário gravar o relatório na pasta padrão RM, para isso o usuário que gera o relatório precisa ter permissão de gravação na pasta.

Clientes que usam Citrix geralmente tem restrição de liberação de acesso à pasta padrão RM, onde consequentemente não conseguem gerar os relatórios PGR, PCMSO, PPRA e LTCAT.

Para atender esses clientes, foi desenvolvido no produto a parametrização abaixo. Clientes que não usam o Citrix e desejam que os relatórios sejam gerados em local específico, também podem usar essa parametrização.

1. No parametrizador do SMT, item Relatórios,  deve ser informado o local onde o relatório será gerado conforme a  figura abaixo.  Deve ser  compartilhada  uma pasta pública, onde os usuários, que geram o relatório, tenham permissão de gravação.

2. No relatório, ao clicar em "Gerar Relatório" o mesmo será salvo na pasta informada no item 1. Se o campo não for preenchido na tela de parâmetros, será considerado o diretório padrão.  
3. No relatório, ao clicar em "Visualizar Relatório", o usuário deverá informar a pasta (geralmente da máquina local), onde o relatório será salvo.

**Importante**

* O PPP não utilizará esse parâmetro porque a geração do relatório é interna.
* A parametrização estará disponível nos patches expedidos a partir do dia 29/06/2022.
